# OOZORA SKY DEFENDER — 大空を守れ

> 北海道大空町・大空高校を全国に届ける弾幕シューティングゲーム
> A regional revitalization bullet-hell game celebrating Hokkaido's Ozora Town and High School

---

## 🌏 地方創生について (Regional Revitalization Purpose)

このゲームは北海道大空町（人口約6,500人）と北海道大空高校の知名度・魅力度向上を目的として制作されました。

ゲームプレイを通じて、プレイヤーが大空町の文化・自然・教育に自然に触れられるよう設計されています。ゲーム内に登場する農地、空港、白鳥、オホーツク海の流氷などは全て実在する大空町の風景です。

**このゲームが届けたいメッセージ：**
- 大空町の美しい自然と広大な農地
- 大空高校の教育理念（主体性・社会性・協働性・探究心）
- 女満別空港の存在と意義
- オホーツク地域の豊かな生態系

---

## 🎮 GAME OVERVIEW

**Title:** OOZORA SKY DEFENDER — 大空を守れ

**Setting:** The airspace above Memanbetsu Airport (女満別空港) in Ozora Town, Eastern Hokkaido.

**Your role:** Pilot a small aerobatic plane to defend the town's skies from rogue laptop drones representing "misdirected learning."

**Gameplay:** Classic bullet-hell with four attack patterns tied to Ozora High School's four growth attributes:
- 主体性 (Initiative)
- 社会性 (Sociality)
- 協働性 (Cooperation)
- 探究心 (Inquiry)

---

## 📋 Contents & How to Play

### Web Version (Browser)

```bash
# Just open in any browser:
web/index.html
```

- Single HTML file, no build needed
- Vanilla JavaScript, Canvas 2D API only
- Works offline

### Pygame Version (Python)

```bash
# Install dependencies
pip install -r pygame/requirements.txt

# Run the game
python pygame/main.py
```

- Python 3.10+
- Identical game logic to web version
- Procedurally drawn graphics (no image files)
- Cross-platform (Windows, macOS, Linux)

---

## 🎨 Visual Design

- **Play field:** 640 × 700 pixels (the sky)
- **Sidebar:** 240 × 300 pixels (HUD + facts)
- **Color palette:** School colors + night sky theme
  - Gold accent: `#f5c83c`
  - Navy accent: `#1e3c82`
  - Star field: realistic density for Ozora's low light pollution

### Key Regional Features

1. **Hokkaido Silhouette** — Title screen shows Hokkaido with Ozora Town marked in gold
2. **Agricultural Horizon** — Game background shows realistic farmland grid, potato fields, corn fields
3. **Memanbetsu Airport Runway** — Visible at bottom of play field with blinking runway lights
4. **Swan Animations** — White birds drift across the horizon (referencing migrating whooper swans)
5. **Shooting Stars** — Every ~600 frames, a star streaks across the sky (Ozora's pristine night sky)
6. **OZORA FACT Cards** — Between each wave, discover facts about the town:
   - Swan migration numbers
   - Flight time to Tokyo
   - Agricultural land comparisons
   - Ice floes on the Sea of Okhotsk
   - And more...

---

## 📍 About Ozora Town (大空町)

Located in Abashiri District, Eastern Hokkaido (オホーツク地域)

**Population:** ~6,500 (one of Hokkaido's smallest towns)

**Famous for:**
- 🦢 **Whooper Swans** — ~3,000 migrate through Lake Notoro and Lake Mokoto annually
- ✈️ **Memanbetsu Airport** — The town's airport, headquarters for flight training
- 🌾 **Agriculture** — Vast potato, corn, and dairy farms stretch to the horizon
- ⭐ **Night Sky** — Near-zero light pollution; the Milky Way is clearly visible

**Ozora High School (北海道大空高校):**
- The only high school in town
- Core educational philosophy: four growth attributes
  - **主体性** (Jishusei) — Self-directed thinking and action
  - **社会性** (Shakaissei) — Connection and contribution to community
  - **協働性** (Kyoudousei) — Collaboration and teamwork
  - **探究心** (Tankyuushin) — Curiosity and inquiry-based learning

These four attributes are woven into the game's enemy attack patterns as a tribute to the school's mission.

---

## 🚀 Quick Start

### For Web (Browser)
1. Download or clone this repository
2. Open `web/index.html` in any web browser
3. Press SPACE to start
4. Use arrow keys or WASD to move
5. Hold SHIFT to slow down
6. Z to shoot

### For Pygame (Python)
```bash
# Clone the repo
git clone https://github.com/onigiriman529/oozora-sky-defender.git
cd oozora-sky-defender

# Install dependencies
pip install -r pygame/requirements.txt

# Run
python pygame/main.py
```

**Controls:**
- Arrow keys or WASD — Move
- SHIFT — Slow mode (reduced speed, tighter aim)
- Z — Shoot

---

## 📊 Game Mechanics

### Player Ship
- Small aerobatic plane (civilian design, not military)
- White fuselage with gold stripe and navy accents
- Starts with 4 lives
- Invulnerability frames after taking damage

### Enemies
- **Laptop Drones** — Screen displays error messages tied to school attributes
- **Waves** — Progressive difficulty, new attack patterns each wave
- **Boss** — Appears every 4 waves, represents "Ozora System ver. ∞"

### Scoring
- Destroy enemies to rack up points
- Clear all waves to beat the game
- High scores displayed in "大空の英雄たち" (Heroes of the Big Sky)

### Between Waves
- 5-second intermission
- **OZORA FACT card** displays: rotating facts about the town
- Card border color matches the dominant enemy attribute from that wave

---

## 🏗️ Project Structure

```
oozora-sky-defender/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── .gitignore                   # Git exclusions
│
├── web/
│   └── index.html               # Complete browser game (single file)
│
├── pygame/
│   ├── main.py                  # Entry point
│   ├── config.py                # Shared constants
│   ├── game.py                  # Main loop & state machine
│   ├── player.py                # Player ship class
│   ├── enemies.py               # Enemy & boss classes
│   ├── bullets.py               # Bullet system
│   ├── particles.py             # Particle effects
│   ├── cutin.py                 # Cut-in system with school branding
│   ├── wave_manager.py          # Wave spawning logic
│   ├── ui.py                    # Sidebar UI & Ozora facts
│   ├── helpers.py               # Utility functions
│   └── requirements.txt         # Dependencies (pygame>=2.0)
│
├── docs/
│   ├── gameplay.md              # Detailed gameplay guide
│   └── about_oozora.md          # Extended Ozora Town information
│
└── assets/
    └── .gitkeep                 # Placeholder (all graphics procedural)
```

---

## 💻 Technical Details

### Web Version
- **Language:** Vanilla JavaScript (ES6+)
- **Graphics:** HTML5 Canvas 2D API
- **No dependencies:** Works completely offline
- **File size:** ~50KB unminified

### Pygame Version
- **Language:** Python 3.10+
- **Dependencies:** pygame 2.0+ only
- **Graphics:** Procedural (no image files)
- **Cross-platform:** Windows, macOS, Linux

Both versions share:
- Identical game logic and constants
- Same visual style and animations
- Same regional identity elements

---

## 🎯 Design Philosophy

Every element of OOZORA SKY DEFENDER serves **two purposes:**

1. **Engaging Gameplay** — A polished, fun bullet-hell experience
2. **Regional Promotion** — Naturally expose players to Ozora Town's beauty, culture, and educational values

Players should finish the game and want to:
- Learn more about Ozora Town
- Visit Memanbetsu Airport
- Support Ozora High School
- Explore Hokkaido's Abashiri District

---

## 📜 License

MIT License — See `LICENSE` file

---

## 🙏 Acknowledgments

- **Ozora Town** (大空町) — The inspiration and subject of this game
- **Ozora High School** (北海道大空高校) — Educational partner
- **Memanbetsu Airport** (女満別空港) — Gateway to the region
- **Touhou Project** — Bullet-hell game design inspiration

---

## 🌐 Learn More

**Official Ozora Town Website:** https://ozora-town.jp

**Play the game and discover Hokkaido's hidden gem! 🌟**

ゲームをプレイして、北海道大空町の魅力を発見してください！

---

*© 2025 Ozora Town Regional Revitalization Project*
