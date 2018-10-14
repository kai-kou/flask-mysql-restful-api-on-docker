from flask_testing import TestCase

from src.app import app

from src.database import db, init_db


class BaseTestCase(TestCase):
  def create_app(self):
    app.config.from_object('src.config.TestingConfig')
    return app

  def setUp(self):
    self.app = self.app.test_client()
    db.create_all()
    db.session.commit()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
