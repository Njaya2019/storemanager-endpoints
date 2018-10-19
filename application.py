from flask import Flask

app=Flask(__name__)

from views import admin_app,attendant_app,admin_sales_app

app.register_blueprint(admin_app)
app.register_blueprint(attendant_app)
app.register_blueprint(admin_sales_app)

if __name__=='__main__':
    app.run(debug=True)