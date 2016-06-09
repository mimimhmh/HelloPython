import os
import re
import shelve

class DataChecker(object):

    def __init__(self, file_path):
        self.file_path = file_path

        try:
            os.path.exists(file_path)
        except FileNotFoundError as e:
            print('FileNotFoundError',e)
        except FileExistsError as e:
            print('FileExistsError',e)
        print('Data gets loading...')


    def getEmpList(self):
        list = []
        with open(self.file_path) as f:
            for line in f.readlines():
                list.append(line.strip().split(','))

        return list

    def check(self,list):
        idList = []
        gList = []
        aList = []
        saleList = []
        bList = []
        incomeList = []
        for i in range(len(list)):
            if re.match('^[A-Z][0-9]{3}$', list[i][0]): #ID
                idList.append(list[i][0])
            else:
                print('nonono')
            if re.match('^(M|F)$', list[i][1]):#Gender
                gList.append(list[i][1])
            else:
                print('nonono')
            if re.match('^[0-9]{2}$', list[i][2]):#Age
                aList.append(list[i][2])
            else:
                print('nonono')
            if re.match('^[0-9]{3}$', list[i][3]):#Sales
                #print(list[i][3])
                saleList.append(list[i][3])
            else:
                print('nonono')
            if re.match('^(Normal|Overweight|Obesity|Underweight)$', list[i][4]):#BMI
                bList.append(list[i][4])
            else:
                print('nonono')
            if re.match('^[0-9]{2,3}$', list[i][5]):#Income
                incomeList.append(list[i][5])
            else:
                print('nonono')


        return idList,gList,aList,saleList,bList,incomeList


    def dataShelve(self):
        list = check(getEmpList)
        db = shelve.open('db.shelf', 'c')
        for i in range(len(list)):
            db['idList'] = idList
            db['genderList'] = gList
            db['ageList'] = aList
            db['saleList'] = saleList
            db['bmiList'] = bList
            db['incomeList'] = incomeList
        db.close()
'''
d = DataChecker('test.txt')
list = d.getEmpList()
print(list)
#d.check(list)
bList =  d.check(list)[4]
print(bList)
'''
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)