

from models.products import products
import time
class sales():
    sales_list=[]
    def __init__(self,product_name,quantity):
        self.product_name=product_name
        self.quantity=quantity
        self.date_sale_made=time.strftime("%b %d, %Y %H:%M %p")
        self.sale_id=len(self.sales_list) + 1

    def make_sale(self):
        sale_dict={}
        for p in products.products_list:
            if self.product_name==p['product_name']:
                total_cost=p['price'] * self.quantity
                sale_dict.update({'sale_id':self.sale_id,
                                  'attendant_id':1,
                                  'product_id':p['product_id'],
                                  'quantity':self.quantity,
                                  'date':self.date_sale_made,
                                  'transanction_cost':total_cost
                })
                self.sales_list.append(sale_dict)
        return 'The sale has been made'
    def get_sale(self, sale_id=None):
        if self.sales_list:
            if sale_id:
                if sale_id > len(self.sales_list):
                    return 'The sale record wasn\'t found'    
                sale_dict={}
                sale_position=len(self.sales_list)-1
                sale_record=self.sales_list[sale_position]
                p_id=sale_record['product_id']
                p_positon=p_id-1
                pro_duct=products.products_list[p_positon]
                sale_dict.update({'Product name':pro_duct['product_name'],
                                'Date sold':sale_record['date'],
                                'Total cost':sale_record['transanction_cost'],
                                'Quantity bought':sale_record['quantity']
                                })
                return sale_dict
    def get_sales(self):
        sale_dict={}
        another_sales_list=[]
        if self.sales_list:
            for s in self.sales_list:
                p_id=s['product_id']
                p_positon=p_id-1
                pro_duct=products.products_list[p_positon]
                sale_dict.update({'Product name':pro_duct['product_name'],
                          'Date sold':s['date'],
                          'Total cost':s['transanction_cost'],
                          'Quantity bought':s['quantity']
                         })
                another_sales_list.append(sale_dict.copy())
            return another_sales_list
        
        else:
            return 'There are no sales records yet'


                
                
        