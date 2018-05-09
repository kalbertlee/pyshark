from app import app
from app.templates import testdb

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/data')
def getdata():
    pass

@app.route('/test')
def test():
    testdb.testdb()