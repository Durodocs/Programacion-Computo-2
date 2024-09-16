from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
#Esta aplicación facilita la recolección de información básica del usuario de manera interactiva y visual,
# adecuada para formularios de entrada de datos en aplicaciones de escritorio.
class VentanaPreferencias(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Crear widgets
        self.etiqueta_genero = QLabel('Selecciona tu género:')
        self.radio_masculino = QRadioButton('Masculino')
        self.radio_femenino = QRadioButton('Femenino')

        self.etiqueta_pais = QLabel('Selecciona tu país:')
        self.combo_pais = QComboBox()
        self.combo_pais.addItems(['El Salvador', 'Guatenala', 'Honduras', 'Costa Rica', 'Apopa'])

        self.etiqueta_edad = QLabel('Selecciona tu edad:')
        self.spinbox_edad = QSpinBox()
        self.spinbox_edad.setRange(0, 120)

        self.boton_enviar = QPushButton('Enviar')
        self.boton_enviar.clicked.connect(self.mostrarResumen)

        # Configurar diseño
        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_genero)
        layout.addWidget(self.radio_masculino)
        layout.addWidget(self.radio_femenino)
        layout.addWidget(self.etiqueta_pais)
        layout.addWidget(self.combo_pais)
        layout.addWidget(self.etiqueta_edad)
        layout.addWidget(self.spinbox_edad)
        layout.addWidget(self.boton_enviar)

        self.setLayout(layout)

        # Configurar ventana
        self.setWindowTitle('Preferencias del Usuario')
        self.setGeometry(300, 300, 300, 200)

    def mostrarResumen(self):
        genero = 'Masculino' if self.radio_masculino.isChecked() else 'Femenino' if self.radio_femenino.isChecked() else 'No especificado'
        pais = self.combo_pais.currentText()
        edad = self.spinbox_edad.value()

        resumen = f'Género: {genero}\nPaís: {pais}\nEdad: {edad}'
        QMessageBox.information(self, 'Resumen', resumen)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPreferencias()
    ventana.show()
    app.exec_()

