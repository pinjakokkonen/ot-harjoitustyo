from tkinter import ttk
from services.uno_service import UnoService

class UI:
    def __init__(self, root):
        self._root = root
        self.service = UnoService()

    def start(self):
        self.view()
        self.service.start_game()
        self.playing_view()
        self.frame.pack()
    
    def view(self):
        self.frame = ttk.Frame(self._root)

        self.first_line = ttk.Frame(self.frame)
        self.first_line.pack(pady=20)
        self.second_frame = ttk.Frame(self.frame)
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

    def _handle_button_click_play(self):
        entry = self._entry.get()
        self.service.play_card(entry)
        if entry == "wild" or entry == "wild draw four":
            self.destroy_view()
            self.view()
            self.choose_color_view()
            self.update_view()
            self.frame.pack()
        else:
            self.update_view()

    def update_view(self):
        self.middle_label.config(text=self.service.stack)

        self.player1_label.config(text=self.service.player1)

        self.player2_label.config(text=self.service.player2)

        self.turn.config(text=self.service.turn)
    
    def _handle_button_click_draw(self):
        self.service.draw_a_card()
        self.update_view()

    def destroy_view(self):
        self.frame.pack_forget()

    def playing_view(self):
        self.turn = ttk.Label(self.frame, text="")
        self.turn.pack()

        self._entry = ttk.Entry(self.frame)
        self._entry.pack()

        button = ttk.Button(self.frame, text="Play card", command=self._handle_button_click_play)
        button.pack()

        button = ttk.Button(self.frame, text="Draw a card", command=self._handle_button_click_draw)
        button.pack()

        actions = ttk.Label(self.frame, text="r=reverse, s=skip, d=draw two")
        actions.pack()
        self.update_view()

    def choose_color_view(self):
        self.turn = ttk.Label(self.frame, text="")
        self.turn.pack()

        self.choose = ttk.Label(self.frame, text="Choose color")
        self.choose.pack()

        red = ttk.Button(self.frame, text="red", command=lambda:self._handle_button_click_choose_color("red"))
        red.pack()

        green = ttk.Button(self.frame, text="green", command=lambda:self._handle_button_click_choose_color("green"))
        green.pack()

        blue = ttk.Button(self.frame, text="blue", command=lambda:self._handle_button_click_choose_color("blue"))
        blue.pack()

        yellow = ttk.Button(self.frame, text="yellow", command=lambda:self._handle_button_click_choose_color("yellow"))
        yellow.pack()
    
    def _handle_button_click_choose_color(self, button_text):
        chosen_color = button_text
        self.service.choose_color(chosen_color)
        self.destroy_view()
        self.view()
        self.playing_view()
        self.frame.pack()
