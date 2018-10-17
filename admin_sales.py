from flask.views import MethodView
from flask import request, jsonify, abort



class admin_sales(MethodView):
    sales=[{'sale_id':1,'attendant_id':2,'product_id':2,'date':'Oct 10, 2018 5:00 P.M','transanction_cost':59.98},
           {'sale_id':2,'attendant_id':1,'product_sold':1,'date':'Oct 10, 2018 6:25 P.M','transanction_cost':100},
           {'sale_id':3,'attendant_id':3,'product_id':3,'date':'Oct 10, 2018 7:30 P.M','transanction_cost':60}]
    
    def get(self):
        return jsonify({'Sales':self.sales})
    def post(self):
        pass
    
