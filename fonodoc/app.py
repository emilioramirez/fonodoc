"""app."""
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QGridLayout, QMessageBox)


class Form(QWidget):
    """asdsad."""

    def __init__(self, parent=None):
        """asdf."""
        super(Form, self).__init__(parent)

        # Componentes
        self.name_label = QLabel("Nombre:")
        self.name_line = QLineEdit()
        self.submit_button = QPushButton("Aceptar")

        # Layout vertical
        button_layout_1 = QVBoxLayout()
        button_layout_1.addWidget(self.name_label)
        button_layout_1.addWidget(self.name_line)
        button_layout_1.addWidget(self.submit_button)

        # Layout Principal
        main_layout = QGridLayout()
        main_layout.addLayout(button_layout_1, 0, 1)

        # Propiedades de ventana inicial
        self.setLayout(main_layout)
        self.setWindowTitle("Hola Qt5")

        # Eventos
        self.submit_button.clicked.connect(self.submit_line)

    def submit_line(self):
        """asdf."""
        name = self.name_line.text()

        if name == "":
            QMessageBox.information(
                self, "Campo vacio",
                "Por favor ingrese algo.")
            return
        else:
            QMessageBox.information(
                self, "Anduvo!",
                "Hola %s!" % name)
