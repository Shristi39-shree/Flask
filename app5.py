from flask import Flask, render_template, request,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/",methods=["GET","POST"])
def form():
  if request.method == "POST":
    name = request.form.get("name")
    if not name:
      flash("Name cannot be empty")
      return redirect(url_for("form"))
    flash(f"Thanks {name}, your feedback was saved")
    return redirect( url_for("thankyou"))
  return render_template("form.html")
@app.route("/thankyou")
def thankyou():
  return render_template("thankyou.html")
  

# @app.route("/")
# def home():
#     return render_template("feedback.html")

# @app.route("/feedback", methods=["GET", "POST"])
# def feedback():
#     if request.method == "POST":
#         name = request.form.get("username")
#         message = request.form.get("message")
#         return render_template("thankyou.html", user=name, message=message)

#     return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)