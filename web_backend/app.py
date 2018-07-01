from flask import Flask,request
import json
import sys
from flask_cors import CORS
import urllib
from eval import TestModel
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hgjdfgfdkj552'

CORS(app)

@app.route('/', methods = ['GET'])
def mainRoute():
    return 'hello, world'

@app.route('/rcv', methods=['GET'])
def receive():
    # if request.method=='GET':
    # print(request.args.get('data'))
    try:
        # data = request.get_json(silent = True, force = True)
        data = json.loads(urllib.parse.unquote(request.args.get('data')))
        # return json.dumps({"message": request.args.get('data')})
        try:
            messages = data.get('messages')
            if len(messages) > 0:
                m = TestModel()
                # return json.dumps({"message": m.testModel(" ".join(messages))})
                result = m.testModel(" ".join(messages))
                if result == 1.0:
                    dictToSend = {
                        "applicationKeys": {
                            "private": "W6XOsV2XW54WRJSm_k77WrcfcBo4POs6InqUrbMVcSk",
                            "public": "BJUDmwELkrENeGIZIAcN6w6p0U13FYardqmxTKF3th0VJcOHQLT7VkmVXDABgocHBxUlH2oHAl9f2wbX_RNe5gw"
                        },
                        "data": "Hello",
                        "subscription": {"endpoint":"https://fcm.googleapis.com/fcm/send/cg-OI7N8yVE:APA91bEm2egJWUwxYhLxqYg4myLWDw1aWdE7ynmoO1Z_-J5LGilFU5h0lvnRz6bXU_7SuPW6ZoM1OUOYKipS3tpbKSQypWSHZfDhaNhQSKFM9s-zTmJsDROWlLr51wQngS1W6X7OH_q1jZQPRtFRGGfLhRhchprLbw","expirationTime":None,"keys":{"p256dh":"BDlDjRAf5YpQWnf44H-G7nYHiJWgPqtt31NrHyOsdlijlpHUXQ8OuJq0WfE8qOMKcwkTsLu9obujVjEfi354En4","auth":"PDaw6it1j-FN2G10jxtojw"}}
                    }
                    res = requests.post('https://web-push-codelab.glitch.me/api/send-push-msg', json=dictToSend)     
                    dictFromServer = res.json()
                    return json.dumps({"success": True})
                else:
                    return json.dumps({"success": False})
            else:
                return json.dumps({"error": "No messages received"})
        except AttributeError:
            return json.dumps({"error": "No messages received"})
    except (ValueError, TypeError, KeyError):
        print("Error caught")

# @app.route('/rcv',methods=['POST'])
# def send_recieve():
#    flag = False
#     # return 'hello'
#    if request.method=='POST':
#       try:
#          data = request.get_json(silent=True, force=True)
#          try:
#             action = data.get('queryResult').get('action')
#             text = data.get('originalDetectIntentRequest').get('payload').get('inputs')[0].get('arguments')[0].get('rawText')

#             if text.find("save") != -1:
#                flag = True

#             if action == "save" or flag == True:
#                # return json.dumps({"fulfillmentText": "We will save you."})
#                # return json.dumps({ "intent": "actions.intent.PLACE", "inputValueData": { "@type": "type.googleapis.com/google.actions.v2.PlaceValueSpec", "dialog_spec": { "extension": { "@type": "type.googleapis.com/google.actions.v2.PlaceValueSpec.PlaceDialogSpec", "requestPrompt": "What is your location?", "permissionContext": "To locate a helper" } } } })
#                return json.dumps({"fullfillmentText": "Help is on the way! "})
#             elif action == "input.welcome":
#                return json.dumps({"fulfillmentText": "Welcome to Safety Bee!"})

#          except AttributeError:
#             return json.dumps({"fulfillmentText": "An error occured."})
#       except (ValueError,TypeError,KeyError):
#          print("Error caught")
#           #send response something is wrong
#           #return json.dumps(control)
#    else:
#       return 'false'

if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True, host='0.0.0.0')