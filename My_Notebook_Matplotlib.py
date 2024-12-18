# %%
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
#importing relevant libraries

# %%
x = np.linspace(0, 5, 11)
y = x ** 2
#creating data points for the graphical distribution

# %%
plt.plot(x, y, 'g') 
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Title')
plt.show()
#ploting the graph


# %%
#multiplots 
plt.subplot(1,2,1)
plt.plot(x, y, 'r--') 
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-');


# %%
#multiple figures

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) 

axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 2 Title')

axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title');


# %%
x = np.arange(0,100)
y = x*2
z = x**2

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))

axes[0].plot(x,y,color="blue", lw=5) #thicker blue graph
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z,color="red", lw=3, ls='--') #dotted graph
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
# %%
