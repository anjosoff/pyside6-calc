from PySide6.QtWidgets import QPushButton,QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber

from PySide6.QtCore import Slot


from typing import TYPE_CHECKING

if TYPE_CHECKING: # Corrige o erro de 'circular import'
    from display import Display
    from history import History


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
    def __init__(self,display:'Display',history:'History', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask=[
            ['C','◀','/','*'],
            ['7','8','9','^'],
            ['4','5','6','+'],
            ['1','2','3','-'],
            ['','0','.','='],
        ]
    
        self.display=display
        self.history=history

        #Getter and Setter
        self._equation=''


        self.equation='QUALQUER'

        self._makeGrid()
    
    @property
    def equation(self):
        return self._equation
    @equation.setter
    def equation(self, value):
        self._equation=value
        self.history.setText(value)

    def _makeGrid(self):
        
        for rowNumber,rowData in enumerate(self._gridMask):
            for columNumber, buttonText in enumerate(rowData):
                button=Button(buttonText)
                if  not isNumOrDot(buttonText) and not isEmpty(buttonText) :
                    button.setProperty('cssClass','specialButton')
                    self._configSpecialButton(button)
                self.addWidget(button, rowNumber, columNumber)

                slot=self._makeSlot(self._insertButtonTextToDisplay,button)
                self._connectButtonClicked(button,slot)


    def _connectButtonClicked(self, button, slot):

         button.clicked.connect(slot)

    def _configSpecialButton(self,button):
        text=button.text()
        if text == 'C':
            slot=self._makeSlot(self._clear, 'Limpo!')
            self._connectButtonClicked(button,slot)
            #button.clicked.connect(self.display.clear)
    
    def _makeSlot(self, func, *args, **kwargs):
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

    def _clear(self,msg):
        self.display.clear()
        self.display.setPlaceholderText(msg)