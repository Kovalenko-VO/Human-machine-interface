import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QDoubleSpinBox
from PyQt5.QtCore import Qt
import math

class FunctionCalculator(QWidget):
    def __init__(self):
        super(FunctionCalculator, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('lab1')

        self.function_label = QLabel('Choose a function:')
        self.function_radio1 = QRadioButton('y = tg(3x) - tg(x) - 4sin(x)')
        self.function_radio2 = QRadioButton('y = (23)^(1+x^2) - (10)^(1-x^3)')

        self.point_label = QLabel('Enter a point:')
        self.point_spinbox = QDoubleSpinBox()
        self.point_spinbox.setDecimals(2)

        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_function)

        self.result_label = QLabel('Result:')

        # Layout setup
        layout = QVBoxLayout()

        function_layout = QVBoxLayout()
        function_layout.addWidget(self.function_label)
        function_layout.addWidget(self.function_radio1)
        function_layout.addWidget(self.function_radio2)

        point_layout = QHBoxLayout()
        point_layout.addWidget(self.point_label)
        point_layout.addWidget(self.point_spinbox)

        layout.addLayout(function_layout)
        layout.addLayout(point_layout)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_function(self):
        point = self.point_spinbox.value()

        if self.function_radio1.isChecked():
            result = f'y = tg(3 * {point}) - tg({point}) - 4 * sin({point}) = {math.tan(3 * point) - math.tan(point) - 4 * math.sin(point)}'
        elif self.function_radio2.isChecked():
            result = f'y = (23)^(1+{point}^2) - (10)^(1-{point}^3) = {math.pow(23, 1 + point**2) - math.pow(10, 1 - point**3)}'
        else:
            result = 'Please select a function'

        self.result_label.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = FunctionCalculator()
    calculator.show()
    sys.exit(app.exec_())
