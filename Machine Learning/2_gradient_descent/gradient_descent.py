import numpy as np
import pandas as pd
from sklearn import linear_model 
from matplotlib import pyplot as plt
def gradient_descent(x,y):
    m_cur=b_cur=0
    intertions=3700
    n= len(x)
    learning_rate=0.05
    for i in range(intertions):
        y_predicted= m_cur*x+b_cur
        cost =(1/n)*sum([val**2 for val in (y-y_predicted)])


        
        md= -(2/n)*sum(x*(y-y_predicted))
        bd= -(2/n)*sum(y-y_predicted)
        m_cur=m_cur-learning_rate*md
        b_cur = b_cur- learning_rate*bd
        print(f"m ={m_cur},  b={b_cur}, cost={cost}, iteration{i} ")







x=np.array([1,2,3,4,5])
y= np.array([5,7,9,11,13])
gradient_descent(x,y)  