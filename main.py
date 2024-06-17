import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import qdarkstyle

# Application Constant
APP_NAME = 'QRnify'

def get_resource_path(relative_path):
    """
    Get the absolute path to the resource based on whether the script is running as an executable or as a script.
    """
    if getattr(sys, 'frozen', False):
        # Running as an executable, use sys._MEIPASS to access bundled files
        base_path = sys._MEIPASS
    else:
        # Running as a script, use the script's directory
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    resource_path = os.path.join(base_path, relative_path)
    return resource_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(get_resource_path("assets/MainWindow.ui"), self)
        self.setWindowTitle(APP_NAME)
        self.setFixedSize(820, 803)
        dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
        # self.setStyleSheet(dark_stylesheet)   

# Application entry point
def main():
    # Initialize the application
    app = QApplication(sys.argv)
    
    # Create and show the main window
    mainWindow = MainWindow()
    mainWindow.show()
    
    # Start the application event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
