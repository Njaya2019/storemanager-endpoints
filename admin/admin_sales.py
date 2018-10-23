from flask.views import MethodView
from flask import request, jsonify, abort



class admin_sales(MethodView):
    sales=[{'sale_id':1,'attendant_id':2,'product_id':2,'quantity':2,'date':'Oct 10, 2018 5:00 P.M','transanction_cost':120},
           {'sale_id':2,'attendant_id':1,'product_id':1,'quantity':1,'date':'Oct 10, 2018 6:25 P.M','transanction_cost':100},
           {'sale_id':3,'attendant_id':3,'product_id':3,'quantity':1,'date':'Oct 10, 2018 7:30 P.M','transanction_cost':80}]
    products=[{'product_id':1,'product_name':'Iphone 6 plus','price':600,'quantity':100},
             {'product_id':2,'product_name':'Logitech keyboard','price':60,'quantity':150},
             {'product_id':3,'product_name':'Subwoofer Desktop Speakers','price':20,'quantity':80}]
    
    def get(self,saleId):
        if saleId:
            sale_position=saleId-1
            p_id=self.sales[sale_position]['product_id']
            p_position=p_id-1
            product_name=self.products[p_position]['product_name']

            if self.sales[sale_position]['quantity'] > self.products[p_position]['quantity']:
                return jsonify({'message':'Quantity exceeds stock'})

            transanction_cost=self.products[p_position]['price'] * self.sales[sale_position]['quantity']
            return jsonify({'Sale':{'product name':product_name,
                                    'Date sold':self.sales[sale_position]['date'],
                                    'Total cost':transanction_cost,
                                    'Quantity bought':self.sales[sale_position]['quantity']}})
        else:
            sa_les={}
            sales_list=[]
            i=0
            for s in self.sales:
                pro_position=s['product_id']-1
                sa_les.update({'product name':self.products[pro_position]['product_name'],
                        'Date sold':s['date'],
                        'Total cost':s['quantity']*self.products[pro_position]['price'],
                        'Quantity bought':s['quantity']
                        })
                sales_list.append(sa_les.copy())
            return jsonify({'Sales':sales_list})
                                                  
                                                  
                                                  
                                                
                                    
            
    def post(self):
        pass
    
