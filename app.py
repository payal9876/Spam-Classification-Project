from flask import Flask


app=Flask(__name__)


@app.route('/',methods=['POST','GET'])

def index():
    return 'this is the nlp project we will love it everyone will love it'
    


if __name__=="__main__":
    app.run()