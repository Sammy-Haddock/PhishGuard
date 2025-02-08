import imaplib
import email
from email.header import decode_header
 
# Email credentials
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"

# Connect to Gmail's IMAP server
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)

# Select the inbox (or another folder)
mail.select("inbox")

# Search for all emails
status, messages = mail.search(None, "ALL")

# Convert message numbers to a list
mail_ids = messages[0].split()

# Read the latest email
latest_email_id = mail_ids[-1]

# Fetch the email
status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

# Parse the email content
for response_part in msg_data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])

        # Decode email subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        print(f"Subject: {subject}")

        # Extract sender
        sender = msg.get("From")
        print(f"From: {sender}")

        # Extract email body (handling plain text & HTML)
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if "attachment" not in content_disposition:
                    try:
                        body = part.get_payload(decode=True).decode()
                        print(f"Body: {body}")
                    except:
                        pass
        else:
            body = msg.get_payload(decode=True).decode()
            print(f"Body: {body}")

# Close connection
mail.logout()