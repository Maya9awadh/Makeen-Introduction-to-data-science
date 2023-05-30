# -*- coding: utf-8 -*-
"""
Create a list of 100 random pair of integers (x,y) between 1 and 100. Draw visualization
of the data using different

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.randint(0,100,size=(100, 2)), columns=list('xy'))
print(df.head())

#draw scatter plot
plt.scatter(df['x'],df['y'])
plt.show()