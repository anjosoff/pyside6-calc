from PySide6.QtGui import QIcon
from PySide6.QtWidgets import  QMainWindow, QWidget,QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None,  *args, **kwargs)-> None:
        super().__init__(parent, *args, **kwargs)
        
    # CONFIGURAÇÕES PADRÃO
        self.cw=QWidget()
        self.v_layout=QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        self.setWindowTitle('Calculadora')
   

    def FixedSize(self):
        self.adjustSize()
    # Ultima coisa a ser feito
        self.setFixedSize(self.width(), self.height())
    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        
    ############################################


