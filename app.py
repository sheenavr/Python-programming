from flask import Flask,render_template,request
import mysql.connector
user_dict={'admin':'1234','user':'5678'}
conn = mysql.connector.connect(host='localhost',user='root',password='',database='ems')
mycursor=conn.cursor()
#create a flask application
app = Flask(__name__)

#Define the route 

@app.route('/')
def hello():
    return render_template('first.html')
@app.route('/first')
def first():
    return render_template('first.html')    
@app.route('/account')
def account():
    return render_template('account.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/home',methods=['POST'])
def home():
    uname=request.form['username']
    pwd=request.form['password']

    if uname not in user_dict:
        return render_template('login.html',msg='Invalid User')
    elif user_dict[uname] != pwd:
        return render_template('login.html',msg='Invalid Password')
    else:
        return render_template('home.html')
@app.route('/view')
def view():
    query="SELECT * FROM ACCOUNT"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/search')
def searchpage():
    return render_template('search.html')


@app.route('/searchresult',methods=['POST'])
def search():
    accountnumber = request.form['account_number']
    query="SELECT * FROM ACCOUNT WHERE ACCOUNT_NUMBER="+accountnumber
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)
    
@app.route('/add')
def add():
    return render_template('account.html')

@app.route('/read',methods=['POST'])
def read():
    accountnumber = request.form['accountnumber']
    customername = request.form['customername']
    amount= request.form['amount']
    accounttype = request.form['accounttype']
    email = request.form['email']
    query = "INSERT INTO ACCOUNT(ACCOUNT_NUMBER,CUSTOMER_NAME,AMOUNT,ACCOUNT_TYPE,EMAIL) VALUES (%s,%s,%s,%s,%s)"
    data = (accountnumber,customername,amount,accounttype,email)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('account.html',msgdata='Added Successfully')


    
#Run the flask app
if __name__=='__main__':
    app.run(port=5001,debug = True)