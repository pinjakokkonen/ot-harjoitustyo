# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmitasoista kerrosarkkitehtuuria ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](./kuvat/pakkausrakenne.png)

Ui sisältää käyttöliittymästä vastaavan koodin, services sovelluslogiikasta ja repositories tiedon tallennuksesta.

## Käyttöliittymä

Käyttöliittymä muodostuu kolmesta eri näkymästä:

- Korttien pelaaminen
- Värin valitseminen
- Voittotilastot

Yksi näkymistä on aina kerrallaan esillä. [UI](../src/ui/ui.py)-luokka huolehtii näkymän näyttämisestä ja käyttöliittymä on pyritty eristämään sovelluslogiikasta. Se kutsuu vain [UnoService](../src/service)-luokkaa.

Kun kortteja pelataan renderöi ui näkymän uudelleen pelattujen korttien mukaan, joiden tiedot on saatu sovelluslogiikalta.

## Sovelluslogiikka

Toiminnallisista kokonaisuuksista vastavat luokat UnoService ja CardsService. Luokat tarjoavat käyttöliittymän toiminnoille metodit. Näihin kuuluu:

- start_game()
- play_card(card)
- draw_a_card()
- choose_color(color)

UnoService pääsee tietojen tallennukseen käsiksi repositoriesissa sijaitsevan UnoRepositoryn kautta.

Ohjelman osien suhdetta kuvaava luokka/pakkauskaavio:

![Pakkausrakenne ja luokat](./kuvat/luokka-pakkauskaavio.png)

## Tietojen pysyväistallennus

Pakkauksen repositories luokka UnoRepository huolehtii tietojen tallennuksesta. Tiedot tallennetaan SQLite-tietokantaan.

Luokka noudattaa Repository-suunnittelumallia ja se on tarvittaessa mahdollista korvata uudella.

### Tiedosto

Sovelluksen juureen sijoitettu konfiguraatiotiedosto [.env](../.env) määrittää tiedoston nimen.

Tulokset tallennetaan SQLite-tietokannan tauluun Users, joka alustetaan [initialize_database.py](../src/initialize_database.py)-tiedostossa.

## Päätoiminnallisuudet

Sekvenssikaavioina kuvattu pelissä olevia toimintoja.

### Pelin aloittaminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UnoService
  participant CardsService
  User->>UI: opens application
  UI->>UI: view()
  UI->>UnoService: start_game()
  UnoService->>CardsService: create_deck()
  CardsService-->>UnoService: deck
  UnoService->>CardsService: set_stack()
  CardsService-->>UnoService: stack
  UnoService->>CardsService: deal_cards(deck)
  CardsService-->>UnoService: (deck, player1, player2)
  UnoService-->>UI: 
  UI->>UI: playing_view()
  UI->>UI: update_view()
  UI->>UI: cards_view()
```

### Kortin pelaaminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UnoService
  User->>UI: click "Play card" button
  UI->>UnoService: play_card("1 green")
  UnoService->>UnoService: continue_to_play(False, ("1", "green"))
  UnoService->>UnoService: check_colors("green")
  UnoService-->>UnoService: True
  UnoService->>UnoService: check_winning("player1")
  UnoService-->>UnoService: False
  UnoService->>UnoService: check_action_card(False, ("1", "green"))
  UnoService-->>UI: 
  UI->>UI: update_view()
```

### Kortin nostaminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UnoService
  User->>UI: click "Draw a card" button
  UI->>UnoService: draw_a_card()
  UnoService-->>UI: 
  UI->>UI: update_view()
```

### Värin valitseminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UnoService
  User->>UI: click "Red" button
  UI->>UnoService: choose_color("red")
  UnoService->>UnoService: skip_turn()
  UnoService-->>UI: 
  UI->>UI: destroy_view()
  UI->>UI: view()
  UI->>UI: playing_view()
  UI->>UI: update_view()
  UI->>UI: card_view()
```
