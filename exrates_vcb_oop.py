import xml.dom.minidom as minidom
from urllib.request import urlopen
import ssl

class Exrate:
    url = ""
    datetime = ""
    source = ""
    att = tuple()
    values = []
    result = []
    parse = False
    def __init__(self):
        self.att = ("CurrencyCode", "CurrencyName", "Buy", "Transfer", "Sell")
        self.values = [None]*5
    def parseData(self):
        # create connection
        context = ssl._create_unverified_context()
        self.url = r"https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx"
        obj = urlopen(self.url, context = context)

        # parsing the data
        data = obj.read()
        document = minidom.parseString(data)
        ex_list = document.getElementsByTagName("Exrate")
        for element in ex_list:
            for i in range(5):
                self.values[i] = element.getAttribute(self.att[i])
            pair = dict(zip(self.att,self.values))
            self.result.append(pair)

        # Get datetime of data
        dt = document.getElementsByTagName("DateTime")[0]
        node = dt.childNodes[0]
        self.datetime = node.data

        # Get source info
        dt = document.getElementsByTagName("Source")[0]
        node = dt.childNodes[0]
        self.source = node.data
        
        self.parse = True
    def info(self):
        if self.parse == False:
            self.parseData()
            self.info()
        else:
            print("*"*70)
            print("Time", self.datetime)
            print(self.source)
    def showAll(self):
        if self.parse == False:
            self.parseData()
            self.showAll()
        else:
            print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(self.att[0],self.att[1],self.att[2],self.att[3],self.att[4]))
            for row in self.result:
                print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(row[self.att[0]],row[self.att[1]],row[self.att[2]],row[self.att[3]],row[self.att[4]]))
            self.info()
    def show(self, code):
        if self.parse == False:
            self.parseData()
            self.show(code)
        else:
            found = False
            for row in self.result:
                if row["CurrencyCode"] == code:
                    print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(self.att[0],self.att[1],self.att[2],self.att[3],self.att[4]))
                    print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(row[self.att[0]],row[self.att[1]],row[self.att[2]],row[self.att[3]],row[self.att[4]]))
                    found = True
                    break
            if found == False:
                print("CurrencyCode is not found in data")
            self.info()
    def buy(self, code):
        if self.parse == False:
            self.parseData()
            self.buy(code)
        else:
            found = False
            for row in self.result:
                if row["CurrencyCode"] == code:
                    print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(self.att[0],self.att[1],self.att[2],"",""))
                    print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(row[self.att[0]],row[self.att[1]],row[self.att[2]],"",""))
                    found = True
                    break
            if found == False:
                print("CurrencyCode is not found in data")
            self.info()
    def transfer(self, code):
        if self.parse == False:
            self.parseData()
            self.transfer(code)
        else:
            found = False
            for row in self.result:
                if row["CurrencyCode"] == code:
                    print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(self.att[0],self.att[1],"",self.att[3],""))
                    print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(row[self.att[0]],row[self.att[1]],"",row[self.att[3]],""))
                    found = True
                    break
            if found == False:
                print("CurrencyCode is not found in data")
            self.info()
    def sell(self, code):
        if self.parse == False:
            self.parseData()
            self.sell(code)
        else:
            found = False
            for row in self.result:
                if row["CurrencyCode"] == code:
                    print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(self.att[0],self.att[1],"","",self.att[4]))
                    print("{:<14}{:<20}{:<12}{:<12}{:<12}".format(row[self.att[0]],row[self.att[1]],"","",row[self.att[4]]))
                    found = True
                    break
            if found == False:
                print("CurrencyCode is not found in data")
            self.info()
if __name__ == "__main__":
    exrate = Exrate()
    exrate.showAll()
