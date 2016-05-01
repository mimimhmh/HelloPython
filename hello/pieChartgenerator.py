import matplotlib.pyplot as plt
import checker

class PieGenerator(object):

    def display_by_weight(self):
         d = checker.DataChecker('test.txt')
         no= 0
         ov = 0
         ob = 0
         un = 0
         list = d.getEmpList()
         bmiList = d.check(list)[4]
         for i in range(len(bmiList)):
              if bmiList[i] == 'Normal':
                no += 1
              elif bmiList[i] == 'Overweight':
                ov += 1
              elif bmiList[i] == 'Obesity':
                ob += 1
              elif bmiList[i] == 'Underweight':
                un += 1
         labels = 'Normal', 'Overweight', 'Obesity', 'Underweight'
         sizes = [no,ov,ob,un]
         colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
         explode = (0, 0.1, 0, 0)
         plt.pie(sizes, explode=explode, labels=labels, colors=colors,
         autopct='%1.1f%%', shadow=True, startangle=90)
         plt.axis('equal')
         plt.show()


