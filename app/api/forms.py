# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, EqualTo

# class SignUp(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired()])
#     password = PasswordField('Passowrd', validators=[DataRequired()])
#     confirm_passowrd = PasswordField('Confirm Passowrd', validators=[DataRequired(), EqualTo('password')])
#     Sign_UP = SubmitField()




# TXTTT USEFUL 
# @api.get('/bike')
# def get_bike():
#     bike = Bikes.query.all()
#     bike_list = [b.to_dic() for b in bike]
#     return {
#         'status' : 'ok',
#         'bike' : bike_list
#     }



    # x = Bikes.query.filter_by(id = int(data['uId'])).all()
    # list_of_bike = [b.to_dic() for b in x]
    # if x:
    #     print(x)