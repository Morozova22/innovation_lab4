from PyQt5 import QtCore, QtGui, QtWidgets
import sys,pymongo

from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 470)
        MainWindow.setFixedSize(800,470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_input = QtWidgets.QTextEdit(self.centralwidget)
        self.text_input.setGeometry(QtCore.QRect(30, 40, 241, 351))
        self.text_input.setObjectName("text_input")
        self.btn_local = QtWidgets.QPushButton(self.centralwidget)
        self.btn_local.setGeometry(QtCore.QRect(20, 400, 130, 30))
        self.btn_local.setObjectName("btn_local")
        self.text_address = QtWidgets.QTextEdit(self.centralwidget)
        self.text_address.setGeometry(QtCore.QRect(160, 400, 370, 60))
        self.text_address.setObjectName("text_address")
        self.btn_get = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_address = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_address.setGeometry(QtCore.QRect(550, 270, 230, 30))
        self.btn_clear_address.setObjectName("btn_clear_address")
        self.lb_text = QtWidgets.QLabel(self.centralwidget)
        self.lb_text.setGeometry(QtCore.QRect(30, 20, 140, 16))
        self.lb_text.setObjectName("lb_text")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.rbtn_c = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_c.setEnabled(True)
        self.rbtn_c.setGeometry(QtCore.QRect(570, 100, 115, 19))
        self.rbtn_c.setObjectName("rbtn_c")
        self.rbtn_c.setChecked(True)
        self.buttonGroup.addButton(self.rbtn_c)
        self.lb_choice = QtWidgets.QLabel(self.centralwidget)
        self.lb_choice.setGeometry(QtCore.QRect(570, 60, 72, 15))
        self.lb_choice.setObjectName("lb_choice")
        self.text_output = QtWidgets.QTextEdit(self.centralwidget)
        self.text_output.setGeometry(QtCore.QRect(280, 40, 251, 351))
        self.text_output.setObjectName("text_output")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 72, 15))
        self.label.setObjectName("label")
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(550, 150, 230, 30))
        self.btn_run.setObjectName("btn_run")
        self.lb_name = QtWidgets.QLabel(self.centralwidget)
        self.lb_name.setEnabled(True)
        self.lb_name.setGeometry(QtCore.QRect(650, 446, 51, 20))
        self.lb_name.setObjectName("lb_name")
        self.btn_clear_input = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_input.setGeometry(QtCore.QRect(550, 190, 230, 30))
        self.btn_clear_input.setObjectName("btn_clear_input")
        self.btn_clear_output = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_output.setGeometry(QtCore.QRect(550, 230, 230, 30))
        self.btn_clear_output.setObjectName("btn_clear_output")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LexicalAnalyzer"))
        self.lb_text.setText(_translate("MainWindow", "Код для анализа:"))
        self.rbtn_c.setText(_translate("MainWindow", "C"))
        self.lb_choice.setText(_translate("MainWindow", "Язык:"))
        self.label.setText(_translate("MainWindow", "Вывод:"))
        self.btn_run.setText(_translate("MainWindow", "Анализ"))
        self.lb_name.setText(_translate("MainWindow", "x1nge."))
        self.btn_clear_input.setText(_translate("MainWindow", "Пусто для анализа"))
        self.btn_local.setText(_translate("MainWindow", "Просматривать"))
        self.text_address.setText(_translate("MainWindow", "Вы можете вручную ввести здесь путь (в настоящее время поддерживаются файлы txt)"))
        self.btn_clear_output.setText(_translate("MainWindow", "Пустой вывод"))
        self.btn_clear_address.setText(_translate("MainWindow", "Пустой путь"))

class main_window(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(main_window,self).__init__()
        self.setupUi(self)

        self.text_output.clear()

        try:
            check_client = pymongo.MongoClient("mongodb://localhost:27017/")
            check_db = check_client["PrincipleOfCompiler"]
            check_col = check_db["ReservedWord"]
        except:
            self.text_output.append("информация: в настоящее время не подключена к предустановленной библиотеке зарезервированных шрифтов mongodb, зарезервированные слова будут распознаваться как юридически определенные идентификаторы или"
                                    "Целочисленная константа \ n --------------------------")

        # Настроить слушателя
        self.btn_clear_input.clicked.connect(self.btn_clear_input_click)
        self.btn_clear_output.clicked.connect(self.btn_clear_output_click)
        self.btn_run.clicked.connect(self.btn_run_click)
        self.btn_local.clicked.connect(self.btn_openfile_click)
        self.btn_get.clicked.connect(self.btn_load_address_click)
        self.btn_clear_address.clicked.connect(self.btn_clear_address_click)

    # Написание функции
    def btn_clear_input_click(self):
         self.text_input.clear()

    def btn_clear_output_click(self):
        self.text_output.clear()

    def btn_openfile_click(self):
        filename,_ = QFileDialog.getOpenFileName()
        self.text_address.setText(filename)
        text = open(filename,'r').read()
        self.text_input.setText(text)

    def btn_load_address_click(self):
        f = open(self.text_address.toPlainText(),'r')
        res = f.read()
        self.text_input.setText(res)
        f.close()

    def btn_clear_address_click(self):
        self.text_address.clear()

    def btn_run_click(self):
        res = self.text_input.toPlainText().replace('\n','').replace('\t','').replace('  ',' ')
        res_lst1 = list(res)
        res_lst1.append("\0")
        print(res)
        print(res_lst1)
        global p
        p = 0
        while p in range(len(res_lst1)):
            if res_lst1[p] == "\0":
                break
            temp_output = ','.join(check_code(res_lst1))
            self.text_output.append(temp_output)

p = 0 # Инициализация
def check_code(res_lst):
    # Инициализация
    result = []
    str_get = []
    ch = get_char(res_lst)
    new_ch = get_blank_ch(ch,res_lst)
    # Идентификационный идентификатор
    if  new_ch.isalpha() or new_ch == '_' or new_ch == '$':
        str_get.append(new_ch)
        new_ch = get_char(res_lst)
        while new_ch.isalpha() or new_ch.isdigit() or new_ch == '_' or new_ch == '$':
            str_get.append(new_ch)
            new_ch = get_char(res_lst)
        retract_pointer()
        str_result = ''.join(str_get)
        code = is_reserved_word(str_result)
        if code == 0 :
            value = insert_identifier(str_result)
            result.append('Ключевое слово') # Здесь 2 используется как код типа идентификатора незарезервированного слова
            result.append(value)
            return result
        else:
            result.append('Идентификатор') # Здесь 1 используется как код категории зарезервированного слова
            result.append(str_result) # В экспериментальном примере значением является само зарезервированное слово
            """
                         result.append ('-') # Зарезервированные слова не имеют собственного значения
            """
            return result
    # Определить целочисленные константы
    elif new_ch.isdigit():
        str_get.append(new_ch)
        new_ch = get_char(res_lst)
        while new_ch.isdigit():
            str_get.append(new_ch)
            new_ch = get_char(res_lst)
        retract_pointer()
        str_result = ''.join(str_get)
        value = insert_constant(str_result)
        result.append('Целочисленная константа') # Здесь 3 используется как код категории целочисленной константы
        result.append(value)
        return result
    #Identification Operator
    elif new_ch == '=' or new_ch == '+' or new_ch == '-' or new_ch == '*' or new_ch == '/' or new_ch == '>'\
        or new_ch == '<' or new_ch == '!' or new_ch == '%':
        if new_ch == '>' or new_ch == '<' or new_ch == '!':
            str_get.append(new_ch)
            value = ''.join(new_ch)
            new_ch = get_char(res_lst)
            if new_ch == '=':
                str_get.append(new_ch)
                str_result = ''.join(str_get)
                result.append('Оператор') # Здесь 4 используется как код типа оператора
                result.append(str_result)
                return result
            else:
                retract_pointer()
                result.append('4')
                result.append(value)
                return result
        elif new_ch == '*':
            str_get.append(new_ch)
            value = ''.join(new_ch)
            new_ch = get_char(res_lst)
            if new_ch == '*':
                str_get.append(new_ch)
                str_result = ''.join(str_get)
                result.append('4')
                result.append(str_result)
                return result
            else:
                retract_pointer()
                result.append('4')
                result.append(value)
                return result
        else:
            value = ''.join(new_ch)
            result.append('4')
            result.append(value)
            return  result
    # Определить разделитель
    elif new_ch == ',' or new_ch == ';' or new_ch == '{' or new_ch == '}' or new_ch == '(' or new_ch == ')':
        value = ''.join(new_ch)
        result.append('Разделитель') # Используйте 5 как код категории разделителя
        result.append(value)
        return result
    else:
        result.append("Error.")
        return result

# Читать следующий символ в new_ch
def get_char(res_lst):
    global p
    temp_ch = res_lst[p]
    p += 1
    return temp_ch

# Пропускаем пробел, пока ch не прочитает не пробел
def get_blank_ch(temp_ch_1,res_lst):
    if temp_ch_1 == ' ':
        temp_ch_2 = get_char(res_lst)
        return temp_ch_2
    return temp_ch_1

# Подключаем символы в ch к str_get
def ch_append():
    # Вызов функции Python напрямую
    return

# Находим, есть ли str_get в таблице зарезервированных слов, если она существует, возвращает 1, в противном случае возвращает 0
def is_reserved_word( str_result ):
    try:
        check_client = pymongo.MongoClient("mongodb://localhost:27017/")
        check_db = check_client["PrincipleOfCompiler"]
        check_col = check_db["ReservedWord"]
        check_query = {"content" : str_result}
        for get_text in check_col.find(check_query):
            # Определяем, является ли сопоставленный get_text пустым, если он не пуст, строка для сопоставления находится в списке зарезервированных слов
            if any(get_text):
                check_client.close()
                return 1
        """
        check_doc = check_col.find(check_query)
        print(check_doc)
        for res in check_doc:
            print(res)
        """
        check_client.close()
    except:
        return 0
    return 0

# Обратный вызов указателя поиска на позицию символа
def retract_pointer():
    global p
    p -= 1
    return

# Если распознается как идентификатор, вставить идентификатор в str_result в таблицу символов и вернуть указатель таблицы символов
def insert_identifier( str_result ):
    return str_result

# Если распознается как константа, вставить константу в str_result в таблицу констант и вернуть указатель таблицы параметров
def insert_constant( str_result ):
    return str(bin(int(str_result)))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_show = main_window()
    main_show.show()
    sys.exit(app.exec())
