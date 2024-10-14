from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Views.ui_Interfaz import Ui_MainWindow
from Views.CustomDialog import Error
import sys
import re
import math
class mainWindow (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pb_p1.clicked.connect(self.pag1)
        self.ui.pb_p2.clicked.connect(self.pag2)
        self.ui.pb_p3.clicked.connect(self.pag3)
        
        # VALIDACIONES
        self.ui.le_xip1.textChanged.connect(lambda: self.valnum('le_xip1'))
        self.ui.le_xsp1.textChanged.connect(lambda: self.valnum('le_xsp1'))
        self.ui.le_xp2.textChanged.connect(lambda: self.valnum('le_xp2'))
        self.ui.le_xip3.textChanged.connect(lambda: self.valnum('le_xip3'))
        self.ui.le_xsp3.textChanged.connect(lambda: self.valnum('le_xsp3'))
        self.ui.le_xp3.textChanged.connect(lambda: self.valnum('le_xp3'))
        
        self.ui.lb_Titulo.setText('f(x) = x¹⁰ - 1')

        self.ui.pb_calcp1.clicked.connect(lambda: self.punto1(self.ui.le_xip1.text(),self.ui.le_xsp1.text()))
        self.ui.pb_calcp2.clicked.connect(lambda: self.punto2(self.ui.le_xp2.text()))
        self.ui.pb_calcp3.clicked.connect(lambda: self.punto3(self.ui.le_xp3.text(),self.ui.le_xip3.text(),self.ui.le_xsp3.text()))
        
    def pag1 (self):
        self.ui.lb_Titulo.setText('f(x) = x¹⁰ - 1')
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def pag2 (self):
        self.ui.lb_Titulo.setText('f(x) = x³ - 155')
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def pag3 (self):
        self.ui.lb_Titulo.setText('f(x) = tan(x) – 0.5x')
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def punto1 (self,XI,XS):
        
        # SI HAY ERROR EN LA ENTRADA DE LOS X SALE MENSAJE
        if not XI or not XS:
            self.vacio()
        else:
            try:
                funcion = '(x**10)-1'
                xi = float(XI)
                xs = float(XS)
                Es = 0.5*10**(2-4)
                x = xi
                Fxi = eval(funcion)
                x = xs
                Fxs = eval(funcion)
                if self.TCS(Fxi,Fxs):
                    self.MBS(xi,xs,'tw_bisecp1',funcion,Es)
                    self.FP(xi,xs,'tw_fpP1', funcion,Es)
                else:
                    self.errorTCS()
            except ValueError:
                self.errorSyntaxis()
            
    def punto2 (self,xp):
        if not xp:
            self.vacio()
        else:
            try:
                x = float(xp)
                Es = 0.5*10**(2-5)
                self.NR(x, 'tw_p2', 'x**3 - 155', '3*(x**2)',Es)
            except ValueError:
                self.errorSyntaxis()
            except ZeroDivisionError:
                self.division0('Newton Raphson', 'valor')
                
    def punto3 (self, xp,XI,XS):
        
        if not xp or not XI or not XS: 
            self.vacio()
        else:
            try:
                funcion = 'math.tan(x)-(0.5*x)'
                x = float(xp)
                xi = float(XI)
                xs = float(XS)
                Es = 0.5*10**(2-4)
                
                x = xi
                Fxi = eval(funcion)
                x = xs
                Fxs = eval(funcion)
                if self.TCS(Fxi, Fxs):
                    self.MBS(xi, xs, 'tw_BisecP3', funcion,Es)
                    self.FP(xi, xs, 'tw_Fsp3',funcion,Es)
                else:
                    self.errorTCS()
                    
                self.MSE(xi,xs,'tw_secP3',funcion,Es)
                self.NR(x,'tw_NRP3',funcion,'((1/math.cos(x))**2)-0.5', Es)
                
            except ValueError:
                self.errorSyntaxis()     
            
    def MBS (self,xi,xs,tabla,funcion,Es):
        try:
            x = xi
            Fxi = eval(funcion)
            x = xs
            Fxs = eval(funcion)

            widget = getattr(self.ui,tabla) #Aqui se obtiene el widget que se va a usar para poder reutilizar la funcion
            if widget.rowCount() > 0:
                self.eliminarElementos(tabla) 
            
            xr = (xi+xs)/2
            
            Er = 100
            i = 1
            
            while Es < Er:

                if i == 1:
                    Er = 100
                    i = 0
                    FXi = Fxi
                    x = xr
                    FXr = eval(funcion)

                else:
                    xr_ant = xr
                    xr = (xi+xs)/2

                    if FXi*FXr < 0:
                        xi = xi
                        xs = xr
                        xr = (xi+xs)/2
                    else:
                        xi = xr
                        xs = xs
                        xr = (xi+xs)/2

                    x = xi
                    FXi = eval(funcion)
                    x = xr
                    FXr = eval(funcion)

                    Er = abs((xr-xr_ant)/xr)*100

                fila = widget.rowCount()
                widget.insertRow(fila)
                widget.setItem(fila,0,QTableWidgetItem(str(xi)))
                widget.setItem(fila,1,QTableWidgetItem(str(xs)))
                widget.setItem(fila,2,QTableWidgetItem(str(xr)))
                widget.setItem(fila,3,QTableWidgetItem(str(FXi)))
                widget.setItem(fila,4,QTableWidgetItem(str(FXr)))
                widget.setItem(fila,5,QTableWidgetItem(str(Er)))
        except ZeroDivisionError:
            self.division0('biseccion', 'intervalo')

    def FP (self, xi, xs, tabla, funcion,Es):
        try:
            x = xi
            FXi = eval(funcion)
            x = xs
            FXs = eval(funcion)
            
            widget = getattr(self.ui, tabla)
            if widget.rowCount() > 0:
                self.eliminarElementos(tabla) 
            
            Er = 100
            i=1
            while Er > Es:
                
                if i==1:
                    xr = xs - ((FXs*(xi-xs))/(FXi-FXs))
                    x = xr
                    FXr = eval(funcion)
                    i=0
                else:
                    xr_ant = xr
                    
                    if FXr * FXi < 0:
                        xs = xr
                    else:
                        xi = xr
                    x = xi
                    FXi = eval(funcion)
                    x = xs
                    FXs = eval(funcion)
                    x = xr
                    FXr = eval(funcion)
                    xr = xs - ((FXs*(xi-xs))/(FXi-FXs))
                    Er = abs((xr-xr_ant)/xr)*100
                    
                fila = widget.rowCount()
                widget.insertRow(fila)
                widget.setItem(fila,0,QTableWidgetItem(str(xi)))
                widget.setItem(fila,1,QTableWidgetItem(str(xs)))
                widget.setItem(fila,2,QTableWidgetItem(str(xr)))
                widget.setItem(fila,3,QTableWidgetItem(str(FXi)))
                widget.setItem(fila,4,QTableWidgetItem(str(FXs)))
                widget.setItem(fila,5,QTableWidgetItem(str(FXr)))
                widget.setItem(fila,6,QTableWidgetItem(str(Er)))
        except ZeroDivisionError:
            self.division0('falsa posición', 'intervalo')

    def NR (self,x,tabla, funcion, derivada,Es):
        try:
            Er = 100
            i = 1
            widget = getattr(self.ui, tabla)
            if widget.rowCount() > 0:
                self.eliminarElementos(tabla) 
            while Er > Es:
                
                if i == 1:
                    fx = eval(funcion)
                    dx = eval(derivada)
                    xn1 = x - (fx/dx)
                    i=0
                else:
                    xant = x
                    x = xn1
                    
                    fx = eval(funcion)
                    dx = eval(derivada)
                    xn1 = x - (fx/dx)
                    Er = abs((x-xant)/x)*100
                
                fila = widget.rowCount()
                widget.insertRow(fila)
                widget.setItem(fila,0,QTableWidgetItem(str(x)))
                widget.setItem(fila,1,QTableWidgetItem(str(xn1)))
                widget.setItem(fila,2,QTableWidgetItem(str(fx)))
                widget.setItem(fila,3,QTableWidgetItem(str(dx)))
                widget.setItem(fila,4,QTableWidgetItem(str(Er)))  
        except ZeroDivisionError:
            self.division0('Newton Raphson', 'valor')
            
    def MSE (self,xi1,xi,tabla,funcion,Es):
        try:
            Er = 100
            widget = getattr(self.ui, tabla)
            i = 1
            if widget.rowCount() > 0:
                self.eliminarElementos(tabla) 
            while Er > Es:
                if i == 1:
                    x = xi
                    Fxi = eval(funcion)
                    x = xi1
                    Fxi1 = eval(funcion)
                    xr = xi -((Fxi*(xi1-xi))/(Fxi1-Fxi))
                    i = 0
                else:
                    xr_ant = xr
                    
                    xi1 = xi
                    xi = xr
                    
                    x = xi
                    Fxi = eval(funcion)
                    x = xi1
                    Fxi1 = eval(funcion)
                    
                    xr = xi -((Fxi*(xi1-xi))/(Fxi1-Fxi))
                    
                    Er = abs((xr-xr_ant)/(xr))*100
                
                fila = widget.rowCount()
                widget.insertRow(fila)
                widget.setItem(fila,0,QTableWidgetItem(str(xi1)))
                widget.setItem(fila,1,QTableWidgetItem(str(xi)))
                widget.setItem(fila,2,QTableWidgetItem(str(xr)))
                widget.setItem(fila,3,QTableWidgetItem(str(Fxi1)))
                widget.setItem(fila,4,QTableWidgetItem(str(Fxi)))   
                widget.setItem(fila,5,QTableWidgetItem(str(Er)))           
        except ZeroDivisionError:
            self.division0('secante','intervalo')
            
    def TCS(self, xi, xs):
        if xi*xs < 0 : return True
        else: return False

    def eliminarElementos(self, tabla):
        widget = getattr(self.ui, tabla)
        while (widget.rowCount() > 0 ):
            widget.removeRow(0)
    # VALIDACIONES FUNCIONES
    def valnum (self, LE):
        # VALIDA QUE SOLO PUEDA UTILIZAR NUMEROS Y PUNTOS
        widget = getattr(self.ui, LE)
        text = widget.text()
        
        patron = r'[0-9\.]+$'
        textF = ''.join(c for c in text if re.match(patron,c))
        
        widget.blockSignals(True)
        widget.setText(textF)
        widget.blockSignals(False)
    # MENSAJES DE ERROR
    def errorTCS (self):
        dialog = Error()
        dialog.lb_error.setText('Intervalo no cumple con TCS!')
        dialog.pb_reintentar.clicked.connect(dialog.close)
        dialog.exec()
    def errorSyntaxis(self):
        dialog = Error()
        dialog.lb_error.setText('Error de sintaxis!')
        dialog.pb_reintentar.clicked.connect(dialog.close)
        dialog.exec()
    def division0(self,metodo,valor):
        dialog = Error()
        dialog.lb_error.setText(f'Division entre 0! En metodo de {metodo}\nCambie {valor}!')
        dialog.pb_reintentar.clicked.connect(dialog.close)
        dialog.exec()
    def vacio(self):
        dialog = Error()
        dialog.lb_error.setText(f'Llene todos los campos!')
        dialog.pb_reintentar.clicked.connect(dialog.close)
        dialog.exec()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())