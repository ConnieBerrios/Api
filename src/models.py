from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    nameFavorite = db.Column(db.String(30), unique= False, nullable=False )
    typeFavorite = db.Column(db.String(30), unique=False, nullable=False)
    relationUser = db.relationship("User")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "nameFavorite": self.nameFavorite,
            "typeFavorite": self.typeFavorite
        }

class Planet(db.Model):
    
    id = db.Column(db.Integer, )
    name = db.Column(db.String(50), primary_key=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            
        }

class Characters(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),  nullable = False)
    homeworld = db.Column(db.String(50), db.ForeignKey('planet.name'))
    relationPlanet = db.relationship("Planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "homeworld": self.homeworld
            
        }