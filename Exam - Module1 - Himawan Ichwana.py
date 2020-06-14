#!/usr/bin/env python
# coding: utf-8

# ### Number 1

# In[1]:


string = input("Input String:")
def Hashtag(string):
    string1 = string.title()
    string2 = string1.replace(" ", "")
    list_str = list(string2)
    list_str.insert(0, "#")
    for i in list_str:
        if len(list_str) > 140 or len(list_str) == 0:
            print("False input")
        else:
            print(i, end = "")
    
Hashtag(string)


# In[3]:


string = input("Input String:")
def Hashtag(string):
    string1 = string.title()
    string2 = string1.replace(" ", "")
    list_str = list(string2)
    list_str.insert(0, "#")
    for i in list_str:
        if len(list_str) > 140 or len(list_str) == 0:
            print("False input")
        else:
            print(i, end = "")
    
Hashtag(string)


# In[9]:


string = input("Input String:")
def Hashtag(string):
    string1 = string.title()
    string2 = string1.replace(" ", "")
    list_str = list(string2)
    list_str.insert(0, "#")
    for i in list_str:
        if len(list_str) > 140 or len(list_str) == 0:
            return False
        else:
            print(i, end = "")
    
Hashtag(string)


# ### Number 2

# In[14]:


def create_phone_number(number):
    list1 = []
    for i in number:
        list1.append("".join(str(i)))
    
    str_1 = list1
    first = "".join(str_1[0:3])
    mid = "".join(str_1[3:6])
    last = "".join(str_1[6:10])
    
    print("({}) {}-{}".format(first, mid, last))
    
create_phone_number([1,2,3,4,5,6,7,8,9,0])


# ### Number 3

# In[112]:


even = []
odd = []

def sort_odd_even(numbers):
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    for k in range(len(even)-1):
                if even[k] < even[k+1]:
                    temp2 = even[k+1]
                    even[k+1] = even[k]
                    even[k] = temp2
    for j in range(len(odd)):
        for u in range(len(odd)-1):
                if odd[u] > odd[u+1]:
                    temp2 = odd[u]
                    odd[u] = odd[u+1]
                    odd[u+1] = temp2 
    combine = odd + even
    combine[2], combine[3] = combine[3], combine[2]
    combine[4], combine[3] = combine[3], combine[4]
    
    return combine
    
print(sort_odd_even([5,3,2,8,1,4,]))


# In[ ]:




