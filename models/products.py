
class products:

    products_list=[]
    def __init__(self, p_name, price,quantity):
        self.p_name=p_name
        self.price=price
        self.quantity=quantity
        self.p_id=len(self.products_list) + 1
    def add_product(self):
        pro_duct={'product_id':self.p_id,
                  'product_name':self.p_name,
                  'price':self.price,
                  'quantity':self.quantity
                }
        self.products_list.append(pro_duct)
        return 'The product has been added'

    def get_a_product(self, product_id=None):
        if self.products_list:
            if product_id:
                if product_id > len(self.products_list):
                    return 'The product wasn\'t found'   
            product_position=len(self.products_list) - 1
            
            pro_duct={'Product name':self.products_list[product_position]['product_name'],
                      'Product price':self.products_list[product_position]['price'],
                      'Quantity available':self.products_list[product_position]['quantity'],
            }
            return pro_duct
        else:
            return "There are no products yet"

            
    def get_products(self):
        if self.products_list:
            another_product_list=[]
            products_dict={}
            for p in self.products_list:
                products_dict.update({'Product name':p['product_name'],
                                    'Product price':p['price'],
                                    'Quantity available':p['quantity']
                                    })
                another_product_list.append(products_dict.copy())
            return another_product_list
        else:
            return 'There are no products yet'



