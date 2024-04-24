#importacion de librerias a usar
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPoint
import sys
import calculo_mallas

#Clase principal de la calculadora de mallas
class Calculadora_mallas(QMainWindow):
    def __init__(self):
        super(Calculadora_mallas, self).__init__()
        #lectura de archivo interfaz
        loadUi('Introduccion a tkinter/gui.ui', self)
        self.click_posicion = QPoint()
        #ocultar resultado hasta que se calcule
        self.resultado.setVisible(False)
        #configuració del ComboBox
        self.valores_calcular = ['Intensidad R1', 'Intensidad R2', 'Intensidad R3',
                                    'Voltaje R1', 'Voltaje R2', 'Voltaje R3']
        self.valores.addItems(self.valores_calcular)
        self.btn_calcular.clicked.connect(self.calculate)
        
    #Función encargada de realizar los calculos
    def calculate(self):
        #asignación de variable a los valores extraidos de inputlabel
        resistencia1 = float(self.r1.text())
        resistencia2 = float(self.r2.text())
        resistencia3 = float(self.r3.text())
        voltaje1 = float(self.v1.text())
        voltaje2 = float(self.v1.text())* -1
        #creacion de objeto "malla" pasandole los valores requeridos para su funcionamiento
        malla = calculo_mallas.MallaTec(resistencia1, resistencia2, resistencia3, voltaje1, voltaje2)
        #extraccion de resultados principales
        self.ir1_value, self.ir2_value = malla.kramer()
        #calculo de las incognitas restantes
        self.ir3_value = (self.ir1_value -self.ir2_value)
        self.vr1 = self.ir1_value * resistencia1
        self.vr2 = self.ir2_value * (-resistencia3)
        self.vr3 = self.ir3_value * resistencia2
        resultado = self.valores.currentText()
        #validacion y muestra de resultados en pantalla
        if resultado == "Intensidad R1":
            self.resultado.setText("Resultado: " + str(round(self.ir1_value, 3)) + "A") 
            self.resultado.setVisible(True) 
        if resultado == "Intensidad R2":
            self.resultado.setText("Resultado: " + str(round(-self.ir2_value, 3)) + "A") 
            self.resultado.setVisible(True)
        if resultado == "Intensidad R3":
            self.resultado.setText("Resultado: " + str(round(self.ir3_value, 3)) + "A") 
            self.resultado.setVisible(True)
        if resultado == "Voltaje R1":
            self.resultado.setText("Resultado: " + str(round(self.vr1, 3)) + "V")
            self.resultado.setVisible(True)
        if resultado == "Voltaje R2":
            self.resultado.setText("Resultado: " + str(round(self.vr2, 3)) + "V")
            self.resultado.setVisible(True) 
        if resultado == "Voltaje R3":
            self.resultado.setText("Resultado: " + str(round(self.vr3, 3)) + "V")
            self.resultado.setVisible(True)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Calculadora_mallas()
    my_app.show()
    sys.exit(app.exec_())
