from models.sales import sales
from models.products import products
import pytest

p=products('Iphone 7',800,40)
p.add_product()
s=sales('Iphone 7', 2)
sa=sales('Iphone 8', 2)
sp=sales('Iphone 7', 41)
def test_make_sale():
    sale=s.make_sale()
    assert sale=={'sale_id':1,'attendant_id':1, 'product_id':1, 'quantity':2, 'date':s.date_sale_made,'transanction_cost':1600} 

def test_gate_sales():
    sales_records=s.get_sales()
    assert sales_records==[{'Product name':'Iphone 7','Date sold':s.date_sale_made, 'Total cost':1600, 'Quantity bought':2,'Sale id':1}]

def test_sale_product_exist():
    pro_not_found=sa.make_sale()
    assert pro_not_found=='The product is not in the inventory'

def test_sale_produc_stock():
    qty_exceeds=sp.make_sale()
    assert qty_exceeds=='Quantity to be bought exceeds amount in invetory'

def test_products_inventory():
    sl=sales('subwoofer',2)
    no_products=sl.make_sale()
    assert no_products=='The product is not in the inventory'

    