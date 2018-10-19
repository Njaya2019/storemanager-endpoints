import pytest, json
from application import app

@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_post(cli_ent):
    response=cli_ent.post('/api/v1/attendant/sales', data=json.dumps(dict(
    product_name='Iphone 6 plus',quantity=1
    )), content_type="application/json")
    data=json.loads(response.data)
    assert "The transaction has been completed" in data["message"]

def test_get_sale_record(cli_ent):
    response=cli_ent.get('/api/v1/attendant/sales/'+str(2))
    data=json.loads(response.data)
    assert data=={'Sale':[{'product name':'Iphone 6 plus',
                        'Date sold':'Oct 10, 2018 6:25 P.M',
                        'Total cost':600,'Quantity bought':1}]}




