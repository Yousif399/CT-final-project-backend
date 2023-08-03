from flask import Blueprint,request, json,render_template,redirect
# from .forms import SignUp
from ..models import Bikes, User, Favourite,Favourite2,Favourite3
from werkzeug.security import check_password_hash
from flask_login import login_user,current_user

api = Blueprint('api', __name__,url_prefix='/api')




@api.post('/get-user')
def get_user():
    data = request.get_json()
    username = data['uId']
    email = data['email']
    password = data['password']
    user = User(username = username, email=email, password=password)
    print(user)
    user.save_user()

    return{
        'status' : 'ok',
        'axios_msg' : 'it\'s working',
        'user' :user.to_dict()
        }
    
        
@api.post('/signin')
def sign_user():
    data = request.get_json()
    print(data)
    email = data['email']
    password= data['password']
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            print(f"welcome bckkkk {email}")
            # login_user(user)
        else:
            print('wrongggggg passss')
            return('yes')
    
    else:
        print('no such  a userrrrr')
        return('yes')
 
    return{
        'status' : 'ok',
        'axios_msg' : 'it\'s working',
        'data' :data
        }


# tv SHOWS
@api.post('/favourite')
def add_to_fav():
    data = request.get_json()
    item_id = data[0]
    img = data[1]
    favourite = Favourite(item_id = item_id, img=img)
    favourite.save_item()
    print(favourite.id)
    return{
        'status' : 'ok',
        'axios_msg' : 'it\'s working',
        'data' :data
        }
# DELETE
@api.post('/delete/favourite')
def delete_fav():
    data = request.get_json()
    item_id = data[0]
    img = data[1]
    favourite = Favourite.query.get(id)
    if favourite:
        favourite.id.delete_item()
    else:
        print('didnt work ')

        
    print('deleted')
    return {
            'status': 'error',
            'message': 'Item not found in favorites.'
            }

    # return{
    #     'status' : 'ok',
    #     'axios_msg' : 'it\'s working',
    #     'data' :data
    #     }

      

@api.get('/get-fav')
def get_fav():
    favourite = Favourite.query.all()
    favourite_list = [f.to_dict() for f in favourite]
    return{
        'status' : 'ok',
        'axios_msg' : 'it\'s working',
        'data' :favourite_list
        }

# ?animes
@api.post('/favourite/anime')
def add_to_fav_anime():
    data = request.get_json()
    item_id = data[0]
    img = data[1]
    favourite = Favourite2(item_id = item_id, img=img)
    favourite.save_item()
    print(data)
    return{
        'status' : 'ok',
        'axios_msg' : 'it\'s working',
        'data' :data
        }
      

@api.get('/get-fav/anime')
def get_fav_anime():
    favourite = Favourite2.query.all()
    favourite_list = [f.to_dict() for f in favourite]
    return{
        'status' : 'ok',
        'axios_msg' : 'it\'s working',
        'data' :favourite_list
        }

# movies
@api.post('/favourite/movie')
def add_to_fav_movie():
    data = request.get_json()
    item_id = data[0]
    img = data[1]

    favourite = Favourite3(item_id = item_id, img=img)
    favourite.save_item()
    print(data)
    return{
        'status' : 'ok',
        'axios_msg' : 'it\'s working',
        'data' :data
        }
      

@api.get('/get-fav/movie')
def get_fav_movie():
    favourite = Favourite3.query.all()
    favourite_list = [f.to_dict() for f in favourite]
    return{
        'status' : 'ok',
        'axios_msg' : 'it\'s working',
        'data' :favourite_list
        }




