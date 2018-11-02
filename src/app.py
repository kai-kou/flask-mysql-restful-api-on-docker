from flask import Flask, jsonify

from flask_restful import Api

from src.database import init_db

from src.apis.parent import ParentListAPI, ParentAPI

from src.apis.hoge import HogeListAPI, HogeAPI


def create_app():

  app = Flask(__name__)
  app.config.from_object('src.config.Config')

  init_db(app)

  api = Api(app)
  api.add_resource(ParentListAPI, '/parents')
  api.add_resource(ParentAPI, '/parents/<id>')
  api.add_resource(HogeListAPI, '/hoges')
  api.add_resource(HogeAPI, '/hoges/<id>')

  return app


app = create_app()
