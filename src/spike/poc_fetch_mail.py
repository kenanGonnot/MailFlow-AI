import os
from imaplib import IMAP4_SSL
import email as email_parser
from dotenv import load_dotenv

from src.spike.poc_oauth2_read_imap_folder import google_authenticate


def fetch_unread_emails(email, access_token):
    """
    Connects to IMAP and fetches unread emails from the INBOX, retrieving date, subject, sender, and body.
    """
    imap = IMAP4_SSL("imap.gmail.com", 993)
    imap.authenticate('XOAUTH2',
                      lambda x: f'user={email}\x01auth=Bearer {access_token}\x01\x01'.encode('utf-8'))

    # Select the INBOX folder
    imap.select('inbox')

    # Search for unread emails in the INBOX
    status, email_ids = imap.search(None, 'UNSEEN')
    if status != 'OK':
        print("No unread messages found!")
        return []

    # Convert email IDs to a list and reverse to get the most recent first
    email_ids = email_ids[0].split()[::-1]

    emails = []

    # Fetch each unread email by ID
    for e_id in email_ids:
        status, data = imap.fetch(e_id, '(RFC822)')
        if status != 'OK':
            print(f"Failed to fetch email ID {e_id}")
            continue

        # Parse the email content
        raw_email = data[0][1]
        msg = email_parser.message_from_bytes(raw_email)

        # Extract date, subject, sender, and body
        email_date = msg.get('Date')
        email_subject = msg.get('Subject')
        email_from = msg.get('From')
        email_body = ""
        if msg.is_multipart():
            for part in msg.get_payload():
                if part.get_content_type() == 'text/plain':
                    email_body += part.get_payload(decode=True).decode('utf-8')
        else:
            email_body = msg.get_payload(decode=True).decode('utf-8')

        emails.append({
            "id": e_id,
            "date": email_date,
            "subject": email_subject,
            "from": email_from,
            "body": email_body
        })

    imap.logout()
    return emails


if __name__ == '__main__':
    load_dotenv()
    credentials = google_authenticate()
    email = os.getenv("EMAIL")
    print("email: %s" % email)

    # Step 4: Fetch inbox mails
    emails = fetch_unread_emails(email, credentials.token)
    print("All the emails : ", emails)
