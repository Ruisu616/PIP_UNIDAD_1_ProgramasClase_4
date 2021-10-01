import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P3_Saludo Nombre_V2.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)

    # Área de los Signals
    self.bt_enviar.clicked.connect(self.enviar)

  # Área de los Slots
  def enviar(self):
      print("¡Hiciste click!")
      nombre = self.bx_texto.text()
      ##print(nombre)
      #self.mensaje("¡Hola " + nombre + "! ¿Que tal?")
      self.bx_texto_2.setText("Hola " + nombre + " que tal?")

  def mensaje(self,msj):
      m = QtWidgets.QMessageBox()
      m.setText(msj)
      m.exec_()


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = MyApp()
  window.show()
  sys.exit(app.exec_())