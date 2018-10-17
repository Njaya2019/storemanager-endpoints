from flask.views import MethodView
from flask import request, jsonify, abort

class admin(MethodView):
    products=[{'product_id':1,'product_name':'Iphone 6 plus','price':600,'quantity':100},
             {'product_id':2,'product_name':'Logitech keyboard','price':60,'quantity':150},
             {'product_id':3,'product_name':'Subwoofer Desktop Speakers','price':20,'quantity':80}]

    def get(self):
        pass
    def post(self):
     #request_keys=('product_name','price','quantity')
        if not request.json:
            abort(400)
        product={'product_id':len(self.products)+1,
                 'product_name':request.json['product_name'],
                 'price':request.json['price'],
                 'quantity':request.json['quantity']
                }
        self.products.append(product)
        return jsonify({'message':'The product was added'})

