from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import os

app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # correct method inside the model
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/random", methods=["GET"])
def get_random_cafe():
    """
    Return a random cafe as JSON.
    Uses SQL-level random selection so we don't load the whole table.
    """
    # Faster: pick a random row using SQL (works for SQLite & many DBs)
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()

    # If there are no cafes in DB, return an error JSON (HTTP 404)
    if not random_cafe:
        return jsonify(error={"message": "No cafes available in the database."}), 404

    return jsonify(cafe=random_cafe.to_dict()), 200


if __name__ == '__main__':
    with app.app_context():
        # create tables if not exist
        db.create_all()

        # Optional test seed: only add sample cafes if table empty
        if not Cafe.query.first():
            sample = Cafe(
                name="Coffee Corner",
                map_url="https://goo.gl/maps/example",
                img_url="https://example.com/photo.jpg",
                location="Karachi",
                seats="20",
                has_toilet=True,
                has_wifi=True,
                has_sockets=True,
                can_take_calls=False,
                coffee_price="$2.50"
            )
            db.session.add(sample)
            db.session.commit()
            print("Inserted one sample cafe for testing.")

    app.run(debug=True)
