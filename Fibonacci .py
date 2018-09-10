
# coding: utf-8

# In[5]:


def fibonacci():
    howmany = int(input("How many fibonacci numbers generate? "))
    i = 1
    if howmany == 0:
        fiblist = [0]
    elif howmany == 1:
        fiblist = [1]
    elif howmany == 2:
        fiblist = [1, 1]
    elif howmany > 2:
        fiblist = [1, 1]
        while i < (howmany - 1):
            fiblist.append(fiblist[i] + fiblist[i - 1])
            i += 1
    return fiblist
print(fibonacci())

