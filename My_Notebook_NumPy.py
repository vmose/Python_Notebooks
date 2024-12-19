# %%
import numpy as np
#importing numpy repository

# %%
z=[1,2,3]
np.array(z)

# %%
q=[[1,2,3],[4,5,6],[7,8,9]]
np.array(q)

# %%
np.linspace(0,20,10)
#evenly spaced values between 0 & 20

# %%
np.random.randn(5,5)

#random values in 5x5 matrix

# %%
x=np.random.randint
x(10,100,10)

#random intergers between 10 & 100

# %%
#Creating sample array
v=np.arange(0,11)
v

# %%
#Get values in a range
v[0:5]

# %%
#Boolean
v>5

# %%
#Indexing 2D arrays
b = np.array(([5,10,15],[20,25,30],[35,40,45]))
b
# %%
b[1]

# %%
b[1][2]

# %%
#Fancy Indexing
d=np.zeros((10,10))
d_length = d.shape[1]

for i in range(d_length):
    d[i] = i
    
d

# %%
a=np.array(([5,10,15],[20,25,30],[35,40,45]))
a

# %%
b=np.array(([6,20,40],[15,55,25],[33,12,43]))
b

# %%
np.mean(b != a)

# %%
x=[]
x.append(np.mean(b != a))

# %%
np.eye(3) * 3

