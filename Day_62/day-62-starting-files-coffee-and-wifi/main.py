from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Location', validators=[DataRequired(), URL(message="Please enter a valid URL starting with http or https")])
    open_time = StringField(label='Open', validators=[DataRequired()], name="open_time")
    close_time = StringField(label='Close', validators=[DataRequired()], name="close_time")
    coffee_rating = SelectField(label = 'Coffee Rating ☕', choices=[
        ('✘'), ('☕'), ('☕☕'), ('☕☕☕'), ('☕☕☕☕'), ('☕☕☕☕☕')
    ], validators=[DataRequired()])
    wifi_rating = SelectField(label = 'Wifi Rating 💪', choices=[
        ('✘'), ('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')
    ], validators=[DataRequired()])

    power_socket_rating = SelectField(label = 'Power Socket Rating 🔌', choices=[
        ('✘'), ('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        print(form.cafe.data)
        print(form.location.data)
        print(form.open_time.data)
        print(form.close_time.data)
        print(form.coffee_rating.data)
        print(form.wifi_rating.data)
        print(form.power_socket_rating.data)
        with open('cafe-data.csv', 'a', encoding="utf-8") as file:
            file.write('\n')
            file.write(f"{form.cafe.data},{form.location.data},{form.open_time.data},{form.close_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_socket_rating.data}")
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes_body=list_of_rows[1:], cafes_head=list_of_rows[0])


if __name__ == '__main__':
    app.run(debug=True)
