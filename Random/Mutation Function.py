#!/usr/bin/env python
# coding: utf-8

# In[52]:


from typing import List
import random
import numpy as np
x = List[int]
def mutation(x, num: int =1) -> x: 
    for _ in range(num):
        index = random.randrange(len(x))
        var = random.randint(0,len(x))
        x[index] = var
    return x
x = [15,2,0,6,4,9,4,2,0,7,20,3,9]
print(x)

mutation(x)
print(x)


# In[ ]:




