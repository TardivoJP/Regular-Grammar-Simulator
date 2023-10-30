import os
import sys
from PyQt6.QtCore import Qt, QTimer, QEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QGuiApplication, QIcon
from manual_input_view import ManualInputView
from file_input_view import FileInputView

## PyInstaller file path handler
if getattr(sys, 'frozen', False):
    # Running as a PyInstaller executable
    base_path = sys._MEIPASS
else:
    # Running as a script
    base_path = os.path.abspath(".")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.manual_input_view = None
        self.file_input_view = None
        
        ## User screen's dimenions
        self.screen = QGuiApplication.primaryScreen()
        self.screen_size = self.screen.availableSize()

        self.setWindowTitle("Simulador de Gramatica Regular")
        self.setWindowIcon(QIcon(os.path.join(base_path, 'resources', 'logo-unespar.jpg')))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        # Application Header
        title_label = QLabel("<h1>Simulador de Gramatica Regular</h1>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Stacked layout
        self.stacked_layout = QStackedLayout()
        
        # First stacked view: Welcome screen
        self.welcome_layout = QVBoxLayout()
        self.welcome_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.choices_layout_label = QLabel("<h2>Bem vindo, escolha a forma de entrada</h2>")
        self.choices_layout_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_layout.addWidget(self.choices_layout_label)
        
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.button_manual_input = (QPushButton("Manual"))
        self.button_manual_input.clicked.connect(self.show_manual_input_view)
        self.button_file_input = (QPushButton("Arquivo"))
        self.button_file_input.clicked.connect(self.show_file_input_view)
        
        self.buttons_layout.addWidget(self.button_manual_input)
        self.buttons_layout.addWidget(self.button_file_input)
        
        self.welcome_layout.addLayout(self.buttons_layout)
        
        ## Finalizing welcome screen layout into a widget
        self.welcome_container = QWidget()
        self.welcome_container.setLayout(self.welcome_layout)
        self.welcome_container.setFixedWidth(int(self.screen_size.width() * 0.80))
        
        ## Adding all views to stacked layout
        self.stacked_layout.addWidget(self.welcome_container)
        self.stacked_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        ## Finalizing stacked layout into a widget
        self.stacked_layout_widget = QWidget()
        self.stacked_layout_widget.setLayout(self.stacked_layout)

        ## Finalizing widgets into main application layout
        self.main_application_layout = QHBoxLayout()
        
        self.left_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_application_layout.addItem(self.left_spacer)
        
        self.main_application_layout.addWidget(self.stacked_layout_widget)
        
        self.right_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_application_layout.addItem(self.right_spacer)
        self.main_application_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(self.main_application_layout)
        
        self.showMaximized()
    
    ## Functions (related to what the user sees and stacked layout management)
    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if self.windowState() & Qt.WindowState.WindowMaximized:
                self.isMaximized = True
            else:
                if self.isMaximized:
                    self.center_on_screen()
                self.isMaximized = False
            
    def center_on_screen(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        
        center_x = int((screen_geometry.width() - self.width()) / 2)
        center_y = int((screen_geometry.height() - self.height()) / 2.5)
        
        self.move(center_x, center_y)
    
    def show_main_menu(self):
        self.stacked_layout.setCurrentWidget(self.main_menu_container)
        
        self.destroy_manual_input_view()
        self.destroy_file_input_view()
        
    def show_manual_input_view(self):
        self.manual_input_view = ManualInputView(self.show_main_menu)
        self.manual_input_view.setFixedWidth(int(self.screen_size.width() * 0.80))
        
        self.stacked_layout.addWidget(self.manual_input_view)
        self.stacked_layout.setCurrentWidget(self.manual_input_view)
        
        if not self.isMaximized:
            QTimer.singleShot(0, self.center_on_screen)
            
    def show_file_input_view(self):
        self.file_input_view = FileInputView(self.show_main_menu)
        self.file_input_view.setFixedWidth(int(self.screen_size.width() * 0.80))
        
        self.stacked_layout.addWidget(self.file_input_view)
        self.stacked_layout.setCurrentWidget(self.file_input_view)
        
        if not self.isMaximized:
            QTimer.singleShot(0, self.center_on_screen)
            
    ## Clean up functions
    def destroy_manual_input_view(self):
        if self.manual_input_view:
            self.manual_input_view.deleteLater()
            self.stacked_layout.removeWidget(self.manual_input_view)
            self.manual_input_view.deleteLater()
            self.manual_input_view = None
            
    def destroy_file_input_view(self):
        if self.file_input_view:
            self.file_input_view.deleteLater()
            self.stacked_layout.removeWidget(self.file_input_view)
            self.file_input_view.deleteLater()
            self.file_input_view = None        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())