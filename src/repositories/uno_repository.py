from database_connection import get_database_connection

class UnoRepository:
    """Tietokantaoperaatioista vastaava luokka."""

    def __init__(self, connection):
        """Luokan konstruktori.
        
        Args:
            connection: Tietokannan olio connection
        """
        self._connection = connection

    def find_wins(self):
        """Palauttaa kaikkien käyttäjien voitot.
        
        Returns:
            Palauttaa voitot tuplena.
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users")

        rows = cursor.fetchall()

        return (rows[0][1], rows[1][1])

    def add_win(self, player):
        """Päivittää voittotilastoja.
        
        Args:
            player: Kenelle voitto tallentuu
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT wins FROM Users WHERE username=?", (player,))

        wins = cursor.fetchone()[0]
        wins += 1

        cursor.execute("UPDATE Users SET wins=? WHERE username=?", (wins, player))

        self._connection.commit()


uno_repository = UnoRepository(get_database_connection())
