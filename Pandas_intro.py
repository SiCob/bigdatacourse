
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[3]:

s


# In[4]:

s.index


# In[5]:

pd.Series(np.random.randn(5))


# In[6]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[9]:

d


# In[10]:

pd.Series(d)


# In[11]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[12]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[13]:

s[0]


# In[14]:

s[:3]


# In[15]:

s[s > s.median()]


# In[16]:

s.median()


# In[17]:

s[4-3]


# In[18]:

s[[4, 3, 1]]


# In[19]:

s[4, 3, 1]


# In[20]:

np.exp(s)


# In[21]:

s['a']


# In[22]:

s['e']=12


# In[23]:

s


# In[24]:

s['f']


# In[25]:

'f' in s


# In[27]:

if 'f' in s:
    print s['f']


# In[28]:

if 'e' in s:
    print s['e']


# In[29]:

s.get('f')


# In[30]:

s.get('e')


# In[31]:

s.get('f', np.nan)


# In[32]:

s + s


# In[33]:

s * 2


# In[34]:

s = s * 2


# In[35]:

s


# In[36]:

s = s /2


# In[37]:

s


# In[38]:

s[1:]


# In[39]:

s[:-1]


# In[40]:

s[1:] + s[:-1]


# In[41]:

s = pd.Series(np.random.randn(5), name='something')


# In[42]:

s


# In[43]:

s.name


# In[44]:

s['f'] = 0


# In[45]:

s


# In[46]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[47]:

d


# In[48]:

df = pd.DataFrame(d)


# In[49]:

df


# In[50]:

pd.DataFrame(d, index=['d', 'a', 'b'])


# In[52]:

pd.DataFrame(d, index=['d', 'a', 'b']), columns = ['two', 'three'])


# In[53]:

pd.DataFrame(d, index=['d', 'a', 'b'], columns = ['two', 'three'])


# In[54]:

pd.DataFrame(d)


# In[55]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[56]:

data


# In[57]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[58]:

data


# In[59]:

pd.DataFrame(data)


# In[65]:

pd.DataFrame(data, index=['first', 'second'])


# In[66]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[67]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[ ]:




# In[68]:

pd.DataFrame(data2)


# In[69]:

pd.DataFrame(data2, index=['first', 'second'])


# In[70]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[71]:

pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
               ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
                 ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
              ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
                  ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})


# In[72]:

df


# In[74]:

df ['one']


# In[75]:

df ['three'] = df ['one'] * df ['two']


# In[76]:

df


# In[78]:

df['flag'] = df['one'] > 2


# In[79]:

df


# In[80]:

del df['two']


# In[81]:

df


# In[82]:

df.loc ['a']


# In[83]:

df


# In[85]:

three = df.pop('three')


# In[86]:

df


# In[87]:

df['foo'] = 'bar'


# In[88]:

df


# In[89]:

df['one_trunc'] = df['one'][:2]


# In[90]:

df


# In[95]:

df.insert(1, 'bar', df['one'])


# In[92]:

df


# In[ ]:



