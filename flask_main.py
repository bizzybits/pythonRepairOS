from flask import Flask, render_template, request, redirect, abort
from models import db, RepairModel, ServiceMenuModel
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repairs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


#create customer
@app.route('/data/customer/create', methods=['GET', 'POST'])
def create_customer():
    if request.method == 'GET':
        return render_template('create_customer.html')

    if request.method == 'POST':
        repair_id = request.form['repair_id']
        customer_name = request.form['customer_name']
        repair_item = request.form['repair_item']
        repair_issue = request.form['repair_issue']
        repair_due_date = request.form['repair_due_date']
        customer = RepairModel(repair_id=repair_id,
                               customer_name=customer_name,
                               repair_item=repair_item,
                               repair_issue=repair_issue,
                               repair_due_date=repair_due_date)
        db.session.add(customer)
        db.session.commit()
        return redirect('/data')


#retrieve full list of customers
@app.route('/data/customer')
def RetrieveCustomerDataList():
    customers = RepairModel.query.all()
    return render_template('datalist_customer.html', customers=customers)


#retrieve single customer
@app.route('/data/customer/<int:id>')
def RetrieveSingleCustomer(id):
    customer = RepairModel.query.filter_by(repair_id=id).first()
    if customer:
        return render_template('data_customer.html', customer=customer)
    return f"Employee with id ={id} Doenst exist"


#update customer
@app.route('/data/customer/<int:id>/update', methods=['GET', 'POST'])
def update_customer(id):
    customer = RepairModel.query.filter_by(repair_id=id).first()
    if request.method == 'POST':
        if customer:
            db.session.delete(customer)
            db.session.commit()

            customer_name = request.form['customer_name']
            repair_item = request.form['repair_item']
            repair_issue = request.form['repair_issue']
            repair_due_date = request.form['repair_due_date']
            customer = RepairModel(repair_id=id,
                                   customer_name=customer_name,
                                   repair_item=repair_item,
                                   repair_issue=repair_issue,
                                   repair_due_date=repair_due_date)

            db.session.add(customer)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Customer repair with id = {id} Does not exist"

    return render_template('update_customer.html', customer=customer)


#delete customer
@app.route('/data/customer/<int:id>/delete', methods=['GET', 'POST'])
def delete_customer(id):
    customer = RepairModel.query.filter_by(repair_id=id).first()
    if request.method == 'POST':
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return redirect('/data')
        abort(404)

    return render_template('delete_customer.html')


@app.route('/')
def hello():
    return render_template("create_customer.html")


#create service
@app.route('/data/service/create', methods=['GET', 'POST'])
def create_service():
    if request.method == 'GET':
        return render_template('create_service.html')

    if request.method == 'POST':
        service_id = request.form['service_id']
        service_name = request.form['service_name']
        service_price = request.form['service_price']

        service = ServiceMenuModel(service_id=service_id,
                                   service_name=service_name,
                                   service_price=service_price)
        db.session.add(service)
        db.session.commit()
        return redirect('/data/service')


#retrieve full list of services
@app.route('/data/service')
def RetrieveServicesDataList():
    services = ServiceMenuModel.query.all()
    return render_template('datalist_service.html', services=services)


#retrieve single service
@app.route('/data/service/<int:id>')
def RetrieveSingleService(id):
    service = ServiceMenuModel.query.filter_by(service_id=id).first()
    if service:
        return render_template('data_service.html', service=service)
    return f"Service with id ={id} Doesn't exist"


#update service
@app.route('/data/service/<int:id>/update', methods=['GET', 'POST'])
def update_service(id):
    service = ServiceMenuModel.query.filter_by(service_id=id).first()
    if request.method == 'POST':
        if service:
            db.session.delete(service)
            db.session.commit()
            service_id = request.form['service_id']
            service_name = request.form['service_name']
            service_price = request.form['service_price']

            service = RepairModel(service_id=service_id,
                                  service_name=service_name,
                                  service_price=service_price)

            db.session.add(service)
            db.session.commit()
            return redirect(f'/data/service/{id}')
        return f"Service with name = {id} Does not exist"

    return render_template('update_service.html', service=service)


#delete service
@app.route('/data/service/<int:id>/delete', methods=['GET', 'POST'])
def delete_service(id):
    service = ServiceMenuModel.query.filter_by(service_id=id).first()
    if request.method == 'POST':
        if service:
            db.session.delete(service)
            db.session.commit()
            return redirect('/data/service')
        abort(404)

    return render_template('delete_service.html')


app.run(host='localhost', port=6789, debug=True)