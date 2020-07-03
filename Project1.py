from Project1_gui import  Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication
from gingerit.gingerit import GingerIt
from pymysql import *

class Grammarectify(QMainWindow,Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.init_pushbotton()
	def init_pushbotton(self):
		self.correct_pushButton.clicked.connect(self.correct_string)
		self.reset_pushButton.clicked.connect(self.reset_string)
		
	def correct_string(self):
		text=self.input_textEdit.toPlainText()
		
		
		
		#self.input_textEdit.clear()
		text = text+" "#added because wasnt parsing till the end

		text_compare=text
		
		
		parser = GingerIt()
		a=parser.parse(text)#stored in a dictionary
		#print(a)
		if a["result"][0]==" ":
			self.output_textEdit.setText(a["result"][1:])
		else:
			self.output_textEdit.setText(a["result"])
		'''if a["result"][0]==" ":
			self.output_textEdit.setText(a["result"][1:])
		else:
		self.output_textEdit.setText(a["result"])'''


			

		
	def reset_string(self):
		self.output_textEdit.clear()
		self.input_textEdit.clear()

if __name__=="__main__":
	application=QApplication([]) #first create QApplication object
	gr=Grammarectify()
	gr.show()
	application.exec_()