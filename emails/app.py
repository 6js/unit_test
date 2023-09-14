from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_data.db'
db = SQLAlchemy(app)

# Define the database model for storing form data
class FormData(db.Model):
    __tablename__ = "FormData"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)

    def __repr__(self):
        return f'<FormData {self.name}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method, request.form)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(name, email, message)

        form_data = FormData(name=name, email=email, message=message)
        db.session.add(form_data)
        db.session.commit()

        # Send email here
        send_email(name, email, message)

    return render_template('form.html')

def send_email(name, email, message):
    # Email configuration
    sender_email = 'jsansu64@gmail.com'
    sender_password = 'Dateofbirth@6'
    recipients = ['viditgupta84@gmail.com', 'jsansu64@gmail.com']  # Add the list of recipient email addresses here

    # Create a multi-part email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = 'Form Submission'

    # Render the email body using the template and the form data
    with app.app_context():
        email_body = render_template('email_template.html', name=name, email=email, message=message)
    msg.attach(MIMEText(email_body, 'html'))

    # Attach the form data to the email
    with open('form_data.db', 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='sqlite')
        attachment.add_header('Content-Disposition', 'attachment', filename='form_data.db')
    msg.attach(attachment)

    # Send the email using SMTP server (in this example, using Gmail's SMTP server)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipients, msg.as_string())
    server.quit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
