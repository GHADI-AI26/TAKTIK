import streamlit as st
from pathlib import Path
import base64
from PIL import Image

from taktik_logic import (
    stadiums,
    matches
)


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="TAKTIK | Match Day",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# PATHS
# =========================================================

ASSETS = Path(__file__).resolve().parent.parent / "assets"

BACKGROUND = ASSETS / "welcometosaudi34.png"

STADIUM_IMAGES = {
    "King Salman Stadium": ASSETS / "king_salman.jpg.jpeg",
    "King Fahad Sports City": ASSETS / "king_fahad.jpg.jpeg",
    "Alinma Stadium": ASSETS / "alinma.jpg.jpeg",
    "Aramco Stadium": ASSETS / "aramco.jpg.jpeg",
}


# =========================================================
# SESSION STATE
# =========================================================

if "selected_stadium" not in st.session_state:
    st.session_state.selected_stadium = None

if "selected_match" not in st.session_state:
    st.session_state.selected_match = None

if "food_type" not in st.session_state:
    st.session_state.food_type = None

if "food_preference" not in st.session_state:
    st.session_state.food_preference = None

if "food_results" not in st.session_state:
    st.session_state.food_results = None


# =========================================================
# BACKGROUND
# =========================================================

def get_base64_image(image_path):

    with open(image_path, "rb") as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode()


background_base64 = get_base64_image(
    BACKGROUND
)


# =========================================================
# FOOD OPTIONS
# =========================================================

FOOD_OPTIONS = {

    "King Salman Stadium": {

        "Cafe": {
            "Specialty Coffee": [
                "Jaqwa | Specialty Coffee",
                "Chess Specialty Coffee",
                "Puzzle Roastery"
            ],

            "Coffee + Dessert": [
                "Thoughts Express",
                "Caribou Coffee",
                "Veni"
            ],

            "Chill & Quiet": [
                "Veni",
                "Jaqwa",
                "Right Now"
            ]
        },

        "Restaurant": {
            "Saudi Food": [
                "Najd Village",
                "Majlah Bahraini Cuisine",
                "Al Armin"
            ],

            "Burgers": [
                "SPREAD",
                "Al Armin",
                "Loziah"
            ],

            "Indian Food": [
                "Mr. Biryani",
                "Shalimar",
                "Shahrukh Khan"
            ],

            "Mexican Food": [
                "Amigos"
            ]
        }
    },


    "King Fahad Sports City": {

        "Cafe": {
            "Specialty Coffee": [
                "Jaqwa | Specialty Coffee",
                "Chess Specialty Coffee",
                "Puzzle Roastery"
            ],

            "Coffee + Dessert": [
                "Thoughts Express",
                "Caribou Coffee",
                "Veni"
            ],

            "Chill & Quiet": [
                "Veni",
                "Jaqwa",
                "Right Now"
            ]
        },

        "Restaurant": {
            "Saudi Food": [
                "Najed Restaurant",
                "Limonah",
                "Qasr Al Liwan"
            ],

            "Burgers": [
                "RED . FOOD STREET",
                "Food Truck Eman",
                "Dhawq Al Aali Al Bukhari"
            ],

            "Indian Food": [
                "Hammam W Maraq",
                "Qasr Al Liwan",
                "Najed Restaurant"
            ],

            "Mexican Food": [
                "Limonah",
                "RED . FOOD STREET"
            ]
        }
    },


    "Alinma Stadium": {

        "Cafe": {
            "Specialty Coffee": [
                "Sica Roastery",
                "Toby's Estate",
                "Cherie Cafe"
            ],

            "Coffee + Dessert": [
                "Comfy",
                "Urth",
                "Cherie Cafe"
            ],

            "Chill & Quiet": [
                "Seventies",
                "Comfy",
                "Urth"
            ]
        },

        "Restaurant": {
            "Burgers": [
                "Burger Boutique",
                "Nevermind Burger & Shakes"
            ],

            "Saudi Food": [
                "Najd Village"
            ],

            "Japanese / Asian": [
                "Nozomi",
                "MYAZU"
            ],

            "International": [
                "Prime Cut",
                "Rudy Pizzeria"
            ]
        }
    },


    "Aramco Stadium": {

        "Cafe": {
            "Specialty Coffee": [
                "95 Celsius The Village",
                "Dohat Alkeef Cafe",
                "Classic Coffee"
            ],

            "Coffee + Dessert": [
                "Caribou Coffee The Village",
                "The House Cafe",
                "Funsize Brew"
            ],

            "Chill & Quiet": [
                "Dohat Alkeef Cafe",
                "95 Celsius The Village",
                "Caribou Coffee The Village"
            ]
        },

        "Restaurant": {
            "Burgers & Fast Food": [
                "Texas Chicken - The Village",
                "Steak House",
                "Al Watan Burger"
            ],

            "Italian Food": [
                "Piatto Restaurant",
                "Sbarro Pizza & Pasta"
            ],

            "Asian Food": [
                "Canton",
                "Emurai Sushi"
            ],

            "Saudi Food": [
                "Labani Restaurant",
                "Masoub Raafat"
            ]
        }
    }
}


# =========================================================
# CSS
# SAME DESIGN AS LOGIN
# =========================================================

st.markdown(
    f"""
    <style>

    /* =========================
       GENERAL
       ========================= */

    .stApp {{
        background-image:
            linear-gradient(
                90deg,
                rgba(2, 13, 9, 0.97) 0%,
                rgba(2, 13, 9, 0.82) 35%,
                rgba(2, 13, 9, 0.45) 68%,
                rgba(2, 13, 9, 0.72) 100%
            ),
            linear-gradient(
                0deg,
                rgba(2, 13, 9, 0.80),
                rgba(2, 13, 9, 0.10)
            ),
            url("data:image/png;base64,{background_base64}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;

        color: white;
    }}


    .block-container {{
        padding-top: 1rem;
        padding-bottom: 4rem;
        max-width: 1450px;
    }}


    [data-testid="stSidebar"] {{
        display: none;
    }}


    #MainMenu,
    footer,
    [data-testid="stToolbar"],
    [data-testid="stHeader"] {{
        display: none;
    }}


    /* =========================
       NAV
       ========================= */

    .nav-brand {{
        font-size: 22px;
        font-weight: 900;
        letter-spacing: 2px;
        color: white;
        margin-top: 5px;
    }}

    .nav-country {{
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 3px;
        color: rgba(255,255,255,0.60);
        text-align: right;
        margin-top: 12px;
    }}


    /* =========================
       HERO
       ========================= */

    .eyebrow {{
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 4px;
        color: #d5aa4d;
        margin-top: 45px;
        margin-bottom: 18px;
    }}

    .hero-title {{
        font-size: clamp(45px, 5vw, 75px);
        line-height: 0.90;
        font-weight: 900;
        letter-spacing: -4px;
        color: white;
    }}

    .hero-gold {{
        color: #d5aa4d;
    }}

    .description {{
        max-width: 570px;
        font-size: 14px;
        line-height: 1.8;
        color: rgba(255,255,255,0.60);
        margin-top: 20px;
        margin-bottom: 40px;
    }}


    /* =========================
       SECTION LABEL
       ========================= */

    .section-label {{
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 3px;
        color: rgba(255,255,255,0.55);
        margin-bottom: 14px;
    }}


    /* =========================
       STADIUM NAME
       ========================= */

    .stadium-name {{
        font-size: 17px;
        font-weight: 800;
        color: white;
        margin-top: 12px;
        margin-bottom: 3px;
    }}

    .stadium-area {{
        font-size: 11px;
        letter-spacing: 1px;
        color: rgba(255,255,255,0.50);
        margin-bottom: 12px;
    }}


    /* =========================
       GLASS CONTAINERS
       ========================= */

    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.13),
                rgba(255,255,255,0.035)
            );

        border: 1px solid rgba(255,255,255,0.18);

        border-radius: 28px;

        box-shadow:
            0 30px 80px rgba(0,0,0,0.45);

        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }}


    /* =========================
       BUTTONS
       ========================= */

    div.stButton > button {{
        width: 100%;
        min-height: 45px;

        border-radius: 30px;

        border: 1px solid rgba(255,255,255,0.18);

        background:
            rgba(255,255,255,0.07);

        color: white;

        font-size: 10px;
        font-weight: 900;
        letter-spacing: 2px;

        transition: all 0.2s ease;
    }}


    div.stButton > button:hover {{
        border-color: #d5aa4d;
        color: #d5aa4d;
        background: rgba(213,170,77,0.10);
    }}


    div.stButton > button[kind="primary"] {{
        background:
            linear-gradient(
                100deg,
                #c49335,
                #f1ce78
            ) !important;

        color: #07120d !important;

        border: none !important;
    }}


    /* =========================
       SELECTBOX
       ========================= */

    div[data-baseweb="select"] > div {{
        background: rgba(0,0,0,0.28) !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        border-radius: 14px !important;
    }}

    div[data-baseweb="select"] span {{
        color: white !important;
    }}


    /* =========================
       RADIO
       ========================= */

    div[role="radiogroup"] label {{
        color: rgba(255,255,255,0.75) !important;
    }}


    /* =========================
       BUILD BUTTON
       ========================= */

    .build-button div.stButton > button {{
        min-height: 55px;

        background:
            linear-gradient(
                100deg,
                #c49335,
                #f1ce78
            ) !important;

        color: #07120d !important;

        border: none !important;

        box-shadow:
            0 10px 30px rgba(203,161,53,0.25);
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# NAV
# =========================================================

nav_left, nav_right = st.columns([1, 1])

with nav_left:

    st.markdown(
        '<div class="nav-brand">TAKTIK · تكتيك</div>',
        unsafe_allow_html=True
    )

with nav_right:

    st.markdown(
        '<div class="nav-country">SAUDI ARABIA · 2034</div>',
        unsafe_allow_html=True
    )


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="eyebrow">
        THE MATCH-DAY EXPERIENCE
    </div>

    <div class="hero-title">
        CHOOSE YOUR <span class="hero-gold">STADIUM.</span>
    </div>

    <div class="description">
        Choose your stadium, match and food preference.
        TAKTIK will build your personalized match-day experience.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 01 — STADIUM
# =========================================================

st.markdown(
    '<div class="section-label">01 · CHOOSE YOUR STADIUM</div>',
    unsafe_allow_html=True
)


stadium_items = list(stadiums.values())

stadium_columns = st.columns(
    len(stadium_items),
    gap="medium"
)


for index, stadium in enumerate(stadium_items):

    stadium_name = stadium["name"]

    with stadium_columns[index]:

        image_path = STADIUM_IMAGES.get(
            stadium_name
        )

        if image_path and image_path.exists():

            image = Image.open(
                image_path
            ).convert("RGB")

            # Make every stadium image the same ratio
            width, height = image.size

            target_ratio = 1.65

            current_ratio = width / height

            if current_ratio > target_ratio:

                new_width = int(
                    height * target_ratio
                )

                left_crop = (
                    width - new_width
                ) // 2

                image = image.crop(
                    (
                        left_crop,
                        0,
                        left_crop + new_width,
                        height
                    )
                )

            else:

                new_height = int(
                    width / target_ratio
                )

                top_crop = (
                    height - new_height
                ) // 2

                image = image.crop(
                    (
                        0,
                        top_crop,
                        width,
                        top_crop + new_height
                    )
                )

            st.image(
                image,
                use_container_width=True
            )

        st.markdown(
            f"""
            <div class="stadium-name">
                {stadium_name}
            </div>

            <div class="stadium-area">
                {stadium["area"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        is_selected = (
            st.session_state.selected_stadium
            == stadium_name
        )

        button_type = (
            "primary"
            if is_selected
            else "secondary"
        )

        if st.button(
            "SELECT",
            key=f"stadium_select_{index}",
            type=button_type,
            use_container_width=True
        ):

            st.session_state.selected_stadium = (
                stadium_name
            )

            st.session_state.selected_match = None

            st.session_state.food_type = None
            st.session_state.food_preference = None
            st.session_state.food_results = None

            st.rerun()


# =========================================================
# 02 — MATCH
# =========================================================

if st.session_state.selected_stadium:

    selected_name = (
        st.session_state.selected_stadium
    )

    selected_stadium = next(
        stadium
        for stadium in stadiums.values()
        if stadium["name"] == selected_name
    )

    st.write("")
    st.write("")

    with st.container(border=True):

        st.markdown(
            '<div class="section-label">'
            '02 · CHOOSE YOUR MATCH'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"### {selected_name}"
        )

        st.caption(
            f"{selected_stadium['area']} · "
            f"{selected_stadium['transport']}"
        )

        # -------------------------------------------------
        # Get matches from ORIGINAL taktik_logic.py
        # -------------------------------------------------

        available_matches = [
            match
            for match in matches.values()
            if match["stadium"] == selected_name
        ]

        # -------------------------------------------------
        # IMPORTANT:
        # Original data uses match["match"]
        # NOT home_team / away_team
        # -------------------------------------------------

        match_labels = []

        for match in available_matches:

            match_labels.append(
                f"{match['match']} · "
                f"{match['date']} · "
                f"{match['time']}"
            )

        selected_label = st.selectbox(
            "MATCH",
            match_labels
        )

        selected_match = available_matches[
            match_labels.index(
                selected_label
            )
        ]

        st.session_state.selected_match = (
            selected_match
        )


# =========================================================
# 03 — FOOD
# =========================================================

if st.session_state.selected_match:

    selected_name = (
        st.session_state.selected_stadium
    )

    st.write("")
    st.write("")

    with st.container(border=True):

        st.markdown(
            '<div class="section-label">'
            '03 · YOUR FOOD STOP'
            '</div>',
            unsafe_allow_html=True
        )

        food_type = st.radio(
            "TYPE",
            ["Cafe", "Restaurant"],
            horizontal=True
        )

        food_preferences = list(
            FOOD_OPTIONS[
                selected_name
            ][food_type].keys()
        )

        food_preference = st.selectbox(
            "PREFERENCE",
            food_preferences
        )

        food_results = FOOD_OPTIONS[
            selected_name
        ][food_type][food_preference]

        st.session_state.food_type = (
            food_type
        )

        st.session_state.food_preference = (
            food_preference
        )

        st.session_state.food_results = (
            food_results
        )


# =========================================================
# 04 — BUILD
# =========================================================

if (
    st.session_state.selected_stadium
    and st.session_state.selected_match
    and st.session_state.food_results
):

    st.write("")
    st.write("")

    build_left, build_right = st.columns(
        [1.4, 0.7],
        gap="large"
    )

    with build_left:

        st.markdown(
            "### YOUR MATCH-DAY IS READY"
        )

        st.caption(
            "Stadium selected · "
            "Match selected · "
            "Food stop selected"
        )

    with build_right:

        st.markdown(
            '<div class="build-button">',
            unsafe_allow_html=True
        )

        build = st.button(
            "BUILD MY MATCH DAY",
            type="primary",
            use_container_width=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        if build:

            # Keep the stadium as its NAME.
            # match_day.py will retrieve the
            # original stadium data from taktik_logic.py.

            st.session_state.selected_stadium = (
                selected_name
            )

            st.session_state.selected_match = (
                selected_match
            )

            st.session_state.food_type = (
                food_type
            )

            st.session_state.food_preference = (
                food_preference
            )

            st.session_state.food_results = (
                food_results
            )

            st.switch_page(
                "pages/match_day.py"
            )