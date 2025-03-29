from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Flask-Mail Configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.getenv('SENDER_EMAIL')  # Your email
app.config["MAIL_PASSWORD"] = os.getenv('PASSWORD')  # App Password
app.config["MAIL_DEFAULT_SENDER"] = os.getenv('SENDER_EMAIL')

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["subject"]
        message = request.form["message"]

        msg = Message(
            subject,
            sender=os.getenv('SENDER_EMAIL'),
            recipients=[os.getenv("REC_EMAIL")]
        )
        msg.body = f"Hello from {name},\n\n{message}"

        try:
            mail.send(msg)
            return redirect(url_for("index"))
        except Exception as e:
            return f"Error sending email: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
