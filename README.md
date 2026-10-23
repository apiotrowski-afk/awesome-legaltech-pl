# Awesome Legaltech PL [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> **Prawo w kodzie** — polskie narzędzia, dane i modele dla prawa, otwarte i półotwarte.

Katalog obejmuje narzędzia, których przedmiotem jest samo prawo: akty prawne, orzecznictwo, umowy, procedura i praktyka kancelaryjna. Nie obejmuje operacji podatkowo-księgowych, bo KSeF, JPK i rejestry gospodarcze mają własne, liczne i dobrze utrzymane ekosystemy. Przy każdym wpisie widać, na jakich warunkach można go użyć w kancelarii.

Produkty zamknięte, czyli SaaS-y, systemy wydawców i platformy, zbieramy osobno w [KOMERCYJNE.md](KOMERCYJNE.md).

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
- 🟣 **Komercyjne** - płatne, bez stałego darmowego poziomu, najwyżej z okresem próbnym.
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
- [LexaurinTheDog](https://github.com/LexaurinTheDog) - 🟢 **106 komentarzy do polskich ustaw**, artykuł po artykule, w tym kodeks cywilny, karny, karny skarbowy, prawo o adwokaturze, AML i cyberbezpieczeństwo. Brzmienie przepisów przeniesione dosłownie z Dziennika Ustaw wraz z odnośnikami tekstu jednolitego. ⚠ Autor zaznacza wprost, że komentarz powstał **wyłącznie z urzędowego tekstu aktu, bez baz komercyjnych, a orzecznictwo nie jest jeszcze jego częścią** — to nie zastępuje komentarza z linią orzeczniczą.
- [legalize-dev/legalize-pl](https://github.com/legalize-dev/legalize-pl) - ⚪ Polskie ustawodawstwo w Markdown, gdzie każda ustawa to plik, a każda nowelizacja to commit. Polska edycja [międzynarodowego projektu](https://github.com/legalize-dev) obejmującego 32 jurysdykcje, więc te same przepisy da się porównywać między krajami w jednym formacie.
- [balwierz/sejm2git](https://github.com/balwierz/sejm2git) - ⚪ Pobiera akty z API Sejmu i nakłada nowelizacje, żeby odtworzyć tekst obowiązujący na daną datę. Historię materializuje w gicie: gałąź na nowelizację, scalenie w dniu wejścia w życie, wyniki głosowań w stopkach commitów.

- [apatryda/polish-law](https://github.com/apatryda/polish-law) - 🟢 Tłumaczy akty prawne najpierw na Markdown, potem na Catalę, czyli język rules-as-code z Inrii. Układ katalogów odwzorowuje hierarchię źródeł prawa: konstytucja, ustawy, umowy międzynarodowe, rozporządzenia, akty prawa miejscowego.
- [PolskiAgentW](https://github.com/PolskiAgentW) - 🟢 Akty, które API Sejmu daje tylko w PDF, w Markdown i JSON: Dziennik Ustaw od 2025 r. (w tym teksty jednolite kodeksów) i Monitor Polski od 2012 r., aktualizowane codziennie, a także akty z lat 1918–2011, których API nie ma w HTML, w trzech zbiorach po dekadach; roczniki sprzed 2000 r. pochodzą z OCR skanów (stan 15.10.2026). Każdy zbiór leży też jako Parquet na Hugging Face. Tekst pochodzi z nieoficjalnej konwersji, wiążący pozostaje PDF; konwerter eli2md ma licencję MIT.
- [nalegaluorg/nalegalu](https://github.com/nalegaluorg/nalegalu) - 🟢 Zestawia akty z Dziennika Ustaw w Markdown z orzecznictwem z bazy SAOS. Przy każdym akcie stoi liczba powiązanych orzeczeń, więc od razu widać, które ustawy sądy cytują najczęściej. Osobna strona pod adresem [nalegalu.org](https://nalegalu.org).
- [Sarverott/P-jol-roll](https://github.com/Sarverott/P-jol-roll) - 🟢 Pobiera akty z Dziennika Ustaw i przerabia je na Markdown, oczyszczony z elementów strony. Wynik leży na Hugging Face jako [zbiór danych](https://huggingface.co/datasets/Sarverott/polish_national_law_docs), obok surowych plików i podglądu online. Kod ma licencję AGPL, zbiór nie ma wskazanej licencji.

### Konektory i klienty

- [numikel/law-scrapper-mcp](https://github.com/numikel/law-scrapper-mcp) - ⚪ Pobiera i analizuje akty prawne przez API Sejmu, jako serwer MCP.
- [leniwyposel/sejm-mcp](https://github.com/leniwyposel/sejm-mcp) - 🟢 Serwer MCP do API Sejmu i bazy aktów prawnych ELI.
- [janisz/sejm-mcp](https://github.com/janisz/sejm-mcp) - 🟢 Wystawia przez MCP i prace Sejmu, i akty prawne: posłów, komisje, głosowania oraz interpelacje z API Sejmu, a dokumenty z bazy ELI. Napisany w Go.
- [ObywatelTB/prawmi-mcp](https://github.com/ObywatelTB/prawmi-mcp) - 🟢 Lokalna nakładka stdio na zdalny serwer PrawMi, udostępniająca polskie akty prawne.
- [jamarpl21/prawo-pl-eli](https://github.com/jamarpl21/prawo-pl-eli) - 🟢 Prawo polskie i unijne z oficjalnych źródeł, czyli ELI Sejmu oraz CELLAR i EUR-Lex, wystawione jako agent skills. Od wersji 2.2 (październik 2026) osiem skilli, w tym Portal Orzeczeń MS, dzienniki urzędowe województw, CBOSA, UODO i Centralny Rejestr Umów.
- [apiotrowski-afk/legal-cite-pl](https://github.com/apiotrowski-afk/legal-cite-pl) - 🟢 Serwer MCP, który sprawdza aktualne brzmienie przepisu polskiego i unijnego prosto ze źródła. Ten sam utrzymujący wydaje weryfikację podmiotów w KRS i na białej liście VAT oraz pamięć trwałą dla asystentów.
- [matematicsolutions](https://github.com/matematicsolutions) - 🟢 Seria serwerów MCP z weryfikowalnymi cytowaniami: SAOS, NSA i szesnaście WSA przez CBOSA, KIO, KRS, Dziennik Ustaw z Monitorem Polskim oraz interpretacje podatkowe z EUREKI. Wydaje też silnik anonimizacji, serwer nad korpusem legalize, infrastrukturę wiedzy prawnej *Repertorium* oraz dwa huby skilli prawniczych, polski i angielski. Ten sam autor utrzymuje konektory ELI dla Niemiec, Francji, Holandii, Słowacji, Turcji, USA i Singapuru.

- [Luzgan/lupa-na-prawo](https://github.com/Luzgan/lupa-na-prawo) - ⚪ Przeszukuje prawo polskie semantycznie i śledzi prace Sejmu oraz Senatu, jako serwer MCP.
- [operatorit/Polish_law_updates_notifier](https://github.com/operatorit/Polish_law_updates_notifier) - ⚪ Automat N8N, który powiadamia o nowelizacjach wybranych aktów.
- [karolpolikarp/ISAP-scraper](https://github.com/karolpolikarp/ISAP-scraper) - ⚪ Pobiera pełne teksty z Dziennika Ustaw i Monitora Polskiego przez API ELI, a śledzone akty trzyma pod obserwacją i melduje zmiany. Ten sam utrzymujący wydaje [Parawan](https://github.com/karolpolikarp/parawan), anonimizator danych osobowych w jednym pliku HTML, który działa w przeglądarce bez połączenia z siecią.
- [ad-m/cbosa](https://github.com/ad-m/cbosa) - ⚪ Przeszukuje CBOSA trzy razy dziennie pod kątem spraw o symbolu 648, czyli dostępu do informacji publicznej, i rozsyła powiadomienia na grupę dyskusyjną.
- [artsiom-andrasovich/polish_law_viewer](https://github.com/artsiom-andrasovich/polish_law_viewer) - ⚪ Przeszukuje akty przez API Sejmu z aplikacji desktopowej w Pythonie i otwiera dokumenty w systemowej przeglądarce PDF.
- [PiotrKantorowski](https://github.com/PiotrKantorowski) - 🟢 [Dziennik upadłościowy](https://github.com/PiotrKantorowski/dziennik-upadlosciowy) monitoruje kontrahentów w KRS, Krajowym Rejestrze Zadłużonych i Monitorze Sądowym i Gospodarczym. [CSM for Word](https://github.com/PiotrKantorowski/csm-for-word) pseudonimizuje polskie dokumenty lokalnie i odwracalnie, wprost w Wordzie. [Naturalne pisanie](https://github.com/PiotrKantorowski/naturalne-pisanie) to skill redakcyjny, który usuwa maniery stylu AI tylko wtedy, gdy się powtarzają, a w tekstach prawniczych pilnuje drogi od tezy przez podstawę i zastosowanie do skutku.
- [soba-labs/krs-mcp](https://github.com/soba-labs/krs-mcp) - 🟢 Szuka spółek w KRS po nazwie, numerze KRS, NIP albo REGON i pobiera urzędowe odpisy. Cztery narzędzia wyłącznie do odczytu, bez klucza i bez konta.
- [pkolawa/krs-poland-mcp-server](https://github.com/pkolawa/krs-poland-mcp-server) - 🟢 Udostępnia publiczne API KRS przez MCP. Uruchamia się przez `npx`, więc nie wymaga instalacji.
- [pwr-ai/JuDDGES](https://github.com/pwr-ai/JuDDGES) - 🟢 Projekt badawczy AI@PWr nad przetwarzaniem orzeczeń: gromadzenie, kodowanie i udostępnianie danych sądowych dla Polski oraz Anglii i Walii. [Aplikacja towarzysząca](https://github.com/pwr-ai/juddges-app) pozwala przeszukiwać i analizować wyroki; całość ma DOI w Zenodo.
- [pawelojdowski/uodo-mcp](https://github.com/pawelojdowski/uodo-mcp) - ⚪ Przeszukuje i analizuje decyzje Prezesa UODO, jako serwer MCP. Pokrywa źródło, którego nie obsługuje żaden inny konektor z tej listy.
- [PawelHaracz/polish-caselaw-mcp](https://github.com/PawelHaracz/polish-caselaw-mcp) - 🟢 Udostępnia polskie orzecznictwo przez protokół MCP.
- [pielas-activy/znajdz-ksiege-wieczysta](https://github.com/pielas-activy/znajdz-ksiege-wieczysta) - 🟢 Ustala numer księgi wieczystej mieszkania na podstawie samego adresu budynku, korzystając z darmowej przeglądarki Ministerstwa Sprawiedliwości. Skill dla Claude Code i Cowork.
- [danielmskuza-blip/Orzeczenia-MS](https://github.com/danielmskuza-blip/Orzeczenia-MS) - 🟢 Udostępnia orzeczenia sądów powszechnych z portalu Ministerstwa Sprawiedliwości.
- [Iskra-YT/sejmium](https://github.com/Iskra-YT/sejmium) - 🟢 Śledzi prace parlamentu na API Sejmu. Przydaje się, gdy trzeba wychwycić nowelizację, zanim trafi do Dziennika Ustaw.
- [legaion/mcp-verifier](https://github.com/legaion/mcp-verifier) - ⚪ Waliduje serwery MCP dla polskiego prawa: dokumentację, schematy narzędzi i zgodność odpowiedzi.
- [LK-Technology/prawnik-mcp](https://github.com/LK-Technology/prawnik-mcp) - 🟢 Serwer MCP, który podaje brzmienie przepisu na wskazany dzień z ELI Sejmu i EUR-Lex oraz orzeczenia z SAOS, SN, TK, KIO, UODO, EUREKI i CBOSA. Zanim asystent odpowie, sprawdza każdy cytat w źródle; zmyślony fragment blokuje eksport pisma.
- [umowyai/polskie-prawo](https://github.com/umowyai/polskie-prawo) - 🔵 Plugin dla Claude Code, ChatGPT i innych klientów MCP nad zdalnym serwerem Umowy.AI: ustawy i rozporządzenia z Dziennika Ustaw w pełnym brzmieniu, także na wskazany dzień, ze statusem obowiązywania sprawdzanym codziennie w ELI. Serwer wymaga logowania e-mailem, w repozytorium są skille i wpis do rejestru MCP.
- [pawelknorps](https://github.com/pawelknorps) - 🟢⚪ Seria serwerów MCP z dziennikiem audytu wywołań. [tk-mcp](https://github.com/pawelknorps/tk-mcp) przeszukuje orzeczenia Trybunału Konstytucyjnego, czytając HTML strony TK, bo Trybunał nie ma API. [echr-mcp](https://github.com/pawelknorps/echr-mcp) sięga do HUDOC po orzeczenia ETPC, a [sejm-process-mcp](https://github.com/pawelknorps/sejm-process-mcp) śledzi proces legislacyjny i druki sejmowe. Licencję Apache ma tylko tk-mcp.
- [TheBeardedPole/sejmomat](https://github.com/TheBeardedPole/sejmomat) - 🟢 Wiąże każde głosowanie nad poprawką z jej treścią, autorem i rekomendacją komisji, a wynik rozkłada na kluby, razem z posłami głosującymi wbrew klubowi. Teksty jednolite nowelizowanych aktów pobiera z ELI.
- [sobolevbel/lexinform](https://github.com/sobolevbel/lexinform) - 🟢 Wyławia projekty ustaw ważne dla cudzoziemców w Polsce i prowadzi je od konsultacji w RCL do publikacji w Dzienniku Ustaw. Streszczenia z oceną wagi od 1 do 5 publikuje na Telegramie, po rosyjsku.

### Standardy i formaty

- [apiotrowski-afk/okf-legal](https://github.com/apiotrowski-afk/okf-legal) - 🟢 Profil prawniczy nad Open Knowledge Format: jednostka pod-dokumentowa z dosłownym cytatem, kierunkiem i statusem ratio albo obiter, relacje typowane, reguły antyhalucynacyjne.
- [ELI](https://eur-lex.europa.eu/eli-register/about.html) - 🔵 European Legislation Identifier, identyfikator używany przez API Sejmu.
- [Akoma Ntoso](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html) - 🔵 Standard OASIS dla aktów prawnych, w Polsce niewdrożony.
- [e-sad/dokumentacja](https://github.com/e-sad/dokumentacja) - 🟢 Porządkuje dokumentację techniczną usługi sieciowej elektronicznego postępowania upominawczego, czyli definicję WSDL i schematy XSD. Przydaje się powodom masowym i pełnomocnikom, którzy składają pozwy w EPU z własnego systemu, bez interfejsu WWW.

## Narzędzia i skille prawnicze

- [michaleiatrak-star/Lex-Machina](https://github.com/michaleiatrak-star/Lex-Machina) - 🟢 Analizuje prawo i umowy, przygotowuje pisma procesowe i ocenia ryzyka w szesnastu dziedzinach prawa. Zabrania cytowania przepisów z pamięci. Istnieje [port na OpenAI Codex](https://github.com/tittlepl-baj-jk/Lex-Machina-for-OpenAI-Codex), a od września 2026 także [aplikacja desktopowa](https://github.com/michaleiatrak-star/Lex-machina-aplikacja) w Tauri, z kodem zastrzeżonym.
- [crankshift/lawpowers](https://github.com/crankshift/lawpowers) - 🟢 Monorepo wtyczek prawniczych z podziałem na jurysdykcje, z wtyczką polską liczącą **22 skille**: przedawnienie, odsetki ustawowe, opłata sądowa, wartość przedmiotu sporu, alimenty, orzecznictwo frankowe, procedury ZUS, USC i cudzoziemców, jurysdykcja, konwencja nowojorska, przegląd umów B2B, nieruchomościowych i pojazdowych. Druga wtyczka obejmuje prawo ukraińskie.
- [trosinski08/ai_agent_compliance](https://github.com/trosinski08/ai_agent_compliance) - ⚪ Analizuje sprawy AML i KYC w architekturze RAG, indeksując polskie przepisy o przeciwdziałaniu praniu pieniędzy wraz z materiałami GIIF i KNF.
- [miskibin](https://github.com/miskibin) - ⚪ [Asystent RP](https://github.com/miskibin/asystent-rp) odpowiada obywatelom na pytania o prawo polskie i działa publicznie pod adresem chat.sejm-stats.pl. [Tygodnik sejmowy](https://github.com/miskibin/tygodnik-sejmowy) streszcza, co dzieje się w Sejmie. Oba korzystają z danych sejm-stats, które opisujemy w [ARCHIWUM.md](ARCHIWUM.md).
- [matematicsolutions/patron](https://github.com/matematicsolutions/patron) - 🟢 Agent dla kancelarii do samodzielnego hostowania. Prowadzi ślad audytowy w łańcuchu skrótów pod art. 12 AI Act, korzysta z własnego modelu i ma dziewięć edycji językowych. Ten sam utrzymujący wydaje pakiety skilli prawniczych, warstwę weryfikacji wyjścia modelu i ocenę gotowości kancelarii na AI.
- [apiotrowski-afk/commercial-legal-pl](https://github.com/apiotrowski-afk/commercial-legal-pl) - 🟢 Redaguje i analizuje umowy B2B, IT oraz IP. Zawiera bazę klauzul, bazę wiedzy doktrynalnej i kontrolę spójności odesłań wewnętrznych.
- [apiotrowski-afk/kancelaria-dms](https://github.com/apiotrowski-afk/kancelaria-dms) - 🟢 Prowadzi obieg dokumentów i CRM kancelarii natywnie w Google Workspace, na własnym serwerze.
- [andrii-mazurchuk/kontrakt-guard](https://github.com/andrii-mazurchuk/kontrakt-guard) - 🟢 Audytuje umowę o pracę klauzula po klauzuli na podstawie tekstów jednolitych prawa pracy. Każdy znaleziony przepis przechodzi ocenę trafności, a odpowiedź powstaje tylko z tego, co ją przeszło — bez podstawy w korpusie narzędzie odmawia zamiast zgadywać. Ma własny dwuwarstwowy zestaw testów jakości.
- [pawelkwaczynski](https://github.com/pawelkwaczynski) - 🟢 Dwa projekty wokół aktualności prawa. [stillaw](https://github.com/pawelkwaczynski/stillaw) sprawdza deterministycznie, czy przepis nadal obowiązuje. [staleness-warnings-pl](https://github.com/pawelkwaczynski/staleness-warnings-pl) mierzy w prerejestrowanym badaniu, czy modele same ostrzegają o nieaktualności; udostępnia kod, prompty, zamrożone fragmenty i sumy kontrolne, ale klucz odpowiedzi zatrzymuje celowo.
- [a-szczudlo](https://github.com/a-szczudlo) - ⚪ Seria otwartych audytorów Creativa Legal, każdy jako skill dla Claude, ChatGPT i Codeksa. [OpenNDA](https://github.com/a-szczudlo/OpenNDA) ocenia umowę o poufności w trzynastu punktach kontrolnych z flagami ryzyka, cross-checkiem spójności i porównaniem wersji po poprawkach. Obok niego [OpenFounders](https://github.com/a-szczudlo/OpenFounders) testuje relacje wspólników sp. z o.o., [OpenGDPR](https://github.com/a-szczudlo/OpenGDPR) skanuje zgodność z RODO, a osobny audytor bierze umowy marketingowe.
- [DawidZabek/leaseguard](https://github.com/DawidZabek/leaseguard) - ⚪ Analizuje wklejoną umowę najmu mieszkania z perspektywy najemcy i wskazuje postanowienia niekorzystne.
- [dominikloza/lawer-up](https://github.com/dominikloza/lawer-up) - ⚪ Pozwala wgrać umowę i rozmawiać o niej z asystentem, z naciskiem na wykrywanie ukrytych ryzyk.
- [emilpinski/lexaro](https://github.com/emilpinski/lexaro) - ⚪ Odpowiada na pytania o prawo polskie w architekturze RAG: HyDE, wyszukiwanie hybrydowe na pgvector i BM25, rerank i cache semantyczny. Działa pod adresem lexaro.pl.
- [PrzemoPle/zalaczniki](https://github.com/PrzemoPle/zalaczniki) - 🟢 Aplikacja macOS, która ze skanów buduje listę załączników do pozwu, rozpoznając tekst lokalnie.
- [Inexpli/Radca-prawny-AI](https://github.com/Inexpli/Radca-prawny-AI) - 🟢 Odpowiada na pytania prawne w architekturze RAG, w całości lokalnie na GPU.
- [jakatora/kredyt-ai](https://github.com/jakatora/kredyt-ai) - ⚪ Analizuje umowy kredytowe pod prawem polskim.
- [rodorn](https://github.com/rodorn) - 🟢 [Klient e-Doręczeń](https://github.com/rodorn/edoreczenia-klient) obsługuje interfejs UA API w Pythonie, nieoficjalnie. [Radar przetargów](https://github.com/rodorn/fluxlab-przetargi-radar) śledzi zamówienia publiczne.
- [tomkolp/e-doreczenia-wizualizacja-EPO](https://github.com/tomkolp/e-doreczenia-wizualizacja-EPO) - ⚪ Wizualizuje elektroniczne potwierdzenie odbioru.
- [mTylewski/dora](https://github.com/mTylewski/dora) - ⚪ Sprawy o kary umowne za opóźnienie dewelopera: z umowy, aneksów i protokołu odbioru wyciąga terminy, cenę i stawkę kary, każdą wartość z cytatem i numerem strony, a karę liczy deterministyczny kod z testami. Flaguje klauzule abuzywne i składa wezwanie do zapłaty w DOCX na szablonie kancelarii; PDF jest anonimizowany w przeglądarce, zanim opuści komputer.
- [marianwitkowski/generator-umow-o-dzielo](https://github.com/marianwitkowski/generator-umow-o-dzielo) - ⚪ Skill dla Claude Code, który z opisu w rozmowie składa komplet do umowy o dzieło z przeniesieniem praw do programu komputerowego: umowę ze specyfikacją i kryteriami odbioru, protokół odbioru i rachunek z wyliczeniem kosztów, zaliczki i składek, w jednym PDF. Działa też bez Claude, jako skrypt.
- [wisniabobo](https://github.com/wisniabobo) - 🟢 Trenażery egzaminacyjne z [prawa konstytucyjnego](https://github.com/wisniabobo/Prawo-konstytucyjne), [administracyjnego](https://github.com/wisniabobo/Prawo-administracyjne) i [doktryn polityczno-prawnych](https://github.com/wisniabobo/doktryny-polityczno-prawne): fiszki z powtórkami SM-2, testy z wyjaśnieniami, kazusy i symulator egzaminu, bez konta i offline. Cytowane przepisy pobiera skrypt z API ELI, więc nie starzeją się po nowelizacji. Kod na MIT, treści CC BY-SA.
- [appliedai-pl/polish-law-checker](https://github.com/appliedai-pl/polish-law-checker) - 🟢 Skill dla Claude Code, który sprawdza cytowania przepisów w gotowym piśmie, także w DOCX, z API ELI. Wskazuje nieaktualny tekst jednolity, zmiany po obwieszczeniu i przepisy uchylone, a przy każdym cytacie podaje dowód ze źródła i poprawkę.
- [mhajder/pyekw](https://github.com/mhajder/pyekw) - 🟢 Biblioteka Pythona do numerów ksiąg wieczystych: sprawdza cyfrę kontrolną i kod wydziału z wykazu ponad 350 sądów, wyłuskuje numery z tekstu i podpowiada poprawny numer przy literówce. Nie ma zależności.
- [b44x/edoreczenia-php](https://github.com/b44x/edoreczenia-php) - 🟢 Nieoficjalne SDK e-Doręczeń w PHP: uwierzytelnienie system-system, wyszukiwarka adresów i obsługa skrzynki. Autor zaznacza, że nie sprawdził go jeszcze na środowiskach INT i PROD.
- [GSkuza/AI-Legal-SkillsPL](https://github.com/GSkuza/AI-Legal-SkillsPL) - 🟢 Sześć pakietów skilli do prawa polskiego i unijnego: analiza czystości patentowej, kontradyktoryjna ocena argumentacji, analiza struktury rozumowania, śledzenie zmian prawa, hipotezy konkurencyjne z macierzą dowodów i wyszukiwanie orzeczeń.
- [Volers321/tsl-case-law](https://github.com/Volers321/tsl-case-law) - 🟢 Spory przewozowe i spedycyjne: szuka podobnych wyroków w SAOS i prognozuje wynik sporu, widząc wyłącznie stan faktyczny, bez sentencji i oceny sądu. Na 1080 sprawach porównuje modele z ocenami praktyka branży i podaje miary niepewności.
- [LateMigo/transport_skill](https://github.com/LateMigo/transport_skill) - ⚪ Baza wiedzy dla Claude Code z polskiego i unijnego prawa transportu drogowego: CMR, prawo przewozowe, czas pracy kierowców, pakiet mobilności, SENT i ADR, ze skryptem odświeżającym teksty.
- [tomaszkrawczyk-cmd/foodlaw.ai](https://github.com/tomaszkrawczyk-cmd/foodlaw.ai) - 🟢 Prawo żywnościowe polskie i unijne dla asystentów AI: opisy rozporządzeń i ustaw, skille dla poszczególnych obszarów i skrypty, które pobierają akty i orzeczenia z EUR-Lex, ISAP, CBOSA i CURIA.
- [marduk112/RAG-LoRA---kadry-i-place](https://github.com/marduk112/RAG-LoRA---kadry-i-place) - 🟢 Asystent kadrowo-płacowy działający lokalnie: Bielik dostrojony przez LoRA, a fakty z przepisów o pracy, ZUS, PIT i PPK dobiera wyszukiwanie w pobranych ustawach. Dziennik budowy opisuje pułapki krok po kroku.
- [konraddre/precyzyjny-paragraf](https://github.com/konraddre/precyzyjny-paragraf) - ⚪ Odpowiada na pytania tylko z tekstów jednolitych siedmiu kodeksów, od KC po KSH, i pokazuje brzmienie powołanych artykułów. Wyszukiwanie jest hybrydowe, odpowiedź pisze Gemini 2.5 Flash.
- [ErykMikolajewicz/prawobiorca](https://github.com/ErykMikolajewicz/prawobiorca) - 🟢 Wyszukiwarka przepisów dla studentów dochodzących swoich praw na uczelni, z teczkami spraw i generowaniem wniosków w DOCX. Rozwija ją koło naukowe Politechniki Wrocławskiej, działa pod adresem prawobiorca.pl.

## Anonimizacja dokumentów

Wszystkie przetwarzają dokument lokalnie, zanim trafi on do modelu. Bez tej warstwy praca z AI na aktach klienta nie domyka się od strony tajemnicy zawodowej.

- [paszkiewiczmichal/poufnik](https://github.com/paszkiewiczmichal/poufnik) - 🟢🟠 Aplikacja desktopowa w Tauri z silnikiem Presidio jako sidecar. Wczytuje PDF, DOCX i skany, rozpoznaje tekst lokalnie, pozwala przejrzeć każde wykrycie i eksportuje dokument z odwracalnymi tokenami. Poziom Basic jest darmowy i nie wymaga konta. Ten sam utrzymujący wydaje [skille dla Claude Code zoptymalizowane pod polszczyznę](https://github.com/paszkiewiczmichal/claude-skills-pl).
- [studiogo/cenzor](https://github.com/studiogo/cenzor) - 🟢 Zastępuje dane tokenami przed wysłaniem do modelu i podstawia je z powrotem w odpowiedzi. Publikuje zmierzoną skuteczność razem z metodą pomiaru.
- [apiotrowski-afk/anon-legal-pl](https://github.com/apiotrowski-afk/anon-legal-pl) - 🟢 Wykrywa dane osobowe przez Presidio i spaCy, sprawdza sumy kontrolne numerów PESEL, NIP i REGON oraz rozpoznaje wzorce sygnatur sądowych. Opcjonalnie rozpoznaje tekst ze skanów.
- [empios](https://github.com/empios) - 🟢⚪ [humanize-pl](https://github.com/empios/humanize-pl) redaguje polskie teksty prawnicze regułowo, bez modelu językowego, ze ścieżką ostrożną dla umów, opinii, pism i regulaminów. [humanizer-polish](https://github.com/empios/humanizer-polish) to skill dla Claude, który usuwa trzydzieści wzorców stylu AI, nie ruszając liczb, przepisów ani modalności. Autor zastrzega przy obu, że nie służą obchodzeniu detektorów AI.
- [LachPawel/Lethe](https://github.com/LachPawel/Lethe) - ⚪ Łączy wyrażenia regularne na danych strukturalnych z modelem PLLuM na rozpoznawaniu kontekstowym. Obsługuje dwadzieścia cztery kategorie danych i polską fleksję, przez API REST albo wiersz poleceń.
- [DawidBochno/Anonimizacja-RODO](https://github.com/DawidBochno/Anonimizacja-RODO) - ⚪ Program desktopowy, który lokalnie czyści DOCX, PDF, skany i zdjęcia z PESEL, NIP, REGON, numerów dowodu, IBAN, adresów e-mail i telefonów, z kontrolą sum kontrolnych i własną listą słów. Powstał pod publikację w BIP i odpowiedzi na wnioski o informację publiczną.
- [quiris11/Anonimizator-PDF](https://github.com/quiris11/Anonimizator-PDF) - 🟢 Jeden plik HTML, który zaczernia PDF trwale: każda strona wyniku jest obrazem, więc zakrytego tekstu nie da się odzyskać. Polityka CSP blokuje wszelkie połączenia sieciowe, a build jest powtarzalny co do bajtu.
- [BartoszRadziszewski/anonimizator](https://github.com/BartoszRadziszewski/anonimizator) - 🟢 Jeden plik HTML z trzema trybami: etykiety odwracalne kluczem sesji, dane fikcyjne z poprawnymi sumami kontrolnymi i trwałe zaczernienie. Dokument nie opuszcza przeglądarki, ale biblioteki i fonty ładują się z sieci przy otwarciu.
- [MaciejKlepacki/mama_anonimizacja](https://github.com/MaciejKlepacki/mama_anonimizacja) - ⚪ Zamienia DOCX i PDF z warstwą tekstową na Markdown z placeholderami, na Presidio i spaCy. Każde trafienie ma poziom pewności, a wątpliwe zatwierdza człowiek. Rozpoznaje też numery działek, ksiąg wieczystych i znaki spraw.
- [mikolaj92/anonimizator3000](https://github.com/mikolaj92/anonimizator3000) - 🟢 Portal do lokalnej anonimizacji dokumentów: Presidio z polskimi walidatorami i opcjonalnym modelem GLiNER. Ostatni krok usuwa tożsamość autorów z metadanych DOCX.

## Modele, korpusy, benchmarki

- [speakleash](https://github.com/speakleash) - 🟢 Rozwija Bielika, polski model językowy, razem z korpusami i narzędziami. Wagi modeli leżą na Hugging Face, a w repozytoriach są tutoriale, dostęp do korpusów i oprzyrządowanie.
- [PLLuM](https://pllum.clarin-pl.eu) - 🟢 Polski model językowy budowany ze środków publicznych. Korzysta z niego między innymi Lethe.

- [spaCy pl_core_news_lg](https://spacy.io/models/pl) - 🟢 Rozpoznaje jednostki nazwane w polszczyźnie. Opiera się na nim większość narzędzi z sekcji o anonimizacji.
- [cloudforge1/PaddleOCR-VL-For-Polish](https://github.com/cloudforge1/PaddleOCR-VL-For-Polish) - 🟢 Model OCR dostrojony do polskich dokumentów współczesnych i historycznych. Przydaje się tam, gdzie akta istnieją wyłącznie jako skan.
- [brokeboiflex/nodeusz](https://github.com/brokeboiflex/nodeusz) - ⚪ Natywne wiązania Node.js do analizatora morfologicznego Morfeusz2. Odmiana polskich nazwisk i nazw to warunek działania anonimizacji.
- [JuDDGES na Hugging Face](https://huggingface.co/JuDDGES) - 🟡 Korpusy orzeczeń: [`pl-court-raw`](https://huggingface.co/datasets/JuDDGES/pl-court-raw) z pełną treścią wyroków z portalu Ministerstwa Sprawiedliwości wraz z metadanymi oraz [`pl-appealcourt-criminal`](https://huggingface.co/datasets/JuDDGES/pl-appealcourt-criminal) — 6050 wyroków karnych sądów apelacyjnych z lat 2003–2024.
- [PiotrSty na Hugging Face](https://huggingface.co/PiotrSty) - 🟡 Trzy korpusy: [orzeczenia w sprawach zamówień publicznych](https://huggingface.co/datasets/PiotrSty/uzp-orzeczenia-pl) z oficjalnej wyszukiwarki UZP, czyli KIO, sądy okręgowe, sądy apelacyjne i Sąd Najwyższy, [decyzje Prezesa UODO](https://huggingface.co/datasets/PiotrSty/uodo-orzeczenia-pl) od 2018 roku oraz [orzeczenia z SAOS](https://huggingface.co/datasets/PiotrSty/saos-polish-court-judgments), od stu tysięcy do miliona pozycji z publicznego zrzutu API. Ostatni z nich nie ma wskazanej licencji.
- [Alght/Bielik-RAG](https://github.com/Alght/Bielik-RAG) - ⚪ Bada skuteczność klasyfikacji polskich tekstów prawnych w architekturze RAG na modelu Bielik.
- [PiotrTyrakowski/PolishLawLLM-Benchmark](https://github.com/PiotrTyrakowski/PolishLawLLM-Benchmark) - ⚪ Sprawdza modele językowe na prawie polskim.
- [matgier/orzeczenia-tezy-dashboard](https://github.com/matgier/orzeczenia-tezy-dashboard) - ⚪ Porównuje, jak Gemma 4 31B, Qwen3 32B i Bielik 11B v3 wydobywają tezy z uzasadnień orzeczeń, z walidatorem dziewięciu kryteriów. Obok stoi wyszukiwarka 262 orzeczeń z 1196 potwierdzonymi tezami i graf tez z siecią cytowań SAOS.

## Poza progiem świeżości

Pozycje bez commita od ponad roku albo z zarchiwizowanym repozytorium trzymamy w osobnym pliku [ARCHIWUM.md](ARCHIWUM.md), razem z datą ostatniego commita. Nie znikają, bo dla zbiorów danych i modeli brak commitów nie oznacza porzucenia, a wytyczne awesome każą trzymać je poza listą główną.

## Footnotes

Katalog prowadzi [Adam Piotrowski](https://github.com/apiotrowski-afk), radca prawny. Część wpisów to jego własne projekty. Opisuje je tym samym schematem, tymi samymi polami automatycznymi i tą samą regułą *jeden utrzymujący, jeden wpis*. Kryterium włączenia: publicznie dostępne, dotyczy polskiego prawa, działa.

Powiązana lista: [ksefuj/awesome-ksef](https://github.com/ksefuj/awesome-ksef) kataloguje narzędzia KSeF, czyli warstwę, której ten katalog świadomie nie obejmuje.

Licencja katalogu, czyli opisów, struktury i skryptów, to [CC BY 4.0](LICENSE). Nie obejmuje projektów, do których katalog odsyła: każdy ma własną licencję, wskazaną przy wpisie.
