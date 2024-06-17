import os
import sys
import qrcode
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, \
                                QPushButton, QSlider, QLineEdit, QColorDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt, pyqtSlot
from PIL import ImageQt
from PyQt6.uic import loadUi
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
        self.setStyleSheet(dark_stylesheet) 
        self.getSetting()
        self.handleButtonPressed()

    def handleButtonPressed(self):
        self.pushButton_generate.clicked.connect(self.generate_QR_code)
        # self.pushButton_fill_colour.clicked.connect()
        # self.pushButton_bg.clicked.connect()
        # self.pushButton_save.clicked.connect()
        pass

    def getSetting(self):
        self.content = self.textEdit_content
        self.version = self.horizontalSlider_version 
        self.qr_size = self.horizontalSlider_box_size
        self.border_size = self.horizontalSlider_border_size
        self.fill_colour = self.lineEdit_fill_colour
        self.bg_colour = self.lineEdit_bg_colour
        self.qr_code = self.label_qr_code

    def clearQRbox(self):
        self.label_qr_code.clear()

    def generate_QR_code(self):  
        # Get data from the input content field
        data = self.content.toPlainText()

        if not data:
            # Clear the QR code display if there's no data
            self.qr_code.clear()
            return


        box_size = self.qr_size.value()
        border = self.border_size.value()
        fill_color = "#000000"
        back_color = "#ffffff"

        # Generate the QR code with the specified parameters
        qr = qrcode.QRCode(
            version=None,  # None or 1 - 40
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )

        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Convert the PIL image object to a QPixmap object
        qr_img_pixmap = QPixmap.fromImage(ImageQt.ImageQt(qr_img))

        # Set the QPixmap as the QR code display
        self.qr_code.setPixmap(qr_img_pixmap)

        

    def initialize_signal_slot(self):

        object_list = [

        ]


    
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
