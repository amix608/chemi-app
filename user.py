from flask_smorest import Blueprint,abort
from flask.views import MethodView
from passlib.hash import pbkdf2_sha256
from db import db
from blocklist import BLOCKLIST
from models import UserModel
from schema_mak import UserSchema
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity,jwt_required,get_jwt
blp=Blueprint("user","user" ,description="usereniii")

@blp.route("/regi")

class userregister(MethodView):
    @blp.arguments(UserSchema)
    def post(self,user_data):
        if UserModel.query.filter(UserModel.user_name==user_data["user_name"]).first():
            abort(409,message="user_name already exists")
        user=UserModel(
            user_name=user_data["user_name"],
            pasword=pbkdf2_sha256.hash(user_data["pasword"])
        )
        db.session.add(user)
        db.session.commit()
        return {"message":"useri daemata ."},201
    @blp.response(200,UserSchema(many=True))
    def get(self):
        return UserModel.query.all()


@blp.route("/regi/<string:user_id>")
class useridregister(MethodView):
    @blp.response(200,UserSchema)
    def get(self,user_id):
        return UserModel.query.get_or_404(user_id)
    def delete(self,user_id):
        user=UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message":"wavshale useri"}
    @blp.route("/login")
    class loginuser(MethodView):
        @blp.arguments(UserSchema)
        def post(self,user_data):
            user=UserModel.query.filter(
                UserModel.user_name==user_data["user_name"]
            ).first()
            if user and pbkdf2_sha256.verify(user_data["pasword"],user.pasword):
                acses_tkn=create_access_token(identity=user.id,fresh=True),
                refresh_tkn=create_refresh_token(identity=user.id)
                return {"acseses_token is":acses_tkn,"refresh token": refresh_tkn}
                abort(401,mesage="ver gavagzavne acses tokeni")

    @blp.route("/logout")
    class logoutuser(MethodView):
         @jwt_required()
         def post(self):
             jti=get_jwt()["jti"]
             BLOCKLIST.add(jti)
             return {"mesage":"gamovida warmatebiy"}
    @blp.route("/refresh")
    class refreshtkn(MethodView):
        @jwt_required(refresh=True)
        def post(self):
            cur_user=get_jwt_identity()
            new_token=create_access_token(identity=cur_user,fresh=False)
            return {"new is":new_token}

