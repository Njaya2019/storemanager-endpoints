from flask.views import MethodView
from flask import request, jsonify, abort
from models.products import products
class admin(MethodView):
   # products=[{'product_id':1,'product_name':'Iphone 6 plus','price':600,'quantity':100},
             #{'product_id':2,'product_name':'Logitech keyboard','price':60,'quantity':150},
             #{'product_id':3,'product_name':'Subwoofer Desktop Speakers','price':20,'quantity':80}]
    p=products('logitech Keyboard',30,20)
    def get(self, product_id):
        if not product_id:
            available_products=self.p.get_products()
            return jsonify({'Products':available_products})
        if product_id:
            requested_product=self.p.get_a_product()
            if not requested_product:
                return jsonify({'message':requested_product})
            return jsonify({'Product':requested_product})

            
        
    def post(self):
     #request_keys=('product_name','price','quantity')
        if not request.json:
            abort(400)
        self.p=products(request.json['product_name'],request.json['price'],request.json['quantity'])
        msg=self.p.add_product()
        return jsonify({'message':msg})

