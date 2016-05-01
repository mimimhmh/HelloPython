import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']

data = [100,200,300,400,500]
x = np.arange(len(data))

plt.plot(x, data, color = 'r')
plt.bar(x, data, alpha = .5, color = 'g')

plt.show()