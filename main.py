from pyfcm import FCMNotification
from flask import Flask, request

app = Flask(__name__)

APIKEY = "AAAAGwXE9D0:APA91bHZncDSGBtGqifCp4mz8dF-3729qKt0GWcmu5mBcL1oESAUIAuhz-infW0YrxUru3PByJ7jnKURrTCWJteostlrCZbvR1nbG-CDDlKt_YtfG3OzRRoc4XtILNJqts1cEqBoelHJ"

push_service = FCMNotification(APIKEY)


@app.route('/')
def ping():
    return {
        "message": "pong"
    }, 200


@app.route('/push', methods=['POST'])
def sendMessage():
    title = request.json("title")
    content = request.json("content")
    token = request.json("token")

    message = {
        "title": title,
        "content": content
    }
    result = push_service.notify_single_device(registration_id=token, data_message=message)
    print(result)
    if result:
        return {
            "message": "push"
        }, 200
    return {
        "message": "fail"
    }, 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)