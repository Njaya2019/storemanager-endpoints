import pytest, json
from application import app
from storeattendant.storeattendant import storeattendant


@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_post(cli_ent):
    response=cli_ent.post('/api/v1/attendant/sales', data=json.dumps(dict(
    product_name='Iphone 6 plus',quantity=1
    )), content_type="application/json")
    data=json.loads(response.data)
    assert 'The sale has been made' in data["message"]



def test_get__empty_sale_record(cli_ent):
    response=cli_ent.get('/api/v1/attendant/sales/'+str(2))
    data=json.loads(response.data)
    assert response.status_code==404
    assert 'The sale record wasn\'t found' in data["message"]




