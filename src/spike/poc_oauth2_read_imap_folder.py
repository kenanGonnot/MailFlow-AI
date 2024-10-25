import os
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow
import requests
from imaplib import IMAP4_SSL


def google_authenticate():
    """
    Performs authentication and returns the credentials.
    If credentials are saved, load them from the file.
    Otherwise, perform the authentication and save the credentials.
    """
    credentials_file = 'credentials.pkl'
    if os.path.exists(credentials_file):
        with open(credentials_file, 'rb') as file:
            credentials = pickle.load(file)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('../client_secret.json',
                                                         scopes=[
                                                             'https://www.googleapis.com/auth/userinfo.profile',
                                                             'https://www.googleapis.com/auth/userinfo.email',
                                                             'openid',
                                                             'https://mail.google.com/'
                                                         ])
        credentials = flow.run_local_server(port=0)
        with open(credentials_file, 'wb') as file:
            pickle.dump(credentials, file)
    return credentials


def read_imap_folders(email, access_token):
    """
    Connects to IMAP and lists available folders.
    """
    imap = IMAP4_SSL("imap.gmail.com", 993)
    imap.authenticate('XOAUTH2',
                      lambda x: f'user={email}\x01auth=Bearer {access_token}\x01\x01'.encode('utf-8'))

    # Listing available folders
    print("Available folders:")
    res, data = imap.list('""', "*")
    if data:
        for mbox in data:
            print(mbox)


def main():
    # Step 1: Authentication and obtaining credentials
    credentials = google_authenticate()

    # Step 2: Use the access token to get the email
    response = requests.get('https://www.googleapis.com/oauth2/v1/userinfo',
                            params={'alt': 'json', 'access_token': credentials.token}
                            )
    email = response.json().get('email')

    # Step 3: Read IMAP folders
    read_imap_folders(email, credentials.token)


if __name__ == "__main__":
    main()
