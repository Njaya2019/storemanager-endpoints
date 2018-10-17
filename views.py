from flask import Blueprint
from admin import admin

admin_app=Blueprint('admin',__name__)
admin_view=admin.as_view('admin_api')

admin_app.add_url_rule('/api/v1/products', view_func=admin_view, methods=['POST'])
admin_app.add_url_rule('/api/v1/products',defaults={'product_id':None},view_func=admin_view, methods=['GET'])
