from flask import Blueprint
from admin import admin
from storeattendant import storeattendant

admin_app=Blueprint('admin',__name__)
attendant_app=Blueprint('attendant',__name__)

admin_view=admin.as_view('admin_api')
attendant_view=storeattendant.as_view('attendant_api')

admin_app.add_url_rule('/api/v1/admin/products', view_func=admin_view, methods=['POST'])
admin_app.add_url_rule('/api/v1/admin/products',defaults={'product_id':None},view_func=admin_view, methods=['GET'])
admin_app.add_url_rule('/api/v1/admin/products/<int:product_id>',view_func=admin_view, methods=['GET'])


attendant_app.add_url_rule('/api/v1/attendant/sales',view_func=attendant_view, methods=['POST'])
attendant_app.add_url_rule('/api/v1/attendant/products',view_func=attendant_view, methods=['GET'])


