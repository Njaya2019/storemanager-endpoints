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
        sale_made=self.s.make_sale()
        return jsonify({'message':sale_made})
            
        

    def get(self, saleId):
        sa_les=self.s.get_sale(saleId)
        if not sa_les:
            
            return jsonify({'message':'The sale record wasn\'t found'}), 404
        
        return jsonify({'Sale':sa_les})
