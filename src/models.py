from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,            
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    nameFavorite = db.Column(db.String(30), unique= False, nullable=False)
    typeFavorite = db.Column(db.String(30), unique= False, nullable=False)
    rel = db.relationship('User')

    # def __repr__(self):
    #     return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name_Favorite": self.nameFavorite,
            "type_Favorite": self.typeFavorite,
        }
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namePlanets = db.Column(db.String(30), unique= False, nullable=False)
    diameterPlanets = db.Column(db.String(30), unique= False, nullable=False)
    populationPlanets = db.Column(db.String(30), unique= False, nullable=False)
    terrainPlanets = db.Column(db.String(30), unique= False, nullable=False)    


    def serialize(self):
        return {
            "id": self.id,
            "namePlanets": self.namePlanets,
            "diameterPlanets": self.diameterPlanets,
            "populationPlanets": self.populationPlanets,
            "terrainPlanets": self.terrainPlanets,                        
        }   

class Characters(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique= False, nullable=False)
    hairColor = db.Column(db.String(30), unique= False, nullable=False)
    skinColor = db.Column(db.String(30), unique= False, nullable=False)
    eyeColor = db.Column(db.String(30), unique= False, nullable=False)
    height = db.Column(db.Integer, unique= False, nullable=False)
    birthYear = db.Column(db.String(30), unique= False, nullable=False)
    homeworld = db.Column(db.String(30), unique= False, nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    relationPlanets = db.relationship('Planets')  

    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "birthYear": self.birthYear,
            "hairColor": self.hairColor,
            "skinColor": self.skinColor,
            "eyeColor": self.eyeColor,
            "homeworld": self.homeworld,
            "planets_id": self.planets_id,            
        }




class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nameVehicles = db.Column(db.String(30), unique= False, nullable=False)
    modelVehicles = db.Column(db.String(30), unique= False, nullable=False)
    manufacturerVehicles =db.Column(db.Integer, db.ForeignKey('planets.id')) 
    lengthVehicles = db.Column(db.String(30), unique= False, nullable=False)
    classVehicles = db.Column(db.String(30), unique= False, nullable=False)
    maxAtmospheringSpeedVehicles = db.Column(db.Integer, unique= False, nullable=False)      
    relationPlanets = db.relationship('Planets') 


    def serialize(self):
        return {
            "id": self.id,
            "nameVehicles": self.nameVehicles,
            "modelVehicles": self.modelVehicles,
            "manufacturerVehicles": self.manufacturerVehicles,
            "lengthVehicles": self.lengthVehicles,
            "classVehicles": self.classVehicles,
            "maxAtmospheringSpeedVehicles": self.maxAtmospheringSpeedVehicles,                      
        }   