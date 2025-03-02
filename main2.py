
from PyQt6.QtWidgets import *
from file_helper import *

app = QApplication([])
notes = {
    "Zamitka 1": 
        "text": "pevnij text",
        "tegi": ["Teg1", "Teg2"]

}

write_in_file(notes)
window = QWidget()
window.setWindowTitle('Rosumni zamitki')
window.resize(900, 600)

list_notes = QListWidget()
list_notes

main_line = QHBoxLayout
pole = QTextEdit()
notes_list_lbl = QLabel("Spisok zamitok")
notatku_list = QListWidget()
create_notatku = QPushButton("Stvoriti zamitku")
delete_notatku = QPushButton("Vidaliti zamitku")
save_notatku = QPushButton("Zberegti zamitku")
teg_list_lbl = QLabel("Spisok tegiv")

main_line = QHBoxLayout()
main_line.addWidget(pole)

h1 = QVBoxLayout()
h1.addWidget(create_notatku)
h1.addWidget(delete_notatku)

d1 = QVBoxLayout()
d1.addWidget(notes_list_lbl)
d1.addWidget(notatku_list)
d1.addLayout(h1)
d1.addWidget(save_notatku)
d1.addWidget(teg_list_lbl)

main_line.addLayout(d1)

window.setLayout(main_line)

def show_note():

    key = list_notes.currentItem().text()
    pole.setText(notes[key]["text"])
    teg_list_lbl.clear()
    teg_list_lbl.addItems(notes[key]["tegi"])
    print(notes[key])

list_notes.itemClicked.connest(show_note)
window.show()
app.exec()