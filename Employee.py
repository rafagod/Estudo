
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QDialog, QInputDialog, QlineEdit, QMessageBox
from PyQt5.QtGui import QIcon

class Ui_Dialog(Qdialog):
    def SetupUi(self,Dialog):
        Dialog.setObjectName('Dialog')
        Dialog.resize(611, 428)
        self.verticalLayout_2 = QtWidgets.QVboxlayout(Dialog)
        self.verticalLayout_2 = setObjectName('verticalLayout_2')
        self.horizontalLayout = QtWidgets.QHBoxlayout()
        self.horizontalLayout.setObjectName('horzontalLayout')
        
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName('listWidget')
        self.verticalLayout.addWidget(self.listWidget)
        
        self.verticalLayout = QtWidgets.QVBoxLayout()        
        self.verticalLayout.setObjectName('verticalLayout')
        
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setObjectName('pushButton_add')        
        self.verticalLayout.addWidget(self.pushButton_add)
                                      
        self.pushButton_edit = QtWidgets.QPushButton(Dialog)        
        self.pushButton_edit.setObjectName('pushButton_edit')
        self.verticalLayout.addWidget(self.pushButton_edit)
                                      
        self.pushButton_remove = QtWidgets.QPushButton(Dialog)
        self.pushButton_remove.setObjectName('pushButton_remove')
        self.verticalLayout.addWidget(self.pushButton_remove)
        
        self.pushButton_up = QtWidgets.QPushButton(Dialog)
        self.pushButton_up.setObjectName('pushButton_up')
        self.verticalLayout.addWidget(self.pushButton_up)
        
        self.pushButton_down = QtWidgets.QPushButton(Dialog)
        self.pushButton_down.setObjectName('pushButton_down')
        self.verticalLayout.addWidget(self.pushButton_down)
                                      
        self.pushButton_sort = QtWidgets.QPushButton(Dialog)
        self.pushButton_sort.setObjectName('pushButton_sort')
        self.verticalLayout.addWidget(self.pushButton_sort)

        spacerItem = QtWidgets.QSpacerItem(20, 40 , QtWidgets.QSizePolicy
                                           .Mininum, QtWigets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
                                      
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setObjectName('pushButton_close')
        self.verticalLayout.addWidget(self.pushButton_close)

        Self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pushButton_add.clicked.connect(self.Add)
        self.pushButton_edit.clicked.connect(self.Edit)
        self.pushButton_remove.clicked.connect(self.Remove)
        self.pushButton_up.clicked.connect(self.Up)
        self.pushButton_down.clicked.connect(self.Down)
        self.pushButton_sort.clicked.connect(self.Sort)
        self.pushButton_close.clicked.connect(self.Close)
        
                                      
        self.label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName('Label')
        self.verticalLayout_2.addWidget(self.label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject,connectSlotsbyName(Dialog)
        self.Employee()
                                      
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Empregados App:"))
        
        Dialog.setWindowIcon(QIcon("admin.png"))
        
        self.pushButton_add.setText(_translate("Dialog", "Add"))
        self.pushButton_edit.setText(_translate("Dialog", "Editar"))
        self.pushButton_remove.setText(_translate("Dialog", "Remover"))
        self.pushButton_up.setText(_translate("Dialog", "Up"))
        self.pushButton_down.setText(_translate("Dialog", "Down"))
        self.pushButton_sort.setText(_translate("Dialog", "Confirmar"))
        self.pushButton_close.setText(_translate("Dialog", "Sair"))
        self.label.setText(_translate('Dialog','<html><head/><body><p align=\"center\"><span style=\"font-size:10pt;color:red\"> vieiratafael42@gmail.com | Todos os direitos reservados</span></body></p></html>'))
        
    def Employee(self):
        self.employee = ['san1', 'san2', 'san3', 'san4']
        self.listWidget.addItems(self.employee)
        self.listWidget.setCurrentRow(0)

    def Add(self):
        row = self.listWidget.currentRow(0)
        text,ok = QInputDialog.getText(self,"Cadastro de Empregados",
                                       "Digite o nome do Funcionarios")
        if ok and text is not None:
            self.listWidget.insertItem(row, text)

    def Edit(self):        
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        string ,ok = QInputDialog.getText(self,"Cadastro de Empregados",
                                          "Digite o nome do Funcionarios", QLineEdit.Normal, item.text())
        if ok and string is not None:
            item.setText(string)

    def Remover(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        
        if item is None:
            return
        reply = QMessageBox.question(self, 'deletar esse funcionário',
                                     'Deseja realmente deletar esse funcionário?'+ str(item.text()),QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item
            reply = QMessageBox.information(self,'Funcionário Deltado com ')

        def Up(self):        
            row = self.listWidget.currentRow()
            if row>=1:
                item = self.listWidget.takeItem(row)
                self.listWidget.insertItem(row-1,item)
                self.listWidget.setCurrentItem(item)

        def Down(self):        
            row = self.listWidget.currentRow()
            if row<self.listWidget.count()-1:
                item = self.listWidget.takeItem(row)
                self.listWidget.insertItem(row+1,item)
                self.listWidget.setCurrentItem(item)

        def Sort(self):
            self.listWidget.sortItem()
            
        def Close(self):
            self.quit()
                           
                
                
          
    
        

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.Q.Dialog()
    ui = Ui_Dialog()
    ui.setupUI(Dialog)
    Dialog.show()
    sys.exit(app.exe_())



        
        
        
