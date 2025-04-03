from tkinter import ttk
from services.uno_service import UnoService

class UI:
    def __init__(self, root):
        self._root = root
        self.service = UnoService()

    def start(self):
        self.view()
        self.service.start_game()
        self.update_view()
    
    def view(self):
        self.first_line = ttk.Frame(self._root)
        self.first_line.pack(pady=20)
        self.second_frame = ttk.Frame(self._root)
        self.second_frame.pack(pady=20)

        self.middle = ttk.LabelFrame(self.first_line, text="middle deck")
        self.middle.grid(row=0, column=0)
        
        self.player1 = ttk.LabelFrame(self.second_frame, text="player1")
        self.player1.grid(row=0, column=0, padx=20, ipadx=20)

        self.player2 = ttk.LabelFrame(self.second_frame, text="player2")
        self.player2.grid(row=0, column=1, ipadx=20)

        self.middle_label = ttk.Label(self.middle, text="")
        self.middle_label.pack(pady=20)

        self.player1_label = ttk.Label(self.player1, text="")
        self.player1_label.pack(pady=20)

        self.player2_label = ttk.Label(self.player2, text="")
        self.player2_label.pack(pady=20)
        
        self.turn = ttk.Label(self._root, text="")
        self.turn.pack()

        self._entry = ttk.Entry(self._root)
        self._entry.pack()

        button = ttk.Button(self._root, text="Play card", command=self._handle_button_click_play)
        button.pack()

        button = ttk.Button(self._root, text="Draw a card", command=self._handle_button_click_draw)
        button.pack()

    def _handle_button_click_play(self):
        entry = self._entry.get()
        self.service.play_card(entry)
        self.update_view()

    def update_view(self):
        self.middle_label.config(text=self.service.stack)

        self.player1_label.config(text=self.service.player1)

        self.player2_label.config(text=self.service.player2)

        self.turn.config(text=self.service.turn)
    
    def _handle_button_click_draw(self):
        self.service.draw_a_card()
        self.update_view()
