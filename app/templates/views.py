from app import app

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/data')
def getdata():
    # !/usr/bin/python3

    import pymysql

    # 打开数据库连接
    db = pymysql.connect("localhost", "sharkuser", "Aa123456", "pyshark")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    return "Database version : %s " % data

    # 关闭数据库连接
    db.close()