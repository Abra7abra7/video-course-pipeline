# Kurz: Grok 2 & Multi-Agent Architektúra (Deep-Dive)

**Autor:** Marian Stančík  
**Formát:** Interaktívny Video & Audio Kurz (ElevenLabs Custom Voice + Hovoriaci AI Avatar + Interaktívny Architektonický Explorer)  
**Dĺžka:** 6 lekcií (~200 sekúnd čistého výkladu)  
**Cieľovka:** Vývojári, AI architekti, technickí zakladatelia a podnikatelia  

---

## Prehľad lekcií

1. [Lekcia 1: Grok 2 a Evolúcia Agentic Systémov](#lekcia-1-grok-2-a-evolúcia-agentic-systémov)
2. [Lekcia 2: Hĺbková Architektúra: Dual-Brain a Router](#lekcia-2-hĺbková-architektúra-dual-brain-a-router)
3. [Lekcia 3: Tool Execution Bus a Sandboxing](#lekcia-3-tool-execution-bus-a-sandboxing)
4. [Lekcia 4: Teach a Task 2.0 a Kompilácia Skillov](#lekcia-4-teach-a-task-20-a-kompilácia-skillov)
5. [Lekcia 5: Multi-Agent Swarm Protocol a P2P Komunikácia](#lekcia-5-multi-agent-swarm-protocol-a-p2p-komunikácia)
6. [Lekcia 6: Enterprise Guardrails a Bezpečnostný Zero-Trust Model](#lekcia-6-enterprise-guardrails-a-bezpečnostný-zero-trust-model)

---

## Lekcia 1: Grok 2 a Evolúcia Agentic Systémov
🎧 *Audio: `audio/lekcia_01_grok2_evolucia.mp3`*

Vitaj v pokročilom kurze Grok 2. Dnes sa pozrieme pod kapotu novej generácie autonómnych agentov od xAI. Grok 2 nepredstavuje len väčší jazykový model s lepším reasoningom. Je to kompletný operačný systém pre umelú inteligenciu. Rozdiel medzi bežným LLM a agentic runtime je zásadný: model len predpovedá tokeny, zatiaľ čo Grok 2 beží v perzistentnom virtuálnom prostredí, má prístup k systémovému bashu, browseru a izolovanému pamäťovému modulu. Poďme sa pozrieť, ako funguje jadro tohto systému.

---

## Lekcia 2: Hĺbková Architektúra: Dual-Brain a Router
🎧 *Audio: `audio/lekcia_02_dual_brain_architektura.mp3`*

Srdcom Grok 2 agenta je architektúra Dual-Brain. Pozostáva z dvoch kľúčových komponentov: Fast Reasoning Kernel a Meta-Controller, známy ako Chief of Staff. Keď príde požiadavka, Router najprv analyzuje jej sémantickú komplexitu. Jednoduché úlohy vybaví priamo v mikrosekundách. Zložité výpočty a viac-krokové workflows rozdelí do stromu podúloh. Tento strom je riadený dynamickým kontextovým oknom, ktoré prepája vektorovú databázu s dlhodobou epizodickou pamäťou. Vďaka tomu agent nikdy nestráca kontext ani po týždňoch behu.

---

## Lekcia 3: Tool Execution Bus a Sandboxing
🎧 *Audio: `audio/lekcia_03_tool_bus_sandboxing.mp3`*

Ako Grok 2 vykonáva akcie bez toho, aby halucinoval? Kľúčom je Tool Execution Bus. Namiesto toho, aby model len vymýšľal odpovede, posiela štruktúrované JSON príkazy do zabezpečeného sandboxu. Sandbox obsahuje plnohodnotný Linux terminál, headless prehliadač Chromium a API adaptéry pre Gmail, Slack či GitHub. Každá akcia prebehne v reálnom čase, výstup sa validuje cez error-handling modul a až overený výsledok sa vracia do mozgu agenta. Tento uzavretý cyklus zaručuje 99-percentnú deterministickú presnosť.

---

## Lekcia 4: Teach a Task 2.0 a Kompilácia Skillov
🎧 *Audio: `audio/lekcia_04_teach_task_kompilacia.mp3`*

V štvrtej lekcii sa pozrieme na najinovatívnejšiu technológiu Grok 2: Teach a Task 2.0. Keď nahráš obrazovku so svojím pracovným postupom, Grok 2 neukladá len pixely. Multimodálny parser analyzuje kliknutia myšou, klávesové skratky a DOM štruktúru webu. Tento vizuálny záznam následne skompiluje do čistého, optimalizovaného Python skriptu. Z jednorazovej ukážky sa stane trvalý, verzovaný skill s vlastným API endpointom, ktorý sa automaticky spúšťa cez cron alebo webhooky.

---

## Lekcia 5: Multi-Agent Swarm Protocol a P2P Komunikácia
🎧 *Audio: `audio/lekcia_05_swarm_protocol_p2p.mp3`*

Keď potrebuješ škálovať desiatky procesov naraz, jeden agent nestačí. Grok 2 využíva Swarm Protocol na koordináciu tímu špecialistov. Inbox bot, Calendar bot, Research bot a Code bot nečakajú na pokyny zhora. Komunikujú cez distribuovanú P2P zbernicu. Keď Research bot dokončí analýzu trhu, vygeneruje stavový handoff token a priamo zobudí Content bota. Synchronizácia prebieha asynchrónne na pozadí, čím dosahuje paralelizáciu práce a extrémne nízku latenciu.

---

## Lekcia 6: Enterprise Guardrails a Bezpečnostný Zero-Trust Model
🎧 *Audio: `audio/lekcia_06_enterprise_guardrails.mp3`*

V poslednej lekcii si prejdeme to najdôležitejšie: ako celý systém bezpečne nasadiť v podniku. Grok 2 implementuje striktný Zero-Trust bezpečnostný model. Každý agent má presne definované RBAC práva. Zavádza sa princíp troch zón: zelená pre autonómne čítanie, oranžová pre draftovanie s notifikáciou a červená pre kritické akcie, ako je platba či odoslanie zmluvy. Tlačidlo finálneho potvrdenia zostáva vždy v rukách človeka. S týmto nastavením máte v rukách bezpečný a nezastaviteľný digitálny tím.

---

*Lektor kurzu: Marian Stančík • Hlas vygenerovaný cez ElevenLabs • Všetky práva vyhradené 2026*
