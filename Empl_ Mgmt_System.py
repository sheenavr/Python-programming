#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[ ]:


# Establish a connection
import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="",
database="ems")

#Insert Employee Details

def insert_employee(emp_list):
    cursor=mydb.cursor()
    query="insert into employee values (%s,%s,%s,%s,%s)"
    values=(emp_list[0],emp_list[1],emp_list[2],emp_list[3],emp_list[4])
    cursor.execute(query,values)
    print("The Employee Details are Inserted")
    mydb.commit()
    cursor.close()
    
 # Update employee details

def update_employee(emp_id,emp_dept):
    cursor=mydb.cursor()
    query = "UPDATE employee SET emp_dept = %s WHERE emp_id = %s"
    values=(emp_dept,emp_id)
    cursor.execute(query,values)
    print("The Employee Details are Updated")
    mydb.commit()
    cursor.close() 
    
# Delete Employee Details    

def delete_employee(emp_id):
    cursor=mydb.cursor()
    query="delete from employee where emp_id=%s"
    values=emp_id
    cursor.execute(query,(values,))
    print("The Employee Details are Deleted")
    mydb.commit()
    cursor.close() 
    
# List all employee details

def list_employee():
    cursor=mydb.cursor()
    query="select * from employee"
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        print("EMPLOYEE DETAILS")
        print("----------------")
        for row in result:
            print("Employee Id: ",row[0])
            print("Employee Name: ",row[1])
            print("Salary: ",row[2])
            print("Department: ",row[3])
            print("Employee Email: ",row[4])
            print("---------------")
    else:
        print("No Employee details found in the table")
    cursor.close()
# sort employee based on department

def sort_employee_department():
    cursor=mydb.cursor()
    query="select * from employee order by emp_dept"
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        print("EMPLOYEE DETAILS")
        print("----------------")
        for row in result:
            print("Employee Id: ",row[0])
            print("Employee Name: ",row[1])
            print("Salary: ",row[2])
            print("Department: ",row[3])
            print("Employee Email: ",row[4])
            print("---------------")
    else:
        print("No Employee details found in the table")
    cursor.close() 
    
# sort employee based on Salary

def sort_employee_salary():
    cursor=mydb.cursor()
    query="select * from employee order by emp_salary"
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        print("EMPLOYEE DETAILS")
        print("----------------")
        for row in result:
            print("Employee Id: ",row[0])
            print("Employee Name: ",row[1])
            print("Salary: ",row[2])
            print("Department: ",row[3])
            print("Employee Email: ",row[4])
            print("---------------")
    else:
        print("No Employee details found in the table")
    cursor.close()     
    
# search employee based on the department

def search_employee_dept(dept):
    cursor=mydb.cursor()
    query="select * from employee where emp_dept=%s"
    values=(dept,)
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
            print("Employee Email: ",row[4])
            print("---------------")
    else:
        print("No MAtching found...")
    cursor.close()   
    
# search employee based on the keyword in the name

def search_employee_name(keyword):
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
            print("Employee Email: ",row[4])
            print("---------------")
    else:
        print("No MAtching found...")
    cursor.close() 
    
# Search employee based on the salary range

def employee_salary_search(minrange,maxrange):
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
            print("Employee Email: ",row[4])
            print("---------------")
    else:
        print("No Employee in this salary range...")
    cursor.close()       
if __name__=="__main__":
    while True:
        print("Employee Management System")
        print("Enter your choices")
        print("1.Create Employee")
        print("2.Update Employee")
        print("3.Delete Employee")
        print("4. List all Employee")
        print("5. Sort Employees based on Department")
        print("6. Sort Employees based on Salary")
        print("7. Employee search based on Department")
        print("8. Employee search based on Salary Range ")
        print("9. Employee name Search ")
        print("10. Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            emp_list=[]
            emp_id=input("Enter Employee Id: ")
            emp_list.append(emp_id)
            emp_name=input("Enter Employee Name: ")
            emp_list.append(emp_name)
            emp_salary=input("Enter Employee Salary: ")
            emp_list.append(emp_salary)
            emp_dept=input("Enter Employee Department: ") 
            emp_list.append(emp_dept)
            emp_email=input("Enter Employee Email: ")
            emp_list.append(emp_email)
            
            insert_employee(emp_list)
        elif ch==2:
            
            emp_id=input("Enter Employee Id to update")
                     
            emp_dept=input("Enter Employee Department") 
                        
            update_employee(emp_id,emp_dept)    
        elif ch==3:
            emp_id=int(input("Enter Employee Id to delete employee details"))
            delete_employee(emp_id)
        elif ch==4:    
            list_employee()
        elif ch==5:    
            sort_employee_department()
        elif ch==6:    
            sort_employee_salary()
        elif ch==7:  
            dept=input("Enter the Department to search:")
            search_employee_dept(dept)          
        elif ch==8: 
            minrange=float(input("Enter minimum salary"))
            maxrange=float(input("Enter maximum salary"))
            employee_salary_search(minrange,maxrange)
            
        elif ch==9:
            keyword=input("Enter the keyword to search:")
            search_employee_name(keyword)     
            
        elif ch==10:
            break
        else:
            print("Invalid choice. Plase try again")
    mydb.close()           
            


# In[ ]:





# In[ ]:





# In[ ]:




