from flask.views import MethodView
from flask import request, jsonify, abort
from models.sales import sales


class admin_sales(MethodView):
   
    s=sales('iphone 7',1)
    def get(self,saleId):
        if saleId:
            requested_sale=self.s.get_sale(saleId)
            if not requested_sale:
                return jsonify({'message':'The sale record wasn\'t found'})
            return jsonify({'Sale':requested_sale})
        else:
            sa_les=self.s.get_sales()
            if not sa_les:
                return jsonify({'message':'There are no sales records yet'})
            return jsonify({'Sales':self.s.get_sales()})
                                                  
                                                  
                                                  
                                                
                                    
            
   
    
