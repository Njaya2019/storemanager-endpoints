import pytest, json 
from application import app

 
@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_post(cli_ent):
    response=cli_ent.post('api/v1/admin/products', data=json.dumps(dict(product_name='Timberland shoes',
    price=40,quantity=10)), content_type="application/json")
    data=json.loads(response.data)
    assert "The product was added" in data["message"]



def test_get(cli_ent):
    response=cli_ent.get('/api/v1/admin/products')
    data=json.loads(response.data)
    assert data=={'Products':[ {'product_name':'Iphone 6 plus','price':600,'quantity':100},
                              {'product_name':'Logitech keyboard','price':60,'quantity':150},
                              {'product_name':'Subwoofer Desktop Speakers','price':20,'quantity':80},
                              {'product_name':'Timberland shoes','price':40,'quantity':10}]}

def test_get_one_pet(cli_ent):
    response=cli_ent.get('/api/v1/admin/products/'+str(3))
    data=json.loads(response.data)
    assert data=={'Product':{'product_name':'Subwoofer Desktop Speakers','price':20,'quantity':80}}


    
      

