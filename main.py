from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from file_helper import *

app = QApplication([])


notes = read_from_file()
window = QWidget()
window.setWindowTitle('Розумні замітки')
window.resize(900, 600)

list_notes = QListWidget()
list_notes.addItems(notes)

list_notes_label = QLabel('Список заміток')

button_note_create = QPushButton('Створити замітку ')
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введіть тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавити до змітки')
button_tag_del = QPushButton('Відкріпити від змітки')
button_tag_search = QPushButton('Шукати замітку по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегів')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
window.setLayout(layout_notes)

def show_note():
    key = list_notes.currentItem().text()
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tegi"])
    print(notes[key])

def create_note_func():
    note_name, ok = QInputDialog.getText(window, "Stvoreny Zamitki", "Nazva Zamitki")


    if ok == True:
        notes[note_name] = {
            "text": "",
            "tegi":  [

            ]
        }
        list_notes.clear()
        list_notes.addItems(notes)
        write_in_file(notes)

def delate_note_func():
    key = list_notes.currentItem().text()
    notes.pop(key)
    list_notes.clear()
    list_notes.addItems(notes)
    write_in_file(notes)


def seve_note_func():
    key = list_notes.currentItem().text()
    notes[key]["text"] = field_text.setText()
    write_in_file(notes)

def add_tag():
    key = list_notes.currentItem().text()
    tag = field_tag.text()
    notes[key]['tegi'].append(tag)
    list_tags.clear()
    list_tags.addItems(notes[key]['tegi'])
    write_in_file(notes)

def del_tag():
    key_note = list_notes.currentItem().text()
    tag = list_tags.currentItem().text()
    notes[key_note]['tegi'].remove(tag)
    list_tags.clear()
    list_tags.addItems(notes[key_note]['tegi'])
    write_in_file(notes)

button_tag_del.clicked.connect(del_tag)
button_tag_add.clicked.connect(add_tag)
button_note_save.clicked.connect(seve_note_func)
button_note_del.clicked.connect(delate_note_func)
button_note_create.clicked.connect(create_note_func)
list_notes.itemClicked.connect(show_note)
window.show()
app.exec()
