import pytest, json
import sys  
sys.path.append('/Users/Andrew/StoreManager/storemanager')
from application import app

 
@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_post(cli_ent):
    response=cli_ent.post('api/v1/products', data=json.dumps(dict(product_name='Timberland shoes',
    price=40,quantity=10)), content_type="application/json")
    data=json.loads(response.data)
    assert "The product was added" in data["message"]

    

