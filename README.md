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
- [Poza progiem świeżości](#poza-progiem-świeżości)

## Zasady

**Pola automatyczne stwierdzają, pola ręczne opisują.** Gwiazdki, data ostatniego commita, flaga `archived` i licencja pochodzą z API GitHuba i noszą datę odczytu. Katalog nie pisze *porzucony* ani *martwy* — podaje datę i zostawia wniosek czytelnikowi. Skrypt `sprawdz_zywotnosc.py` odświeża te pola co tydzień.

**Opisy własne.** Piszemy po otwarciu repozytorium. Nie kopiujemy pola `description` ani treści README.

**Jeden utrzymujący, jeden wpis.** Serię powiązanych repozytoriów opisujemy w jednej linii. Lista nie jest czyimś dorobkiem, ale mapą krajobrazu.

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

- [API Sejmu / ELI](https://api.sejm.gov.pl/eli) - 🔵 Udostępnia akty z Dziennika Ustaw i Monitora Polskiego, teksty jednolite oraz datowane listy aktów zmieniających. Tekst HTML jest strukturalny — każda jednostka redakcyjna ma stabilny identyfikator, więc na artykuły dzieli się deterministycznie.
- [SAOS](https://www.saos.org.pl) - 🔵 Zbiera orzecznictwo sądów powszechnych, Sądu Najwyższego i sądów wojskowych.
- [CBOSA](https://orzeczenia.nsa.gov.pl) - 🔵 Gromadzi orzeczenia Naczelnego Sądu Administracyjnego i wojewódzkich sądów administracyjnych.
- [Orzeczenia KIO](https://orzeczenia.uzp.gov.pl) - 🔵 Udostępnia wyroki Krajowej Izby Odwoławczej w sprawach zamówień publicznych.
- [EUREKA](https://eureka.mf.gov.pl) - 🔵 Zbiera interpretacje i informacje podatkowe Ministerstwa Finansów.
- [Rejestr klauzul niedozwolonych UOKiK](https://rejestr.uokik.gov.pl) - 🟡 Zawiera archiwalne wyroki SOKiK w wersji zanonimizowanej. Status prawny rejestru zmienił się w 2026 roku, więc sprawdź go, zanim się na niego powołasz.

### Akty prawne jako dane

- [kbchojnacki](https://github.com/kbchojnacki) - ⚪ Piętnaście repozytoriów: każdy polski kodeks i Konstytucja jako historia gita, gdzie jeden commit to jedna nowelizacja w dacie wejścia w życie. Polecenie `git blame` na przepisie pokazuje, kiedy zmieniło się brzmienie. Okresu przed pierwszym tekstem jednolitym autor nie cytuje, lecz rekonstruuje — i zaznacza to wprost.
- [legalize-dev/legalize-pl](https://github.com/legalize-dev/legalize-pl) - ⚪ Polskie ustawodawstwo w Markdown, gdzie każda ustawa to plik, a każda nowelizacja to commit. Polska edycja [międzynarodowego projektu](https://github.com/legalize-dev) obejmującego 32 jurysdykcje, więc te same przepisy da się porównywać między krajami w jednym formacie.
- [balwierz/sejm2git](https://github.com/balwierz/sejm2git) - ⚪ Pobiera akty z API Sejmu i nakłada nowelizacje, żeby odtworzyć tekst obowiązujący na daną datę. Historię materializuje w gicie: gałąź na nowelizację, scalenie w dniu wejścia w życie, wyniki głosowań w stopkach commitów.

- [apatryda/polish-law](https://github.com/apatryda/polish-law) - 🟢 Tłumaczy akty prawne najpierw na Markdown, potem na Catalę, czyli język rules-as-code z Inrii. Układ katalogów odwzorowuje hierarchię źródeł prawa: konstytucja, ustawy, umowy międzynarodowe, rozporządzenia, akty prawa miejscowego.

### Konektory i klienty

- [numikel/law-scrapper-mcp](https://github.com/numikel/law-scrapper-mcp) - ⚪ Pobiera i analizuje akty prawne przez API Sejmu, jako serwer MCP.
- [jamarpl21/prawo-pl-eli](https://github.com/jamarpl21/prawo-pl-eli) - 🟢 Prawo polskie i unijne z oficjalnych źródeł, czyli ELI Sejmu oraz CELLAR i EUR-Lex, wystawione jako agent skills.
- [apiotrowski-afk/legal-cite-pl](https://github.com/apiotrowski-afk/legal-cite-pl) - 🟢 Serwer MCP, który sprawdza aktualne brzmienie przepisu polskiego i unijnego prosto ze źródła. Ten sam utrzymujący wydaje weryfikację podmiotów w KRS i na białej liście VAT oraz pamięć trwałą dla asystentów.
- [matematicsolutions](https://github.com/matematicsolutions) - 🟢 Seria serwerów MCP z weryfikowalnymi cytowaniami: SAOS, NSA i szesnaście WSA przez CBOSA, KIO, KRS, Dziennik Ustaw z Monitorem Polskim oraz interpretacje podatkowe z EUREKI. Wydaje też silnik anonimizacji, serwer nad korpusem legalize, infrastrukturę wiedzy prawnej *Repertorium* oraz dwa huby skilli prawniczych, polski i angielski. Ten sam autor utrzymuje konektory ELI dla Niemiec, Francji, Holandii, Słowacji, Turcji, USA i Singapuru.

- [Luzgan/lupa-na-prawo](https://github.com/Luzgan/lupa-na-prawo) - ⚪ Przeszukuje prawo polskie semantycznie i śledzi prace Sejmu oraz Senatu, jako serwer MCP.
- [operatorit/Polish_law_updates_notifier](https://github.com/operatorit/Polish_law_updates_notifier) - ⚪ Automat N8N, który powiadamia o nowelizacjach wybranych aktów.
- [ad-m/cbosa](https://github.com/ad-m/cbosa) - ⚪ Przeszukuje CBOSA trzy razy dziennie pod kątem spraw o symbolu 648, czyli dostępu do informacji publicznej, i rozsyła powiadomienia na grupę dyskusyjną.
- [artsiom-andrasovich/polish_law_viewer](https://github.com/artsiom-andrasovich/polish_law_viewer) - ⚪ Przeszukuje akty przez API Sejmu z aplikacji desktopowej w Pythonie i otwiera dokumenty w systemowej przeglądarce PDF.
- [PiotrKantorowski](https://github.com/PiotrKantorowski) - 🟢 [Dziennik upadłościowy](https://github.com/PiotrKantorowski/dziennik-upadlosciowy) monitoruje kontrahentów w KRS, Krajowym Rejestrze Zadłużonych i Monitorze Sądowym i Gospodarczym. [CSM for Word](https://github.com/PiotrKantorowski/csm-for-word) pseudonimizuje polskie dokumenty lokalnie i odwracalnie, wprost w Wordzie.
- [pawelojdowski/uodo-mcp](https://github.com/pawelojdowski/uodo-mcp) - ⚪ Przeszukuje i analizuje decyzje Prezesa UODO, jako serwer MCP. Pokrywa źródło, którego nie obsługuje żaden inny konektor z tej listy.
- [PawelHaracz/polish-caselaw-mcp](https://github.com/PawelHaracz/polish-caselaw-mcp) - 🟢 Udostępnia polskie orzecznictwo przez protokół MCP.
- [pielas-activy/znajdz-ksiege-wieczysta](https://github.com/pielas-activy/znajdz-ksiege-wieczysta) - 🟢 Ustala numer księgi wieczystej mieszkania na podstawie samego adresu budynku, korzystając z darmowej przeglądarki Ministerstwa Sprawiedliwości. Skill dla Claude Code i Cowork.
- [danielmskuza-blip/Orzeczenia-MS](https://github.com/danielmskuza-blip/Orzeczenia-MS) - 🟢 Udostępnia orzeczenia sądów powszechnych z portalu Ministerstwa Sprawiedliwości.
- [Iskra-YT/sejmium](https://github.com/Iskra-YT/sejmium) - 🟢 Śledzi prace parlamentu na API Sejmu. Przydaje się, gdy trzeba wychwycić nowelizację, zanim trafi do Dziennika Ustaw.
- [legaion/mcp-verifier](https://github.com/legaion/mcp-verifier) - ⚪ Waliduje serwery MCP dla polskiego prawa: dokumentację, schematy narzędzi i zgodność odpowiedzi.

### Standardy i formaty

- [apiotrowski-afk/okf-legal](https://github.com/apiotrowski-afk/okf-legal) - 🟢 Profil prawniczy nad Open Knowledge Format: jednostka pod-dokumentowa z dosłownym cytatem, kierunkiem i statusem ratio albo obiter, relacje typowane, reguły antyhalucynacyjne.
- [ELI](https://eur-lex.europa.eu/eli-register/about.html) - 🔵 European Legislation Identifier, identyfikator używany przez API Sejmu.
- [Akoma Ntoso](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html) - 🔵 Standard OASIS dla aktów prawnych, w Polsce niewdrożony.

## Narzędzia i skille prawnicze

- [michaleiatrak-star/Lex-Machina](https://github.com/michaleiatrak-star/Lex-Machina) - 🟢 Analizuje prawo i umowy, przygotowuje pisma procesowe i ocenia ryzyka w szesnastu dziedzinach prawa. Zabrania cytowania przepisów z pamięci. Istnieje [port na OpenAI Codex](https://github.com/tittlepl-baj-jk/Lex-Machina-for-OpenAI-Codex).
- [crankshift/lawpowers](https://github.com/crankshift/lawpowers) - 🟢 Monorepo wtyczek prawniczych z podziałem na jurysdykcje, z wtyczką polską liczącą **22 skille**: przedawnienie, odsetki ustawowe, opłata sądowa, wartość przedmiotu sporu, alimenty, orzecznictwo frankowe, procedury ZUS, USC i cudzoziemców, jurysdykcja, konwencja nowojorska, przegląd umów B2B, nieruchomościowych i pojazdowych. Druga wtyczka obejmuje prawo ukraińskie.
- [trosinski08/ai_agent_compliance](https://github.com/trosinski08/ai_agent_compliance) - ⚪ Analizuje sprawy AML i KYC w architekturze RAG, indeksując polskie przepisy o przeciwdziałaniu praniu pieniędzy wraz z materiałami GIIF i KNF.
- [miskibin](https://github.com/miskibin) - ⚪ [Asystent RP](https://github.com/miskibin/asystent-rp) odpowiada obywatelom na pytania o prawo polskie i działa publicznie pod adresem chat.sejm-stats.pl. [Tygodnik sejmowy](https://github.com/miskibin/tygodnik-sejmowy) streszcza, co dzieje się w Sejmie. Oba korzystają z danych sejm-stats, które opisujemy w [ARCHIWUM.md](ARCHIWUM.md).
- [matematicsolutions/patron](https://github.com/matematicsolutions/patron) - 🟢 Agent dla kancelarii do samodzielnego hostowania. Prowadzi ślad audytowy w łańcuchu skrótów pod art. 12 AI Act, korzysta z własnego modelu i ma dziewięć edycji językowych. Ten sam utrzymujący wydaje pakiety skilli prawniczych, warstwę weryfikacji wyjścia modelu i ocenę gotowości kancelarii na AI.
- [apiotrowski-afk/commercial-legal-pl](https://github.com/apiotrowski-afk/commercial-legal-pl) - 🟢 Redaguje i analizuje umowy B2B, IT oraz IP. Zawiera bazę klauzul, bazę wiedzy doktrynalnej i kontrolę spójności odesłań wewnętrznych.
- [apiotrowski-afk/kancelaria-dms](https://github.com/apiotrowski-afk/kancelaria-dms) - 🟢 Prowadzi obieg dokumentów i CRM kancelarii natywnie w Google Workspace, na własnym serwerze.
- [pawelkwaczynski](https://github.com/pawelkwaczynski) - 🟢 Dwa projekty wokół aktualności prawa. [stillaw](https://github.com/pawelkwaczynski/stillaw) sprawdza deterministycznie, czy przepis nadal obowiązuje. [staleness-warnings-pl](https://github.com/pawelkwaczynski/staleness-warnings-pl) mierzy w prerejestrowanym badaniu, czy modele same ostrzegają o nieaktualności; udostępnia kod, prompty, zamrożone fragmenty i sumy kontrolne, ale klucz odpowiedzi zatrzymuje celowo.
- [a-szczudlo](https://github.com/a-szczudlo) - ⚪ Seria otwartych audytorów Creativa Legal, każdy jako skill dla Claude, ChatGPT i Codeksa. [OpenNDA](https://github.com/a-szczudlo/OpenNDA) ocenia umowę o poufności w trzynastu punktach kontrolnych z flagami ryzyka, cross-checkiem spójności i porównaniem wersji po poprawkach. Obok niego [OpenFounders](https://github.com/a-szczudlo/OpenFounders) testuje relacje wspólników sp. z o.o., [OpenGDPR](https://github.com/a-szczudlo/OpenGDPR) skanuje zgodność z RODO, a osobny audytor bierze umowy marketingowe.
- [DawidZabek/leaseguard](https://github.com/DawidZabek/leaseguard) - ⚪ Analizuje wklejoną umowę najmu mieszkania z perspektywy najemcy i wskazuje postanowienia niekorzystne.
- [dominikloza/lawer-up](https://github.com/dominikloza/lawer-up) - ⚪ Pozwala wgrać umowę i rozmawiać o niej z asystentem, z naciskiem na wykrywanie ukrytych ryzyk.
- [emilpinski/lexaro](https://github.com/emilpinski/lexaro) - ⚪ Odpowiada na pytania o prawo polskie w architekturze RAG: HyDE, wyszukiwanie hybrydowe na pgvector i BM25, rerank i cache semantyczny. Działa pod adresem lexaro.pl.
- [Inexpli/Radca-prawny-AI](https://github.com/Inexpli/Radca-prawny-AI) - 🟢 Odpowiada na pytania prawne w architekturze RAG, w całości lokalnie na GPU.
- [jakatora/kredyt-ai](https://github.com/jakatora/kredyt-ai) - ⚪ Analizuje umowy kredytowe pod prawem polskim.
- [rodorn](https://github.com/rodorn) - 🟢 [Klient e-Doręczeń](https://github.com/rodorn/edoreczenia-klient) obsługuje interfejs UA API w Pythonie, nieoficjalnie. [Radar przetargów](https://github.com/rodorn/fluxlab-przetargi-radar) śledzi zamówienia publiczne.
- [tomkolp/e-doreczenia-wizualizacja-EPO](https://github.com/tomkolp/e-doreczenia-wizualizacja-EPO) - ⚪ Wizualizuje elektroniczne potwierdzenie odbioru.

## Anonimizacja dokumentów

Wszystkie przetwarzają dokument lokalnie, zanim trafi on do modelu. Bez tej warstwy praca z AI na aktach klienta nie domyka się od strony tajemnicy zawodowej.

- [paszkiewiczmichal/poufnik](https://github.com/paszkiewiczmichal/poufnik) - 🟢🟠 Aplikacja desktopowa w Tauri z silnikiem Presidio jako sidecar. Wczytuje PDF, DOCX i skany, rozpoznaje tekst lokalnie, pozwala przejrzeć każde wykrycie i eksportuje dokument z odwracalnymi tokenami. Poziom Basic jest darmowy i nie wymaga konta. Ten sam utrzymujący wydaje [skille dla Claude Code zoptymalizowane pod polszczyznę](https://github.com/paszkiewiczmichal/claude-skills-pl).
- [studiogo/cenzor](https://github.com/studiogo/cenzor) - 🟢 Zastępuje dane tokenami przed wysłaniem do modelu i podstawia je z powrotem w odpowiedzi. Publikuje zmierzoną skuteczność razem z metodą pomiaru.
- [apiotrowski-afk/anon-legal-pl](https://github.com/apiotrowski-afk/anon-legal-pl) - 🟢 Wykrywa dane osobowe przez Presidio i spaCy, sprawdza sumy kontrolne numerów PESEL, NIP i REGON oraz rozpoznaje wzorce sygnatur sądowych. Opcjonalnie rozpoznaje tekst ze skanów.
- [sebob/donotfeedai](https://github.com/sebob/donotfeedai) - ⚪ Podmienia imiona, PESEL, NIP, IBAN, telefony, adresy i pliki na dane fikcyjne, zanim trafią do ChatGPT, Claude'a albo Gemini, i przywraca je w odpowiedzi. Bez serwera dostawcy i bez telemetrii.
- [LachPawel/Lethe](https://github.com/LachPawel/Lethe) - ⚪ Łączy wyrażenia regularne na danych strukturalnych z modelem PLLuM na rozpoznawaniu kontekstowym. Obsługuje dwadzieścia cztery kategorie danych i polską fleksję, przez API REST albo wiersz poleceń.

## Modele, korpusy, benchmarki

- [speakleash](https://github.com/speakleash) - 🟢 Rozwija Bielika, polski model językowy, razem z korpusami i narzędziami. Wagi modeli leżą na Hugging Face, a w repozytoriach są tutoriale, dostęp do korpusów i oprzyrządowanie.
- [PLLuM](https://pllum.clarin-pl.eu) - 🟢 Polski model językowy budowany ze środków publicznych. Korzysta z niego między innymi Lethe.

- [spaCy pl_core_news_lg](https://spacy.io/models/pl) - 🟢 Rozpoznaje jednostki nazwane w polszczyźnie. Opiera się na nim większość narzędzi z sekcji o anonimizacji.
- [cloudforge1/PaddleOCR-VL-For-Polish](https://github.com/cloudforge1/PaddleOCR-VL-For-Polish) - 🟢 Model OCR dostrojony do polskich dokumentów współczesnych i historycznych. Przydaje się tam, gdzie akta istnieją wyłącznie jako skan.
- [brokeboiflex/nodeusz](https://github.com/brokeboiflex/nodeusz) - ⚪ Natywne wiązania Node.js do analizatora morfologicznego Morfeusz2. Odmiana polskich nazwisk i nazw to warunek działania anonimizacji.
- [PiotrTyrakowski/PolishLawLLM-Benchmark](https://github.com/PiotrTyrakowski/PolishLawLLM-Benchmark) - ⚪ Sprawdza modele językowe na prawie polskim.

## Poza progiem świeżości

Pozycje bez commita od ponad roku albo z zarchiwizowanym repozytorium trzymamy w osobnym pliku [ARCHIWUM.md](ARCHIWUM.md), razem z datą ostatniego commita. Nie znikają, bo dla zbiorów danych i modeli brak commitów nie oznacza porzucenia, a wytyczne awesome każą trzymać je poza listą główną.

## Footnotes

Katalog prowadzi [Adam Piotrowski](https://github.com/apiotrowski-afk), radca prawny. Część wpisów to jego własne projekty. Opisuje je tym samym schematem, tymi samymi polami automatycznymi i tą samą regułą *jeden utrzymujący, jeden wpis*. Kryterium włączenia: publicznie dostępne, dotyczy polskiego prawa, działa.

Powiązana lista: [ksefuj/awesome-ksef](https://github.com/ksefuj/awesome-ksef) kataloguje narzędzia KSeF, czyli warstwę, której ten katalog świadomie nie obejmuje.

Licencja katalogu, czyli opisów, struktury i skryptów, to [CC BY 4.0](LICENSE). Nie obejmuje projektów, do których katalog odsyła: każdy ma własną licencję, wskazaną przy wpisie.
