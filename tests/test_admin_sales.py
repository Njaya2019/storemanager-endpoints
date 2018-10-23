import pytest, json
from application import app
from admin.admin_sales import admin_sales

 
@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_get(cli_ent):
    response=cli_ent.get('/api/v1/admin/sales')
    data=json.loads(response.data)
    if not data:
        assert "There are no sales records yet" in data["message"]
    assert data== {"Sales":admin_sales.s.get_sales()}


def test_get_sale_record(cli_ent):
    response=cli_ent.get('/api/v1/admin/sales/'+str(2))
    data=json.loads(response.data)
    if not data:
        assert 'The sale record wasn\'t found' in data["message"]
    assert data=={'Sale':admin_sales.s.get_sale()}