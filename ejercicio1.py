import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PersonalInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle('Información Personal')
        self.setGeometry(100, 100, 400, 200)

        # Fondo de la ventana
        self.setStyleSheet("background-color: #f0f0f0;")  # color de fondo

        # Layout principal
        layout = QVBoxLayout()
        layout.setSpacing(20)  # espaciado entre widgets

        # nombre completo centrado
        self.name_label = QLabel('Nombre Completo:Jorge Alexis Salgado Amaya')
        self.name_label.setAlignment(Qt.AlignCenter)  # centrar el texto
        self.name_label.setFont(QFont('Arial', 16, QFont.Bold))  # fuente más grande y negrita
        self.name_label.setStyleSheet("color: #2e8b57;")  # color de texto verde
        layout.addWidget(self.name_label)

        # edad centrada
        self.age_label = QLabel('Edad: 20 años')
        self.age_label.setAlignment(Qt.AlignLeft)  # Alinear el texto a la izquierda
        self.age_label.setFont(QFont('Verdana', 14, QFont.Italic))  # Fuente Verdana, tamaño 14, cursiva
        self.age_label.setStyleSheet("color: #ff6347;")  # Color de texto rojo tomate

        layout.addWidget(self.age_label)

        # Configurar layout
        self.setLayout(layout)

# inicializamos la aplicación 
app = QApplication(sys.argv)
window = PersonalInfoWindow()
window.show()
sys.exit(app.exec_())