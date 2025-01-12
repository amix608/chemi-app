from db import db
class UserModel(db.Model):
    __tablename__="userm"
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(80),unique=True,nullable=False)
    pasword=db.Column(db.String(),nullable=False)