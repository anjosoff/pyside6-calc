from PySide6.QtWidgets import QLabel,QWidget
from variables import HISTORY_FONT_SIZE
from PySide6.QtCore import Qt


class History(QLabel):
    def __init__(self,text:str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {HISTORY_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        
        
        