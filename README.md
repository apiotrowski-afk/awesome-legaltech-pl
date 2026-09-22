# Prawo w kodzie

> Polskie narzędzia, dane i modele dla prawa — otwarte i półotwarte.
> Każdy wpis mówi, **na jakich warunkach można tego użyć w kancelarii**.

Katalog obejmuje narzędzia, których przedmiotem jest **samo prawo**: akty prawne,
orzecznictwo, umowy, procedura i praktyka kancelaryjna. Nie obejmuje operacji
podatkowo-księgowych — KSeF, JPK i rejestry gospodarcze mają własne, liczne
i dobrze utrzymane ekosystemy.

## Zasady

**Pola automatyczne stwierdzają, pola ręczne opisują.** Gwiazdki, data ostatniego
commita, flaga `archived` i licencja pochodzą z API GitHuba i noszą datę odczytu.
Katalog nie pisze „porzucony" ani „martwy" — podaje datę i zostawia wniosek
czytelnikowi. [`sprawdz_zywotnosc.py`](sprawdz_zywotnosc.py) odświeża te pola co tydzień.

**Opisy własne.** Piszemy po otwarciu repo. Nie kopiujemy `description` ani README.

**Jeden utrzymujący = jeden wpis.** Serię powiązanych repo opisujemy w jednej
linii. Lista ma pokazywać krajobraz, nie czyjś dorobek.

**Chcesz zniknąć z listy** → zgłoś issue, usuwamy bez pytania o powód.

## Skala otwartości

| | Znaczenie |
|---|---|
| 🟢 | **kod otwarty** — repo + licencja OSI |
| 🟡 | **źródło otwarte, narzędzie zamknięte** — dane publiczne, software nie |
| 🔵 | **API publiczne** — dostęp otwarty, bez licencji OSS |
| 🟠 | **komercyjne z progiem** — freemium / darmowy tier |
| ⚪ | **licencja nieokreślona** — brak pliku LICENSE; to nie znaczy „wolno", tylko pełne prawo autorskie autora |

W polskim prawie najwięcej wartości siedzi w 🟡 i 🔵 — otwarte dane bez otwartego
narzędzia. Katalogi anglosaskie tej kategorii nie mają, bo tam problem wygląda inaczej.

---

## 1. Źródła prawa i orzecznictwo

### Dane i API państwowe

- **API Sejmu / ELI** 🔵 — `api.sejm.gov.pl`. Akty z Dz.U. i M.P., teksty jednolite, datowane listy aktów zmieniających. Tekst HTML jest strukturalny: każda jednostka redakcyjna ma stabilny identyfikator (`arti_353_1`), więc podział na artykuły jest deterministyczny
- **SAOS** 🔵 — orzecznictwo sądów powszechnych, SN i wojskowych, `saos.org.pl`
- **CBOSA** 🔵 — sądy administracyjne, `orzeczenia.nsa.gov.pl`
- **Orzeczenia KIO** 🔵 — zamówienia publiczne, `orzeczenia.uzp.gov.pl`
- **EUREKA** 🔵 — interpretacje podatkowe
- **Rejestr klauzul niedozwolonych UOKiK** 🟡 — archiwalne wyroki SOKiK; obecnie udostępniany w wersji zanonimizowanej. Przed powołaniem się sprawdź aktualny status prawny rejestru, bo zmienił się w 2026 r.

### Akty prawne jako dane

- [`kbchojnacki`](https://github.com/kbchojnacki) ⚪ — **15 repozytoriów: każdy polski kodeks i Konstytucja jako historia gita, gdzie jeden commit = jedna nowelizacja w dacie wejścia w życie.** `git blame` na przepisie pokazuje, kiedy zmieniło się brzmienie. Źródło: ISAP / API Sejmu. ⚠ Okres przed pierwszym tekstem jednolitym jest rekonstruowany, nie cytowany — autor zaznacza to wprost
- [`andilabs/polish-law`](https://github.com/andilabs/polish-law) 🟢 MIT + [`polish-law-data`](https://github.com/andilabs/polish-law-data) ⚪ — historia prawa polskiego od 1918
- [`apatryda/polish-law`](https://github.com/apatryda/polish-law) 🟢 GPL-3.0 — akty prawne tłumaczone najpierw na Markdown, potem na **Catala** (język rules-as-code z Inrii); układ katalogów wg hierarchii źródeł prawa: konstytucja, ustawy, umowy międzynarodowe, rozporządzenia, akty prawa miejscowego
- [`KrzysztofBogdan/Kodeks_cywilny`](https://github.com/KrzysztofBogdan/Kodeks_cywilny) 🟢 MIT — k.c. jako tekst w repo

### Konektory i klienty

- [`numikel/law-scrapper-mcp`](https://github.com/numikel/law-scrapper-mcp) — serwer MCP nad API Sejmu: pobieranie i analiza aktów
- [`jamarpl21/prawo-pl-eli`](https://github.com/jamarpl21/prawo-pl-eli) 🟢 MIT — prawo polskie i unijne z oficjalnych źródeł (ELI Sejmu + CELLAR/EUR-Lex), wystawione jako agent skills
- [`apiotrowski-afk/legal-cite-pl`](https://github.com/apiotrowski-afk/legal-cite-pl) 🟢 Apache-2.0 — serwer MCP weryfikujący aktualne brzmienie przepisu PL/UE prosto ze źródła; ten sam utrzymujący ma `krs-verify` (KRS + biała lista VAT) i pamięć trwałą dla asystentów
- [`matematicsolutions`](https://github.com/matematicsolutions) 🟢 MIT/Apache-2.0 — seria serwerów MCP z weryfikowalnymi cytowaniami: SAOS, NSA i 16 WSA przez CBOSA, KIO, KRS, prawo polskie; ten sam autor utrzymuje konektory ELI dla DE, FR, NL, SK, TR, US i SG
- [`miskibin/sejm-stats`](https://github.com/miskibin/sejm-stats) — baza i serwis o pracach Sejmu, na którym stoi `asystent-rp`
- [`Ansvar-Systems/polish-law-mcp`](https://github.com/Ansvar-Systems/polish-law-mcp) — baza przepisów o ochronie danych i cyberbezpieczeństwie ⚠ archived
- [`Luzgan/lupa-na-prawo`](https://github.com/Luzgan/lupa-na-prawo) ⚪ — wyszukiwanie semantyczne w prawie polskim plus śledzenie prac Sejmu i Senatu, jako serwer MCP
- [`operatorit/Polish_law_updates_notifier`](https://github.com/operatorit/Polish_law_updates_notifier) — automat N8N powiadamiający o nowelizacjach wybranych aktów
- [`ad-m/cbosa`](https://github.com/ad-m/cbosa) ⚪ — automat przeszukujący CBOSA trzy razy dziennie pod kątem spraw o symbolu 648 (dostęp do informacji publicznej) i rozsyłający powiadomienia na grupę dyskusyjną
- [`artsiom-andrasovich/polish_law_viewer`](https://github.com/artsiom-andrasovich/polish_law_viewer) ⚪ — aplikacja desktopowa (Python, customtkinter) do przeszukiwania aktów przez API Sejmu, z otwieraniem PDF-ów w systemowej przeglądarce

### Standardy i formaty

- [`apiotrowski-afk/okf-legal`](https://github.com/apiotrowski-afk/okf-legal) 🟢 Apache-2.0 — profil prawniczy nad Open Knowledge Format: jednostka pod-dokumentowa z dosłownym cytatem, kierunkiem i statusem ratio/obiter, relacje typowane, reguły antyhalucynacyjne
- **ELI** (European Legislation Identifier) 🔵 — identyfikator używany przez API Sejmu
- **Akoma Ntoso / LegalDocML** (OASIS) — międzynarodowy standard dla aktów prawnych; w Polsce niewdrożony

## 2. Narzędzia i skille prawnicze

- [`michaleiatrak-star/Lex-Machina`](https://github.com/michaleiatrak-star/Lex-Machina) 🟢 GPL-3.0 — analityka prawa, przygotowanie pism procesowych, analiza umów i ryzyk, 16 dziedzin prawa, zakaz cytowania przepisów z pamięci; istnieje [port na OpenAI Codex](https://github.com/tittlepl-baj-jk/Lex-Machina-for-OpenAI-Codex)
- [`miskibin/asystent-rp`](https://github.com/miskibin/asystent-rp) ⚪ — asystent czatowy dla obywateli, odpowiadający o prawie polskim na danych z `sejm-stats.pl`; działa publicznie pod `chat.sejm-stats.pl`
- [`matematicsolutions/patron`](https://github.com/matematicsolutions/patron) 🟢 AGPL-3.0 — self-hosted agent dla kancelarii z łańcuchem skrótów jako śladem audytowym (art. 12 AI Act), własny model, 9 edycji językowych; ten sam utrzymujący wydaje pakiety skilli prawniczych, warstwę weryfikacji wyjścia modelu i ocenę gotowości kancelarii na AI
- [`apiotrowski-afk/commercial-legal-pl`](https://github.com/apiotrowski-afk/commercial-legal-pl) 🟢 Apache-2.0 — redakcja i analiza umów B2B, IT i IP: baza klauzul, baza wiedzy doktrynalnej, kontrola spójności odesłań § / ust. / pkt
- [`apiotrowski-afk/kancelaria-dms`](https://github.com/apiotrowski-afk/kancelaria-dms) 🟢 — DMS i CRM dla kancelarii, natywny dla Google Workspace, self-hosted
- [`pawelkwaczynski/staleness-warnings-pl`](https://github.com/pawelkwaczynski/staleness-warnings-pl) ⚪ — prerejestrowany pomiar tego, czy modele ostrzegają o nieaktualności odpowiedzi na polskich ustawach (OSF h7286); kod, prompty, zamrożone fragmenty i sumy kontrolne, **klucz odpowiedzi zatrzymany celowo**
- [`tuul-ai/lexedit`](https://github.com/tuul-ai/lexedit), [`jakatora/kredyt-ai`](https://github.com/jakatora/kredyt-ai) (analiza umów kredytowych), [`zeddq/cywil`](https://github.com/zeddq/cywil) ⚪ — projekty wczesne, jednoosobowe

### e-Doręczenia

- [`rodorn/edoreczenia-klient`](https://github.com/rodorn/edoreczenia-klient) 🟢 MIT — nieoficjalny klient interfejsu UA API w Pythonie
- [`tomkolp/e-doreczenia-wizualizacja-EPO`](https://github.com/tomkolp/e-doreczenia-wizualizacja-EPO) — wizualizacja elektronicznego potwierdzenia odbioru

## 3. Anonimizacja dokumentów

Cztery projekty na jednym polu. Wszystkie przetwarzają dokument lokalnie, przed
wysłaniem go do modelu — to jest warstwa, bez której praca z AI na aktach klienta
nie domyka się od strony tajemnicy zawodowej.

- [`paszkiewiczmichal/poufnik`](https://github.com/paszkiewiczmichal/poufnik) 🟢 Apache-2.0 / 🟠 — aplikacja desktopowa (Tauri + silnik Presidio jako sidecar): import PDF/DOCX/skanów, lokalny OCR, przegląd każdego wykrycia, eksport i odwracalne tokeny. Wersja Basic darmowa bez konta, Pro i Enterprise planowane
- [`studiogo/cenzor`](https://github.com/studiogo/cenzor) 🟢 MIT — CLI w Pythonie z pełnym obiegiem: tokenizacja przed wysłaniem, podstawienie danych z powrotem w odpowiedzi modelu. **Publikuje zmierzoną skuteczność** (nazwiska 98,9%) wraz z metodą pomiaru
- [`apiotrowski-afk/anon-legal-pl`](https://github.com/apiotrowski-afk/anon-legal-pl) 🟢 Apache-2.0 — Presidio + spaCy, sumy kontrolne PESEL/NIP/REGON, wzorce sygnatur sądowych, opcjonalny OCR
- [`LachPawel/Lethe`](https://github.com/LachPawel/Lethe) ⚪ — podejście hybrydowe: regex na dane strukturalne plus PLLuM (polski model publiczny) na NER kontekstowy; 24 kategorie danych, obsługa fleksji (Kowalski → Kowalskiego), API REST i CLI

## 4. Modele, korpusy, benchmarki

- [`speakleash`](https://github.com/speakleash) 🟢 MIT — **Bielik**, polski model językowy i korpusy: [`Bielik-how-to-start`](https://github.com/speakleash/Bielik-how-to-start) (tutoriale i baza wiedzy), [`speakleash`](https://github.com/speakleash/speakleash) (dostęp do korpusów), [`bielik-tools`](https://github.com/speakleash/bielik-tools). Same wagi modeli są na Hugging Face
- **PLLuM** 🟢 — polski model językowy budowany ze środków publicznych, używany m.in. przez `Lethe`
- [`allegro/HerBERT`](https://github.com/allegro/HerBERT) ⚪ — model BERT dla polszczyzny (MLM z dynamicznym maskowaniem całych słów); repo bez licencji, ostatnie zmiany 2022
- spaCy [`pl_core_news_lg`](https://github.com/explosion/spacy-models) 🟢 MIT — NER dla polszczyzny; stoi na nim większość narzędzi z sekcji 3
- [`PiotrTyrakowski/PolishLawLLM-Benchmark`](https://github.com/PiotrTyrakowski/PolishLawLLM-Benchmark) ⚪ — benchmark modeli językowych na prawie polskim

---

## Nota o autorstwie

Katalog prowadzi [Adam Piotrowski](https://github.com/apiotrowski-afk), radca prawny.
Część wpisów to jego własne projekty — opisane tym samym schematem, z tymi samymi
polami automatycznymi i objęte tą samą regułą „jeden utrzymujący = jeden wpis".
Kryterium włączenia: publicznie dostępne, dotyczy polskiego prawa, działa.

Brakuje czegoś? Zgłoś issue albo pull request.

## Licencja

[CC BY 4.0](LICENSE) — korzystaj, kopiuj, przerabiaj, podaj źródło.
