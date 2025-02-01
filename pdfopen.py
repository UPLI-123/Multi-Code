import sys
import os
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout


class PDFOpener(QWidget):
    def __init__(self, pdf_path):
        super().__init__()
        self.pdf_path = pdf_path
        self.setWindowTitle("Open PDF")

        button = QPushButton("打开 PDF")
        button.clicked.connect(self.open_pdf)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    def open_pdf(self):
        if sys.platform == "win32":
            os.startfile(self.pdf_path)
        elif sys.platform == "darwin":  # macOS
            os.system(f"open '{self.pdf_path}'")
        else:  # Linux
            os.system(f"xdg-open '{self.pdf_path}'")
            pass
        pass
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFOpener("help\系统说明文档.pdf")  # 替换为实际路径
    window.show()
    sys.exit(app.exec_())