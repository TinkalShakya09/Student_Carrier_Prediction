#!/usr/bin/env python
# coding: utf-8

# In[17]:


from keras.models import load_model


# In[18]:


model=load_model("student.h5")


# In[20]:


y_pred=model.predict([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]])
y_pred


# In[ ]:




