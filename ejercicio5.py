import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class DatosPersonaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Datos de una Persona")

        self.etiquetas = ["Nombre", "Apellido", "Comida Favorita", "Serie Favorita", "Cantante Favorito", 
                          "REAL MADRID o Barcelona", "Animal Favorito", "Teléfono", "Correo Electrónico", "Spiderman o Batman"]

        self.entradas = []  

        
        layout_principal = QVBoxLayout()

       
        for etiqueta in self.etiquetas:
            layout_horizontal = QHBoxLayout()
            label = QLabel(etiqueta + ":")
            entrada = QLineEdit()

            layout_horizontal.addWidget(label)
            layout_horizontal.addWidget(entrada)

            
            self.entradas.append(entrada)

            
            layout_principal.addLayout(layout_horizontal)

        
        boton_mostrar = QPushButton("Mostrar Datos")
        boton_mostrar.clicked.connect(self.mostrar_datos)
        layout_principal.addWidget(boton_mostrar)

        
        self.setLayout(layout_principal)

    def mostrar_datos(self):
        datos = []
        for i, entrada in enumerate(self.entradas):
            valor = entrada.text()
            if valor:
                datos.append(f"{self.etiquetas[i]}: {valor}")
            else:
                QMessageBox.warning(self, "Advertencia", f"Por favor, ingrese su {self.etiquetas[i].lower()}.")
                return
        
        
        QMessageBox.information(self, "Datos Ingresados", "\n".join(datos))


if __name__ == "__main__":
    app = QApplication(sys.argv)


    ventana = DatosPersonaApp()
    ventana.show()

    sys.exit(app.exec_())