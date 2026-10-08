import streamlit as st
from pathlib import Path
import base64


# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="TAKTIK | تكتيك",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================
# PATHS
# =========================

ASSETS = Path(__file__).resolve().parent.parent / "assets"

BACKGROUND = ASSETS / "welcometosaudi34.png"


# =========================
# LOGIN STATE
# =========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# =========================
# BACKGROUND IMAGE
# =========================

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


background_base64 = get_base64_image(BACKGROUND)


# =========================
# CSS
# =========================

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

        color: white;
    }}


    .block-container {{
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1450px;
    }}


    [data-testid="stSidebar"] {{
        display: none;
    }}


    /* =========================
       TOP NAV
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

    .eyebrow-text {{
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 4px;
        color: #d5aa4d;
        margin-bottom: 18px;
    }}

    .hero-title {{
        font-size: clamp(55px, 6vw, 96px);
        line-height: 0.90;
        font-weight: 900;
        letter-spacing: -5px;
        color: white;
        margin: 0;
    }}

    .hero-gold {{
        color: #d5aa4d;
    }}

    .arabic-title {{
        font-size: 24px;
        font-weight: 500;
        color: rgba(255,255,255,0.88);
        margin-top: 25px;
    }}

    .description-text {{
        max-width: 520px;
        font-size: 15px;
        line-height: 1.8;
        color: rgba(255,255,255,0.65);
        margin-top: 20px;
    }}


    /* =========================
       LOGIN CARD
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

        padding: 35px;
    }}


    .login-title {{
        font-size: 26px;
        font-weight: 800;
        color: white;
        margin-bottom: 5px;
    }}

    .login-subtitle {{
        font-size: 13px;
        color: rgba(255,255,255,0.55);
        margin-bottom: 28px;
    }}


    /* =========================
       INPUTS
       ========================= */

    div[data-testid="stTextInput"] label {{
        color: rgba(255,255,255,0.55) !important;
        font-size: 10px !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
    }}

    div[data-testid="stTextInput"] input {{
        height: 52px !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        background: rgba(0,0,0,0.28) !important;
        color: white !important;
        padding-left: 18px !important;
        font-size: 14px !important;
    }}

    div[data-testid="stTextInput"] input:focus {{
        border-color: #d5aa4d !important;
        box-shadow: 0 0 0 1px #d5aa4d !important;
    }}


    /* =========================
       BUTTON
       ========================= */

    div.stButton > button {{
        width: 100%;
        height: 55px;
        margin-top: 18px;
        border: none;
        border-radius: 30px;

        background:
            linear-gradient(
                100deg,
                #c49335,
                #f1ce78
            );

        color: #07120d;

        font-size: 12px;
        font-weight: 900;
        letter-spacing: 2px;

        transition: all 0.25s ease;

        box-shadow:
            0 10px 30px rgba(203,161,53,0.25);
    }}

    div.stButton > button:hover {{
        transform: translateY(-3px);

        box-shadow:
            0 15px 35px rgba(203,161,53,0.4);

        color: #07120d;
        border: none;
    }}


    /* =========================
       FOOTER
       ========================= */

    .footer-text {{
        font-size: 10px;
        letter-spacing: 2px;
        color: rgba(255,255,255,0.45);
        margin-top: 45px;
    }}


    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 900px) {{

        .hero-title {{
            font-size: 58px;
        }}

        .description-text {{
            font-size: 14px;
        }}

        div[data-testid="stVerticalBlockBorderWrapper"] {{
            margin-top: 40px;
        }}

    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# TOP NAV
# =========================

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


# =========================
# SPACE
# =========================

st.write("")


# =========================
# MAIN LAYOUT
# =========================

left, right = st.columns(
    [1.35, 0.8],
    gap="large"
)


# =========================
# LEFT SIDE
# =========================

with left:

    st.markdown(
        '<div class="eyebrow-text">THE MATCH-DAY EXPERIENCE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-title">
            YOUR<br>
            <span class="hero-gold">MATCH.</span><br>
            YOUR<br>
            MOMENT.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="arabic-title">يومك الكروي… بتكتيك</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="description-text">
            One match. One city. One unforgettable day.
            <br><br>
            TAKTIK creates your personalized match-day
            experience — from the stadium to the final whistle.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# RIGHT SIDE — LOGIN
# =========================

with right:

    with st.container(border=True):

        st.markdown(
            '<div class="login-title">WELCOME TO TAKTIK</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-subtitle">Start your match-day journey.</div>',
            unsafe_allow_html=True
        )

        username = st.text_input(
            "USERNAME",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "PASSWORD",
            type="password",
            placeholder="Enter your password"
        )

        login = st.button(
            "ENTER TAKTIK",
            use_container_width=True
        )

if login:
    if username.strip() and password:
        st.session_state.logged_in = True
        st.session_state.username = username.strip()
        st.switch_page("pages/planner.py")
    else:
        st.error("Please enter a username and password.")


# =========================
# FOOTER
# =========================

footer_left, footer_right = st.columns([1, 1])

with footer_left:
    st.markdown(
        '<div class="footer-text">Your journey starts here · Saudi Arabia 2034</div>',
        unsafe_allow_html=True
    )

with footer_right:
    st.markdown(
        '<div class="footer-text" style="text-align:right;">TAKTIK</div>',
        unsafe_allow_html=True
    )