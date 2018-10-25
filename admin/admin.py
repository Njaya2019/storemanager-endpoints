from flask.views import MethodView
from flask import request, jsonify, abort
from models.products import products
from Validators.validate_json import validate_json_numeric_value,validate_json_string_value

class admin(MethodView):
   
    p=products(p_name=None, price=None,quantity=None)

    def get(self, product_id):
        if not product_id:
            available_products=self.p.get_products()
            return jsonify({'Products':available_products}), 200
        if product_id:
            requested_product=self.p.get_a_product(product_id)
            return jsonify({'Product':requested_product}), 200
    
    def post(self):
        if not request.json:
            abort(400)
        pro_name=request.json['product_name']
        pro_price=request.json['price']
        pro_qty=request.json['quantity']
        if not validate_json_numeric_value(pro_price) or not validate_json_string_value(pro_name) or not validate_json_numeric_value(pro_qty):
            return jsonify({'message':'Please provide valid strings or integers'})
        if not pro_name or not pro_price or not pro_qty:
            return jsonify({'message':'Please provide all values'})
        self.p=products(pro_name,pro_price, pro_qty)
        msg=self.p.add_product()
        return jsonify({'message':msg}), 200

