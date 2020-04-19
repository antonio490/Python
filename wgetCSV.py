#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import wget
import os


# In[2]:


ndir = "/Books"
wdir = os.getcwd()

if not os.path.exists(wdir+ndir):
    os.mkdir(wdir+ndir) 

os.chdir("Books")


# In[3]:


ebooks = pd.read_csv('../ebookList.csv',header=0, usecols=[0,1,11,18])


# In[4]:


ebooks.head()


# In[5]:


root = "https://link.springer.com/content/pdf/10.1007%2F"


# In[6]:


def downloadByPKG(pkg):  
    books = ebooks[ebooks["English Package Name"]==pkg]    
    for b in books.itertuples():
        isbn = b.OpenURL[-17:]
        url = root + str(isbn) + ".pdf"
        book_title = str(b[1])

        if os.path.isfile(book_title):
            print("Book exists!")
        else:
            try:
                print("Downloading..." + url)
                file = wget.download(url)
                os.rename(file, book_title)
            except:
                print("Error downloading")


# In[ ]:


downloadByPKG("Computer Science")


# In[ ]:




