import pytest, json
from application import app

 
@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_get(cli_ent):
    response=cli_ent.get('/api/v1/admin/sales')
    data=json.loads(response.data)
    assert data== {'Sales':[{'sale_id':1,'attendant_id':2,'product_id':2,'date':'Oct 10, 2018 5:00 P.M','transanction_cost':59.98},
                  {'sale_id':2,'attendant_id':1,'product_sold':1,'date':'Oct 10, 2018 6:25 P.M','transanction_cost':100},
                  {'sale_id':3,'attendant_id':3,'product_id':3,'date':'Oct 10, 2018 7:30 P.M','transanction_cost':60}]}