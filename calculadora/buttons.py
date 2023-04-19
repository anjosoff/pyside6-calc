from PySide6.QtWidgets import QPushButton,QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display
from PySide6.QtCore import Slot

class Button (QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f'font-size:{MEDIUM_FONT_SIZE}px;')
        font=self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75,75)
        

class ButtonsGrid(QGridLayout):
    def __init__(self,display:Display, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask=[
            ['C','◀','/','*'],
            ['7','8','9','^'],
            ['4','5','6','+'],
            ['1','2','3','-'],
            ['','0','.','='],
        ]

        self.display=display
        self._makeGrid()
    def _makeGrid(self):
        
        for rowNumber,rowData in enumerate(self._gridMask):
            for columNumber, buttonText in enumerate(rowData):
                button=Button(buttonText)
                if  not isNumOrDot(buttonText) and not isEmpty(buttonText) :
                    button.setProperty('cssClass','specialButton')
                self.addWidget(button, rowNumber, columNumber)

                buttonSlot=self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button,

                    )
                button.clicked.connect(buttonSlot)


                

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
        

    def _insertButtonTextToDisplay(self, button):
        buttonText=button.text()
        
        newDisplayValue=self.display.text()+buttonText


        if not isValidNumber(newDisplayValue):
            return 

        self.display.insert(buttonText) 