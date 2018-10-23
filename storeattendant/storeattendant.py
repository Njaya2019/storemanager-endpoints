from flask.views import MethodView
from flask import request, jsonify, abort
from admin.admin import admin
from models.sales import sales



class storeattendant(MethodView):

    s=sales('Samsung galaxy  S8',1)

    def post(self):
        if not request.json:
            abort(400)
        self.s=sales(request.json['product_name'],request.json['quantity'])
        sale_being_made=self.s.make_sale()
        return jsonify({'message':'The sale has been made'})

    def get(self, saleId):
        sa_les=self.s.get_sale(saleId)
        if not sa_les:
            
            return jsonify({'message':'There are no sales records yet'})
        
        return jsonify({'Sale':sa_les})
