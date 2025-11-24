class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading From Excel")

class MYSQLDBConnection:
    @staticmethod
    def readMySQLFile():
        print("Reading From MySQL")

class TC1:

    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")
tc1=TC1()
tc1.runTC()
tc2=TC1()
tc2.runTC()
