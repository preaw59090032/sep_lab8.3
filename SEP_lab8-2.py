import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QWidget):
    newPoint = pyqtSignal(QPoint)
    def __init__(self):
        QWidget.__init__(self)
        self.resize(640,480)
        self.path = QPainterPath()    
        
        self.button = QPushButton('Clear', self)
        self.button.clicked.connect(self.Clear)

        self.text = QLabel()
        self.text.setText("Drag the mouse to draw")
        self.text.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(self.button)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPath(self.path)

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        self.newPoint.emit(event.pos())
        self.update()
        
    def sizeHint(self):
        return QSize(600, 400)

    def Clear(self):
        self.eraseRect(650,500)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
