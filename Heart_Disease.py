# %%
import numpy as np
import pandas as pd
import seaborn as sb

# %%
heart=pd.read_csv('heart.csv')
heart.head()

# %%
heart.info()

# %%
heart.describe()

# %%
heart.corr()

# %%
sb.heatmap(heart.corr())

# %%
sb.heatmap(heart.isnull(),cbar=False)

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

reg=LogisticRegression(solver='lbfgs', max_iter=1000)
X_train,X_test,y_train,y_test = train_test_split(heart.drop('target',axis=1),heart['target'],test_size=0.3,random_state=101)

# %%
reg.fit(X_train,y_train)


# %%
pred=reg.predict(X_test)

# %%
from sklearn.metrics import classification_report,confusion_matrix

# %%
print(confusion_matrix(y_test,pred))

# %%
print(classification_report(y_test,pred))

