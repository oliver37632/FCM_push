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
    body = request.json["content"]

    message = {
        "body": body,
        "title": title
    }

    result = push_service.notify_multiple_devices(registration_ids=registration_ids, data_message=message)

    return {
            "message": result
        }, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)





