"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favorite, People, Planets 
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])                        #USER GET
def handle_hello_user():
    users = User.query.all()        # Query all users from the database
    response_body = [               # Format users into a list of dictionaries
        {"id": user.id, 
         "email": user.email, 
         "is_active": user.is_active}
        for user in users
    ]
    return jsonify(response_body), 200  # Return the response

@app.route('/user', methods=['POST'])                  #USER POST
def add_new_user():
    request_body = request.json
    email = request_body.get("email")
    password = request_body.get("password")
    is_active = request_body.get("is_active", True) 
    user = User(email=email, password=password, is_active=is_active)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added successfully", "user": {"email": email, "is_active": is_active}}), 201


@app.route('/user/<int:user_id>', methods=['DELETE'])  #USER DELETE    
def delete_user(user_id):
    user = User.query.get(user_id)                  # Fetch the user by ID
    db.session.delete(user)                         # Delete the user from the database
    db.session.commit()                             # Commit the deletion
    return jsonify([{"id": user.id, "email": user.email} for user in User.query.all()]), 200  # Return the updated list of users




@app.route('/user/<int:id>/favorites', methods=['GET'])              #GET USER FAVORITE
def handle_hello_favorites(id):
    response_body = {
        "msg": "Hello, this is your GET /user/favorites response "
    }
    return jsonify(response_body), 200



@app.route('/people', methods=['GET'])                      #GET ALL PEOPLE
def get_all_people():
    all_people = People.query.all()  # Fetch all records from the People table
    all_people = list(map(lambda x: x.serialize(), all_people))
    return jsonify(all_people), 200  # Return the list of people as a JSON response


@app.route('/people/<int:people_id>', methods=['GET'])      # GET request for a single PERSON
def get_single_person(people_id):
    person = People.query.get(people_id)                    # Fetch a single person by their ID
    response_body = {                                       # Convert the person object to a dictionary
        "id": person.id,                                    # Include the person's ID
        "name": person.name,                                # Include the person's name
        "url": person.url                                   # Include the person's URL
    }
    return jsonify(response_body), 200                      # Return the person's data as a JSON response

@app.route('/people/<int:person_id>', methods=['DELETE'])  #PERSON DELETE    
def delete_person(person_id):
    person = person.query.get(person_id)                  # Fetch the PERSON by ID
    db.session.delete(person)                         # Delete the person from the database
    db.session.commit()                             # Commit the deletion
    return jsonify([{"id": person.id, "email": person.email} for person in person.query.all()]), 200  # Return the updated list of persons








@app.route('/planets', methods=['GET'])                      #GET ALL PLANETS
def get_all_planets():
    all_planets = Planets.query.all()  # Fetch all records from the People table
    all_planets = list(map(lambda x: x.serialize(), all_planets))
    return jsonify(all_planets), 200  # Return the list of people as a JSON response


@app.route('/planets/<int:planet_id>', methods=['GET'])      # GET request for a single PLANET
def get_single_planet(planet_id):
    planet = People.query.get(planet_id)                    # Fetch a single planet by their ID
    response_body = {                                       # Convert the planet object to a dictionary
        "id": planet.id,                                    # Include the planet's ID
        "name": planet.name,                                # Include the planet's name
        "url": planet.url                                   # Include the planet's URL
    }
    return jsonify(response_body), 200                      # Return the person's data as a JSON response






# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
