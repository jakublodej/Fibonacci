
# coding: utf-8

# In[3]:


#Fibonacci


def fibonacci():
    howmany=input("How many fibonacci numbers generate?")
    fiblist=[]
    
    if howmany == 0:
        fiblist =[0]
    elif howmany == 1:
        fiblist=[1]
    elif howmany == 2:
        fiblist=[1,1]
    else:
        pass
    return fibonacci()
    print(fibonacci())

   
    

