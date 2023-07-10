from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton
import sys
import subprocess
import os



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 300)    #(xpos, ypos, width, height)
        self.setWindowTitle("Choose PPE to be detected & Press Q to quit")
        self.initUI()

    def initUI(self):
        self.checkbox_list = []

        helmet_checkbox = QCheckBox("Helmet", self)
        helmet_checkbox.move(20, 20)
        self.checkbox_list.append(helmet_checkbox)

        mask_checkbox = QCheckBox("Mask", self)
        mask_checkbox.move(20, 50)
        self.checkbox_list.append(mask_checkbox)

        jacket_checkbox = QCheckBox("Jacket", self)
        jacket_checkbox.move(20, 80)
        self.checkbox_list.append(jacket_checkbox)

        shoe_checkbox = QCheckBox("Shoe", self)
        shoe_checkbox.move(20, 110)
        self.checkbox_list.append(shoe_checkbox)

        harness_checkbox = QCheckBox("Harness", self)
        harness_checkbox.move(20, 140)
        self.checkbox_list.append(harness_checkbox)

        enter_button = QPushButton("Enter", self)
        enter_button.move(20, 170)
        enter_button.clicked.connect(self.enter_button_clicked)

        self.show()

    def get_selected_objects(self):
        selected_objects = []
        for index, checkbox in enumerate(self.checkbox_list):
            if checkbox.isChecked():
                selected_objects.append(index)
        return selected_objects

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
