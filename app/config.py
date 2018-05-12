
class DevConfig():
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sharkuser:Aa123456@localhost:3306/pyshark'
    #SQLALCHEMY_TRACK_MODIFICATIONS = True
    #encoding:utf-8
    #dialect+driver://username:password@host:port/database
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'sharkuser'
    PASSWORD = 'Aa123456'
    HOST = 'localhost'
    PORT = '3306'
    DATABASE = 'pyshark'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False