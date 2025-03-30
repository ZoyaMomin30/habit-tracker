from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# app = Flask(__name__)
app = Flask(__name__, static_folder='static', template_folder='templates')

# Flask-Mail Configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.getenv('SENDER_EMAIL')
app.config["MAIL_PASSWORD"] = os.getenv('PASSWORD')
app.config["MAIL_DEFAULT_SENDER"] = os.getenv('SENDER_EMAIL')

mail = Mail(app)

# Pixela configuration
token = os.getenv('token')
username = os.getenv('username')
pixela_endpoint = os.getenv('pixela_endpoint')
graph_id = "graph2"





@app.route('/')
def home():
    # Get random quote (with error handling)
    try:
        # response = requests.get("https://zenquotes.io/api/random")
        # quote = response.json()[0]
        quote_text = "hi"
        author = "zoya"
    except:
        quote_text = "Coding is the art of thinking in algorithms"
        author = "Anonymous Developer"
    
    # Check if habit exists
    if 'habit_created' in session:
        return render_template('index.html',
                           habit_created=True,
                           habit_name=session['habit_name'],
                           target=session['target'],
                           graph_id=session['graph_id'],
                           quote_text=quote_text,
                           author=author
                           )

    return render_template('index.html',
                        habit_created=False,
                        quote_text=quote_text,
                        author=author)

@app.route('/add_habit', methods=['POST'])
def add_habit():
    # Get form data
    habit = request.form['habit']
    quantity = request.form['quantity']
    
    # Store in session
    session['habit'] = habit
    session['quantity'] = quantity
    
    # Create graph ID from habit name (lowercase, no spaces)
    graph_id = habit.lower().replace(" ", "_")[:15]
    session['graph_id'] = graph_id
    
    # Create Pixela graph
    create_pixela_graph(graph_id, habit, quantity)
    
    return redirect(url_for('home'))

def create_pixela_graph(graph_id, name, unit):
    """Create a new graph on Pixela"""
    graph_config = {
        "id": graph_id,
        "name": name,
        "unit": request.form["quantity"],
        "type": "float",
        "color": "kuro",   #black
        "timezone": "Asia/Kolkata"
    }
    
    headers = {"X-USER-TOKEN": token}
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
    
    response = requests.post(graph_endpoint, json=graph_config, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to create graph: {response.text}")



# Habit Tracker Routes (from app.py)
@app.route("/submit", methods=["POST"])
def submit():
    if request.method=="POST":
        quantity = request.form["quantity"]
        post_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

        headers = {"X-USER-TOKEN": token}
        today = datetime.now()

        color_param = {
            "date": today.strftime("%Y%m%d"),
            "quantity": quantity,
        }
        pixel_color_response = requests.post(url=post_endpoint, json=color_param, headers=headers)

        if pixel_color_response.status_code==200:
            return redirect('/')
        else:
            return f"Error: {pixel_color_response.text}", pixel_color_response.status_code

# Email Route (from email.py)
@app.route("/send_email", methods=["POST"])
def send_email():
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
        



@app.route('/reset')
def reset():
    """Clear session (for testing)"""
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)