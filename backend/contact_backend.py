from flask import Flask, request, jsonify, render_template_string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
SMTP_USERNAME = 'powershdw@gmail.com'  # Replace with your Gmail address
SMTP_PASSWORD = 'jpkl jitu cacn gcdu'  # Replace with your Gmail App Password
RECEIVER_EMAIL = 'vamshikrishnaramasamy@gmail.com' # Repalce with email to which question is being asked

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = f'New Contact Form Submission from {name}'

        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        success_message = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Success</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f5f5f5;
                    color: #333;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .message-container {
                    background-color: #ffffff;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }
                h2 {
                    color: #4CAF50;
                }
                p {
                    font-size: 16px;
                }
                a {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: #ffffff;
                    text-decoration: none;
                    border-radius: 5px;
                }
                a:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="message-container">
                <h2>Thank you!</h2>
                <p>Your message has been successfully delivered.</p>
                <a href="http://127.0.0.1:5500/pages/contact.html">Go Back</a>
            </div>
        </body>
        </html>
        """
        return render_template_string(success_message), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
