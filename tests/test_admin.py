import pytest, json 
from application import app
from models.products import products
from admin.admin import admin


 
@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_post(cli_ent):
    response=cli_ent.post('api/v1/admin/products', data=json.dumps(dict(product_name='Timberland shoes',
    price=40,quantity=10)), content_type="application/json")
    data=json.loads(response.data)
    assert "The product has been added" in data["message"]



def test_get(cli_ent):
    response=cli_ent.get('/api/v1/admin/products')
    data=json.loads(response.data)
    if data:
        assert data=={'Products':admin.p.get_products()}
    else:
        assert "There are no products yet" in data["message"]

def test_get_one_pet(cli_ent):
    response=cli_ent.get('/api/v1/admin/products/'+str(1))
    data=json.loads(response.data)
    if data:
        assert data=={'Product':admin.p.get_a_product(product_id=1)}
    else:
        assert "The product wasn\'t found" in data["message"]
        
    


    
      

