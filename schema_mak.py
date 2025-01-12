from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    
class PlaintagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
   


class ItemSchema(PlainItemSchema):
    store_id = fields.Str(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(PlainStoreSchema):
    item = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
class UserSchema(Schema):
    id=fields.Int(dump_only=True)
    user_name=fields.Str(required=True)
    pasword=fields.Str(required=True)


    


