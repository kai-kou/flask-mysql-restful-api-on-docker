from flask_restful import Resource, reqparse, abort

from flask import jsonify

from models.hoge import HogeModel, HogeSchema

from database import db


class HogeListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', required=True)
    self.reqparse.add_argument('state', required=True)
    super(HogeListAPI, self).__init__()


  def get(self):
    results = HogeModel.query.all()
    jsonData = HogeSchema(many=True).dump(results).data
    return jsonify({'items': jsonData})


  def post(self):
    args = self.reqparse.parse_args()
    hoge = HogeModel(args.name, args.state)
    db.session.add(hoge)
    db.session.commit()
    res = HogeSchema().dump(hoge).data
    return res, 201


class HogeAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name')
    self.reqparse.add_argument('state')
    super(HogeAPI, self).__init__()


  def get(self, id):
    hoge = db.session.query(HogeModel).filter_by(id=id).first()
    if hoge == None:
      abort(404)

    res = HogeSchema().dump(hoge).data
    return res


  def put(self, id):
    hoge = db.session.query(HogeModel).filter_by(id=id).first()
    if hoge == None:
      abort(404)
    args = self.reqparse.parse_args()
    for name, value in args.items():
      if value is not None:
        setattr(hoge, name, value)
    db.session.add(hoge)
    db.session.commit()
    return None, 204


  def delete(self, id):
    hoge = db.session.query(HogeModel).filter_by(id=id).first()
    if hoge is not None:
      db.session.delete(hoge)
      db.session.commit()
    return None, 204
