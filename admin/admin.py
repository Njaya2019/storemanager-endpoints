from flask.views import MethodView
from flask import request, jsonify, abort

class admin(MethodView):
    products=[{'product_id':1,'product_name':'Iphone 6 plus','price':600,'quantity':100},
             {'product_id':2,'product_name':'Logitech keyboard','price':60,'quantity':150},
             {'product_id':3,'product_name':'Subwoofer Desktop Speakers','price':20,'quantity':80}]

    def get(self, product_id):
        if not product_id:
            pr_odcts=[]
            pr_odct={}
            for p in self.products:
                pr_odct.update({'Product name':p['product_name'],
                'Quantity':p['quantity'],'Price':p['price']
                })
                pr_odcts.append(pr_odct.copy())
            return jsonify({'Products':pr_odcts})
        if product_id:
            pr_position=product_id-1
            return jsonify({'Product':{
                        'product_name':self.products[pr_position]['product_name']
                        ,'price':self.products[pr_position]['price'],
                        'quantity':self.products[pr_position]['quantity']}})

            
        
    def post(self):
     #request_keys=('product_name','price','quantity')
        if not request.json:
            abort(400)
        product={"product_id":len(self.products)+1,
                 "product_name":request.json["product_name"],
                 "price":request.json["price"],
                 "quantity":request.json["quantity"]
                }
        self.products.append(product)
        return jsonify({"message":"The product was added"})

