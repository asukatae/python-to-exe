
import sys, os

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QGridLayout,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QTextEdit,
    QLabel,
    QComboBox,
    QSizePolicy,
    QLineEdit,
)
from PyQt5.QtGui import QPixmap

#import clipboard as cb
from PyQt5.QtCore import *
isChecked = 1
class Window(QWidget):
    
    def __init__(self):
        
        
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Finance Calculator")

        
        self.resize(430, 110)
        # Create a top-level layout
       
        layout = QGridLayout()

        self.num2000 =0
        self.num1000 =0
        self.num500 = 0
        self.num100 = 0
        self.num50 = 0
        self.num10 = 0
        self.num5 = 0
        self.num1 = 0

        self.sum2000 = 0
        self.sum1000 = 0
        self.sum500 = 0
        self.sum100 = 0
        self.sum50 = 0
        self.sum10 = 0
        self.sum5 = 0
        self.sum1 = 0
        self.total = 0

        self.lbl2000 = QLabel('$2000')
        self.lbl1000 = QLabel('$1000')
        self.lbl500 = QLabel('$500')
        self.lbl100 = QLabel('$100')
        self.lbl50 = QLabel('$50')
        self.lbl10 = QLabel('$10')
        self.lbl5 = QLabel('$5')
        self.lbl1 = QLabel('$1')
        self.lblTotal = QLabel('Total')

        self.lbl2000.setAlignment(Qt.AlignCenter)
        self.lbl1000.setAlignment(Qt.AlignCenter)
        self.lbl500.setAlignment(Qt.AlignCenter)
        self.lbl100.setAlignment(Qt.AlignCenter)
        self.lbl50.setAlignment(Qt.AlignCenter)
        self.lbl10.setAlignment(Qt.AlignCenter)
        self.lbl5.setAlignment(Qt.AlignCenter)
        self.lbl1.setAlignment(Qt.AlignCenter)
        self.lblTotal.setAlignment(Qt.AlignCenter)

        self.txt2000 = QLineEdit()
        self.txt1000 = QLineEdit()
        self.txt500 = QLineEdit()
        self.txt100 = QLineEdit()
        self.txt50 = QLineEdit()
        self.txt10 = QLineEdit()
        self.txt5 = QLineEdit()
        self.txt1 = QLineEdit()

        self.btnSave = QPushButton("Save", self)
        self.btnSave.clicked.connect(self.on_btn_clicked)

        self.txt2000.textChanged.connect(self.on_text_changed2000)
        self.txt1000.textChanged.connect(self.on_text_changed1000)
        self.txt500.textChanged.connect(self.on_text_changed500)
        self.txt100.textChanged.connect(self.on_text_changed100)
        self.txt50.textChanged.connect(self.on_text_changed50)
        self.txt10.textChanged.connect(self.on_text_changed10)
        self.txt5.textChanged.connect(self.on_text_changed5)
        self.txt1.textChanged.connect(self.on_text_changed1)

        self.txt2000.setAlignment(Qt.AlignCenter)
        self.txt1000.setAlignment(Qt.AlignCenter)
        self.txt500.setAlignment(Qt.AlignCenter)
        self.txt100.setAlignment(Qt.AlignCenter)
        self.txt50.setAlignment(Qt.AlignCenter)
        self.txt10.setAlignment(Qt.AlignCenter)
        self.txt5.setAlignment(Qt.AlignCenter)
        self.txt1.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.lbl2000, 0, 0)
        layout.addWidget(self.lbl1000, 0, 1)
        layout.addWidget(self.lbl500, 0, 2)
        layout.addWidget(self.lbl100, 0, 3)
        layout.addWidget(self.lbl50, 0, 4)
        layout.addWidget(self.lbl10, 0, 5)
        layout.addWidget(self.lbl5, 0, 6)
        layout.addWidget(self.lbl1, 0, 7)
        layout.addWidget(self.lblTotal, 0, 8)

        layout.addWidget(self.txt2000, 1, 0)
        layout.addWidget(self.txt1000, 1, 1)
        layout.addWidget(self.txt500, 1, 2)
        layout.addWidget(self.txt100, 1, 3)
        layout.addWidget(self.txt50, 1, 4)
        layout.addWidget(self.txt10, 1, 5)
        layout.addWidget(self.txt5, 1, 6)
        layout.addWidget(self.txt1, 1, 7)
        layout.addWidget(self.btnSave, 1, 8)

        self.lblSum2000 = QLabel(str(self.sum2000))
        self.lblSum1000 = QLabel(str(self.sum1000))
        self.lblSum500 = QLabel(str(self.sum500))
        self.lblSum100 = QLabel(str(self.sum100))
        self.lblSum50 = QLabel(str(self.sum50))
        self.lblSum10 = QLabel(str(self.sum10))
        self.lblSum5 = QLabel(str(self.sum5))
        self.lblSum1 = QLabel(str(self.sum1))
        self.txtSumTotal = QLineEdit(str(self.total))
        self.txtSumTotal.setFixedWidth(350)

        self.lblSum2000.setAlignment(Qt.AlignCenter)
        self.lblSum1000.setAlignment(Qt.AlignCenter)
        self.lblSum500.setAlignment(Qt.AlignCenter)
        self.lblSum100.setAlignment(Qt.AlignCenter)
        self.lblSum50.setAlignment(Qt.AlignCenter)
        self.lblSum10.setAlignment(Qt.AlignCenter)
        self.lblSum5.setAlignment(Qt.AlignCenter)
        self.lblSum1.setAlignment(Qt.AlignCenter)
        self.txtSumTotal.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.lblSum2000, 2, 0)
        layout.addWidget(self.lblSum1000, 2, 1)
        layout.addWidget(self.lblSum500, 2, 2)
        layout.addWidget(self.lblSum100, 2, 3)
        layout.addWidget(self.lblSum50, 2, 4)
        layout.addWidget(self.lblSum10, 2, 5)
        layout.addWidget(self.lblSum5, 2, 6)
        layout.addWidget(self.lblSum1, 2, 7)
        layout.addWidget(self.txtSumTotal, 2, 8)

        self.setLayout(layout)
        self.file_path = os.path.join(os.getcwd(), 'saved_input.txt')
        self.open_file()

    def on_text_changed2000(self, text):
        try:
            val = int(text)
        except ValueError:
            text = ""

        if text == "":
            text = 0

        self.num2000 = int(text)
        self.sum2000 = 2000*self.num2000
        print(self.sum2000)
        self.lblSum2000.setText(str(self.sum2000))
        self.on_text_changedTotal()
        self.btnSave.setText("Save")

    def on_text_changed1000(self, text):
        try:
            val = int(text)
        except ValueError:
            text = ""
            
        if text == "":
            text = 0

        self.num1000 = int(text)
        self.sum1000 = 1000*self.num1000
        print(self.sum1000)
        self.lblSum1000.setText(str(self.sum1000))
        self.on_text_changedTotal()
        self.btnSave.setText("Save")

    def on_text_changed500(self, text):
        try:
            val = int(text)
        except ValueError:
            text = ""

        if text == "":
            text = 0

        self.num500 = int(text)
        self.sum500 = 500 * self.num500
        print(self.sum500)
        self.lblSum500.setText(str(self.sum500))
        self.on_text_changedTotal()
        self.btnSave.setText("Save")

    def on_text_changed100(self, text):
        try:
            val = int(text)
        except ValueError:
            text = ""

        if text == "":
            text = 0

        self.num100 = int(text)
        self.sum100 = 100 * self.num100
        print(self.sum100)
        self.lblSum100.setText(str(self.sum100))
        self.on_text_changedTotal()
        self.btnSave.setText("Save")
    
    def on_text_changed50(self, text):
        try:
            val = int(text)
        except ValueError:
            text = ""

        if text == "":
            text = 0

        self.num50 = int(text)
        self.sum50= 50 * self.num50
        print(self.sum50)
        self.lblSum50.setText(str(self.sum50))
        self.on_text_changedTotal()
        self.btnSave.setText("Save")

    def on_text_changed10(self, text):
        try:
            val = int(text)
        except ValueError:
            text = ""

        if text == "":
            text = 0

        self.num10 = int(text)
        self.sum10 = 10 * self.num10
        print(self.sum10)
        self.lblSum10.setText(str(self.sum10))
        self.on_text_changedTotal()
        self.btnSave.setText("Save")

    def on_text_changed5(self, text):
        try:
            val = int(text)
        except ValueError:
            text = ""

        if text == "":
            text = 0

        self.num5 = int(text)
        self.sum5 = 5 * self.num5
        print(self.sum5)
        self.lblSum5.setText(str(self.sum5))
        self.on_text_changedTotal()
        self.btnSave.setText("Save")

    def on_text_changed1(self, text):
        try:
            val = int(text)
        except ValueError:
            text = ""

        if text == "":
            text = 0

        self.num1 = int(text)
        self.sum1 = 1 * self.num1
        print(self.sum1)
        self.lblSum1.setText(str(self.sum1))
        self.on_text_changedTotal()
        self.btnSave.setText("Save")

    def on_text_changedTotal(self):

        self.total = self.sum2000 + self.sum1000 + self.sum500 + self.sum100 + self.sum50 + self.sum10 + self.sum5 + self.sum1
        print(self.total)
        self.txtSumTotal.setText(str(self.total))

    def on_btn_clicked(self):
        self.input_text = str(self.num2000) + '\n' +str(self.num1000) + '\n' + str(self.num500) + '\n' + str(self.num100)+ '\n' +str (self.num50)+ '\n' +str(self.num10)+'\n'+str(self.num5)+'\n'+str(self.num1)
        self.save_to_file()
        self.btnSave.setText("Saved!")

    def save_to_file(self):
        with open('saved_input.txt','w') as file:
            file.write(self.input_text)

    def open_file(self):
        """
        Reads the content of a hardcoded file path and displays it in the QPlainTextEdit.
        """
        if os.path.exists(self.file_path):
            try:
                # Use standard Python file reading (with 'utf-8' encoding is generally a good practice)
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    file_chunks = content.split('\n')

                    self.num2000 =int(file_chunks[0])
                    self.num1000 =int(file_chunks[1])
                    self.num500  =int(file_chunks[2])
                    self.num100  =int(file_chunks[3])
                    self.num50   =int(file_chunks[4])
                    self.num10   =int(file_chunks[5])
                    self.num5    =int(file_chunks[6])
                    self.num1    =int(file_chunks[7])

                    self.txt2000.setText(file_chunks[0])
                    self.txt1000.setText(file_chunks[1])
                    self.txt500.setText(file_chunks[2])
                    self.txt100.setText(file_chunks[3])
                    self.txt50.setText(file_chunks[4])
                    self.txt10.setText(file_chunks[5])
                    self.txt5.setText(file_chunks[6])
                    self.txt1.setText(file_chunks[7])

                    self.on_text_changedTotal()


                    print(f"Successfully loaded file: {self.file_path}")
            except IOError as e:
                self.btnSave.setText(f"Error reading file: {e}")
                print(f"Error reading file: {e}")
        else:
            #self.btnSave.setText(f"Error: File not found at '{self.file_path}'")
            print(f"Error: File not found at '{self.file_path}'")
            
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    
    sys.exit(app.exec_())
