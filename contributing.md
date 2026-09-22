# Contribution Guidelines

Dziękujemy za chęć uzupełnienia katalogu. Poniżej to, czego szukamy i jak to zgłosić.

## Co wchodzi

Narzędzie, dane albo model, których **przedmiotem jest samo prawo**: akty prawne, orzecznictwo, umowy, procedura, praktyka kancelaryjna. Musi być publicznie dostępne, dotyczyć prawa polskiego i działać.

## Co nie wchodzi

- Operacje podatkowo-księgowe: KSeF, JPK, rejestry gospodarcze. Mają własne, dobrze utrzymane ekosystemy.
- Strony wizytówkowe kancelarii i projekty zaliczeniowe bez opisu.
- Narzędzia bez związku z prawem polskim.

## Zasady, które wyróżniają ten katalog

**Pola automatyczne stwierdzają, pola ręczne opisują.** Gwiazdki, data ostatniego commita, flaga `archived` i licencja pochodzą z API GitHuba. Nie wpisuj ich ręcznie i nie zastępuj ich oceną. Katalog nie pisze „porzucony" ani „martwy", tylko podaje datę odczytu.

**Opisy pisz własne**, po otwarciu repozytorium. Nie kopiuj pola `description` ani treści README, bo to cudzy tekst pod cudzą licencją.

**Jeden utrzymujący, jeden wpis.** Jeśli ktoś wydaje serię powiązanych repozytoriów, opisujemy ją w jednej linii z linkiem do profilu. Lista pokazuje krajobraz, nie czyjś dorobek. Dotyczy to także projektów osoby prowadzącej katalog.

**Wpisy nieutrzymywane zostają.** Repozytorium zarchiwizowane albo bez commita od lat nie znika z listy: dostaje datę i znacznik. Czytelnik wyciąga wniosek sam. To świadoma różnica wobec typowej awesome-listy.

## Format wpisu

```
- [nazwa](https://github.com/owner/repo) - 🟢 Opis własny, jedno albo dwa zdania, zakończone kropką.
```

Znacznik otwartości wybierz ze skali w README: 🟢 kod otwarty, 🟡 źródło otwarte a narzędzie zamknięte, 🔵 API publiczne, 🟠 komercyjne z progiem, ⚪ licencja nieokreślona.

Wpis dodaj na końcu właściwej sekcji. Separatorem między linkiem a opisem jest zwykły myślnik z odstępami, nie półpauza.

## Jak zgłosić

Pull request albo issue. W opisie napisz, dlaczego to pasuje do katalogu, i podaj link. Jeden pull request na jeden projekt, chyba że zgłaszasz serię jednego utrzymującego.

Przed wysłaniem uruchom kontrolę:

```
python3 sprawdz_zywotnosc.py README.md
npx awesome-lint
```

## Usunięcie wpisu

Jesteś autorem projektu i nie chcesz go na liście? Zgłoś issue. Usuwamy bez pytania o powód i bez dyskusji.
