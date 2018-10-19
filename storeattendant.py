from flask.views import MethodView
from flask import request, jsonify, abort
from admin import admin
import time
class storeattendant(MethodView):
    sales=[{'sale_id':1,'attendant_id':2,'product_id':2,'quantity':2,'date':'Oct 10, 2018 5:00 P.M','transanction_cost':120},
           {'sale_id':2,'attendant_id':1,'product_id':1,'quantity':1,'date':'Oct 10, 2018 6:25 P.M','transanction_cost':600},
           {'sale_id':3,'attendant_id':3,'product_id':3,'quantity':1,'date':'Oct 10, 2018 7:30 P.M','transanction_cost':80}]

    products=[{'product_id':1,'product_name':'Iphone 6 plus','price':600,'quantity':100},
             {'product_id':2,'product_name':'Logitech keyboard','price':60,'quantity':150},
             {'product_id':3,'product_name':'Subwoofer Desktop Speakers','price':20,'quantity':80}]
    
    def post(self):
        if not request.json:
            abort(400)
        p_name=request.json['product_name']
        sale_quantity=request.json['quantity']
        attendant_id=1
        date_sold=time.strftime("%b %d, %Y %H:%M %p")
        sale_id=len(self.sales)+1
        for produ_ct in self.products:
            if produ_ct['product_name']==p_name:
                p_id=produ_ct['product_id']
                p_price=produ_ct['price']
                sale_total_cost=p_price * sale_quantity

        sale={'sale_id':sale_id,
                 'attendant_id':attendant_id,
                 'product_id':p_id,
                 'date':date_sold,
                 'transanction_cost':sale_total_cost
                }
        self.sales.append(sale)
        return jsonify({'message':'The transaction has been completed'})
    def get(self, saleId):
        attendant_id=1
        sale_record=self.sales[saleId-1]
        if sale_record['attendant_id']==attendant_id:
            sa_les={}
            sales_list=[]
            pro_position=sale_record['product_id']-1
            sa_les.update({'product name':self.products[pro_position]['product_name'],
                        'Date sold':sale_record['date'],
                        'Total cost':sale_record['transanction_cost'],
                        'Quantity bought':sale_record['quantity']
                        })
            sales_list.append(sa_les.copy())
            return jsonify({'Sale':sales_list})
