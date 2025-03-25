import smtplib
from email.message import EmailMessage
from app.config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, ADMIN_EMAIL

def send_critical_error_alert(error_details):
    msg = EmailMessage()
    msg['Subject'] = f"[CRITICAL] Error Logged: {error_details['message']}"
    msg['From'] = SMTP_USER
    msg['To'] = ADMIN_EMAIL

    # Email Body
    body = f"""
    Critical Error Alert!
    --------------------------------
    Error ID: {error_details['id']}
    Message: {error_details['message']}
    Severity: {error_details['severity']}
    Time: {error_details['timestamp']}
    """
    
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
            print("Email alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

