from PyQt5.QtWidgets import QDialog, QVBoxLayout, QCalendarWidget, QPushButton
from PyQt5.QtCore import QDate
from . import filtro_update

class DateSelectorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleziona la data")

        layout = QVBoxLayout()

        # Aggiunta del widget calendario
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        layout.addWidget(self.calendar)

        # Aggiunta del pulsante di conferma
        self.ok_button = QPushButton("Aggiorna filtri", self)
        self.ok_button.clicked.connect(self.update_filters)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def update_filters(self):
        # Recupera la data selezionata dal calendario
        selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        # Chiama la funzione per aggiornare i filtri con la data selezionata
        filtro_update.aggiorna_filtri(selected_date)
        self.accept()  # Chiudi la finestra
