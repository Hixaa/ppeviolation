from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton, QLabel, QVBoxLayout, QWidget
import sys
import subprocess
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 400)    # (xpos, ypos, width, height)
        self.setWindowTitle("PPE Detector")
        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Adding the image
        image_label = QLabel(self)
        pixmap = QtGui.QPixmap("hixaa.jpg")  # Replace with your image file's name
        pixmap = pixmap.scaledToHeight(100)  # Set the height of the image as required
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label, alignment=QtCore.Qt.AlignLeft)

        # Adding the text
        text_label = QLabel("Choose PPE to be detected", self)
        layout.addWidget(text_label, alignment=QtCore.Qt.AlignLeft)

        # Adding the checkboxes
        self.checkbox_list = []
        ppe_list = ["Helmet", "Mask", "Jacket", "Shoe", "Harness"]
        for ppe in ppe_list:
            checkbox = QCheckBox(ppe, self)
            layout.addWidget(checkbox, alignment=QtCore.Qt.AlignLeft)
            self.checkbox_list.append(checkbox)

        # Adding the "Enter" button
        enter_button = QPushButton("Enter", self)
        enter_button.clicked.connect(self.enter_button_clicked)
        layout.addWidget(enter_button, alignment=QtCore.Qt.AlignLeft)

        # Add some spacing at the bottom
        layout.addStretch()

        self.show()

    def get_selected_objects(self):
        selected_objects = []
        for checkbox in self.checkbox_list:
            if checkbox.isChecked():
                object_name = checkbox.text()
                if object_name == "Helmet":
                    selected_objects.extend([0, 5])
                elif object_name == "Mask":
                    selected_objects.extend([1, 6])
                elif object_name == "Jacket":
                    selected_objects.extend([2, 7])
                elif object_name == "Shoe":
                    selected_objects.extend([3, 8])
                elif object_name == "Harness":
                    selected_objects.extend([4, 9])
        return sorted(selected_objects)

    def enter_button_clicked(self):
        selected_objects = self.get_selected_objects()
        class_ids_str = ",".join(map(str, selected_objects))
        os.environ["CLASS_IDS"] = class_ids_str
        subprocess.run(["python", r"realtime.py"])

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
