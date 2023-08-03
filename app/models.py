from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class Bikes(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)
    price = db.Column(db.Numeric(9, 2))
    make = db.Column(db.String)
    bike_model = db.Column(db.String)
    year = db.Column(db.Integer)
    img = db.Column(db.String)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self,title,rating,price,make,bike_model,year,img):
        self.title = title
        self.rating = rating
        self.price = price
        self.make = make
        self.bike_model = bike_model
        self.year = year
        self.img = img
   

    def save_bike(self):
        db.session.add(self)
        db.session.commit()
        

    def save_chnages(self):
        db.session.commit()


    def to_dic(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'rating' : self.rating,
            'price' : self.price,
            'make' : self.make,
            'model' : self.bike_model,
            'year' : self.year,
            'img' : self.img
                
        }
    
adds = db.Table(
    'adds',
    db.Column('user_id',db.Integer, db.ForeignKey('user.id'),nullable=False),
    db.Column('favourite_id',db.Integer, db.ForeignKey('favourite.id'),nullable=False)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False,unique=True)
    email = db.Column(db.String, nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            'id' : self.id,
            'username': self.username,
            'email': self.email
        }




class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False, unique=True)
    img = db.Column(db.String)
    # added = db.relationship('User',
    #                     secondary = 'adds',
    #                     backref = 'added',
    #                     lazy = 'dynamic'
    #                     )
    # def __init__(self,item_id,user_id):
    #     self.item_id = item_id
    #     self.user_id = user_id

    def __init__(self,item_id,img):
        self.item_id =item_id
        self.img = img

    def save_item(self):
        db.session.add(self)
        # self.added.append(user)
        db.session.commit()

    def delete_item(self):
        db.session.delete(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            'id' : self.id,
            'item_id' : self.item_id,
            'img' : self.img
        }

    # def data_base(self):
    #     db.session.add(self)
    #     db.session.commit()



class Favourite2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False, unique=True)
    img = db.Column(db.String)

    
    def __init__(self,item_id,img):
        self.item_id =item_id,
        self.img = img

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    def delete_item2(self):
        db.session.delete(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            'id' : self.id,
            'item_id' : self.item_id,
            'img' : self.img
        }
    

class Favourite3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False, unique=True)
    img = db.Column(db.String)

    
    def __init__(self,item_id,img):
        self.item_id =item_id,
        self.img = img

    def save_item(self):
        db.session.add(self)
        db.session.commit()
    def delete_item3(self):
        db.session.delete(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            'id' : self.id,
            'item_id' : self.item_id,
            'img' : self.img
        }