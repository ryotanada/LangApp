from flask import Flask, request
from langdetect import detect

app = Flask(__name__)


# root
@app.route("/")
def index():
    return "Root"


# POST
@app.route('/', methods=['GET', 'POST'])
def get_text_prediction():
    text = request.data.decode('utf-8')
    lang = detect(text)

    if len(text) == 0:
        return "Invalid Input"

    print("incoming: "+text+", outcoming: "+lang) 
    
    return "Language is: "+lang


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
