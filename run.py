"""run."""
from PyQt5.QtWidgets import QApplication
from fonodoc.app import Form


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    print(loco())

    sys.exit(app.exec())
