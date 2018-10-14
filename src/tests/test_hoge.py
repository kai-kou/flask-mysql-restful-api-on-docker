from .base import BaseTestCase

import json

from src.app import app


class TestHogeListAPI(BaseTestCase):

  def test_get_hoges_no_data(self):
    response = self.app.get('/hoges')
    self.assert_200(response)
    assert(
      json.loads(response.get_data()) == {'items': []}
    )

  def test_delete_hoges_200(self):
    postPrms = {
      'name': 'hoge',
      'state': 'hoge'
    }
    response = self.app.post('/hoges',
        data=json.dumps(postPrms),
        content_type='application/json'
    )
    self.assert_status(response, 201)

    data = json.loads(response.get_data())
    id = data['id']
    response = self.app.get(f'/hoges/{id}')
    self.assert_status(response, 200)

  def test_get_hoges_one_data(self):
    postPrms = {
      'name': 'hoge',
      'state': 'hoge'
    }
    response = self.app.post('/hoges',
        data=json.dumps(postPrms),
        content_type='application/json'
    )
    self.assert_status(response, 201)

    response = self.app.get('/hoges')
    self.assert_200(response)
    data = json.loads(response.get_data())
    assert(len(data['items']) == 1)


class TestHogeAPI(BaseTestCase):

  def test_get_hoges_404(self):
    response = self.app.get('/hoges/xxx')
    self.assert_404(response)

  def test_post_hoges_201(self):
    prms = {
      'name': 'hoge',
      'state': 'hoge'
    }
    response = self.app.post('/hoges',
        data=json.dumps(prms),
        content_type='application/json'
    )
    self.assert_status(response, 201)

  def test_put_hoges_204(self):
    postPrms = {
      'name': 'hoge',
      'state': 'hoge'
    }
    response = self.app.post('/hoges',
        data=json.dumps(postPrms),
        content_type='application/json'
    )
    self.assert_status(response, 201)

    data = json.loads(response.get_data())
    id = data['id']
    putPrms = {
      'name': 'hoge2',
      'state': 'hoge2'
    }
    response = self.app.put(f'/hoges/{id}',
        data=json.dumps(putPrms),
        content_type='application/json'
    )
    self.assert_status(response, 204)

  def test_delete_hoges_204(self):
    postPrms = {
      'name': 'hoge',
      'state': 'hoge'
    }
    response = self.app.post('/hoges',
        data=json.dumps(postPrms),
        content_type='application/json'
    )
    self.assert_status(response, 201)

    data = json.loads(response.get_data())
    id = data['id']
    response = self.app.delete(f'/hoges/{id}')
    self.assert_status(response, 204)

  def test_get_hoges_200(self):
    postPrms = {
      'name': 'hoge',
      'state': 'hoge'
    }
    response = self.app.post('/hoges',
        data=json.dumps(postPrms),
        content_type='application/json'
    )
    self.assert_status(response, 201)

    data = json.loads(response.get_data())
    id = data['id']
    response = self.app.get(f'/hoges/{id}')
    self.assert_status(response, 200)

