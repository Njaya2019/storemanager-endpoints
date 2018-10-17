import pytest, json
from application import app

@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_post(cli_ent):
    response=cli_ent.post('/api/v1/attendant/sales', data=json.dumps(dict(attendant_id=1,
    product_id=2,date='Oct 9, 2018 2:52 P.M',transanction_cost=80)), content_type="application/json")
    data=json.loads(response.data)
    assert "The transaction has been completed" in data["message"]


