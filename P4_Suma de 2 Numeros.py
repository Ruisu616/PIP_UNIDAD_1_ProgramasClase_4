import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P4_Suma de 2 Numeros.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)

    # Área de los Signals
    self.bt_sumar.clicked.connect(self.sumar)

  # Área de los Slots
  def sumar(self):
    #try:
      print("¡Hiciste click!")
      A = self.num1.text()
      B = self.num2.text()
      if (A == ""):
          A==0
      else:
          A = int(A)
          #A = float(A)
      if (B == ""):
              B == 0
      else:
              B = int(B)
      result = str(A + B)
      self.resultado.setText(result)
    #except Exception as error:
        #print(sys.exc_info())

  def mensaje(self,msj1):
      m = QtWidgets.QMessageBox()
      m.setText(msj)
      m.exec_()


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = MyApp()
  window.show()
  sys.exit(app.exec_())