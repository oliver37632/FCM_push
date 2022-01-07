from pyfcm import FCMNotification
from flask import Flask, request
from config import api_key, registration_ids

app = Flask(__name__)

push_service = FCMNotification(api_key)


@app.route('/')
def ping():
    return {
        "message": "pong"
    }, 200


@app.route('/push', methods=['POST'])
def sendMessage():
    title = request.json["title"]
    content = request.json["content"]

    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=title, message_body=content)

    return {
            "message": result
        }, 200


if __name__ == '__main__':
    app.run(debug=True)
