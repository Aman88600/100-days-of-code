from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Setup database base and init
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.context_processor
def inject_user():
    # Makes 'logged_in' available in all templates
    return dict(logged_in=current_user.is_authenticated)

# User model inherits UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")  # logged_in available automatically in templates

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {e}")
            return redirect(url_for('register'))

        # Automatically log in after registration
        login_user(new_user)
        return redirect(url_for('secrets'))

    return render_template("register.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    message = False
    warning = ""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.session.execute(db.select(User).where(User.email == email)).scalar_one_or_none()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)  # <-- LOG IN the user here!
                return redirect(url_for('secrets'))
            else:
                message = True
                warning = "Incorrect password. Try again."
                flash(warning)
        else:
            message = True
            warning = "Email not found. Please register first."
            flash(warning)

    return render_template("login.html", message=message, warning=warning)

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory=os.path.join(app.root_path, 'static', 'files'),
        path='cheat_sheet.pdf',
        as_attachment=False
    )

if __name__ == "__main__":
    app.run(debug=True)
