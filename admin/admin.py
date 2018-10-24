from flask.views import MethodView
from flask import request, jsonify, abort
from models.products import products
class admin(MethodView):
   
    p=products(p_name=None, price=None,quantity=None)
    def get(self, product_id):
        if not product_id:
            available_products=self.p.get_products()
            return jsonify({'Products':available_products}), 200
        if product_id:
            requested_product=self.p.get_a_product()
            return jsonify({'Product':requested_product}), 200

            
        
    def post(self):
        if not request.json:
            abort(400)
        self.p=products(request.json['product_name'],request.json['price'],request.json['quantity'])
        msg=self.p.add_product()
        return jsonify({'message':msg}), 200

