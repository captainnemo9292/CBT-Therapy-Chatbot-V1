# import flask dependencies
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/)
def index():
    return render_template("index.html")

# function for responses
def results():

    # build a request object
    req = request.get_json(force=True)
    logger.info("Incoming request: %s", req)

    # fetch action from json
    #action = req.get('queryResult').get('action')
    #logger.info('Detected action %s', action)

    #get intent name
    intent = get_intent_from_req(req)
    logger.info('Detected intent %s', intent)

    # return a fulfillment response
    return {'fulfillmentText': 'This is a response from webhook.'}

#get intent name from dialogflow request
def get_intent_from_req(req):

    try:
        intent_name = req['queryResult']['intent']['displayName']

    except KeyError:
        return None

    return intent_name

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()
