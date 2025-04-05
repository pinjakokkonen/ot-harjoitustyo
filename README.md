# Ohjelmistotekniikka, harjoitustyö

Toteutan **UNO** *korttipelin*.

## Dokumentaatio

[vaatimusmäärittely](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[arkkitehtuurikuvaus](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[työaikakirjanpito](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
