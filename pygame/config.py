"""
OOZORA SKY DEFENDER - Configuration & Constants

Shared constants for both web and pygame versions.
All magic numbers are centralized here for easy tweaking.
"""

# ============================================================================
# DISPLAY & LAYOUT
# ============================================================================
PLAY_W = 640
PLAY_H = 700
SIDEBAR_W = 240
SCREEN_W = PLAY_W + SIDEBAR_W  # 880
SCREEN_H = PLAY_H  # 700
FPS = 60

# ============================================================================
# COLORS (Ozora High School brand colors + atmosphere)
# ============================================================================
COLOR_BG_DARK = (8, 12, 26)           # #080c1a — deep blue-black
COLOR_BG_GRAD = (13, 18, 48)          # #0d1230 — radial gradient target
COLOR_ACCENT_GOLD = (245, 200, 60)    # #f5c83c — school gold
COLOR_ACCENT_NAVY = (30, 60, 130)     # #1e3c82 — school navy
COLOR_GLOW_CYAN = (120, 200, 255)     # #78c8ff — enemy glow
COLOR_TEXT_LIGHT = (232, 234, 244)    # #e8eaf4 — UI text
COLOR_FIELD_DARK = (26, 46, 16)       # #1a2e10 — dark farmland
COLOR_FIELD_GRID = (42, 68, 24)       # #2a4418 — field grid lines
COLOR_POTATO = (61, 92, 26)           # #3d5c1a — potato field
COLOR_CORN = (74, 107, 16)            # #4a6b10 — corn field
COLOR_MOUNTAIN = (26, 30, 46)         # #1a1e2e — Shiretoko silhouette
COLOR_RUNWAY = (64, 64, 64)           # #404040 — runway asphalt
COLOR_RUNWAY_LIGHT = (255, 255, 100)  # #ffff64 — runway lights (warm white)
COLOR_SWAN = (240, 240, 240)          # #f0f0f0 — swan white
COLOR_SHIP_BODY = (240, 240, 240)     # #f0f0f0 — plane fuselage
COLOR_SHIP_STRIPE = (245, 200, 60)    # #f5c83c — gold stripe
COLOR_SHIP_ACCENT = (30, 60, 130)     # #1e3c82 — navy accent
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_STAR_NEAR = (200, 210, 255)     # Slightly blue for depth

# ============================================================================
# PLAYER MECHANICS
# ============================================================================
PLAYER_SPEED = 280           # pixels per second
PLAYER_SLOW_MULT = 0.45      # Slow mode multiplier when holding SHIFT
PLAYER_HITBOX_R = 4          # Hitbox radius (pixels)
PLAYER_SHOOT_COOLDOWN = 7    # Frames between shots
PLAYER_BULLET_SPEED = 500    # pixels per second
PLAYER_BULLET_RADIUS = 2.5   # Drawn radius
PLAYER_INVULN_FRAMES = 90    # Invulnerability after taking damage
PLAYER_LIVES = 4

# ============================================================================
# ENEMIES
# ============================================================================
ENEMY_SPAWN_DISTANCE = 700        # Spawn beyond screen edge
LAPTOP_SIZE = 32                   # Width/height of laptop sprite
LAPTOP_SPEED_RANGE = (80, 200)     # Min/max speed for regular enemies
LAPTOP_HEALTH = 1
LAPTOP_SHOOT_COOLDOWN = 40         # Frames between enemy shots
LAPTOP_BULLET_SPEED = 250
LAPTOP_BULLET_RADIUS = 2
SUPPORT_DRONE_SIZE = 16
SUPPORT_DRONE_SPEED = 120
SUPPORT_DRONE_HEALTH = 1

# ============================================================================
# BOSS (大空システム ver.∞)
# ============================================================================
BOSS_SIZE = 64                      # Larger laptop
BOSS_HEALTH_BASE = 150              # Phase 1 health
BOSS_HEALTH_PHASE_2 = 100           # Phase 2 health
BOSS_HEALTH_PHASE_3 = 80            # Phase 3 health
BOSS_HEALTH_PHASE_4 = 60            # Phase 4 health
BOSS_EVERY_N_WAVES = 4              # Boss appears every 4th wave
BOSS_BULLET_SPEED = 300

# ============================================================================
# WAVES & PROGRESSION
# ============================================================================
WAVE_START_DELAY = 60               # Frames before first enemy spawns
WAVE_INTERMISSION = 300             # Frames between waves (5 seconds)
WAVES_TO_WIN = 16                   # Clear all 16 waves to beat game

# ============================================================================
# PARTICLES & EFFECTS
# ============================================================================
PARTICLE_POOL_SIZE = 500
PARTICLE_LIFETIME_SHORT = 30        # Frames
PARTICLE_LIFETIME_MEDIUM = 60
PARTICLE_LIFETIME_LONG = 120

# ============================================================================
# CUT-IN SYSTEM (敵出現時のカットイン)
# ============================================================================
CUTIN_SLIDE_IN_FRAMES = 14
CUTIN_STAY_FRAMES = 30
CUTIN_SLIDE_OUT_FRAMES = 14
CUTIN_TOTAL_FRAMES = CUTIN_SLIDE_IN_FRAMES + CUTIN_STAY_FRAMES + CUTIN_SLIDE_OUT_FRAMES

# ============================================================================
# OZORA REGIONAL ELEMENTS
# ============================================================================
OZORA_POPULATION = 6500
OZORA_SWANS_MIGRATE = 3000
SWAN_COUNT = 3                      # Number of swans in horizon layer
SWAN_SPEED = 0.4                    # pixels per frame (very slow, drifting)
SWAN_Y = 100                        # Y position in agricultural horizon
SHOOTING_STAR_INTERVAL = 600        # Frames between shooting stars
SHOOTING_STAR_DURATION = 20         # Frames to traverse screen
SHOOTING_STAR_DISTANCE = 200        # Pixels to travel

# ============================================================================
# FOUR GROWTH ATTRIBUTES (大空高校の4つの成長属性)
# OZORA: Each attribute is an enemy attack pattern + school curriculum connection
# ============================================================================
ATTRIBUTES = [
    {
        'id': 0,
        'name_jp': '主体性',
        'name_en': 'Initiative',
        'name_romaji': 'Jishusei',
        'description': '自ら考え、自ら動く',
        'color': (255, 100, 100),     # Red diamonds
        'pattern': 'waves'             # Bullet pattern type
    },
    {
        'id': 1,
        'name_jp': '社会性',
        'name_en': 'Sociality',
        'name_romaji': 'Shakaissei',
        'description': '地域と繋がる力',
        'color': (100, 200, 255),     # Cyan circles
        'pattern': 'spiral'
    },
    {
        'id': 2,
        'name_jp': '協働性',
        'name_en': 'Cooperation',
        'name_romaji': 'Kyoudousei',
        'description': '仲間と創る未来',
        'color': (200, 100, 255),     # Purple hexagons
        'pattern': 'burst'
    },
    {
        'id': 3,
        'name_jp': '探究心',
        'name_en': 'Inquiry',
        'name_romaji': 'Tankyuushin',
        'description': 'オホーツクの自然から学ぶ',
        'color': (255, 255, 100),     # Yellow circles
        'pattern': 'aimed'
    }
]

# ============================================================================
# OZORA FACTS (displayed between waves as regional promotion)
# OZORA: Facts cycle through all items, then shuffle and repeat
# ============================================================================
OZORA_FACTS = [
    {
        'title': '白鳥の里',
        'text': '大空町には北海道で最も多く\n白鳥が飛来します\n（約3,000羽）',
        'emoji': '🦢',
    },
    {
        'title': '空の玄関口',
        'text': '女満別空港から東京まで\n約1時間30分',
        'emoji': '✈️',
    },
    {
        'title': '大空高校',
        'text': '大空高校の生徒は\n町の人口の約1%を占めます',
        'emoji': '🏫',
    },
    {
        'title': 'オホーツク海',
        'text': 'オホーツク海は冬になると\n流氷で覆われます',
        'emoji': '🧊',
    },
    {
        'title': '広大な農地',
        'text': '大空町の農地面積は\n東京都の約1/3に相当します',
        'emoji': '🌾',
    },
    {
        'title': '星が多い',
        'text': '北海道の空は本州より\n星が30%多く見えると言われています',
        'emoji': '⭐',
    },
]

# ============================================================================
# SCORING & UI
# ============================================================================
SCORE_ENEMY_KILL = 100
SCORE_WAVE_CLEAR = 500
SCORE_BOSS_KILL = 5000
HIGH_SCORE_FILE = 'high_score.txt'
