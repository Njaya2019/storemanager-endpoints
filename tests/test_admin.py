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
    assert data=={'Products':[ {'Product name':'Iphone 6 plus','Price':600,'Quantity':100},
                              {'Product name':'Logitech keyboard','Price':60,'Quantity':150},
                              {'Product name':'Subwoofer Desktop Speakers','Price':20,'Quantity':80},
                              {'Product name':'Timberland shoes','Price':40,'Quantity':10}]}

def test_get_one_pet(cli_ent):
    response=cli_ent.get('/api/v1/admin/products/'+str(3))
    data=json.loads(response.data)
    assert data=={'Product':{'product_name':'Subwoofer Desktop Speakers','price':20,'quantity':80}}


    
      

