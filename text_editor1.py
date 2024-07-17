from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMenu, QAction
import requests
from thesaurus import Ui_Thesaurus
class Ui_text_editor(object):
    def setupUi(self, text_editor):
        text_editor.setObjectName("text_editor")
        text_editor.resize(1000, 1000)
        text_editor.setStyleSheet("background-color: #7A6563;\n")
        
        self.textEdit = QtWidgets.QTextEdit(text_editor)
        self.textEdit.setGeometry(QtCore.QRect(25, 90, 950, 900))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 18pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        
        self.saveButton = QtWidgets.QPushButton(text_editor, clicked=lambda: self.save_it())
        self.saveButton.setGeometry(QtCore.QRect(885, 20, 90, 40))
        self.saveButton.setStyleSheet("background-color: #ECE2D0;\n"
                                      "font: 13pt \"Sylfaen\";\n"
                                      "border-radius: 10px;\n"
                                      "  min-height: 20px;\n"
                                      "  min-width: 20px;")
        self.saveButton.setObjectName("saveButton")
        
        self.fontComboBox = QtWidgets.QFontComboBox(text_editor)
        self.fontComboBox.currentFontChanged.connect(self.change_font)
        self.fontComboBox.setGeometry(QtCore.QRect(110, 50, 181, 30))
        self.fontComboBox.setStyleSheet("background-color: rgb(236, 226, 208);")
        self.fontComboBox.setObjectName("fontComboBox")
        
        self.sizeSpinBox = QtWidgets.QSpinBox(text_editor, valueChanged=lambda: self.change_size(self.sizeSpinBox.value()))
        self.sizeSpinBox.setGeometry(QtCore.QRect(110, 15, 111, 30))
        self.sizeSpinBox.setStyleSheet("background-color: rgb(236, 226, 208);")
        self.sizeSpinBox.setObjectName("sizeSpinBox")
        self.sizeSpinBox.setRange(1, 40)
        self.sizeSpinBox.setValue(18)
        
        self.sizeLabel = QtWidgets.QLabel(text_editor)
        self.sizeLabel.setGeometry(QtCore.QRect(25, 15, 71, 21))
        self.sizeLabel.setStyleSheet("background-color: rgb(211, 165, 136);\n"
                                     "border-radius: 10px;\n"
                                     "  min-height: 30px;\n"
                                     "  min-width: 30px;\n"
                                     "font: 11pt \"Sylfaen\";")
        self.sizeLabel.setObjectName("sizeLabel")
        
        self.fontLabel = QtWidgets.QLabel(text_editor)
        self.fontLabel.setGeometry(QtCore.QRect(25, 50, 71, 21))
        self.fontLabel.setStyleSheet("background-color: rgb(211, 165, 136);\n"
                                     "border-radius: 10px;\n"
                                     "  min-height: 30px;\n"
                                     "  min-width: 30px;\n"
                                     "font: 11pt \"Sylfaen\";")
        self.fontLabel.setObjectName("fontLabel")
        
        self.textEdit.textChanged.connect(self.update_font_and_size)
        
        self.retranslateUi(text_editor)
        QtCore.QMetaObject.connectSlotsByName(text_editor)

        # Set custom context menu for the textEdit widget
        self.textEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textEdit.customContextMenuRequested.connect(self.show_custom_context_menu)

    def show_custom_context_menu(self, position):
        cursor = self.textEdit.textCursor()
        if cursor.hasSelection():
            # Create custom context menu
            menu = self.textEdit.createStandardContextMenu()
            
            custom_action_1 = QAction('Thesaurus', self.textEdit)
            custom_action_1.triggered.connect(self.thesaurus)
            menu.addAction(custom_action_1)

            # custom_action_2 = QAction('Custom Action 2', self.textEdit)
            # custom_action_2.triggered.connect(self.custom_action_2)
            # menu.addAction(custom_action_2)

            # Show the context menu
            menu.exec_(self.textEdit.mapToGlobal(position))
        else:
        # Show the default context menu
            menu = self.textEdit.createStandardContextMenu()
            menu.exec_(self.textEdit.mapToGlobal(position))

    def thesaurus(self):
        self.thesaurus=QtWidgets.QMainWindow()
        self.ui = Ui_Thesaurus()
        self.ui.setupUi(self.thesaurus)
        self.ui.lineEdit.setText(self.textEdit.textCursor().selectedText())
        self.thesaurus.show()



    def save_it(self):
        # Open a folder selection dialog
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder = QFileDialog.getExistingDirectory(None, "Select Folder", "", options=options)
        
        if folder:
            # Ask for file name
            text, ok = QInputDialog.getText(None, 'File Name', 'Enter file name:')
            if ok and text:
                file_path = f"{folder}/{text}.txt"  # Use the entered file name
                str = self.textEdit.toPlainText()
                with open(file_path, 'w') as f:
                    f.write(str)
    def change_size(self,size):
        self.textEdit.setFontPointSize(size)
    def change_font(self, font):
        current_size = self.sizeSpinBox.value()  # Get the current font size
        self.textEdit.setCurrentFont(font)
        self.textEdit.setFontPointSize(current_size)
    def update_font_and_size(self):
        # Check if the content is empty
        if not self.textEdit.toPlainText():
            # Get current font and size
            current_font = self.fontComboBox.currentFont()
            current_size = self.sizeSpinBox.value()
            self.textEdit.setCurrentFont(current_font)
            self.textEdit.setFontPointSize(current_size)
    def retranslateUi(self, text_editor):
        _translate = QtCore.QCoreApplication.translate
        text_editor.setWindowTitle(_translate("text_editor", "Dialog"))
        self.saveButton.setText(_translate("text_editor", "Save"))
        self.sizeLabel.setText(_translate("text_editor", "<html><head/><body><p align=\"center\">Size</p></body></html>"))
        self.fontLabel.setText(_translate("text_editor", "<html><head/><body><p align=\"center\">Font</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    text_editor = QtWidgets.QDialog()
    ui = Ui_text_editor()
    ui.setupUi(text_editor)
    text_editor.show()
    sys.exit(app.exec_())