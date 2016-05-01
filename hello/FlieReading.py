from cmd import Cmd
import pieChartgenerator
import BarChartCreater
import sys


class CmdTest(Cmd):

    def __init__(self):            #
        Cmd.__init__(self)
        self.prompt = '->'

    def help_load(self):
        print("loading data from a txt file")
        print('Input should include absolute path otherwise the default file will be used.')

    def do_load(self,file_path=''):
        if not file_path == '':
            with open(file_path, 'r') as f:
                for line in f.readlines():
                    print(line.strip())
        else:
            with open('test.txt', 'r') as f:
                for line in f.readlines():
                    print(line.strip())

    def help_pie(self):
        print('Print a pie chart.')

    def do_pie(self,inst):
         p = pieChartgenerator.PieGenerator()
         p.display_by_weight()

    def help_bar(self):
        print('Print a bar chart.')

    def do_bar(self,inst):
        b = BarChartCreater.BarGenerator()
        b.display_by_sales()

    def help_exit(self):
        print("program exit")

    def do_exit(self,line):
        print("Exit:",line)
        sys.exit()

if __name__ =="__main__":
    cmd=CmdTest()
    cmd.cmdloop()
