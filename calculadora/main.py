# Trabalhando com classes e herança no PySide6
import sys

from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from display import Display
from history import History
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,QLabel)
from styles import setupTheme
from buttons import Button, ButtonsGrid
if __name__ == '__main__':
# Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

# Define os icones
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    app.setApplicationName('Calculadora')

# History

    history=History('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(history)

# Display
    display=Display()
    display.setPlaceholderText('Digite aqui...')
    window.addWidgetToVLayout(display)

# Grid
    buttonsGrid= ButtonsGrid(display)
    window.v_layout.addLayout(buttonsGrid)

    
    

# Executa tudo
    window.FixedSize()
    window.show()
    app.exec()  # O loop da apl