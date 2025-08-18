from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_random_cafe():
    cafes = Cafe.query.all()
    print(cafes)
    if cafes:
        random_cafe = random.choice(cafes)
        return jsonify(cafe=random_cafe.to_dict())
    else:
        return jsonify(error="No cafes found"), 404

@app.route("/all", methods=['GET'])
def get_all_cafes():
    cafes = Cafe.query.all()
    if cafes:
        cafes_list = []
        for cafe in cafes:
            cafes_list.append(cafe.to_dict())
        return jsonify(cafe=cafes_list)

    else:
        return jsonify(error="No cafes found"), 404
    
@app.route("/search", methods=["GET"])
def search_cafes():
    # Get the location from the query parameter (?loc=...)
    query_location = request.args.get("loc")
    
    if not query_location:
        return jsonify(error="Please provide a location using the 'loc' query parameter."), 400

    # Filter cafes by location (case-sensitive exact match)
    cafes = Cafe.query.filter_by(location=query_location).all()

    if cafes:
        cafes_list = [cafe.to_dict() for cafe in cafes]
        return jsonify(cafes=cafes_list)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(int(request.form.get("has_toilet"))),
            has_wifi=bool(int(request.form.get("has_wifi"))),
            has_sockets=bool(int(request.form.get("has_sockets"))),
            can_take_calls=bool(int(request.form.get("can_take_calls"))),
            coffee_price=request.form.get("coffee_price")
        )

        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response={"success": "Successfully added the new cafe."}), 201

    except Exception as e:
        return jsonify(error={"message": str(e)}), 400

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        try:
            cafe = db.get(Cafe, cafe_id)
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
