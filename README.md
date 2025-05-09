# Ohjelmistotekniikka, harjoitustyö

Sovellus on **UNO** *korttipeli*, jota pystyy pelaamaan kaksi käyttäjää samalta näytöltä. Pelissä on käytössä normaalit UNO:n säännöt.

## Releases

- [viikon 5 release](https://github.com/pinjakokkonen/ot-harjoitustyo/releases/tag/viikko5)
- [viikon 6 release](https://github.com/pinjakokkonen/ot-harjoitustyo/releases/tag/viikko6)
- [loppupalautus](https://github.com/pinjakokkonen/ot-harjoitustyo/releases/tag/loppupalautus)

## Dokumentaatio

[vaatimusmäärittely](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[arkkitehtuurikuvaus](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[käyttöohje](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[testausdokumentti](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)

[työaikakirjanpito](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/pinjakokkonen/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

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
