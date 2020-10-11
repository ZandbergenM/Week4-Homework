#!/usr/bin/env python
# coding: utf-8

# In[11]:


import arcgis
from IPython.display import display


# In[12]:


from arcgis.gis import GIS
gis = GIS()


# In[13]:


map1 = gis.map('Seattle')
map1


# In[14]:


Test_layer = gis.content.search("Seattle", item_type = "Feature Layer")
Test_layer


# In[15]:


item = gis.content.search("title: SeattleParkTrails owner: tnewton2_NCSU", "Feature Layer")[0]


# In[16]:


map1.add_layer(item)


# In[ ]:




