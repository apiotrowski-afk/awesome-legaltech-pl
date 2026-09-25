#!/usr/bin/env python3
"""
sprawdz_zywotnosc.py — kontrola żywotności wpisów katalogu awesome-prawo-pl.

Zasada: skrypt STWIERDZA fakty z API GitHuba i nic nie ocenia.
Nie pisze "porzucony" ani "martwy" — podaje datę ostatniego commita, flagę
archived i datę odczytu. Wniosek wyciąga czytelnik.

Źródło prawdy = README.md. Nie ma osobnego pliku danych, więc nic nie drifuje.

Użycie:
    python3 sprawdz_zywotnosc.py README.md              # raport na stdout
    python3 sprawdz_zywotnosc.py README.md --md         # tabela markdown
    python3 sprawdz_zywotnosc.py README.md --json out.json

Wymaga zalogowanego `gh` (gh auth status) — używa jego tokenu przez gh api.
"""
import re, sys, json, subprocess, datetime, collections, time

RE_REPO = re.compile(r'https://github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)')

def zbierz(path):
    txt = open(path, encoding="utf-8").read()
    out = []
    for owner, repo in RE_REPO.findall(txt):
        repo = repo.rstrip('.')
        if repo.lower() in {".github"}:
            continue
        slug = f"{owner}/{repo}"
        if slug not in out:
            out.append(slug)
    return out

def gh(endpoint, proby=3):
    """Odpytuje API. Ponawia, bo pojedyncze niepowodzenie sieciowe nie znaczy,
    że repozytorium zniknęło — a fałszywy alarm podkopuje zaufanie do kontroli."""
    for i in range(proby):
        r = subprocess.run(["gh", "api", endpoint], capture_output=True, text=True)
        if r.returncode == 0:
            try:
                return json.loads(r.stdout)
            except json.JSONDecodeError:
                return None
        # 404 od GitHuba jest rozstrzygające; błąd sieci nie jest
        if "Not Found" in (r.stderr or "") or "HTTP 404" in (r.stderr or ""):
            return None
        if i < proby - 1:
            time.sleep(2 * (i + 1))
    return None

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    dzis = datetime.date.today().isoformat()
    slugs = zbierz(path)
    print(f"# wpisów GitHub w {path}: {len(slugs)}\n", file=sys.stderr)

    wyniki, bledy = [], []
    for i, slug in enumerate(slugs, 1):
        d = gh(f"repos/{slug}")
        if d is None:
            bledy.append(slug)
            print(f"  [{i}/{len(slugs)}] {slug} — NIEDOSTĘPNE (404/prywatne/przeniesione)", file=sys.stderr)
            continue
        wyniki.append({
            "repo": slug,
            "gwiazdki": d.get("stargazers_count", 0),
            "ostatni_commit": (d.get("pushed_at") or "")[:10],
            "archived": bool(d.get("archived")),
            "licencja_api": (d.get("license") or {}).get("spdx_id") or "brak",
            "odczyt": dzis,
        })
        print(f"  [{i}/{len(slugs)}] {slug}", file=sys.stderr)

    if "--json" in sys.argv:
        out = sys.argv[sys.argv.index("--json") + 1]
        json.dump({"odczyt": dzis, "wpisy": wyniki, "niedostepne": bledy},
                  open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"\nzapisano: {out}", file=sys.stderr)

    if "--md" in sys.argv:
        print(f"<!-- kontrola żywotności: {dzis} -->\n")
        print("| Repo | ★ | Ostatni commit | Archived | Licencja (API) |")
        print("|---|---|---|---|---|")
        for w in sorted(wyniki, key=lambda x: -x["gwiazdki"]):
            print(f"| [{w['repo']}](https://github.com/{w['repo']}) | {w['gwiazdki']} | "
                  f"{w['ostatni_commit']} | {'tak' if w['archived'] else 'nie'} | {w['licencja_api']} |")
        if bledy:
            print(f"\n**Niedostępne przy odczycie {dzis}:** " + ", ".join(f"`{b}`" for b in bledy))
        return

    # raport domyślny — grupowanie po dacie, bez etykiet ocennych
    prog = (datetime.date.today() - datetime.timedelta(days=365)).isoformat()
    starsze = [w for w in wyniki if w["ostatni_commit"] < prog]
    arch = [w for w in wyniki if w["archived"]]
    braklic = [w for w in wyniki if w["licencja_api"] == "brak"]
    print(f"\nodczyt: {dzis}   sprawdzonych: {len(wyniki)}   niedostępnych: {len(bledy)}")
    print(f"bez commita od {prog}: {len(starsze)}")
    for w in starsze: print(f"   {w['ostatni_commit']}  {w['repo']}")
    print(f"archived=true: {len(arch)}")
    for w in arch: print(f"   {w['repo']}")
    print(f"bez pliku LICENSE: {len(braklic)}")
    for w in braklic: print(f"   {w['repo']}")
    if bledy:
        print(f"niedostępne: {', '.join(bledy)}")

if __name__ == "__main__":
    main()
