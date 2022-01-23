from flask import Flask, render_template, url_for, redirect, request
from authlib.integrations.flask_client import OAuth
import paypalrestsdk as paypal
from paypalrestsdk import *
import json
import os
from server import Server


with open("secret.json") as json_data_file:
    secret: dict = json.load(json_data_file)

app = Flask(__name__)
app.secret_key = secret.get("app")

app.config['SERVER_NAME'] = 'localhost:8000'
oauth = OAuth(app)
serv = Server("192.168.0.100", 8080)
serv.service()
uuid_ = None


def to_json(func):
    def wrapper(*args, **kwargs):
        get_fun = func(*args, **kwargs)
        return json.dumps(get_fun)

    return wrapper


@app.route('/')
def index():
    return render_template('index.html')

# region Google
@app.route('/google/')
def google():
    # Google Oauth Config
    # Get client_id and client_secret from environment variables
    # For developement purpose you can directly put it here inside double quotes
    GOOGLE_CLIENT_ID = "51021424438-a4l0cshnqgodomj2cjbcqd1okrcm1uk7.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "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"
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    print(" Google User ", user)
    return redirect('/')

# endregion

# region Facebook
@app.route('/facebook/')
def facebook():
    facebook_data: dict = secret.get("facebook")
    FACEBOOK_CLIENT_ID = facebook_data.get("client_id")
    FACEBOOK_CLIENT_SECRET = facebook_data.get("client_secret")
    oauth.register(
        name='facebook',
        client_id=FACEBOOK_CLIENT_ID,
        client_secret=FACEBOOK_CLIENT_SECRET,
        access_token_url='https://graph.facebook.com/oauth/access_token',
        access_token_params=None,
        authorize_url='https://www.facebook.com/dialog/oauth',
        authorize_params=None,
        api_base_url='https://graph.facebook.com/',
        client_kwargs={'scope': 'email'},
    )
    redirect_uri = url_for('facebook_auth', _external=True)
    print(f"redirection : {redirect_uri}")
    print(oauth.facebook.authorize_redirect(redirect_uri))
    return oauth.facebook.authorize_redirect(redirect_uri)


@app.route('/facebook/<_uuid>')
def facebook_(_uuid):
    # Facebook Oauth Config
    global uuid_
    uuid_ = _uuid
    print(f"1 : {_uuid}")
    print(f"2 : {uuid_}")
    facebook_data: dict = secret.get("facebook")
    FACEBOOK_CLIENT_ID = facebook_data.get("client_id")
    FACEBOOK_CLIENT_SECRET = facebook_data.get("client_secret")
    oauth.register(
        name='facebook',
        client_id=FACEBOOK_CLIENT_ID,
        client_secret=FACEBOOK_CLIENT_SECRET,
        access_token_url='https://graph.facebook.com/oauth/access_token',
        access_token_params=None,
        authorize_url='https://www.facebook.com/dialog/oauth',
        authorize_params=None,
        api_base_url='https://graph.facebook.com/',
        client_kwargs={'scope': 'email'},
    )
    redirect_uri = url_for('facebook_auth', _external=True)

    return oauth.facebook.authorize_redirect(redirect_uri)


@app.route('/facebook/auth/')
def facebook_auth():
    print("authentication")
    token = oauth.facebook.authorize_access_token()
    resp = oauth.facebook.get(
        'https://graph.facebook.com/me?fields=id,name,email')
    profile = resp.json()
    print("Facebook User ", profile)
    profile.update({"uuid": uuid_})
    serv.write({101: profile})
    print("end")
    return redirect('/')

# endregion

# region Paypal

@app.route('/paypal')
def paypal_init():
    amount = request.args.get("amount")
    name = request.args.get("name")
    msg = request.args.get("msg")
    paypal_data: dict = secret.get("paypal")
    paypal.configure({
        "mode": "sandbox",  # sandbox or live
        "client_id": paypal_data.get("client_id"),
        "client_secret": paypal_data.get("client_secret")})
    history = paypal.Payment.all({"count": 50})
    history_dic = {}
    history_list = []
    for payment in history.payments:
        history_dic['payment_id'] = payment.id
        history_dic['sale_id'] = payment.transactions[0].related_resources[0].sale.id
        history_dic['amount'] = payment.transactions[0].amount.total + " " + history.payments[0].transactions[0].amount.currency
        history_list.append(history_dic)
        history_dic = {}
    return render_template("paypal.html", **locals())

@app.route('/paypal_Return', methods=['GET'])
def paypal_Return():
    # ID of the payment. This ID is provided when creating payment.
    paymentId = request.args['paymentId']
    payer_id = request.args['PayerID']
    payment = paypal.Payment.find(paymentId)

    # PayerID is required to approve the payment.
    if payment.execute({"payer_id": payer_id}):  # return True or False
        print("Payment[%s] execute successfully" % (payment.id))
        return 'Payment execute successfully!' + payment.id
    else:
        print(payment.error)
        return 'Payment execute ERROR!'


@app.route('/paypal_payment', methods=['GET'])
def paypal_payment():
    amount = str(request.args.get("amount"))
    name = request.args.get("name")
    msg = request.args.get("msg")

    payment = paypal.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:8000/paypal_Return?success=true",
            "cancel_url": "http://localhost:8000/paypal_Return?cancel=true"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": name,
                    "sku": "item",
                    "price": amount,
                    "currency": "EUR",
                    "quantity": 1}]},
            "amount": {
                "total": amount,
                "currency": "EUR"},
            "description": msg}]})

    # payment = paypal.Payment()
    if payment.create():
        print("Payment[%s] created successfully" % (payment.id))
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = str(link.href)
                print("Redirect for approval: %s" % (redirect_url))
                return redirect(redirect_url)
    else:
        print("Error while creating payment:")
        print(payment.error)
        return "Error while creating payment"


@app.route('/credit_card_payment', methods=['GET'])
def credit_card_payment():
    # Payment
    # A Payment Resource; create one using
    # the above types and intent as 'sale'
    payment = Payment({
        "intent": "sale",

        # Payer
        # A resource representing a Payer that funds a payment
        # Use the List of `FundingInstrument` and the Payment Method
        # as 'credit_card'
        "payer": {
            "payment_method": "credit_card",

            # FundingInstrument
            # A resource representing a Payeer's funding instrument.
            # Use a Payer ID (A unique identifier of the payer generated
            # and provided by the facilitator. This is required when
            # creating or using a tokenized funding instrument)
            # and the `CreditCardDetails`
            "funding_instruments": [{

                # CreditCard
                # A resource representing a credit card that can be
                # used to fund a payment.
                "credit_card": {
                    "type": "visa",
                    "number": "4032037537194421",
                    "expire_month": "11",
                    "expire_year": "2021",
                    "cvv2": "875",
                    "first_name": "twtrubiks",
                    "last_name": "test",

                    # Address
                    # Base Address used as shipping or billing
                    # address in a payment. [Optional]
                    "billing_address": {
                        "line1": "1 Main St",
                        "city": "San Jose",
                        "state": "CA",
                        "postal_code": "95131",
                        "country_code": "US"}}}]},

        # Transaction
        # A transaction defines the contract of a
        # payment - what is the payment for and who
        # is fulfilling it.
        "transactions": [{

            # ItemList
            "item_list": {
                "items": [{
                    "name": "item",
                    "sku": "item",
                    "price": "30.00",
                    "currency": "USD",
                    "quantity": 1}]},

            # Amount
            # Let's you specify a payment amount.
            "amount": {
                "total": "30.00",
                "currency": "USD"},
            "description": "This is the payment transaction description."}]})

    # Create Payment and return status( True or False )
    if payment.create():
        print("Payment[%s] created successfully" % (payment.id))
        return "Payment " + payment.id + " created successfully"
    else:
        # Display Error message
        print("Error while creating payment:")
        print(payment.error)
        return "Payment Error!"


@app.route('/API/refund_payment', methods=['POST'])
@to_json
def refund_payment():
    sale_id = request.json.get('sale_id')
    amount = request.json.get('amount')
    sale = Sale.find(sale_id)

    # Make Refund API call
    # Set amount only if the refund is partial
    refund = sale.refund({
        "amount": {
            "total": int(amount),
            "currency": "USD"}})

    if refund.success():
        print("Refund[%s] Success" % (refund.id))
        return 11
    else:
        print("Unable to Refund")
        print(refund.error)
        return 44

# endregion

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')

