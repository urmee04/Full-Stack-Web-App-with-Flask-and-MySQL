from flask import Flask, render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField, TextField
import mysql.connector 
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


############################################

mydb = mysql.connector.connect(
     host='localhost',
     user='root',
     password = 'Biroktikor211'
    )
cursor = mydb.cursor()

cursor.execute("CREATE DATABASE new_app")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Biroktikor211@localhost/new_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)
###################################################################################################

class Sales(db.Model):
   __tablename__ = 'sales_details'
   id = db.Column(db.Integer, primary_key=True,autoincrement=True)
   employee_id = db.Column(db.Text)
   week_no = db.Column(db.Text)
   weekly_sales = db.Column(db.Integer)
   sales_year = db.Column(db.Integer)
   item_details = db.Column(db.Text)
   dates = db.relationship('Dates', backref = 'sales_details', lazy = True)
   products = db.relationship('Products', backref = 'sales_details', lazy = True)
   

   
   
   
   def __init__(self,employee_id,week_no,weekly_sales,sales_year,item_details):
     
     self.employee_id = employee_id
     self.week_no = week_no
     self.weekly_sales = weekly_sales
     self.sales_year = sales_year
     self.item_details = item_details
     
  

class Products(db.Model):
  __tablename__ = 'prod_details'
  id = db.Column(db.Integer,primary_key= True)
  region = db.Column(db.Text)
  sales_details_id = db.Column(db.Integer,db.ForeignKey('sales_details.id'))
  

  def __init__(self,sales_details_id,region):
     self.sales_details_id = sales_details_id
     self.region = region
     


class Dates(db.Model):
   __tablename__ = 'date_info'
   id = db.Column(db.Integer,primary_key= True)
   date_QQ = db.Column(db.Text)
   YYYYQQ = db.Column(db.Text)
   date_month = db.Column(db.Text)
   sales__details_id = db.Column(db.Integer,db.ForeignKey('sales_details.id'))

   def __init__(self,date_QQ,YYYQQ,date_month,sales_details_id):
     self.date_QQ = date_QQ
     self.YYYYQQ = YYYQQ
     self.date_month = date_month
     self.sales_details_id = sales_details_id
   
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


class AddSalesRecord(FlaskForm):
    
 
  employee_id = SelectField('Employee_Id', choices=[ ('' , ''), ('EMP244', 'EMP244'), ('EMP256', 'EMP256'),
        ('EMP234', 'EMP234'),
        ('EMP267', 'EMP267'),
        ('EMP290', 'EMP290') ])
  week_no = TextField('Week Number')
  weekly_sales = IntegerField('Quantity of Weekly Sales')
  sales_year = IntegerField('Enter Year')
  item_details = SelectField('Item Details', choices =[('' , ''), ('ESP_001', 'ESP_001'), ('ESP_002', 'ESP_002'), ('ESP_003', 'ESP_003'), ('ESP_004', 'ESP_004'), ('ESP_005', 'ESP_005'), ('ESP_006', 'ESP_006'), ('ESP_007', 'ESP_007'), ('ESP_008', 'ESP_008'), ('PROD_001', 'PROD_001'), ('PROD_002', 'PROD_002'), ('PROD_003', 'PROD_003'), ('PROD_004', 'PROD_004'), ('PROD_005', 'PROD_005'), ('PROD_006', 'PROD_006'), ('PROD_007', 'PROD_007'), ('PROD_008', 'PROD_008') ])
    
  submit = SubmitField('Add/Update Record') 
     

@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    form = AddSalesRecord()
    if form.validate_on_submit():
        
      
        employee_id = request.form['employee_id']
        week_no = request.form['week_no']
        weekly_sales = request.form['weekly_sales']
        sales_year = request.form['sales_year']
        item_details = request.form['item_details']
        record = Sales(employee_id, week_no, weekly_sales, sales_year,item_details)
        
        db.session.add(record)
        db.session.commit()
        
        return redirect(url_for('add_record'))
    return render_template('add_record.html', form = form )   


if __name__ == "__main__":
  app.run(debug=True)                 		
	    









   
  


  	






