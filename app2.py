from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html" )

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    print("Username:", repr(username))
    print("Password:",repr(password))

    # if username == "shree123" and password == "pass":
    #     return render_template("welcome.html", name=username)
    # else:
    #     return "Invalid username or password"

    valid_users = {
        'admin':'123',
        'shree123':'pass',
        'jha':'456'
    }

    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html", name=username)
    
    else:
        return "Invalid credentials"
    
if __name__ == "__main__":
    app.run(debug=True)