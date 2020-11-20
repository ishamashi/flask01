from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)
app.secret_key = "ishamashi"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["nm"]
		session["user"] = user
		flash("Login Berhasil.!!")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Anda Sudah Login.!")
			return redirect(url_for("user"))

		return render_template("login.html")

@app.route("/user")
def user():
	if  "user" in session:
		user = session["user"]
		return render_template("user.html", user=user)
	else:
		flash("Anda Belum Login.!!")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	if "user" in session:
		user = session["user"]
		flash(f"Anda Ter-Logout, {user}!", "info")
	session.pop("user", None)
	return redirect(url_for("login"))

if __name__=="__main__":
	app.run(debug=True)

# Wait ya



# MALAM INI SAYA MAU BACA DOANG 
# GAK CODING