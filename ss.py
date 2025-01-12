
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schema_mak import StoreSchema
from models.store import StoreModel
from sqlalchemy.exc import SQLAlchemyError
from db import db


blp = Blueprint("Stores", __name__, description="Operations on stores")

@blp.route("/store")
class xura(MethodView):
   @jwt_required()
   @blp.response(200,StoreSchema(many=True))
   def get(self):
        return StoreModel.query.all()

  
   @blp.arguments(StoreSchema)
   @blp.response(201,StoreSchema)
   def post(self,axali_data):
        store=StoreModel(**axali_data)
        try:
            db.session.add(store)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="hui")
        return store

       
@blp.route("/store/<string:store_id>")
class xura1(MethodView):
    @jwt_required()
    @blp.response(200,StoreSchema)
    def get(self,store_id):
        store=StoreModel.query.get_or_404(store_id)
        return store
    @jwt_required()
    def delete(self,store_id):
         store=StoreModel.query.get_or_404(store_id)
         db.session.delete(store)
         db.session.commit()
         return{"message":"wavshale store"}