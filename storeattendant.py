from flask.views import MethodView
from flask import request, jsonify, abort
from admin import admin

class storeattendant(MethodView):
    sales=[{'sale_id':1,'attendant_id':1,'product_id':2,'date':'Oct 8, 2018 12:00 P.M','transanction_cost':59.98},
           {'sale_id':2,'attendant_id':1,'product_sold':1,'date':'Oct 9, 2018 9:00 A.M','transanction_cost':100},
           {'sale_id':3,'attendant_id':1,'product_id':3,'date':'Oct 9, 2018 11:30 A.M','transanction_cost':60}]
    
    def post(self):
        if not request.json:
            abort(400)
        sale={'sale_id':len(self.sales)+1,
                 'attendant_id':request.json['attendant_id'],
                 'product_id':request.json['product_id'],
                 'date':request.json['date'],
                 'transanction_cost':request.json['transanction_cost']
                }
        self.sales.append(sale)
        return jsonify({'message':'The transaction has been completed'})
    def get(self):
        pass