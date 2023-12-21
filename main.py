from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_socketio import join_room, leave_room, send, SocketIO
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
from sqlalchemy import func
from werkzeug.security import check_password_hash, generate_password_hash



app = Flask (__name__)
app.config["SECRET_KEY"]= "jsjdjsjhd"
socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animesphere.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Chatroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chatname = db.Column(db.String(255), unique=True, nullable=False)
    image = db.Column(db.String(255), nullable=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('messages', lazy=True), foreign_keys=[user_id])
    
    chatroom_id = db.Column(db.Integer, db.ForeignKey('chatroom.id'), nullable=False)
    chatroom = db.relationship('Chatroom', backref=db.backref('messages', lazy=True), foreign_keys=[chatroom_id])



with app.app_context():
    db.create_all()
    


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("password")
        action = request.form.get("action")

        if not username or not password:
            return render_template("home.html", error="Bitte trage sowohl Benutzernamen als auch Passwort ein!", username=username)

        existing_user = User.query.filter_by(username=username).first()

        if action == "sign_in":
            if not existing_user:
                # Speichere den Benutzer in der Datenbank, wenn er nicht vorhanden ist
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                new_user = User(username=username, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                return render_template("home.html", message="Dein Benutzer wurde registriert!", username=username)
            else:
                return render_template("home.html", error="Dieser Benutzername existiert bereits!", username=username)

        elif action == "log_in":
            if existing_user and check_password_hash(existing_user.password, password):
                session["name"] = username
                return redirect(url_for("rooms"))
            else:
                return render_template("home.html", error="Benutzername oder Passwort ist falsch!", username=username)

    return render_template("home.html")



#rooms.html

@app.route("/rooms", methods=["GET"])
def rooms():
    chatrooms = Chatroom.query.all()

    if "name" in session:
        username = session["name"]
        welcome_message = f"Willkommen, {username}!"
        return render_template("rooms.html", welcome_message=welcome_message, chatrooms=chatrooms)
    else:
        return redirect(url_for("home"))



def normalize_chatname(chatname):
    return chatname.lower().strip()

@app.route("/create_room", methods=["POST"])
def create_room():
    chatname = request.form.get("chatname")
    normalized_chatname = normalize_chatname(chatname)

    image = request.files.get("image")

    if not chatname or not image:
        flash("Bitte fülle alle Felder aus.", "error")
        return redirect(url_for("rooms"))

    if not allowed_file(image.filename):
        flash("Ungültige Dateiendung. Erlaubt sind: png, jpg, jpeg, gif", "error")
        return redirect(url_for("rooms"))

    # Überprüfe, ob ein Chatroom mit dem normalisierten Namen bereits existiert
    existing_chatroom = Chatroom.query.filter(func.lower(Chatroom.chatname) == normalized_chatname).first()

    if existing_chatroom:
        flash("Einen Chatroom zu diesem Anime existiert bereits!", "error")
        return redirect(url_for("rooms"))

    image_folder = os.path.join("static", "img", "chatrooms")
    image_path = os.path.join(image_folder, secure_filename(image.filename))
    image.save(image_path)


    new_chatroom = Chatroom(chatname=chatname, image=image_path)
    db.session.add(new_chatroom)
    db.session.commit()

    flash("Chatroom erfolgreich erstellt!", "success")
    return redirect(url_for("rooms"))
            
    
    
if __name__ == "__main__":
    socketio.run(app, debug=True)