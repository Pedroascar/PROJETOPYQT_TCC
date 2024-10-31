from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys

# Importar a janela principal e as abas
from main_window import Ui_MainWindow
from project_tab import Ui_ProjectTab
from train_tab import Ui_TrainTab
from test_tab import Ui_TestTab
from prediction_tab import Ui_PredictionTab
from help_tab import Ui_HelpTab
from views.ui.main_window import Ui_MainWindow


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        
        # Configurar a janela principal
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Carregar cada aba como um widget separado
        self.project_tab = QWidget()
        self.train_tab = QWidget()
        self.test_tab = QWidget()
        self.prediction_tab = QWidget()
        self.help_tab = QWidget()

        # Configurar cada aba com seu conteúdo específico
        self.project_ui = Ui_ProjectTab()
        self.project_ui.setupUi(self.project_tab)
        
        self.train_ui = Ui_TrainTab()
        self.train_ui.setupUi(self.train_tab)
        
        self.test_ui = Ui_TestTab()
        self.test_ui.setupUi(self.test_tab)
        
        self.prediction_ui = Ui_PredictionTab()
        self.prediction_ui.setupUi(self.prediction_tab)
        
        self.help_ui = Ui_HelpTab()
        self.help_ui.setupUi(self.help_tab)

        # Adicionar as abas ao QTabWidget da janela principal
        self.ui.tabWidget.addTab(self.project_tab, "Project")
        self.ui.tabWidget.addTab(self.train_tab, "Train")
        self.ui.tabWidget.addTab(self.test_tab, "Test")
        self.ui.tabWidget.addTab(self.prediction_tab, "Prediction")
        self.ui.tabWidget.addTab(self.help_tab, "Help")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
