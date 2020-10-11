#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercise 8.2
#Reference Code from figure 8.7
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# In[2]:


#use string method count
#write an invocation that counts the number of a's in 'banana'
#want to "invoke" count on banana


# In[3]:


word = 'banana'
word.count('a')


# In[4]:


#Exercise 8.3 
fruit = 'banana'
fruit[0:5:2]


# In[5]:


#write a one line version of the is_palindrome from 6.3
#Reference Code 
def is_palindrome(word):
    if word == word[:: -1]:
        return True
    else:
        return False


# In[11]:


#Use the == operator to determine if the "word" is True or false. The slice has a beginning and end at 0 and will start from the end of the string
def is_palindrome(word):
    return word == word[:: -1]
    
print (is_palindrome('noon'))
print (is_palindrome('today'))


# In[ ]:




