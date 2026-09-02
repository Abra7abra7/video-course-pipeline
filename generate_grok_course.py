import os
import sys
import subprocess

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from voice_engine import generate_voice

LESSONS = [
    {
        "id": 1,
        "title": "Čo je Grok Bot a prečo je to zlom",
        "filename": "lekcia_01_co_je_grok_bot.mp3",
        "text": """Vitaj v kurze o Grok Bote. Som Marian Stančík a v tomto kurze ti ukážem, čo sa skrýva za virálnym workshopom SpaceX AI inžinierky Lauren Tan, ktorý obletel celé X.

Grok Bot je niečo, čo tu ešte nebolo. Nie je to chatbot, ktorému píšeš otázky a on ti vráti text. Je to tím AI agentov, ktorí majú vlastný počítač v cloude. Každý z nich sa vie prihlásiť do tvojich nástrojov — do Gmailu, kalendára, Slacku, GitHubu — a pracovať v nich presne ako ty. Rozdiel je v tom, že oni nezaspávajú. Nepotrebujú pauzu. A keď zatvoríš laptop, oni stále pracujú.

Lauren Tan, inžinierka ktorá na Grok Bote priamo pracuje, vo svojom workshope ukázala ako behá 10 až 20 týchto agentov. A všetkých ovláda cez jediného Chief of Staff agenta. Jej tvrdenie? Automatizuje 90 percent svojej dennej rutiny.

Poďme sa pozrieť na to, čo to v praxi znamená a ako si to môžeš postaviť aj ty."""
    },
    {
        "id": 2,
        "title": "Architektúra — Chief of Staff a špecialisti",
        "filename": "lekcia_02_architektura.mp3",
        "text": """Celý systém stojí na jednom jednoduchom princípe: nekomunikuješ so všetkými botmi. Komunikuješ len s jedným — s Chief of Staff.

Predstav si ho ako svojho osobného asistenta, ktorý pozná všetkých odborníkov v tvojej firme. Ty mu povieš: "Potrebujem pripraviť ponuku pre klienta." A on už vie, ktorý bot spracuje cenovú kalkuláciu, ktorý pripraví text ponuky a ktorý pošle email. Ty to nemusíš riešiť.

Pod Chief of Staff sedia špecialisti s trvalými rolami:
Inbox Manager — spravuje tvoju poštu.
Calendar Scheduler — plánuje stretnutia.
To-Do Organizer — sleduje úlohy.
Research bot — robí prieskum trhu.
Content bot — pripravuje obsah.

Každý z nich má svoju doménu, dlhodobú pamäť a zlepšuje sa v nej. A vedia medzi sebou komunikovať priamo, bez toho aby museli ísť cez Chief of Staff.

Toto je kľúčový insight: nejde o to mať jeden super-agent, ktorý vie všetko. Ide o to mať tím špecialistov, ktorých koordinuje jeden orchestrátor."""
    },
    {
        "id": 3,
        "title": "Ako začať — prvý bot a pripojenie nástrojov",
        "filename": "lekcia_03_ako_zacat.mp3",
        "text": """Poďme na praktickú časť. Ako si to celé nastavíš?

Prvý krok je stiahnuť Grok Bot appku na macOS alebo iOS. Android zatiaľ nie je podporovaný.

Keď appku otvoríš, vytvoríš svojho prvého bota. Nepremýšľaj nad tým príliš — daj mu rolu Chief of Staff. To je tá najdôležitejšia voľba, ktorú spravíš.

Potom ho požiadaj, aby ťa previedol pripojením tvojich nástrojov. Gmail, Google Calendar, Slack — to sú prvé tri, ktoré odporúčam. Grok Bot ťa prevedie autentifikáciou. Stačí raz, a všetci tvoji budúci boti budú mať prístup k týmto nástrojom automaticky.

Dôležitá rada: nepripájaj hneď všetko. Začni s emailom a kalendárom. Nechaj bota ukázať čo vie, a až potom pridávaj ďalšie integrácie.

Keď máš Chief of Staff hotového a nástroje pripojené, sprav to najdôležitejšie — daj mu voľnosť. Povedz mu: "Tu sú moje nástroje, tu je moja práca. Navrhni mi tím, ktorý by mi pomohol." On ti navrhne zloženie tímu, ty schváliš a on ho postaví.

Toto je moment, ktorý väčšina ľudí preskočí. A potom sa čudujú, prečo im to nefunguje."""
    },
    {
        "id": 4,
        "title": "Učenie skillov a rutiny",
        "filename": "lekcia_04_ucenie_skillov.mp3",
        "text": """Toto je podľa mňa najsilnejšia časť Grok Botu. Nazýva sa to Teach a Task.

Namiesto písania zložitých promptov proste ukážeš botovi čo má robiť. Spustíš nahrávanie obrazovky, urobíš úlohu — napríklad spracovanie príchodzej faktúry — a bot sa to naučí. Uloží si to ako skill a nabudúce to spraví sám.

Ale pozor, nie je to len o automatizácii. Je to o tom, že bot sa učí tvoje preferencie. Keď mu povieš "faktúry radšej spracúvam večer, nie ráno", zapamätá si to. Keď opravíš nejaký detail, nabudúce ho spraví správne.

Z týchto skillov potom vytváraš rutiny. Rutina je automatizácia, ktorá beží na základe času alebo udalosti. Napríklad:
Každé ráno o 8:00 mi priprav sumár emailov.
Keď príde faktúra nad 1000 eur, označ ju na schválenie.
Každý pondelok o 9:00 pošli report o stave projektov.

Rutiny bežia na cloude. Nepotrebuješ mať appku otvorenú. Zatvoríš laptop, ideš spať a ráno máš hotovo.

Najsilnejší príklad z workshopu: Lauren ukázala feedback loop. Keď jej tím nahlási bug na Grok Bote, jej boti ho automaticky začnú fixovať ešte skôr, než si stihne prečítať ticket. To nie je automatizácia. To je zamestnanec."""
    },
    {
        "id": 5,
        "title": "Guardrails a bezpečnosť",
        "filename": "lekcia_05_guardrails.mp3",
        "text": """Toto je najdôležitejšia lekcia v celom kurze. Lebo dať botovi prístup k tvojmu emailu je ako najať zamestnanca. A zamestnanec potrebuje pravidlá.

Každý bot v tvojom tíme by mal mať jasne nastavené hranice:
Čo smie robiť bez pýtania?
Na čo potrebuje schválenie?
Čo nesmie robiť nikdy?

Príklad z praxe: boti vedia písať emaily, ale nič neodošle bez tvojho schválenia. Môžu draftovať odpovede, môžu pripravovať ponuky, ale tlačidlo send máš len ty.

Toto nie je obmedzenie. Je to nevyhnutnosť. Bot, ktorý sa musí pýtať na všetko, je nepoužiteľný. Ale bot, ktorý sa nepýta nikdy, je nebezpečný.

Druhá vec — cloud computer je zdieľaný. Všetci tvoji boti sídlia na jednom počítači. To znamená, že ak jeden bot získa prístup k nejakému heslu, majú ho všetci. Preto:
Nikdy nedávaj botovi prístup k veciam, ktoré nepotrebuje.
Pravidelne kontroluj čo boti robia.
Ak niečo vyzerá podozrivo, okamžite to zastav.

Bezpečnosť nie je nastavenie, je to návyk."""
    },
    {
        "id": 6,
        "title": "Ako to celé spojiť a čo ďalej",
        "filename": "lekcia_06_ako_to_spojit.mp3",
        "text": """Poďme si zhrnúť celý postup, ktorý potrebuješ na to, aby si mal vlastný tím AI agentov.

Krok 1: Stiahni Grok Bot appku na macOS.
Krok 2: Vytvor Chief of Staff bota.
Krok 3: Pripoj Gmail a kalendár.
Krok 4: Nechaj Chief of Staff navrhnúť tím.
Krok 5: Schváľ a nechaj ho postaviť špecialistov.
Krok 6: Nastav guardrails — čo smie každý bot bez pýtania.
Krok 7: Nauč prvý skill cez Teach a Task.
Krok 8: Vytvor rutinu na základe skillu.
Krok 9: Testuj, opravuj, rozširuj.

A teraz najdôležitejšia rada: nezačínaj s tímom. Začni s jedným botom, ktorý robí jednu vec dobre. Každý multi-agent setup, ktorý zlyhal, zlyhal pretože niekto postavil šesť priemerných agentov namiesto jedného dobrého.

Tvoja prvá otázka pre Chief of Staff by mala byť: "Akého jedného bota by si mi odporučil na začiatok?" A až keď ten funguje, rozširuj.

Grok Bot nie je nástroj. Je to nový spôsob ako uvažovať o práci. Nie "aký prompt napíšem", ale "akého človeka najmem". A to je posun, ktorý definuje rok 2026.

Ak máš otázky, napíš mi na marianstancik@agentmail.to.

Ďakujem za pozornosť."""
    }
]

def main():
    output_dir = os.path.join(os.getcwd(), "course_grok_bot", "audio")
    os.makedirs(output_dir, exist_ok=True)

    print("\n=======================================================")
    print("🎙️ SPÚŠŤAM GENEROVANIE AUDIO KURZU CEZ ELEVENLABS")
    print(f"Počet lekcií: {len(LESSONS)}")
    print("=======================================================\n")

    audio_files = []
    for lesson in LESSONS:
        out_path = os.path.join(output_dir, lesson["filename"])
        print(f"\n--- Lekcia {lesson['id']}: {lesson['title']} ---")
        generate_voice(lesson["text"], out_path)
        audio_files.append(out_path)

    print("\n=======================================================")
    print("✅ VŠETKY LEKCIE BOLI ÚSPEŠNE VYGENEROVANÉ!")
    print(f"Priečinok: {output_dir}")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
