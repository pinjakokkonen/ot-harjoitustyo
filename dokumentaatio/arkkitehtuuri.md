# Arkkitehtuurikuvaus

Luokka/pakkauskaavio:

![Pakkausrakenne ja luokat](./kuvat/luokka-pakkauskaavio1.png)

## Päätoiminnallisuudet

Sekvenssikaavioina kuvattu pelissä olevia toimintoja.

### Pelin aloittaminen

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UnoService
  User->>UI: opens application
  UI->>UI: view()
  UI->>UnoService: start_game()
  UnoService->>UnoService: create_deck()
  UnoService->>UnoService: deal_cards()
  UnoService-->>UI: 
  UI->>UI: update_view()
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
  UnoService->>UnoService: check_action_card(False, ("1", "green"))
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
  UnoService-->>UI: 
  UI->>UI: destroy_view()
```
