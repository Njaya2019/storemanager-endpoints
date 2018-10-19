import pytest, json
from application import app

 
@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_get(cli_ent):
    response=cli_ent.get('/api/v1/admin/sales')
    data=json.loads(response.data)
    assert data== {'Sales':[{"product name": "Logitech keyboard","Date sold": "Oct 10, 2018 5:00 P.M","Total cost": 120,"Quantity bought": 2,},
                            {"product name": "Iphone 6 plus","Date sold": "Oct 10, 2018 6:25 P.M","Total cost": 600,"Quantity bought": 1},
                            {"product name": "Subwoofer Desktop Speakers","Date sold": "Oct 10, 2018 7:30 P.M","Total cost": 20,"Quantity bought": 1}]}


def test_get_sale_record(cli_ent):
    response=cli_ent.get('/api/v1/admin/sales/'+str(2))
    data=json.loads(response.data)
    assert data=={'Sale':{'product name':'Iphone 6 plus',
    'Date sold':'Oct 10, 2018 6:25 P.M',
    'Total cost':600,'Quantity bought':1}}