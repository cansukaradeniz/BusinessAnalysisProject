#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import pm4py 
log = pm4py.read.read_xes(os.path.join("tests","input_data",'C:/Users/cansu/cansudata/BPI_Challenge_2013_open_problems.xes'))
dfg,start_activities,end_activities = pm4py.discover_dfg_typed(log)
pm4py.view_dfg(dfg,start_activities,end_activities)


# In[ ]:




