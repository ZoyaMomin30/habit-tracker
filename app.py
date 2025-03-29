from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

token = os.getenv('token')
username = os.getenv('username')
pixela_endpoint = os.getenv('pixela_endpoint')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# STEP1 CREATE ACCOUNT 


user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# we have set up a user account on pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_id = "graph2"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"


@app.route("/submit", methods=["POST"])
def submit():
    if request.method=="POST":
        quantity = request.form["quantity"]
        graph_id = "graph2"
        post_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

        headers = {
        "X-USER-TOKEN" : token
        }  

        today=datetime.now()

        color_param = {
        "date": today.strftime("%Y%m%d"),
        "quantity": quantity,
        }
        pixel_color_response = requests.post(url=post_endpoint, json=color_param, headers=headers)
        print(pixel_color_response.text)

    if pixel_color_response.status_code==200:
        # return pixel_color_response.text
        return redirect('/')
    
    else:
        return f"Error: {pixel_color_response.text}", pixel_color_response.status_code

@app.route("/update", methods=["POST"])
def update():
    graph_id = "graph2"
    
    # Get values from the form
    date = request.form['date']
    quantity = request.form['quantity']
    
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y%m%d")  # Convert to correct format
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD.", 400  # Error handling for incorrect date format

    update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{formatted_date}"

    headers = {
        "X-USER-TOKEN": token
    }

    new_param = {
        "quantity": quantity,  # "date" is not required in the payload
    }

    # Send the request
    pixel_update_response = requests.put(url=update_endpoint, json=new_param, headers=headers)

    if pixel_update_response.status_code == 200:
        return redirect('/')
    else:
        return pixel_update_response.text, pixel_update_response.status_code 
    
@app.route("/delete", methods=["POST"])
def delete():
    date = request.form["date"]

    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y%m%d")  # Convert to correct format
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD.", 400  # Error handling for incorrect date format

    delete_endpoint=f"{pixela_endpoint}/{username}/graphs/{graph_id}/{formatted_date}"

    headers = {
        "X-USER-TOKEN": token
    }

    pixel_delete_response = request.delete(url=delete_endpoint, headers = headers)

    if pixel_delete_response == 200:
        return redirect("/")
    
    else:
        return pixel_delete_response.text, pixel_delete_response.status_code 


if __name__ == "__main__":
    app.run(debug=True)