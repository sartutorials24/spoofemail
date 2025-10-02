import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import streamlit as st

st.title("Advanced Email Spoofing App")
st.write("Caution: This app is for educational purposes only. Do not use for illegal activities.")

# Input fields for sender information
sender_name = st.text_input("Sender Name")
sender_email = st.text_input("Sender Email Address")

# Input field for recipient email
recipient_email = st.text_input("Recipient Email Address")

# Input field for subject and body
subject = st.text_input("Email Subject")
body = st.text_area("Email Body")

# SMTP server and credentials
smtp_server = st.text_input("SMTP Server", value="smtp.example.com")
smtp_port = st.text_input("SMTP Port", value="587")
smtp_username = st.text_input("SMTP Username")
smtp_password = st.text_input("SMTP Password", type="password")

# Button to send the spoofed email
if st.button("Send Spoofed Email"):
    message = MIMEText(body)
    message["From"] = formataddr((sender_name, sender_email))
    message["To"] = recipient_email
    message["Subject"] = subject

    server = smtplib.SMTP(smtp_server, int(smtp_port))
    server.starttls()
    server.login(smtp_username, smtp_password)

    server.sendmail(sender_email, recipient_email, message.as_string())

    st.success("Spoofed email sent successfully!")
    server.quit()

st.write("Note: This app should only be used for testing and learning purposes. Sending spoofed emails without consent is illegal and unethical.")
