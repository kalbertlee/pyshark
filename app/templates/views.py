from app import app

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/data')
def getdata():
    pass