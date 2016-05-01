import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import checker

class BarGenerator(object):

    def display_by_sales(self):
        mpl.rcParams['font.family'] = 'sans-serif'
        mpl.rcParams['font.sans-serif'] = [u'SimHei']
        d = checker.DataChecker('test.txt')
        empList = d.getEmpList()
        n_group = len(empList)
        saleList = d.check(empList)[3]
        #print(saleList) #dayin
        u1 = 0
        u2 = 0
        u3 = 0
        u4 = 0
        for i in range(len(saleList)):
            int_value  = int(saleList[i])
            if 100<= int_value <= 300:
                u1 += 1
            elif 301 <= int_value <= 500:
                u2 += 1
            elif 501<= int_value <= 700:
                u3 += 1
            elif 701 <= int_value:
                u4 += 1
        data = [u1,u2,u3,u4]
        x = np.arange(len(data))
        plt.plot(x, data, color = 'r')
        plt.xlabel('sales')
        plt.ylabel('amount')
        plt.title("display_by_sales")
        plt.bar(x, data, alpha = .5, color = 'g',yerr = 0.0001)
        plt.show()
