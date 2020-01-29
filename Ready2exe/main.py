from PySide2 import QtCore, QtGui, QtWidgets
import sys
import random
 
#UI
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(361, 458)
        Form.setMinimumSize(QtCore.QSize(360, 458))
        Form.setMaximumSize(QtCore.QSize(360, 458))
        Form.setStyleSheet("QCheckBox { font-size: 14px; }")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 350, 321, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet("QPushButton { \n"
"font-size: 18px;\n"
"width: 75px;\n"
"height: 60px;\n"
" }")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 200, 321, 132))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setStyleSheet("QCheckBox { font-size: 14px; }")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setStyleSheet("QCheckBox { font-size: 14px; }")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setStyleSheet("QCheckBox { font-size: 14px; }")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setStyleSheet("QCheckBox { font-size: 14px; }")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 321, 91))
        self.lineEdit.setStyleSheet("QLineEdit {font-size: 52px; }")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 41))
        self.label.setStyleSheet("QLabel { font-size: 18px; }")
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(20, 160, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 261, 21))
        self.label_2.setStyleSheet("QLabel {font-size: 16px; }")
        self.label_2.setObjectName("label_2")
 
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
 
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("PSW_Gen", "Генератор паролей", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("PSW_Gen", "Сгенерировать", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("PSW_Gen", "Символы в верхнем регистре", None, -1))
        self.checkBox_3.setText(QtWidgets.QApplication.translate("PSW_Gen", "Символы в нижнем регистре", None, -1))
        self.checkBox_4.setText(QtWidgets.QApplication.translate("PSW_Gen", "Цифры", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("PSW_Gen", "Дополнительные символы", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("PSW_Gen", "Безопасный генератор паролей", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("PSW_Gen", "Количество символов", None, -1))
 
 
 
#Создание приложения
app = QtWidgets.QApplication(sys.argv)
 
#Cоздание интерфейса
Form = QtWidgets.QWidget()
Form.setWindowTitle("Form")
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
 
#Список символов
Big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
Low = 'qwertyuiopasdfghjklzxcvbnm'
Num = '1234567890'
Spe = '!@#$%^&*()'
 
def bp(): #блок действий
    BI = (ui.checkBox_2.isChecked())  
    LO = (ui.checkBox_3.isChecked())
    NU = (ui.checkBox_4.isChecked())  
    PS = (ui.checkBox.isChecked())
 
    Pass_Symbol = []
    if BI == True:
        Pass_Symbol.extend(list(Big))
    if LO == True:
        Pass_Symbol.extend(list(Low))
    if NU == True:
        Pass_Symbol.extend(list(Num))
    if PS == True:
        Pass_Symbol.extend(list(Spe))
 
    random.shuffle(Pass_Symbol)
 
    Password_len = int(ui.spinBox.text())#Кол-во символов
    psw = [] #пустой список для пароля
    psw.append(''.join([random.choice(Pass_Symbol) for x in range(Password_len)])) #Генерация пароля
   
    ui.lineEdit.setText( '\n'.join(psw) )#Запись результата в LineEdit
 
ui.pushButton.clicked.connect( bp )#запуск генерации по кнопке
 
#Запуск основного цикла
sys.exit(app.exec_())