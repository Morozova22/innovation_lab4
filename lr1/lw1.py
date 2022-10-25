from PyQt5 import QtCore, QtGui, QtWidgets
import math
import pyqtgraph as pg
import pyqtgraph.exporters
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btngraph = QtWidgets.QPushButton(self.centralwidget)
        self.btngraph.setGeometry(QtCore.QRect(40, 30, 191, 31))
        self.btngraph.setObjectName("btngraph")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 100, 340, 440))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.extremum = QtWidgets.QPushButton(self.centralwidget)
        self.extremum.setGeometry(QtCore.QRect(10, 570, 351, 31))
        self.extremum.setObjectName("extremum")
        self.copygraph = QtWidgets.QPushButton(self.centralwidget)
        self.copygraph.setGeometry(QtCore.QRect(10, 620, 351, 31))
        self.copygraph.setObjectName("copygraph")
        self.graphic = pg.PlotWidget(self.centralwidget)
        self.graphic.setGeometry(QtCore.QRect(380, 30, 790, 510))
        self.graphic.setObjectName("graphic")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 580, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(760, 580, 160, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(760, 610, 160, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(760, 640, 160, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(630, 550, 350, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.izmereniya = QtWidgets.QLineEdit(self.centralwidget)
        self.izmereniya.setGeometry(QtCore.QRect(590, 580, 141, 22))
        self.izmereniya.setObjectName("izmereniya")
        self.srznach = QtWidgets.QLineEdit(self.centralwidget)
        self.srznach.setGeometry(QtCore.QRect(920, 580, 220, 22))
        self.srznach.setObjectName("srznach")
        self.sko = QtWidgets.QLineEdit(self.centralwidget)
        self.sko.setGeometry(QtCore.QRect(920, 610, 220, 22))
        self.sko.setObjectName("sko")
        self.disprs = QtWidgets.QLineEdit(self.centralwidget)
        self.disprs.setGeometry(QtCore.QRect(920, 640, 220, 22))
        self.disprs.setObjectName("disprs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btngraph.clicked.connect(lambda: self.openmemo())
        self.copygraph.clicked.connect(lambda: self.SaveCall())
        self.extremum.clicked.connect(lambda: self.SaveMemo())
        self.x = []
        self.y = []
        self.sum = 0
        self.cko = 0
        self.ex = []
        self.maxX = []
        self.maxY = []
        self.fname = ''

        if (self.checkBox.checkState() and self.fname != ''):
            self.mygr()
            for i in range(len(self.maxY)):
                self.text2 = pg.TextItem(str(self.maxX[i]), 'r')
                self.text2.setPos(self.maxX[i], self.maxY[i])
                self.graphic.addItem(self.text2)
    def mygr(self):
        self.graphic.clear()
        # Add Background colour to white
        self.graphic.setBackground('w')
        # Add Title
        self.graphic.setTitle("Экстремумы функции", color="b", size="10pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphic.setLabel("left", "Х", **styles)
        self.graphic.setLabel("bottom", "Y", **styles)
        # Add legend
        self.graphic.addLegend()
        # Add grid
        self.graphic.showGrid(x=True, y=True)
        # Set Range
        self.graphic.setXRange(0, 10000, padding=0)
        self.graphic.setYRange(0, 0.1, padding=0)

        self.plot(self.x, self.y, "По оси Х", 'b')
        if(self.checkBox.checkState()):
            self.mygr()
            for i in range(len(self.maxY)):
                self.text2 = pg.TextItem(str(self.maxX[i]), 'r')
                self.text2.setPos(self.maxX[i], self.maxY[i])
                self.graphic.addItem(self.text2)
    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphic.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=5, symbolBrush=(color))


    def openmemo(self):
        self.x = []
        self.y = []
        self.sum = 0
        self.cko = 0
        self.ex = []
        self.maxX = []
        self.maxY = []
        self.izmereniya.setText('')
        self.srznach.setText('')
        self.disprs.setText('')
        self.sko.setText('')
        self.plainTextEdit.clear()
        self.fname = QtWidgets.QFileDialog.getOpenFileName()[0]
        f = open(self.fname, 'r')
        with f:
            while True:
                line = f.readline()
                # прерываем цикл, если строка пустая
                if not line:
                    break
                temp = line.split('|')
                self.x.append(float(temp[0]))
                self.y.append(float(temp[1]))

        self.sr = sum(self.y) / len(self.y)
        for i in range(len(self.y)):
            self.cko += (self.y[i] - self.sr)*(self.y[i] - self.sr)
            if (i>0 and i<len(self.y)) :
                if self.y[i] >= self.y[i - 1] and self.y[i] > self.y[i + 1] and self.y[i] > 0.01:
                    self.maxX.append(self.x[i])
                    self.maxY.append(self.y[i])
                    self.plainTextEdit.insertPlainText(str(self.x[i])+' ' + str(self.y[i]) + '\n')


        self.disp = float(self.cko/len(self.y))
        self.izmereniya.setText(str(len(self.x)))
        self.srznach.setText(str(sum(self.y)/len(self.y)))
        self.disprs.setText(str(self.disp))
        self.sko.setText(str(math.sqrt(self.cko/len(self.y))))

        self.mygr()

    def SaveCall(self):
        self.exporter = pg.exporters.ImageExporter(self.graphic.plotItem)
        self.exporter.params.param('width').setValue(900, blockSignal=self.exporter.widthChanged)
        self.exporter.params.param('height').setValue(500, blockSignal=self.exporter.heightChanged)
        self.exporter.export('ImgGraph.png')
        сlipboard = QtWidgets.QApplication.clipboard()
        сlipboard.setPixmap(QtGui.QPixmap('ImgGraph.png'))

    def SaveMemo(self):
        сlipboard = QtWidgets.QApplication.clipboard()
        сlipboard.setText(self.plainTextEdit.toPlainText())
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа №1"))
        self.label.setText(_translate("MainWindow", "Найденные экстремумы"))
        self.btngraph.setText(_translate("MainWindow", "Построить график"))
        self.extremum.setText(_translate("MainWindow", "Скопировать экстремумы в буфер ММО"))
        self.copygraph.setText(_translate("MainWindow", "Скопировать график в буфер ММО"))
        self.label_2.setText(_translate("MainWindow", "Считано измерений"))
        self.label_3.setText(_translate("MainWindow", "Среднее значение"))
        self.label_4.setText(_translate("MainWindow", "СКО"))
        self.label_5.setText(_translate("MainWindow", "Дисперсия"))
        self.checkBox.setText(_translate("MainWindow", "убрать/поставить метки эктремумов"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    def update_Ed():
        if (ui.checkBox.checkState() and ui.fname != ''):
            for i in range(len(ui.maxY)):
                ui.text2 = pg.TextItem(str(ui.maxX[i]), 'r')
                ui.text2.setPos(ui.maxX[i], ui.maxY[i])
                ui.graphic.addItem(ui.text2)
        else:
            ui.mygr()


    timer = QtCore.QTimer()
    timer.timeout.connect(update_Ed)
    timer.start(100)
    sys.exit(app.exec_())
