from pyfcm import FCMNotification
from flask import Flask, request

app = Flask(__name__)

api_key = "AAAAGwXE9D0:APA91bHENucI7NBQkW5JGLSWbD4V0zyAdLprB4e7hUeQSTc3TXMF3ainy1IKMpkUSQuPLKksNRl5-5T6Q-urBgVPZhAvWNBGZFp7YT4JJ0quxqjJF2zUkYrNjeAVusoWZtLuFkxElQoK"

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
    token = "f7OXGZh89ETmgreDRUPOpj:APA91bGsnwOE1hLwGRuIXZHdXl8cvg0NQKENdX2QeRmk9uWsPlS5u9HLWgRV_zyB5JXKlec1zeu2_-lXr0bNWYmndCIUzllO2Uo50ZHePxbmmr1giHW2bDRQaNekObICZ36pix-g7xpM"

    result = push_service.notify_multiple_devices(registration_ids=token, message_title=title, message_body=content)
    if result:
        return {
            "message": result
        }, 200
    return {
        "message": "fail"
    }, 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)