class Student(object):
   def __init__(self,name,score):
       self.__name = name
       self.__score = score

   def __str__(self):
        return  'I am ' + self.__name + ' and ' + self.__score

   def print_score(self):
        print('%s: %s' %(self.__name, self.__score))

   def get_grade(self):
       if self.__score >= 90:
           return 'A'
       elif self.__score >=60:
           return 'B'
       else:
           return 'C'

bart = Student('Mike',96)
bart.__name
print(bart.get_grade())