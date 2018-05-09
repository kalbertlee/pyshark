from ext import db
from app import app
db.init_app(app)

class User(db.Model):
    __tablename__ = 'my_user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255))

class Address(db.Model):
    __tablename__ = 'my_address'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User',back_populates='user')

User.addresses = db.relationship('Address', order_by=Address.id, back_populates='user')

def testdb():
    print('start test db')
    db.drop_all()
    db.create_all()

    user1 = User(name = 'xiaoming')
    user1.addresses = [Address(email = 'a@git.com',user_id=user1.id), Address(email = 'b@git.com',user_id=user1.id)]

    db.session.add(user1)
    db.session.commit()