from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Views.ui_Interfaz import Ui_MainWindow
from Views.CustomDialog import Error
import sys
import re

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
        
    def pag1 (self):
        self.ui.lb_Titulo.setText('f(x) = x¹⁰ - 1')
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def pag2 (self):
        self.ui.lb_Titulo.setText('f(x) = √x')
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def pag3 (self):
        self.ui.lb_Titulo.setText('f(x) = = tan(x) – 0.5x')
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def punto1 (self,XI,XS):
        try:
            # SI HAY ERROR EN LA ENTRADA DE LOS X SALE MENSAJE
            xi = float(XI)
            xs = float(XS)
            self.MBS(xi,xs,'tw_bisecp1')
            self.FP(xi,xs,'tw_fpP1')
        except:
            self.errorSyntaxis()
    
    def MBS (self,xi,xs,tabla):
        Fxi = (xi)**10.0-1.0
        Fxs = (xs)**10.0-1.0
        
        if self.TCS(Fxi,Fxs):
            widget = getattr(self.ui,tabla) #Aqui se obtiene el widget que se va a usar para poder reutilizar la funcion
            
            xr = (xi+xs)/2
            Es = 0.5 * 10**(2-4)
            Er = 100
            i = 1
            
            while Es < Er:

                if i == 1:
                    Er = 100
                    i = 0
                    FXi = Fxi
                    FXr = xr**10 - 1

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

                    FXi = xi**10 - 1
                    FXr = xr**10 - 1

                    Er = abs((xr-xr_ant)/xr)*100

                fila = self.ui.tw_bisecp1.rowCount()
                widget.insertRow(fila)
                widget.setItem(fila,0,QTableWidgetItem(str(xi)))
                widget.setItem(fila,1,QTableWidgetItem(str(xs)))
                widget.setItem(fila,2,QTableWidgetItem(str(xr)))
                widget.setItem(fila,3,QTableWidgetItem(str(FXi)))
                widget.setItem(fila,4,QTableWidgetItem(str(FXr)))
                widget.setItem(fila,5,QTableWidgetItem(str(Er)))

        else:
            self.errorTCS()

    def FP (self, xi, xs, tabla):
        FXi = xi**10 - 1
        FXs = xs**10 - 1
        if self.TCS(FXi,FXs):
            widget = getattr(self.ui, tabla)
            Es = 0.5*10**(2-4)
            Er = 100
            i=1
            while Er > Es:
                
                if i==1:
                    xr = xs - ((FXs*(xi-xs))/(FXi-FXs))
                    FXr = xr**10 - 1
                    i=0
                else:
                    xr_ant = xr
                    
                    if FXr * FXi < 0:
                        xs = xr
                    else:
                        xi = xr
                    
                    FXi = xi**10 - 1
                    FXs = xs**10 - 1
                    FXr = xr**10 - 1
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
        else:
            self.errorTCS()

    def TCS(self, xi, xs):
        if xi*xs < 0 : return True
        else: return False

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
        dialog.lb_error.setText('No cumple con TCS!')
        dialog.pb_reintentar.clicked.connect(dialog.close)
        dialog.exec()
    def errorSyntaxis(self):
        dialog = Error()
        dialog.lb_error.setText('Error de sintaxis!')
        dialog.pb_reintentar.clicked.connect(dialog.close)
        dialog.exec()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec()
