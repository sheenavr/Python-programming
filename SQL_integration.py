#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[3]:


import mysql.connector


# In[6]:


# Establish a connection
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="",
database="ems")


# In[7]:


cursor=mydb.cursor()
cursor.execute("select * from Employee")
rows=cursor.fetchall()
for row in rows:
    print(row)


# In[8]:





# In[ ]:


# Establish a connection
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="",
database="ems")

def search_employee(keyword):
    cursor=mydb.cursor()
    query="select * from employee where emp_name like '{}%'".format(keyword)
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        print("EMPLOYEE DETAILS")
        print("----------------")
        for row in result:
            print("Employee Id",row[0])
            print("Employee Name",row[1])
            print("Salary",row[2])
            print("Department",row[3])
            print("---------------")
    else:
        print("No MAtching found...")
    cursor.close()   
def salary_search(minrange,maxrange):
    cursor=mydb.cursor()
    query="select * from employee where emp_salary between %s and %s"
    values=(minrange,maxrange)
    cursor.execute(query,values)
    result=cursor.fetchall()
    if result:
        print("EMPLOYEE DETAILS")
        print("----------------")
        for row in result:
            print("Employee Id",row[0])
            print("Employee Name",row[1])
            print("Salary",row[2])
            print("Department",row[3])
            print("---------------")
    else:
        print("No Employee in this salary range...")
    cursor.close()     
    
if __name__=="__main__":
    while True:
        print("Employee Management System")
        print("Enter your choices")
        print("1.Employee search")
        print("2.Salary range Search")
        print("3. Exit")
        ch=int(input("Enter your choice"))
        if ch==1:
            keyword=input("Enter the keyword to search:")
            search_employee(keyword)
        elif ch==2:
            minrange=float(input("Enter minimum salary"))
            maxrange=float(input("Enter maximum salary"))
            salary_search(minrange,maxrange)
        elif ch==3:
            break
        else:
            print("Invalid choice. Plase try again")
    mydb.close()           
            


# In[ ]:





# In[ ]:




