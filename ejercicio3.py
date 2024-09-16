import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

class PersonalInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle('Formulario de Información Personal')
        self.setGeometry(100, 100, 400, 250)

        # Configuración del fondo de la ventana
        self.setStyleSheet("background-color: #f5f5f5;")  # Color de fondo gris claro

        # Layout principal
        layout = QVBoxLayout()
        layout.setSpacing(15)  # espaciado entre widgets

        # etiqueta y campo de entrada para el número de DUI
        self.cedula_label = QLabel('Número de DUI:')
        self.cedula_label.setFont(QFont('Arial', 12, QFont.Bold))  # fuente más grande y negrita
        self.cedula_label.setStyleSheet("color: #333333;")  # Color de texto gris oscuro
        layout.addWidget(self.cedula_label)

        self.cedula_input = QLineEdit()
        self.cedula_input.setPlaceholderText('Ingrese su número de DUI')  # texto de marcador de posición
        self.cedula_input.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")  # estilo de borde y relleno
        layout.addWidget(self.cedula_input)

        # etiqueta y campo de entrada para colocar el nombre completo
        self.nombre_label = QLabel('Nombre Completo:')
        self.nombre_label.setFont(QFont('Arial', 12, QFont.Bold))  # fuente más grande y negrita
        self.nombre_label.setStyleSheet("color: #333333;")  # Color de texto gris oscuro
        layout.addWidget(self.nombre_label)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText('Ingrese su nombre completo')  # texto de marcador de posición
        self.nombre_input.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")  # estilo de borde y relleno
        layout.addWidget(self.nombre_input)

        # este es el botón para enviar la información
        self.submit_button = QPushButton('Enviar')
        self.submit_button.setFont(QFont('Arial', 12, QFont.Bold))  # Fuente del botón
        self.submit_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 10px;")  # Estilo del botón
        self.submit_button.clicked.connect(self.submit_info)
        layout.addWidget(self.submit_button)

        # Configurar layout
        self.setLayout(layout)

    def submit_info(self):
        # Obtenemos los datos ingresados
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()

        # Validamos que se hayan ingresado todos los datos
        if not cedula or not nombre:
            QMessageBox.warning(self, 'Error', 'Por favor, ingrese tanto el número de cédula como el nombre completo.')
        else:
            QMessageBox.information(self, 'Información Enviada', f'Número de Cédula: {cedula}\nNombre Completo: {nombre}')

# inicializamos la aplicacion 
app = QApplication(sys.argv)
window = PersonalInfoWindow()
window.show()
sys.exit(app.exec_())