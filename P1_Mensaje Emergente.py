import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P1_Mensaje Emergente.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)

    # Área de los Signals
    self.bt_saludo.clicked.connect(self.saludo)

  # Área de los Slots
  def saludo(self):
      print("¡Hiciste click!")
      self.mensaje("¡Hola que tal!")
  def mensaje(self,msj):
      m = QtWidgets.QMessageBox()
      m.setText(msj)
      m.exec_()


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = MyApp()
  window.show()
  sys.exit(app.exec_())