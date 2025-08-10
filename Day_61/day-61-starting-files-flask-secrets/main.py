from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class MyForm(FlaskForm):
    # Email field
    email = EmailField(label='email', validators=[DataRequired(), Email()])
    # Password Field
    password = PasswordField(label='password', validators=[DataRequired()])
    # Submit Filed
    submit = SubmitField(label="Log In")

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = 'aman_basoya'


@app.route("/")
def home():
    form = MyForm()
    return render_template('index.html', form = form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # If email = admin@email.com and password = 12345678
        if email == "admin@email.com" and password == "12345678":
            # Go to success.html
            return render_template("success.html")
        else:
        # Else Go to denied.html
            return render_template("denied.html")
        
        print(f"Email=  {email} Password = {password}")
        # Add your login logic here (e.g., check against a database)
        print("validated")
        return f'Logged in as {email}'
    print("Not Validated")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
