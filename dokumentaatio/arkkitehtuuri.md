# Arkkitehtuurikuvaus

Luokka/pakkauskaavio:

![Pakkausrakenne ja luokat](./kuvat/luokka-pakkauskaavio1.png)

Sekvenssikaavio pelin aloituksesta:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UnoService
  User->>UI: opens application
  UI->>UI: view()
  UI->>UnoService: start_game()
  UnoService->UnoService: create_deck()
  UnoService->UnoService: deal_cards()
  UnoService-->>UI: 
  UI->>UI: update_view()
```
