from tkinter import ttk
from services.uno_service import UnoService

class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Pohjustaa käyttöliittymästä vastaavan luokan.

        Args:
            root: Käyttöliittymän alustus
            service: UnoService luokkaan viittaaminen
        """
        self._root = root
        self.service = UnoService()

    def start(self):
        """Pelin aloitus näkymän luominen."""
        self.view()
        self.service.start_game()
        self.playing_view()
        self.frame.pack()
    
    def view(self):
        """Perusnäkymä, joka on aina esillä."""
        self.frame = ttk.Frame(self._root)

        self.first_line = ttk.Frame(self.frame)
        self.first_line.pack(pady=20)
        self.second_frame = ttk.Frame(self.frame)
        self.second_frame.pack(pady=20)

        self.middle = ttk.LabelFrame(self.first_line, text="middle deck")
        self.middle.grid(row=0, column=0)

        self.player = ttk.LabelFrame(self.second_frame, text="")
        self.player.grid(row=0, column=0, padx=20, ipadx=20)

        self.middle_label = ttk.Label(self.middle, text="")
        self.middle_label.pack(pady=20)

        self.player_label = ttk.Label(self.player, text="")
        self.player_label.pack(pady=20)

    def _handle_button_click_play(self):
        """Huolehtii kortin pelaamisesta."""
        entry = self._entry.get()
        self.service.play_card(entry)
        if self.service.win:
            self.destroy_view()
            charts = self.service.find_charts()
            self.winning_view(charts)
        elif entry == "wild" or entry == "wild draw four":
            self.destroy_view()
            self.view()
            self.choose_color_view()
            self.update_view()
            self.frame.pack()
        else:
            self.update_view()

    def update_view(self):
        """Päivittää näkymän."""
        self.middle_label.config(text=self.service.stack)

        self.card_view()
    
    def card_view(self):
        """Päivittää näkymään oikean pelaajan kortit ja kumman vuoro on."""
        self.player.config(text=self.service.turn)
        if self.service.turn == "player1":
            self.player_label.config(text=self.service.player1)
        else:
            self.player_label.config(text=self.service.player2)

        self.turn.config(text=self.service.turn)

    def _handle_button_click_draw(self):
        """Huolehtii kortin nostamisesta."""
        self.service.draw_a_card()
        self.update_view()

    def destroy_view(self):
        """Tuhoaa näkymän."""
        self.frame.pack_forget()

    def playing_view(self):
        """Näkymä, jossa pystyy pelaamaan kortteja."""
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
        """Näkymä, jossa pystyy valitsemaan seuraavaksi pelattavan värin."""
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
        """Huolehtii värin valitsemisesta."""
        chosen_color = button_text
        self.service.choose_color(chosen_color)
        self.destroy_view()
        self.view()
        self.playing_view()
        self.frame.pack()

    def winning_view(self, charts):
        wins1 = str(charts[0])
        wins2 = str(charts[1])
        self.frame = ttk.Frame(self._root)

        charts = ttk.Label(self.frame, text="Wins", font=(60))
        charts.pack(pady=40)

        player1 = ttk.Label(self.frame, text="player1")
        player1.pack()

        player1_wins = ttk.Label(self.frame, text=wins1)
        player1_wins.pack()

        player2 = ttk.Label(self.frame, text="player2")
        player2.pack()

        player2_wins = ttk.Label(self.frame, text=wins2)
        player2_wins.pack()

        button = ttk.Button(self.frame, text="Play again", command=self._handle_button_click_play_again)
        button.pack()

        self.frame.pack(pady=20)

    def _handle_button_click_play_again(self):
        self.destroy_view()
        self.start()
