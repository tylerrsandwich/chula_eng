import tkinter as tk
import random

# List of Thai consonants with their names
thai_consonants = [
    ("ก", "กอ ไก่ (gor gai)"),
    ("ข", "ขอ ไข่ (khor khai)"),
    ("ฃ", "ฃอ ขวด (khor khuat)"),
    ("ค", "คอ ควาย (khor khwai)"),
    ("ฅ", "ฅอ คน (khor khon)"),
    ("ฆ", "ฆอ ระฆัง (khor rakhang)"),
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_card = random.choice(thai_consonants)
        self.showing_name = False
        
        self.card_label = tk.Label(root, text=self.current_card[0], font=("Arial", 100), width=10, height=5, relief="solid")
        self.card_label.pack(pady=20)
        
        self.flip_button = tk.Button(root, text="Flip", font=("Arial", 20), command=self.flip_card)
        self.flip_button.pack()
        
        self.next_button = tk.Button(root, text="Next", font=("Arial", 20), command=self.next_card)
        self.next_button.pack()
    
    def flip_card(self):
        if self.showing_name:
            self.card_label.config(text=self.current_card[0])
        else:
            self.card_label.config(text=self.current_card[1])
        self.showing_name = not self.showing_name
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.card_label.config(text=self.current_card[0])
        self.showing_name = False

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()
