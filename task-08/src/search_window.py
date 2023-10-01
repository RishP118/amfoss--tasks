import os
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
import requests
from PySide6.QtCore import Qt 
from PySide6.QtGui import QPixmap
from display import Display

class SearchWindow(QWidget):

    def __init__(self):
        super().__init__()


        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('/home/rishp11/Desktop/amfoss/amfoss--tasks/task-08/assets/landing.jpg'))
        self.background.setGeometry(0, 0, 850, 500)
       
        self.w = None        
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
      
        label1 = QLabel("Enter The Name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter = QPushButton("Search", self)
        enter.setGeometry(50, 300, 160, 43)
        enter.setStyleSheet("QPushButton { margin: 2px; background-color: black; color: white; border: 2px solid red; border-radius: 10px; font-weight: bold; } QPushButton:hover { background-color: red; color: black; }")

        capture = QPushButton("Capture", self)
        capture.setGeometry(50, 350, 160, 43)
        capture.setStyleSheet(" QPushButton { margin: 2px; background-color:black; color:white; border: 2px solid red; border-radius: 10px; font-weight: bold;} QPushButton:hover {background-color: red; color:black;}")

        display = QPushButton("Display", self)
        display.setGeometry(50, 400, 160, 43)
        display.setStyleSheet(" QPushButton { margin: 2px; background-color:black; color:white; border: 2px solid red; border-radius: 10px; font-weight: bold;} QPushButton:hover {background-color: red; color:black;}")

        self.pnamelabel = QLabel(self)
        self.pnamelabel.setGeometry(300, 100, 200, 30)

        self.pablabel = QLabel(self)
        self.pablabel.setGeometry(300, 150, 200, 30)

        self.ptypeslabel = QLabel(self)
        self.ptypeslabel.setGeometry(300, 200, 200, 30)

        self.pstatslabel = QLabel(self)
        self.pstatslabel.setGeometry(300, 250, 200, 100)

        self.pokemon_artwork_label = QLabel(self)
        self.pokemon_artwork_label.setGeometry(500, 100, 200, 200)

        enter.clicked.connect(self.fetch_pokemon_data)

        capture.clicked.connect(self.capture_pokemon)

        display.clicked.connect(self.open_display_window)
        
        self.pname = ""
        self.pab = []
        self.ptypes = []
        self.pstats = {}
        self.pokemon_artwork_url = ""
        self.captured_pokemon =  []


    def fetch_pokemon_data(self):
        self.background.hide()
        pname = self.textbox.text()
        if pname:
             url = f"https://pokeapi.co/api/v2/pokemon/{pname.lower()}"
             response = requests.get(url)
             if response.status_code == 200:
                pokemon_data = response.json()

                self.pname = pokemon_data['name']
                self.pab = [ability['ability']['name'] for ability in pokemon_data['abilities']]
                self.ptypes = [type_data['type']['name'] for type_data in pokemon_data['types']]
                self.pstats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
                self.pokemon_artwork_url = pokemon_data['sprites']['other']['official-artwork']['front_default']

                self.pnamelabel.setText(f"Name: {self.pname}")
                self.pablabel.setText(f"Abilities: {', '.join(self.pab)}")
                self.ptypeslabel.setText(f"Types: {', '.join(self.ptypes)}")
                stats_text = "\n".join([f"{stat_name}: {stat_value}" for stat_name, stat_value in self.pstats.items()])
                self.pstatslabel.setText(f"Stats:\n{stats_text}")

                try:
                    pixmap = QPixmap()
                    pixmap.loadFromData(requests.get(self.pokemon_artwork_url).content)

                    if not pixmap.isNull():
                       label_size = self.pokemon_artwork_label.size()
                       scaled_pixmap = pixmap.scaled(
                           label_size,
                           aspectMode=Qt.KeepAspectRatio,
                           mode=Qt.SmoothTransformation
                       )

                       self.pokemon_artwork_label.setPixmap(scaled_pixmap)
                    else:
                        print("Failed to load Pokemon artwork.")
                except Exception as e:
                    print(f"Failed to load artwork image: {e}")
             else:
                 print("Pokemon not found.")
        else:
           print("Please enter a Pokemon name.")



    
    def capture_pokemon(self):
        if self.pokemon_artwork_url:
            response = requests.get(self.pokemon_artwork_url)

            if response.status_code == 200:
                cap_path = os.path.join('cap', f"{self.pname}.png")
                os.makedirs('cap', exist_ok=True)
                with open(cap_path, "wb") as image_file:
                    image_file.write(response.content)
                print("Pokemon captured!")
               
                self.captured_pokemon.append({
                    'name': self.pname,
                    'image': f"{self.pname}.png",
                    'stats': [f"{stat_name}: {stat_value}" for stat_name, stat_value in self.pstats.items()],
                    'abilities': self.pab
                })
            else:
                print("Failed to capture Pokémon image.")
    
    def open_display_window(self):
        if self.captured_pokemon:  
           self.display = Display()
           self.display.show()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
