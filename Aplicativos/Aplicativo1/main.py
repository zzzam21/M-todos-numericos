from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Vistas.ui_Interfaz import Ui_Aplicativo1
from Vistas.CustomDialog import Error
import sys
import math
from py_expression_eval import Parser
import re

class MainWindow(QMainWindow):
    def __init__ (self):
        
        super().__init__()
        self.ui = Ui_Aplicativo1()
        self.ui.setupUi(self)
        self.ui.tw_datos.setColumnWidth(0,10)
        self.ui.tw_datos.setColumnWidth(1,126)
        self.ui.tw_datos.setColumnWidth(2,126)
        self.ui.tw_datos.setColumnWidth(3,126)
        
        self.ui.pb_calcular.clicked.connect(self.calcular)
        self.ui.pb_limpiar.clicked.connect(self.limpiar)
        self.ui.le_ncs.textChanged.connect(self.soloNumeros)
        self.ui.le_x.textChanged.connect(self.operadores)
        self.ui.pb_pi.clicked.connect(self.agregarPi)
        self.ui.pb_limpiar.clicked.connect(self.limpiar)
        
    # METODO PARA CALCULAR LA SERIE
    def calcular (self):
        if not self.ui.le_ncs.text() or not self.ui.le_x.text():
            mensaje = Error()
            mensaje.pb_reintentar.clicked.connect(lambda: mensaje.close())
            mensaje.exec()
        else:
            texto = self.ui.le_x.text()
            expresion = Parser()
            # EVALUAR QUE LA EXPRESIÓN MATEMATICA ESTE CORRECTA
            try:
                x = expresion.evaluate(texto, {'π': math.pi})
                
                # LIMPIAR TABLA
                self.limpiarTabla()
                es = self.Es()
                if self.ui.cb_selfun.currentIndex() == 0:
                    self.sen(es,x)
                else:
                    self.cos(es,x)
            except:
                # MENSAJE DE ERROR
                mensaje = Error()
                mensaje.lb_error.setText('Error de sintaxis!')
                mensaje.pb_reintentar.clicked.connect(lambda:mensaje.close())
                mensaje.exec()
      
    # METODO PARA LIMPIAR LAS ENTRADAS
    def limpiar (self):
        self.ui.le_ncs.setText('')
        self.ui.le_x.setText('')
        self.ui.lb_criterioError.setText('Criterio de error(Es): ')
        self.limpiarTabla()
        
    # METODO PARA LIMPIAR TABLA
    def limpiarTabla (self):
        while (self.ui.tw_datos.rowCount() > 0 ):
            self.ui.tw_datos.removeRow(0)
    
    # METODO PARA VALIDAR QUE SEA SOLO NUMERO EN LAS ENTRADAS
    def soloNumeros (self):
        texto = self.ui.le_ncs.text()
        # Formatear el texto
        texto = ''.join(c for c in texto if c.isdigit())
        
        # Actualizar texto del line edit
        self.ui.le_ncs.blockSignals(True) #Bloquea la entrada, para no crear bucle
        self.ui.le_ncs.setText(texto)
        self.ui.le_ncs.blockSignals(False)
    
    # METODO PARA QUE SOLO INGRESE OPERADORES MATEMATICOS
    def operadores (self):
        texto = self.ui.le_x.text()
        
        patron = r'[0-9\(\)\*/\-\+\π\.\^]+$'
        
        texto = ''.join(c for c in texto if re.match(patron, c))
        
       # Actualizar texto del line edit
        self.ui.le_x.blockSignals(True) #Bloquea la entrada, para no crear bucle
        self.ui.le_x.setText(texto)
        self.ui.le_x.blockSignals(False)
    
    # METODO PARA AGREGAR EL VALOR DE π
    def agregarPi (self):
        texto = self.ui.le_x.text()
        texto += 'π'
        self.ui.le_x.setText(texto)
    
    # CALCULAR ES
    def Es (self):
        self.ui.lb_criterioError.setText('Criterio de error (Es): ')
        ncs = float(self.ui.le_ncs.text())
        es = (0.5*10**(2-ncs))
        
        texto = self.ui.lb_criterioError.text()
        texto = texto + str(es)
        self.ui.lb_criterioError.setText(texto)
        return es
    
    # CALCULAR SEN(X)
    def sen (self,es,x):
            
        n = 1
        i = 1
        resultado = 0
        sumatoria = 0
        e = 100
        vant = 0
        
        while e > es:
                        
            resultado = (x**n)/math.factorial(n)
            
            vant = sumatoria
            if i == 1:
                sumatoria = resultado
            else:
                if i%2 == 0:
                    sumatoria = sumatoria - resultado
                else:
                    sumatoria = sumatoria + resultado
            
            e = abs(((sumatoria-vant)/sumatoria)*100)
            
            n += 2
            i += 1
            
            fila = self.ui.tw_datos.rowCount()
            self.ui.tw_datos.insertRow(fila)
            self.ui.tw_datos.setItem(fila,0,QTableWidgetItem(str(n)))
            self.ui.tw_datos.setItem(fila,1,QTableWidgetItem(str(resultado)))
            self.ui.tw_datos.setItem(fila,2,QTableWidgetItem(str(sumatoria)))
            self.ui.tw_datos.setItem(fila,3,QTableWidgetItem(str(e)))
    
    # CALCULAR COS(X)
    def cos (self,es,x):
        n = 0
        i = 1
        resultado = 0
        sumatoria = 0
        e = 100
        vant = 0
        
        while e > es:
                        
            resultado = (x**n)/math.factorial(n)
            
            vant = sumatoria
            if i == 1:
                sumatoria = resultado
            else:
                if i%2 == 0:
                    sumatoria = sumatoria - resultado
                else:
                    sumatoria = sumatoria + resultado
            
            e = abs(((sumatoria-vant)/sumatoria)*100)
            
            n += 2
            i += 1
            
            fila = self.ui.tw_datos.rowCount()
            self.ui.tw_datos.insertRow(fila)
            self.ui.tw_datos.setItem(fila,0,QTableWidgetItem(str(n)))
            self.ui.tw_datos.setItem(fila,1,QTableWidgetItem(str(resultado)))
            self.ui.tw_datos.setItem(fila,2,QTableWidgetItem(str(sumatoria)))
            self.ui.tw_datos.setItem(fila,3,QTableWidgetItem(str(e)))
        
if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = MainWindow()
     window.show()
     sys.exit(app.exec())
     