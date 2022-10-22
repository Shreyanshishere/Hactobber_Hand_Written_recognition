
from sklearn.datasets import fetch_openml

mnist=fetch_openml('mnist_784')
 
  #1 Update X and Y values
  
  
x=mnist.data.values
y=mnist.target

temp=x[95]
temp.shape

# 2 import matplotlib and show a digit

import matplotlib.pyplot as plt

plt.imshow(temp.reshape(28,28)) 
y[95]

#3 import the train test library

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=10)

#4 import the logistic regression model


model.fit(xtrain,ytrain)

model.score(xtrain,ytrain)

model.score(xtest,ytest)

