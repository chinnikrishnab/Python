#!/usr/bin/env python
# coding: utf-8

# # Project 1.0

# In[10]:


print("WELCOME To")
Instute = str(input("Enter your instute :"))
name = str(input("Enter your firstName :"))
batch = str(input("Enter your batch :"))
section = str(input("Enter your Section :"))
rollnumber =int(input("Enter Your RollNumber :"))


# In[11]:


print("3 SUBJECTS")
print("*"*35)


# In[12]:


subject1 = str(input("Enter first Subject :"))
subject2 = str(input("Enter second Subject :"))
subject3 = str(input("Enter third Subject3 :"))
subject1score = int(input("Enter first Subject Score :"))
subject2score = int(input("Enter second Subject Score :"))
subject3score = int(input("Enter thiord Subject Score :"))


# In[13]:


# marks Total
totalMarks = subject1score + subject2score + subject3score
print(totalMarks)


# In[14]:


#Percentage for three subjects 
percentage = totalMarks / 3
print(percentage)


# In[16]:


c = "successfully completed firest project in python i.e Project1.0"
print(c)

