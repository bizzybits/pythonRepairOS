from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class RepairModel(db.Model):
    __tablename__ = "repair_table"

    id = db.Column(db.Integer, primary_key=True)
    repair_id = db.Column(db.Integer(), unique=True)
    customer_name = db.Column(db.String())
    repair_item = db.Column(db.String())
    repair_issue = db.Column(db.String(80))
    repair_due_date = db.Column(db.Integer())

    def __init__(self, repair_id, customer_name, repair_item, repair_issue,
                 repair_due_date):
        self.repair_id = repair_id
        self.customer_name = customer_name
        self.repair_item = repair_item
        self.repair_issue = repair_issue
        self.repair_due_date = repair_due_date

    def __repr__(self):
        return f"{self.customer_name}:{self.repair_item}"


class ServiceMenuModel(db.Model):
    __tablename__ = "service_menu_table"

    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer(), unique=True)
    service_name = db.Column(db.Text())
    service_price = db.Column(db.Integer())

    def __init__(self, service_id, service_name, service_price):
        self.service_id = service_id
        self.service_name = service_name
        self.service_price = service_price

    def __repr__(self):
        return f"{self.service_id}:{self.service_name}"