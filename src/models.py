from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)


    def __repr__(self):
        return '<People %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
        }


    

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)


    def __repr__(self):
        return '<People %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
        }




class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def __repr__(self):
        return '<Favorite %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "planets_id": self.planets_id
            # do not serialize the password, its a security breach
        }



    





        # swapi_id = db.Column(db.String(250), nullable=False)
    # mass = db.Column(db.Integer, nullable=False)
    # hair_color = db.Column(db.String(250), nullable=False)
    # skin_color = db.Column(db.String(250), nullable=False)
    # eye_color = db.Column(db.String(250), nullable=False)
    # birth_year = db.Column(db.String(250), nullable=False)
    # gender = db.Column(db.String(250), nullable=False)
    # created = db.Column(db.String(250), nullable=False)
    # edited = db.Column(db.String(250), nullable=False)
    # homeworld = db.Column(db.String(250), nullable=False)




        # diameter = db.Column(db.Integer, nullable=False)
    # rotation_period = db.Column(db.Integer, nullable=False)
    # orbital_period = db.Column(db.Integer, nullable=False)
    # gravity = db.Column(db.String(250), nullable=False)
    # population = db.Column(db.Integer, nullable=False)
    # climate = db.Column(db.String(250), nullable=False)
    # terrain = db.Column(db.String(250), nullable=False)
    # surface_water = db.Column(db.Integer, nullable=False)
    # created = db.Column(db.String(250), nullable=False)
    # edited = db.Column(db.String(250), nullable=False)
    # name = db.Column(db.String(250), nullable=False)
    # url = db.Column(db.String(250), nullable=False)