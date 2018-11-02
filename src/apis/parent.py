from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.models.parent import ParentModel, ParentSchema

from src.database import db


class ParentListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', required=True)
    super(ParentListAPI, self).__init__()


  def get(self):
    results = ParentModel.query.all()
    jsonData = ParentSchema(many=True).dump(results).data
    return jsonify({'items': jsonData})


  def post(self):
    args = self.reqparse.parse_args()
    parent = ParentModel(args.name)
    db.session.add(parent)
    db.session.commit()
    res = ParentSchema().dump(parent).data
    return res, 201


class ParentAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name')
    super(ParentAPI, self).__init__()


  def get(self, id):
    parent = db.session.query(ParentModel).filter_by(id=id).first()
    if parent == None:
      abort(404)

    res = ParentSchema().dump(parent).data
    return res


  def put(self, id):
    parent = db.session.query(ParentModel).filter_by(id=id).first()
    if parent == None:
      abort(404)
    args = self.reqparse.parse_args()
    for name, value in args.items():
      if value is not None:
        setattr(parent, name, value)
    db.session.add(parent)
    db.session.commit()
    return None, 204


  def delete(self, id):
    parent = db.session.query(ParentModel).filter_by(id=id).first()
    if parent is not None:
      db.session.delete(parent)
      db.session.commit()
    return None, 204
