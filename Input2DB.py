import sqlite3
  
class PA:
    
    def __init__(self):
        self.data=[]        

    def Input2DB(self,date,barcode,group,type1,mynote,qty,price):
        self.conn = sqlite3.connect("D:\Python\Python36-32\Обучение\SqlLite3\example.db")
        self.c=self.conn.cursor()
        self.data=[(date,barcode,group,type1,mynote,qty,price)]
        self.c.executemany('INSERT INTO Stock VALUES (?,?,?,?,?,?,?)',self.data)
        self.conn.commit()
        self.conn.close()

    def ExtData(self,barcode):
        self.conn = sqlite3.connect("D:\Python\Python36-32\Обучение\SqlLite3\example.db")
        self.Ext=self.conn.cursor()
        self.BarcodeReceived=barcode
        self.Ext.execute("SELECT *  FROM Stock WHERE barcode='%s'"% self.BarcodeReceived)
        rows=self.Ext.fetchone()
        self.conn.commit()
        self.conn.close()
        return rows
    def SalesRec(self, sales):
        self.conn = sqlite3.connect("D:\Python\Python36-32\Обучение\SqlLite3\example.db")
        self.c=self.conn.cursor()
        self.sales=[(sales[0],sales[1],sales[2],sales[3])]
        self.c.executemany('INSERT INTO Sales VALUES (?,?,?,?)',self.sales)
        self.conn.commit()
        self.conn.close()

    def StockBal(self,barcode):
        conn = sqlite3.connect("D:\Python\Python36-32\Обучение\SqlLite3\example.db")
        c=conn.cursor()
        c.execute("SELECT qty,price FROM Stock WHERE barcode='%s'" %barcode)
        rows=c.fetchone()
        c.execute("SELECT SUM(qty) FROM Sales WHERE barcode='%s'" %barcode)
        rowsSales=c.fetchall()        
        conn.commit()
        conn.close()
        return (rows[0],rowsSales[0][0],rows[1])
    
    def EntStockBal(self,barcode,entr):
        conn = sqlite3.connect("D:\Python\Python36-32\Обучение\SqlLite3\example.db")
        c=conn.cursor()
        data=[(barcode,(entr[0]-entr[1]),entr[2])]
        c.executemany('INSERT INTO StockBalance VALUES (?,?,?)',data)
        conn.commit()
        conn.close()
        
     
        
        
if __name__=='__main__':
    s=PA()
    data=s.StockBal('9556412600006')
    s.EntStockBal('9556412600006',entr=data)
       

        
        
'''F=PA()
F.Input2DB('a','b','a','a',1,9)'''
