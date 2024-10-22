# Email Automation Project with GPT and Application Analysis

This project is a Python application designed to automate the management of professional emails. It includes functionalities for retrieving emails, automatically generating responses using the GPT-4 API, and tracking job applications by creating a structured report in Markdown format.

## Features

### 1. **Email Retrieval**
The project connects to your inbox via IMAP, retrieves unread emails, and processes messages efficiently. It includes the following features:

- **Unread Email Retrieval**: Fetches unread emails and generates automatic responses.
- **Job Application Filtering**: Specifically retrieves emails related to job applications for in-depth analysis.

### 2. **Automatic Response Generation**
With the integration of the GPT-4 API, the project automatically generates contextual and personalized responses for each unread email. Users can review the response before sending it.

### 3. **Job Application Analysis**
Emails related to job applications are recorded in a detailed Markdown file containing the following information:
- Date of application
- Email sender
- Subject and content of the email

This feature allows for easy tracking of all applications.

## Project Structure

The project is structured into several modules for better organization and maintainability:

```
project_root/
│
├── src/
│   ├── mail_service/
│   │   ├── imap_client.py       # IMAP connection and email retrieval
│   │   ├── smtp_client.py       # Sending emails (future development)
│   │   └── contact_manager.py   # Contact management (future development)
│   │
│   ├── ai_engine/
│   │   ├── gpt_api.py           # Interaction with the GPT API to generate responses
│   │   └── language_detector.py # Language detection for emails (future development)
│   │
│   ├── ui/
│   │   └── validation_ui.py     # User interface for validating generated emails (future development)
│   │
│   ├── main.py                  # Main entry point
│   └── utils/
│       ├── config.py            # General configuration (loading environment variables)
│       └── logger.py            # Log manager (future development)
│
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
└── .env                         # File for sensitive environment variables
```

## Installation

### Prerequisites
- Python 3.8+
- OpenAI account with access to the GPT-4 API
- Access to your email via IMAP

### Installation Steps
1. Clone the project repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root for sensitive information:
   ```dotenv
   IMAP_SERVER=imap.your_provider.com
   EMAIL=your_email@example.com
   PASSWORD=your_secure_password
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Running the Project
1. Run the main file `main.py`:
   ```bash
   python main.py
   ```

2. The script will connect to your mailbox, retrieve unread emails, generate responses via GPT-4, and create a Markdown file `applications_report.md` for job applications.

### Manual Validation
- **Response Validation**: Before sending a generated response, you can manually validate it via a user interface to be developed in the future.

## Future Development
- **Validation Interface**: Develop a user interface (UI) to validate responses before sending.
- **Language Detection**: Add functionality to detect the language of emails to adjust responses automatically.
- **Email Sending**: Implement an SMTP module for the automated sending of validated responses.
- **Contact Management**: Add a contact manager to save email senders directly to your contacts application.

## Security
- Sensitive information such as login credentials and API keys is stored in a `.env` file and should not be shared.
- It is recommended to use an application password for emails and enable two-factor authentication (2FA) whenever possible.

## Dependencies
- **imaplib**: For connecting and reading emails via IMAP.
- **email**: For parsing email messages.
- **openai**: For integration with the GPT-4 API.
- **dotenv**: For loading environment variables from the `.env` file.

## Contributing
Contributions are welcome! If you would like to make changes, please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b new_feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push your changes:
   ```bash
   git push origin new_feature
   ```
5. Create a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or suggestions, feel free to contact me via email at: [your_email@example.com](mailto:your_email@example.com).

---
Thank you for using this project! I hope it helps you automate your email management and track your job applications more easily.

