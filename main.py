from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QHBoxLayout, QLineEdit
from PyQt6.QtCore import Qt
import json

def read_file():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data
def search_word():
        dict_data = read_file()
        definition_output = ''
        # print(dict_data)
        for key, value in dict_data.items():
            if key == word_input.text():
                for definition in value:
                    definition_output += definition + "\n"
                output_label.setText(str(definition_output))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Word Definition')

layout = QVBoxLayout()

input_layout = QHBoxLayout()
layout.addLayout(input_layout)

word_input = QLineEdit()
word_input.setFixedWidth(500)
input_layout.addWidget(word_input)

convert_btn = QPushButton('Convert')
convert_btn.setFixedWidth(100)
input_layout.addWidget(convert_btn)
convert_btn.clicked.connect(search_word)

output_label = QLabel('...')
output_label.setFixedWidth(600)
output_label.setWordWrap(True)
layout.addWidget(output_label)


window.setLayout(layout)
window.show()
app.exec()