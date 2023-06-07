#!/usr/bin/env python
# coding: utf-8

# In[7]:


price_tv=20000
EMI_OPTION=False
money=int(input("Enter the money you have"))
if(price_tv<money):
    print("Please Pack the TV")
else :
    if EMI_OPTION:
        print("I will buy now")
    else:
        print("I will buy it later")


# In[9]:


# program to check the number is even or not
number=(int(input("Enter the number")))
if number%2==0:
    print("The number is Even")
else:
    print("The number is odd")


# In[1]:


price_tv=20000
EMI_OPTION=True
money=int(input("Enter the money you have"))
if(price_tv<money):
    print("Please Pack the TV")
elif EMI_OPTION:
    print("I will buy now")
else:
    print("I will buy it later")


# In[6]:


num=(int(input("Enter the number")))
if num==0:
    print("The number is neither positive nor negative")
elif num<0:
    print("The number is negative")
else:
    print("The number is positive")


# In[7]:


a=10
id(a)


# In[8]:


b=10
id(b)


# In[9]:


a=19
id(a)


# In[12]:


input("Enter the numbers").split(' ')


# In[15]:


x,y,z=map(int,['2','3','4'])
print(x,y,z)


# In[19]:


x,y=map(int,input("Enter the numbers").split(' '))
if x==y:
    print("both is same")
elif x>y:
    print("{} is greater than {}".format(x,y))
else:
    print("{} is greater than {}".format(y,x))
    


# In[ ]:


x,y,z=map(int,input("Enter the numbers").split(' '))
if x==y:
    print("both is same")
elif x>y:
    print("{} is greater than {}".format(x,y))
else:
    
    print("{} is greater than {}".format(y,x))


# In[29]:


str=input("Enter the String:")

if str.lower()==str[::-1]:
    print("the string is palindrome")
else:
    print("not palindrome")


# In[36]:


#company decided to give  bonus 5% to employee if tenure>5
emp_exp=int(input("Enter the Years of experience"))
emp_sal=int(input("Enter the Salary"))
if emp_exp>5:
    bonus=emp_sal*0.05
    emp_sal=emp_sal+bonus
    print("Bonus",bonus)
    print("updated salary",emp_sal)
else:
    print("No Bonus")


# In[38]:


#Given the participants' score sheet for your University Sports Day, you are required to
#find the runner-up score. You are given scores. Store them in a list and find the score of
#the runner-up. (Create an array of scores and print the runner up score
participant_arr = list(map(int, input().split()))
set_arr = set(participant_arr)
resul_arr = sorted(set_arr)
print(resul_arr[-2])


# In[44]:


#A dictionary is given D={‘John’ [25,32,43],’Peter’:[87,55,96],’Ram’:[58,55,43],’Meena’:[63,79,85]}
#Get a name from user if the name in the dictionary change the values corresponding to
#that user to [88,77,99] and print the dictionary. Else print ‘Name not found
personal_dic={'John': [25,32,43],'Peter':[87,55,96],'Ram':[58,55,43],'Meena':[63,79,85]}
name_str=input("Enter the name")
if name_str in personal_dic:
    d1={name_str: [88,77,99]}
    personal_dic.update(d1)
    print(personal_dic) 
else:
    print("The name not found in the dictionary")
    


# In[54]:


#Ticket Price Calculator:
#I. Ask the user to enter their age.
#II. Use control statements (if-elif-else) to calculate the ticket price based on the 
#following conditions:
#a. If the age is below 5, the ticket price is free.
#b. If the age is between 5 and 12 (inclusive), the ticket price is Rs.10.
#c. If the age is above 12, the ticket price is Rs.50.
#d. If the age is above 60, the ticket price is free.
#e. If the gender is female, the ticket price is 50% of the applicable rates.
#III. Display the ticket price to the user

user_age=int(input("Enter the age"))
gender=input("Enter the gender")
if user_age<5 or user_age>60:
    print("The ticket is free")
elif gender=='female' and   5>=  user_age and  user_age<=12 :
    new_rate=10*0.5
    print("the ticket price is ",new_rate)
elif gender=='female' and  user_age>12 : 
    new_rate=50*0.5
    print("the ticket price is ",new_rate)
elif  5>=  user_age and  user_age<=12:
    print("The ticket price is Rs.10")
elif user_age>12: 
    print("The ticket price is Rs.50")

    
  


# In[53]:


print(print("hello"))


# In[ ]:




