from pyfcm import FCMNotification
from flask import Flask, request

app = Flask(__name__)


push_service = FCMNotification("AAAAGwXE9D0:APA91bGPBRbffiSYqFFLpYiIUDFFDBiT_uwTXkelWydm3zWnzQN-NopZ6fgbKohBOvvZ9Bb7ZSRWDDzGColVJuNjFoG1Ra-M_Xxm5jY3K38sO3WrGErueto-6P7wAXvfdBNxBUfK55x-")

@app.route('/')
def ping():
    return {
        "message": "pong"
    }, 200


@app.route('/push', methods=['POST'])
def sendMessage():
    title = request.json["title"]
    content = request.json["content"]
    token = request.json["token"]

    message = {
        "title": title,
        "content": content
    }
    result = push_service.notify_single_device(registration_id=token, data_message=message)
    print(result)
    if result:
        return {
            "message": result
        }, 200
    return {
        "message": "fail"
    }, 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)