import sys
from PyQt5 import QtWidgets
import mysql.connector
from datetime import datetime
from connection import connection
import math,time
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox

connection=connection
mycursor=connection.cursor()

class Program(QtWidgets.QMainWindow):
    def __init__(self):
        super(Program,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnKaydet.clicked.connect(self.urunEkleme)
        self.ui.btnSil.clicked.connect(self.urunSilme)
        self.ui.btnKullan.clicked.connect(self.urunKullanimi)
        self.ui.btnEnvanteriListele.clicked.connect(self.urunListele)
        self.ui.btnAzalanlariGoster.clicked.connect(self.urunListeleAzalan)
        self.ui.btnTemizle.clicked.connect(self.temizleTW)

    def urunEkleme(self):
        ad=self.ui.urunAdiKayit.text()
        adet=self.ui.urunSayisiKayit.text()
        sql = ("INSERT INTO urunler (urun_ismi,urun_adeti,giris_tarihi) VALUES (%s,%s,%s)")
        tarih = datetime.now()
        values = (ad, adet, tarih)
        mycursor.execute(sql, values)
        try:
            connection.commit()
            QtWidgets.QMessageBox.warning(self, 'Warning', f'{ad} Product {adet} unit has been added.',
                                          QtWidgets.QMessageBox.Ok)
        except mysql.connector.Error as err:
            print('Error:', err)

    def urunSilme(self):
        id=self.ui.urunIdSilmek.text()
        sql = ('DELETE FROM urunler WHERE id_urunler=%s')
        value = (id,)
        mycursor.execute(sql, value)

        q=QtWidgets.QMessageBox.question(self, 'Warning', f'Do you want to delete the number {id} product?',
                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )

        if q==QMessageBox.Yes:
            try:
                connection.commit()
            except mysql.connector.Error as err:
                print('Error:', err)
        else:
            QtWidgets.QMessageBox.close()

    def urunKullanimi(self):
        ad=self.ui.urunAdiKullan.text()
        miktar=self.ui.urunSayisiKullan.text()
        sql1 = ('SELECT urun_ismi=%s,SUM(urun_adeti) AS TOTAL FROM urunler  GROUP BY urun_ismi ORDER BY sum(urun_adeti)')
        values1 = (ad,)
        mycursor.execute(sql1, values1)
        varolan = mycursor.fetchall()
        for i in varolan:
            if i[0]==1:
                toplam=i[1]

        if int(toplam) > int(miktar):
            yeni=int(toplam)-int(miktar)
            sql = ('DELETE FROM urunler WHERE urun_ismi=%s')
            tarih=datetime.now()
            value = (ad,)
            mycursor.execute(sql, value)
            sql2=("INSERT INTO urunler (urun_ismi,urun_adeti,giris_tarihi) VALUES (%s,%s,%s)")
            values2=(ad,yeni,tarih)
            mycursor.execute(sql2, values2)
            try:
                connection.commit()
                QtWidgets.QMessageBox.warning(self, 'Warning', f'{ad} prodcut {miktar} unit has been deleted.',QtWidgets.QMessageBox.Ok)
            except mysql.connector.Error as err:
                print('Error:', err)

        elif toplam == int(miktar):
            sql = ('DELETE FROM urunler WHERE urun_ismi= %s')
            value = (ad)
            mycursor.execute(sql, value)
            try:
                connection.commit()
                QtWidgets.QMessageBox.warning(self, 'Warning', f'{ad} product {miktar} has been deleted.',
                                              QtWidgets.QMessageBox.Ok)
            except mysql.connector.Error as err:
                print('Error:', err)
        else:
            print('Yetersiz urun..')
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Demanded product number is not enough.', QtWidgets.QMessageBox.Ok)



    def urunListele(self):
        ad=self.ui.lineEdit.text()

        sql = ("Select * From urunler Where urun_ismi = %s")
        value = (ad,)
        mycursor.execute(sql, value)


        result = mycursor.fetchall()



        self.ui.tableWidget.setRowCount(len(result))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Urun Id', 'Urun Adi','Urun Adeti','Giris Tarihi'))
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 300)


        rowIndex = 0
        for i in result:

            self.ui.tableWidget.setItem(rowIndex, 0, QTableWidgetItem(str(i[0])))
            self.ui.tableWidget.setItem(rowIndex, 1, QTableWidgetItem(str(i[1])))
            self.ui.tableWidget.setItem(rowIndex, 2, QTableWidgetItem(str(i[2])))
            self.ui.tableWidget.setItem(rowIndex, 3, QTableWidgetItem(str(i[3])))
            rowIndex += 1


    def urunListeleAzalan(self):
        esik_deger=self.ui.esikDeger.text()
        sql=('SELECT urun_ismi,SUM(urun_adeti)<=%s,SUM(urun_adeti) AS TOTAL FROM urunler  GROUP BY urun_ismi ORDER BY sum(urun_adeti)')

        value = (esik_deger,)
        mycursor.execute(sql, value)


        result = mycursor.fetchall()


        self.ui.tableWidget.setRowCount(len(result))
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Urun Adi', 'Urun Adeti'))
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 200)
        rowIndex=0

        for i in result:

            if i[1] ==1:
                self.ui.tableWidget.setItem(rowIndex, 0, QTableWidgetItem(str(i[0])))
                self.ui.tableWidget.setItem(rowIndex, 1, QTableWidgetItem(str(i[2])))
                rowIndex += 1
        try:
            connection.commit()
        except mysql.connector.Error as err:
            print('Error:', err)

    def temizleTW(self):
        self.ui.tableWidget.clear()
def application():
    app = QtWidgets.QApplication(sys.argv)
    win = Program()
    win.show()
    sys.exit(app.exec_())


application()




