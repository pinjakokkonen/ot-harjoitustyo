```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- "0..*" Rahaa
    Ruutu "1" -- "1" Toiminto
    Ruutu "1" -- "1" Aloitusruutu
    Ruutu "1" -- "1" Vankila
    Ruutu "6" -- "6" Sattuma ja yhteismaa
    Ruutu "6" -- "6" Asemat ja laitokset
    Ruutu "26" -- "26" Normaalit kadut
    Sattuma ja yhteismaa "1" -- "20" Kortit
    Kortit "1" -- "1" Toiminto
    Normaalit kadut "1" -- "0..4" Talot
    Normaalit kadut "1" -- "0..1" Hotelli
    Normaalit kadut "0..*" -- "1" Pelaaja
```
