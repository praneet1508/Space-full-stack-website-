import os
from datetime import datetime
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI") + "Spacestudysite"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, doc):
        self.doc = doc
        self.id = str(doc["_id"])
        self.username = doc.get("username")
        self.is_admin = doc.get("is_admin", False)

@login_manager.user_loader
def load_user(user_id):
    doc = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return User(doc) if doc else None

@app.route("/")
def index():
    facts = list(mongo.db.facts.find().limit(8))
    quizzes = list(mongo.db.quizzes.find().limit(6))
    return render_template("index.html", facts=facts, quizzes=quizzes)

@app.route("/quiz/<quiz_id>")
def quiz_page(quiz_id):
    quiz = mongo.db.quizzes.find_one({"_id": ObjectId(quiz_id)})
    if not quiz:
        flash("Quiz not found", "warning")
        return redirect(url_for("index"))
    return render_template("quiz.html", quiz=quiz)

@app.route("/quiz/<quiz_id>/submit", methods=["POST"])
def submit_quiz(quiz_id):
    data = request.get_json() or {}
    answers = data.get("answers", {})
    quiz = mongo.db.quizzes.find_one({"_id": ObjectId(quiz_id)})
    if not quiz:
        return jsonify({"error": "Quiz not found"}), 404

    score = 0
    for idx, q in enumerate(quiz["questions"]):
        correct = int(q["answer_index"])
        user_choice = answers.get(str(idx))
        if user_choice is not None and int(user_choice) == correct:
            score += 1
    total = len(quiz["questions"])
    result = {"score": score, "total": total, "percent": round(score / total * 100, 2)}

    if current_user.is_authenticated:
        mongo.db.attempts.insert_one({
            "user_id": ObjectId(current_user.get_id()),
            "quiz_id": ObjectId(quiz_id),
            "score": score,
            "total": total,
            "created_at": datetime.utcnow()
        })
    return jsonify(result)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        pw = request.form["password"]

        if mongo.db.users.find_one({"email": email}):
            flash("Email already registered", "danger")
            return redirect(url_for("register"))

        hashed = generate_password_hash(pw)
        res = mongo.db.users.insert_one({
            "username": username,
            "email": email,
            "password": hashed,
            "created_at": datetime.utcnow()
        })
        user_doc = mongo.db.users.find_one({"_id": res.inserted_id})
        login_user(User(user_doc))
        flash("Account created successfully! Welcome 🚀", "success")
        return redirect(url_for("index"))
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        pw = request.form["password"]
        doc = mongo.db.users.find_one({"email": email})
        if doc and check_password_hash(doc["password"], pw):
            login_user(User(doc))
            flash(f"Welcome back, {doc['username']}! 🎉", "success")
            return redirect(url_for("index"))
        flash("Invalid credentials", "danger")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You’ve been logged out. See you soon 👋", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
