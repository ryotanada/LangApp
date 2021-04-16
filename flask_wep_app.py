from flask import Flask, request, jsonify
from langdetect import detect

app = Flask(__name__)


# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is root!!!!"


# GET
@app.route('/users/<user>')
def hello_user(user):
    """
    this serves as a demo purpose
    :param user:
    :return: str
    """
    return "Hello %s!" % user


# POST
@app.route('/', methods=['GET', 'POST'])
def get_text_prediction():
    text = request.data.decode('utf-8')
    lang = detect(text)

    if len(text) == 0:
        return "Invalid Input"

    return "Language is: "+lang


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
