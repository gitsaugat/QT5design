from PyQt5 import QtWidgets

from test import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow,Ui_Calculator):

	def __init__(self):

		super().__init__()

		self.setupUi(self)

		self.show()

