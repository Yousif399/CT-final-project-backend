from flask import Blueprint,request, jsonify
import json
import os
import stripe




payment = Blueprint('payment', __name__,url_prefix='/pay')

stripe.api_key = os.environ.get('STRIPE_KEY')

def check_total(cart):
    pass


@payment.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        print(data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount= 100,
            #userr
            currency='cad',
            payment_method_types=['card']
        )
        return jsonify({
            'clientSecret': intent['client_secret']
        }), 200
    except Exception as e:
        return jsonify(error=str(e)), 403