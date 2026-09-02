# YouTube: The Ultimate Guide to Hermes Desktop Plugins

- **Video ID**: `SLUtt-po_OE`
- **URL**: [https://www.youtube.com/watch?v=SLUtt-po_OE](https://www.youtube.com/watch?v=SLUtt-po_OE)
- **Kanál**: [Tonbi's AI Garage](https://www.youtube.com/channel/UCqB1bhMwGsW-yefBxYwFCCg)
- **Dĺžka**: 19:52
- **Dátum vydania**: 2026-08-11
- **Kategória**: Návod / Technický deep-dive (Tutorial & Architecture)

---

## 📌 Rýchle zhrnutie (TL;DR)
Tento video sprievodca do hĺbky rozoberá **Hermes Desktop Plugin SDK** pre desktopovú aplikáciu Hermes Agent. Autor demonštruje **25 rôznych pozícií v používateľskom rozhraní (UI)**, kam je možné pluginy umiestniť (panes, docky, status bar, title bar, composer, popovery, routes). Vysvetľuje architektúru pluginov (UI renderery vs. Python backendy pre ťažké výpočty), ich možnosti aj bezpečnostné limity a naživo stavia 4 funkčné pluginy: **Slides Viewer**, **Krypto/Trading terminál (Hyperliquid + TradingView)**, **Spotify Controller** a **SNES emulátor**.

---

## 🎯 Hlavné poznatky (Key Takeaways)

1. **25 umiestnení v UI (Placement Playground):** Plugin nie je len jedno okno – môže byť celoobrazovkový pane, dokovateľná lišta, ikona v title bare, status widget na spodnej lište, popover, alebo prvok priamo v compose paneli (vedľa textového poľa pre prompt).
2. **Pravidlo "Form Follows Function":**
   - **Compact / Ambient awareness:** Malý widget v status bare (napr. počasie, cena Bitcoinu, monitorovanie stavu).
   - **Anchored / Quick Control:** Popover menu pre rýchle akcie bez opustenia aktuálnej konverzácie (napr. Spotify prehrávač).
   - **Expansive / Full Application:** Samostatná záložka / panel pre komplexné workflows (napr. Trading terminál, slides, analytika).
   - **Declarative:** Poskytnutie štruktúrovaných dát, kde Hermes sám rozhodne o finálnom zobrazení.
3. **Architektúra pluginov a zdroj výkonu:**
   - Plugin môže čerpať stav priamo z Hermes runtime (informácie o agentoch, cron joby, kanban, workspace).
   - Samotný frontend pluginu slúži ako UI renderer.
   - Ak je potrebná databáza, lokálne súbory, natívne knižnice, websockety alebo spracovanie médií (FFmpeg, machine learning), pripája sa **Python backend**.
4. **Čo plugin nemôže / nesmie robiť (Limity & Bezpečnosť):**
   - Nemá priamy prístup k neobmedzeným natívnym API mimo Hermes sandboxu.
   - Nemôže si vymýšľať ľubovoľné nové oblasti v UI mimo 25 definovaných zón.
   - Nejde o perzistentné úložisko – interné úložisko je len malý JSON stav (pre veľké dáta sa musí použiť externá databáza).
   - Beží iba vtedy, keď je otvorená desktopová aplikácia Hermes.

---

## 🧭 Prehľad 25 umiestnení v používateľskom rozhraní (UI Placements)

| Kategória | Pozícia | Typické využitie |
| :--- | :--- | :--- |
| **Panes** | `pane main`, `pane left`, `pane right`, `pane top`, `pane bottom` | Plnohodnotné aplikácie, zoznamy súborov, integrované terminály. |
| **Workspace Docks** | `workspace top`, `workspace bottom`, `dock workspace left`, `dock workspace right`, `workspace center` | Pripnuté panely okolo hlavného pracovného priestoru. |
| **Status Bar** | `status bar left`, `status bar right` | Ambientné informácie (stav siete, health status, malé tickery). |
| **Title Bar** | `title bar left`, `title bar center`, `title bar right` | Kompaktné ikony v hornej lište okna s možnosťou kliknutia. |
| **Popovers** | `popover top`, `popover bottom`, `popover left`, `popover right` | Kontextové vyskakovacie okná pre rýchle akcie bez zmeny kontextu. |
| **Composer** | `composer top`, `composer bottom`, `composer leading`, `composer actions`, `composer attachments` | Doplnky priamo do vstupného poľa pre prompt (napr. špeciálne prílohy, rýchle príkazy). |
| **Sidebar / Route**| `workspace route & sidebar` | Samostatné plnoformátové sekcie prekrývajúce bežné sedenia (Slides, Kanban, trhy). |

---

## 🛠️ Praktické ukážky vytvorených pluginov

### 1. Slide Deck Presenter (`00:43`)
- **Účel**: Prezentácia HTML slidov priamo v prostredí Hermes Desktop.
- **Umiestnenie**: V postrannom paneli (Sessions bar pod Kanbanom).
- **Funkcie**: Otváranie HTML súborov na jedno kliknutie a ich interaktívne premietanie.

### 2. Multi-Surface Trading Terminal (`13:00`)
- **Účel**: Sledovanie krypto a finančných trhov.
- **Umiestnenie**: 3-úrovňový dizajn – ticker v status bare (ambient state), rýchly popover a plnohodnotná záložka v bočnom paneli (Markets).
- **Integrácia**: Napojenie na **Hyperliquid** (orderbook, aktuálne ceny BTC, ETH, Hype s rôznymi timeframeami 15m, 1h, 4h) + vloženie interaktívneho grafu z **TradingView**.

### 3. Spotify Controller (`15:51`)
- **Účel**: Ovládanie hudby pri kódovaní a práci s agentom.
- **Umiestnenie**: Popover na spodnej lište.
- **Integrácia**: OAuth autorizácia cez Spotify App API. Umožňuje vyhľadávanie skladieb/umelcov a ovládanie prehrávania na pozadí (vyžaduje spustenú Spotify desktop app).

### 4. SNES Emulator (`17:43`)
- **Účel**: Hranie retro hier počas čakania na dokončenie úloh agenta.
- **Technológia**: Vstavaný emulátor postavený na **emulator.js**.
- **Demonštrácia**: Načítanie ROM hry *The Legend of Zelda: A Link to the Past* s možnosťou pauzovania a návratu k práci v druhej záložke.

---

## 💬 Kľúčové postrehy z komentárov (Community Insights)

- **Využitie s diaľkovým gatewayom (@hongseon880911)**: Diváci sa pýtali, ako pluginy fungujú pri pripojení desktopovej aplikácie k vzdialenému gatewayu (VPS Docker) – UI pluginu beží lokálne v desktop klientovi, pričom dáta čerpá cez sieť.
- **Integrácia Language Server Protocol / LSP (@dominick253)**: Pridanie LSP pluginu poskytuje lokálnemu modelu okamžitú spätnú väzbu pri písaní kódu.
- **Hermes ako náhrada desktopového OS (@claytonjohnsonseo, @JonathanBylos)**: Komunita vyzdvihuje prechod od CLI nástrojov k plnohodnotným natívnym GUI rozšíreniam, kde Hermes prepája agentov, systémové služby a UI nástroje do jedného ekosystému.
- **Chrome rozšírenie (@24ifix66)**: Odporúčanie na prepojenie Hermes s otvorenými tabmi v Google Chrome cez dedikované open-source rozšírenie.

---

## 🔗 Referencie a odkazy
- **GitHub autora**: [Tombstone Studio (GitHub)](https://github.com/)
- **X / Twitter**: Oznámenia o zverejnení repozitára s open-source pluginmi
