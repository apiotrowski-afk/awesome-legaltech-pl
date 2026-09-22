# Awesome Legaltech PL [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> **Prawo w kodzie** — polskie narzędzia, dane i modele dla prawa, otwarte i półotwarte.

Katalog obejmuje narzędzia, których przedmiotem jest samo prawo: akty prawne, orzecznictwo, umowy, procedura i praktyka kancelaryjna. Nie obejmuje operacji podatkowo-księgowych, bo KSeF, JPK i rejestry gospodarcze mają własne, liczne i dobrze utrzymane ekosystemy. Przy każdym wpisie widać, na jakich warunkach można go użyć w kancelarii.

## Contents

- [Zasady](#zasady)
- [Skala otwartości](#skala-otwartości)
- [Źródła prawa i orzecznictwo](#źródła-prawa-i-orzecznictwo)
- [Narzędzia i skille prawnicze](#narzędzia-i-skille-prawnicze)
- [Anonimizacja dokumentów](#anonimizacja-dokumentów)
- [Modele, korpusy, benchmarki](#modele-korpusy-benchmarki)

## Zasady

**Pola automatyczne stwierdzają, pola ręczne opisują.** Gwiazdki, data ostatniego commita, flaga `archived` i licencja pochodzą z API GitHuba i noszą datę odczytu. Katalog nie pisze *porzucony* ani *martwy* — podaje datę i zostawia wniosek czytelnikowi. Skrypt `sprawdz_zywotnosc.py` odświeża te pola co tydzień.

**Opisy własne.** Piszemy po otwarciu repozytorium. Nie kopiujemy pola `description` ani treści README.

**Jeden utrzymujący, jeden wpis.** Serię powiązanych repozytoriów opisujemy w jednej linii. Lista pokazuje krajobraz, nie czyjś dorobek.

**Chcesz zniknąć z listy?** Zgłoś issue, usuwamy bez pytania o powód.

## Skala otwartości

- 🟢 **Kod otwarty** - repozytorium i licencja OSI.
- 🟡 **Źródło otwarte, narzędzie zamknięte** - dane publiczne, software nie.
- 🔵 **API publiczne** - dostęp otwarty, bez licencji OSS.
- 🟠 **Komercyjne z progiem** - freemium albo darmowy poziom.
- ⚪ **Licencja nieokreślona** - brak pliku LICENSE, co nie znaczy *wolno*, tylko pełne prawo autorskie autora.

W polskim prawie najwięcej wartości siedzi w 🟡 i 🔵, czyli w otwartych danych bez otwartego narzędzia. Katalogi anglosaskie tej kategorii nie mają, bo tam problem wygląda inaczej.

## Źródła prawa i orzecznictwo

### Dane i API państwowe

- [API Sejmu / ELI](https://api.sejm.gov.pl/eli) - 🔵 Akty z Dziennika Ustaw i Monitora Polskiego, teksty jednolite, datowane listy aktów zmieniających. Tekst HTML jest strukturalny: każda jednostka redakcyjna ma stabilny identyfikator, więc podział na artykuły jest deterministyczny.
- [SAOS](https://www.saos.org.pl) - 🔵 Orzecznictwo sądów powszechnych, Sądu Najwyższego i sądów wojskowych.
- [CBOSA](https://orzeczenia.nsa.gov.pl) - 🔵 Centralna Baza Orzeczeń Sądów Administracyjnych.
- [Orzeczenia KIO](https://orzeczenia.uzp.gov.pl) - 🔵 Wyroki Krajowej Izby Odwoławczej w sprawach zamówień publicznych.
- [EUREKA](https://eureka.mf.gov.pl) - 🔵 Interpretacje i informacje podatkowe Ministerstwa Finansów.
- [Rejestr klauzul niedozwolonych UOKiK](https://rejestr.uokik.gov.pl) - 🟡 Archiwalne wyroki SOKiK, udostępniane w wersji zanonimizowanej. Przed powołaniem się sprawdź aktualny status prawny rejestru, bo zmienił się w 2026 roku.

### Akty prawne jako dane

- [kbchojnacki](https://github.com/kbchojnacki) - ⚪ Piętnaście repozytoriów: każdy polski kodeks i Konstytucja jako historia gita, gdzie jeden commit to jedna nowelizacja w dacie wejścia w życie. Polecenie `git blame` na przepisie pokazuje, kiedy zmieniło się brzmienie. Okres przed pierwszym tekstem jednolitym jest rekonstruowany, nie cytowany, co autor zaznacza wprost.
- [andilabs/polish-law](https://github.com/andilabs/polish-law) - 🟢 Historia prawa polskiego od 1918 roku, wraz z [zestawem danych](https://github.com/andilabs/polish-law-data).
- [apatryda/polish-law](https://github.com/apatryda/polish-law) - 🟢 Akty prawne tłumaczone najpierw na Markdown, potem na Catalę, czyli język rules-as-code z Inrii. Układ katalogów odwzorowuje hierarchię źródeł prawa: konstytucja, ustawy, umowy międzynarodowe, rozporządzenia, akty prawa miejscowego.
- [KrzysztofBogdan/Kodeks_cywilny](https://github.com/KrzysztofBogdan/Kodeks_cywilny) - 🟢 Kodeks cywilny jako tekst w repozytorium.

### Konektory i klienty

- [numikel/law-scrapper-mcp](https://github.com/numikel/law-scrapper-mcp) - ⚪ Serwer MCP nad API Sejmu: pobieranie i analiza aktów prawnych.
- [jamarpl21/prawo-pl-eli](https://github.com/jamarpl21/prawo-pl-eli) - 🟢 Prawo polskie i unijne z oficjalnych źródeł, czyli ELI Sejmu oraz CELLAR i EUR-Lex, wystawione jako agent skills.
- [apiotrowski-afk/legal-cite-pl](https://github.com/apiotrowski-afk/legal-cite-pl) - 🟢 Serwer MCP weryfikujący aktualne brzmienie przepisu polskiego i unijnego prosto ze źródła. Ten sam utrzymujący wydaje weryfikację podmiotów w KRS i na białej liście VAT oraz pamięć trwałą dla asystentów.
- [matematicsolutions](https://github.com/matematicsolutions) - 🟢 Seria serwerów MCP z weryfikowalnymi cytowaniami: SAOS, NSA i szesnaście WSA przez CBOSA, KIO, KRS oraz prawo polskie. Ten sam autor utrzymuje konektory ELI dla Niemiec, Francji, Holandii, Słowacji, Turcji, USA i Singapuru.
- [miskibin/sejm-stats](https://github.com/miskibin/sejm-stats) - ⚪ Baza i serwis o pracach Sejmu, na którym stoi Asystent RP.
- [Luzgan/lupa-na-prawo](https://github.com/Luzgan/lupa-na-prawo) - ⚪ Wyszukiwanie semantyczne w prawie polskim oraz śledzenie prac Sejmu i Senatu, jako serwer MCP.
- [operatorit/Polish_law_updates_notifier](https://github.com/operatorit/Polish_law_updates_notifier) - ⚪ Automat N8N powiadamiający o nowelizacjach wybranych aktów.
- [ad-m/cbosa](https://github.com/ad-m/cbosa) - ⚪ Automat przeszukujący CBOSA trzy razy dziennie pod kątem spraw o symbolu 648, czyli dostępu do informacji publicznej, i rozsyłający powiadomienia na grupę dyskusyjną.
- [artsiom-andrasovich/polish_law_viewer](https://github.com/artsiom-andrasovich/polish_law_viewer) - ⚪ Aplikacja desktopowa w Pythonie do przeszukiwania aktów przez API Sejmu, z otwieraniem dokumentów w systemowej przeglądarce PDF.
- [Ansvar-Systems/polish-law-mcp](https://github.com/Ansvar-Systems/polish-law-mcp) - ⚪ Baza przepisów o ochronie danych i cyberbezpieczeństwie. Repozytorium jest zarchiwizowane.

### Standardy i formaty

- [apiotrowski-afk/okf-legal](https://github.com/apiotrowski-afk/okf-legal) - 🟢 Profil prawniczy nad Open Knowledge Format: jednostka pod-dokumentowa z dosłownym cytatem, kierunkiem i statusem ratio albo obiter, relacje typowane, reguły antyhalucynacyjne.
- [ELI](https://eur-lex.europa.eu/eli-register/about.html) - 🔵 European Legislation Identifier, identyfikator używany przez API Sejmu.
- [Akoma Ntoso](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html) - 🔵 Standard OASIS dla aktów prawnych, w Polsce niewdrożony.

## Narzędzia i skille prawnicze

- [michaleiatrak-star/Lex-Machina](https://github.com/michaleiatrak-star/Lex-Machina) - 🟢 Analityka prawa, przygotowanie pism procesowych, analiza umów i ryzyk, szesnaście dziedzin prawa, zakaz cytowania przepisów z pamięci. Istnieje [port na OpenAI Codex](https://github.com/tittlepl-baj-jk/Lex-Machina-for-OpenAI-Codex).
- [miskibin/asystent-rp](https://github.com/miskibin/asystent-rp) - ⚪ Asystent czatowy dla obywateli, odpowiadający o prawie polskim na danych z sejm-stats.pl. Działa publicznie pod adresem chat.sejm-stats.pl.
- [matematicsolutions/patron](https://github.com/matematicsolutions/patron) - 🟢 Self-hosted agent dla kancelarii z łańcuchem skrótów jako śladem audytowym pod art. 12 AI Act, własnym modelem i dziewięcioma edycjami językowymi. Ten sam utrzymujący wydaje pakiety skilli prawniczych, warstwę weryfikacji wyjścia modelu i ocenę gotowości kancelarii na AI.
- [apiotrowski-afk/commercial-legal-pl](https://github.com/apiotrowski-afk/commercial-legal-pl) - 🟢 Redakcja i analiza umów B2B, IT oraz IP: baza klauzul, baza wiedzy doktrynalnej i kontrola spójności odesłań wewnętrznych.
- [apiotrowski-afk/kancelaria-dms](https://github.com/apiotrowski-afk/kancelaria-dms) - 🟢 System obiegu dokumentów i CRM dla kancelarii, natywny dla Google Workspace, do samodzielnego hostowania.
- [pawelkwaczynski/staleness-warnings-pl](https://github.com/pawelkwaczynski/staleness-warnings-pl) - ⚪ Prerejestrowany pomiar tego, czy modele ostrzegają o nieaktualności odpowiedzi na polskich ustawach. Zawiera kod, prompty, zamrożone fragmenty i sumy kontrolne, a klucz odpowiedzi jest zatrzymany celowo.
- [jakatora/kredyt-ai](https://github.com/jakatora/kredyt-ai) - ⚪ Analiza umów kredytowych pod prawem polskim.
- [rodorn/edoreczenia-klient](https://github.com/rodorn/edoreczenia-klient) - 🟢 Nieoficjalny klient interfejsu UA API usługi e-Doręczenia, w Pythonie.
- [tomkolp/e-doreczenia-wizualizacja-EPO](https://github.com/tomkolp/e-doreczenia-wizualizacja-EPO) - ⚪ Wizualizacja elektronicznego potwierdzenia odbioru.

## Anonimizacja dokumentów

Wszystkie przetwarzają dokument lokalnie, przed wysłaniem go do modelu. To warstwa, bez której praca z AI na aktach klienta nie domyka się od strony tajemnicy zawodowej.

- [paszkiewiczmichal/poufnik](https://github.com/paszkiewiczmichal/poufnik) - 🟢🟠 Aplikacja desktopowa w Tauri z silnikiem Presidio jako sidecar: import PDF, DOCX i skanów, lokalny OCR, przegląd każdego wykrycia, eksport oraz odwracalne tokeny. Poziom Basic jest darmowy i nie wymaga konta.
- [studiogo/cenzor](https://github.com/studiogo/cenzor) - 🟢 Narzędzie wiersza poleceń w Pythonie z pełnym obiegiem: tokenizacja przed wysłaniem i podstawienie danych z powrotem w odpowiedzi modelu. Publikuje zmierzoną skuteczność wraz z metodą pomiaru.
- [apiotrowski-afk/anon-legal-pl](https://github.com/apiotrowski-afk/anon-legal-pl) - 🟢 Presidio i spaCy, sumy kontrolne numerów PESEL, NIP i REGON, wzorce sygnatur sądowych, opcjonalny OCR.
- [LachPawel/Lethe](https://github.com/LachPawel/Lethe) - ⚪ Podejście hybrydowe: wyrażenia regularne na dane strukturalne oraz model PLLuM na rozpoznawanie kontekstowe. Dwadzieścia cztery kategorie danych, obsługa polskiej fleksji, API REST i wiersz poleceń.

## Modele, korpusy, benchmarki

- [speakleash](https://github.com/speakleash) - 🟢 Bielik, polski model językowy, wraz z korpusami i narzędziami. Wagi modeli są na Hugging Face, w repozytoriach są tutoriale, dostęp do korpusów i oprzyrządowanie.
- [PLLuM](https://pllum.clarin-pl.eu) - 🟢 Polski model językowy budowany ze środków publicznych, używany między innymi przez Lethe.
- [allegro/HerBERT](https://github.com/allegro/HerBERT) - ⚪ Model BERT dla polszczyzny, trenowany na korpusach polskich z dynamicznym maskowaniem całych słów.
- [spaCy pl_core_news_lg](https://spacy.io/models/pl) - 🟢 Rozpoznawanie jednostek nazwanych dla polszczyzny. Stoi na nim większość narzędzi do anonimizacji.
- [PiotrTyrakowski/PolishLawLLM-Benchmark](https://github.com/PiotrTyrakowski/PolishLawLLM-Benchmark) - ⚪ Benchmark modeli językowych na prawie polskim.

## Footnotes

Katalog prowadzi [Adam Piotrowski](https://github.com/apiotrowski-afk), radca prawny. Część wpisów to jego własne projekty, opisane tym samym schematem, z tymi samymi polami automatycznymi i objęte tą samą regułą *jeden utrzymujący, jeden wpis*. Kryterium włączenia: publicznie dostępne, dotyczy polskiego prawa, działa.

Licencja katalogu, czyli opisów, struktury i skryptów, to [CC BY 4.0](LICENSE). Nie obejmuje projektów, do których katalog odsyła: każdy ma własną licencję, wskazaną przy wpisie.
