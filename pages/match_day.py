import streamlit as st
from pathlib import Path
import base64

from taktik_logic import (
    stadiums,
    activities_recommendation,
    recommend_hotels,
    hotels
)


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="TAKTIK | Your Match Day",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# PATHS
# =========================================================

ASSETS = Path(__file__).resolve().parent.parent / "assets"
BACKGROUND = ASSETS / "welcometosaudi34.png"


# =========================================================
# SESSION DATA
# =========================================================

selected_stadium_name = st.session_state.get("selected_stadium")
selected_match = st.session_state.get("selected_match")

food_results = st.session_state.get("food_results", [])
food_type = st.session_state.get("food_type", "")
food_preference = st.session_state.get("food_preference", "")


# =========================================================
# CHECK DATA
# =========================================================

if not selected_stadium_name or not selected_match:

    st.warning("Please build your match day first.")

    if st.button("← BACK TO PLANNER"):
        st.switch_page("pages/planner.py")

    st.stop()


# =========================================================
# FIND STADIUM
# =========================================================

selected_stadium = None

for stadium in stadiums.values():

    if stadium["name"] == selected_stadium_name:
        selected_stadium = stadium
        break


if selected_stadium is None:

    st.error("Selected stadium could not be found.")

    if st.button("← BACK TO PLANNER"):
        st.switch_page("pages/planner.py")

    st.stop()


# =========================================================
# BACKGROUND
# =========================================================

def get_base64_image(image_path):

    with open(image_path, "rb") as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode()


background_base64 = get_base64_image(BACKGROUND)


# =========================================================
# TEAM FLAGS
# =========================================================

TEAM_FLAGS = {
    "Saudi Arabia": "🇸🇦",
    "Argentina": "🇦🇷",
    "Brazil": "🇧🇷",
    "England": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "France": "🇫🇷",
    "Spain": "🇪🇸",
    "Germany": "🇩🇪",
    "Italy": "🇮🇹",
    "Portugal": "🇵🇹",
    "Netherlands": "🇳🇱"
}


# =========================================================
# TEAM NAMES
# =========================================================

home_team = selected_match["match"].split(" vs ")[0]
away_team = selected_match["match"].split(" vs ")[1]

home_flag = TEAM_FLAGS.get(home_team, "🏳️")
away_flag = TEAM_FLAGS.get(away_team, "🏳️")


# =========================================================
# ACTIVITIES
# =========================================================

try:

    selected_activities = activities_recommendation(
        selected_match
    )

except Exception:

    selected_activities = []


# =========================================================
# HOTELS
# =========================================================

try:

    selected_hotels = recommend_hotels(
        selected_stadium["name"]
    )

except Exception:

    selected_hotels = []


# If no hotels returned, use original hotels dictionary

if not selected_hotels:

    try:

        original_hotels = hotels.get(
            selected_stadium["name"],
            []
        )

        if isinstance(original_hotels, list):

            selected_hotels = sorted(
                original_hotels,
                key=lambda hotel: hotel.get(
                    "minutes",
                    999
                )
                if isinstance(hotel, dict)
                else 999
            )

    except Exception:

        selected_hotels = []


# =========================================================
# CSS
# =========================================================

st.markdown(
    f"""
    <style>

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

    /* NAV */

    .nav-brand {{
        font-size: 22px;
        font-weight: 900;
        letter-spacing: 2px;
        color: white;
    }}

    .nav-country {{
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 3px;
        color: rgba(255,255,255,0.60);
        text-align: right;
        margin-top: 10px;
    }}

    /* TITLES */

    .eyebrow {{
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 4px;
        color: #d5aa4d;
        margin-top: 35px;
        margin-bottom: 15px;
    }}

    .hero-title {{
        font-size: clamp(48px, 6vw, 82px);
        line-height: 0.9;
        font-weight: 900;
        letter-spacing: -4px;
        color: white;
    }}

    .hero-subtitle {{
        margin-top: 20px;
        font-size: 16px;
        line-height: 1.8;
        color: rgba(255,255,255,0.72);
    }}

    .section-label {{
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 3px;
        color: #d5aa4d;
        margin-bottom: 8px;
    }}

    .section-title {{
        font-size: 24px;
        font-weight: 800;
        color: white;
    }}

    .section-text {{
        font-size: 14px;
        line-height: 1.7;
        color: rgba(255,255,255,0.65);
    }}

    /* GLASS */

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

    /* TEAM */

    .team-flag {{
        font-size: 52px;
        text-align: center;
        line-height: 1;
        margin-bottom: 12px;
    }}

    .team-name {{
        font-size: 25px;
        font-weight: 900;
        text-align: center;
        color: white;
    }}

    .vs-text {{
        font-size: 12px;
        font-weight: 900;
        letter-spacing: 3px;
        color: #d5aa4d;
        text-align: center;
        padding-top: 50px;
    }}

    .match-info {{
        text-align: center;
        font-size: 14px;
        color: rgba(255,255,255,0.68);
        margin-top: 25px;
    }}

    /* HOTEL */

    .hotel-name {{
        font-size: 17px;
        font-weight: 800;
        color: white;
    }}

    .hotel-detail {{
        font-size: 12px;
        line-height: 1.7;
        color: rgba(255,255,255,0.60);
        margin-top: 8px;
    }}

    /* TIMELINE */

    .timeline-box {{
        border-left: 1px solid rgba(213,170,77,0.45);
        padding-left: 20px;
    }}

    .timeline-label {{
        font-size: 10px;
        font-weight: 900;
        letter-spacing: 2px;
        color: #d5aa4d;
    }}

    .timeline-title {{
        font-size: 15px;
        font-weight: 800;
        color: white;
        margin-top: 5px;
    }}

    .timeline-detail {{
        font-size: 12px;
        color: rgba(255,255,255,0.60);
        margin-top: 5px;
    }}

    /* BUTTON */

    div.stButton > button {{
        min-height: 48px;
        border-radius: 28px;
        background:
            linear-gradient(
                100deg,
                #c49335,
                #f1ce78
            );
        color: #07120d;
        border: none;
        font-size: 11px;
        font-weight: 900;
        letter-spacing: 2px;
    }}

    div.stButton > button:hover {{
        color: #07120d;
        border: none;
        transform: translateY(-2px);
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

nav_left, nav_right = st.columns([1, 1])

with nav_left:

    st.markdown(
        '<div class="nav-brand">TAKTIK · تكتيك</div>',
        unsafe_allow_html=True
    )

with nav_right:

    st.markdown(
        f'<div class="nav-country">'
        f'{selected_match["date"]} · SAUDI ARABIA · 2034'
        f'</div>',
        unsafe_allow_html=True
    )


# =========================================================
# BACK BUTTON
# =========================================================

if st.button("← BACK TO PLANNER"):

    st.switch_page("pages/planner.py")


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="eyebrow">YOUR PERSONALIZED EXPERIENCE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">'
    'YOUR <span style="color:#d5aa4d;">MATCH DAY.</span>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Everything you need. Exactly when you need it.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")


# =========================================================
# MATCH CARD
# =========================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-label">01 · YOUR MATCH</div>',
        unsafe_allow_html=True
    )

    left_team, middle, right_team = st.columns(
        [1, 0.25, 1]
    )

    with left_team:

        st.markdown(
            f'<div class="team-flag">{home_flag}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="team-name">{home_team}</div>',
            unsafe_allow_html=True
        )

    with middle:

        st.markdown(
            '<div class="vs-text">VS</div>',
            unsafe_allow_html=True
        )

    with right_team:

        st.markdown(
            f'<div class="team-flag">{away_flag}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="team-name">{away_team}</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div class="match-info">'
        f'{selected_match["date"]} · '
        f'{selected_match["time"]} · '
        f'{selected_stadium["name"]}'
        f'</div>',
        unsafe_allow_html=True
    )


# =========================================================
# FOOD + ACTIVITIES
# =========================================================

st.write("")
st.write("")

food_column, activities_column = st.columns(
    [1, 1],
    gap="large"
)


# =========================================================
# FOOD
# =========================================================

with food_column:

    with st.container(border=True):

        st.markdown(
            '<div class="section-label">02 · FOOD & DRINKS</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-title">Your food plan</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="section-text">'
            f'{food_type} · {food_preference}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.write("")

        if food_results:

            for food in food_results:

                st.markdown(
                    f'<div style="padding:12px 0; '
                    f'border-bottom:1px solid rgba(255,255,255,0.08);">'
                    f'<div style="font-size:15px; '
                    f'font-weight:800; color:white;">'
                    f'{food}'
                    f'</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )

        else:

            st.write(
                "No food recommendations available."
            )


# =========================================================
# ACTIVITIES
# =========================================================

with activities_column:

    with st.container(border=True):

        st.markdown(
            '<div class="section-label">03 · ACTIVITIES</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-title">Things to do</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-text">'
            'Recommended activities around your match date.'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        if selected_activities:

            for activity in selected_activities:

                if isinstance(activity, dict):

                    activity_name = activity.get(
                        "name",
                        activity.get(
                            "activity",
                            "Activity"
                        )
                    )

                    location = activity.get(
                        "location",
                        ""
                    )

                    time = activity.get(
                        "time",
                        ""
                    )

                    detail_parts = []

                    if location:
                        detail_parts.append(
                            str(location)
                        )

                    if time:
                        detail_parts.append(
                            str(time)
                        )

                    detail = " · ".join(
                        detail_parts
                    )

                else:

                    activity_name = str(activity)
                    detail = ""

                st.markdown(
                    f'<div style="padding:12px 0; '
                    f'border-bottom:1px solid rgba(255,255,255,0.08);">'
                    f'<div style="font-size:15px; '
                    f'font-weight:800; color:white;">'
                    f'{activity_name}'
                    f'</div>'
                    f'<div style="font-size:12px; '
                    f'color:rgba(255,255,255,0.60); margin-top:5px;">'
                    f'{detail}'
                    f'</div>'
                    f'</div>',
                    unsafe_allow_html=True
                )

        else:

            st.write(
                "No activities available for this match."
            )


# =========================================================
# HOTELS
# =========================================================

st.write("")
st.write("")

st.markdown(
    '<div class="section-label">04 · WHERE TO STAY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Recommended hotels</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-text">'
    'Hotels recommended from your selected stadium.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


if selected_hotels:

    hotel_count = min(
        3,
        len(selected_hotels)
    )

    hotel_columns = st.columns(
        hotel_count,
        gap="medium"
    )

    for index, hotel in enumerate(
        selected_hotels[:3]
    ):

        with hotel_columns[index]:

            if isinstance(hotel, dict):

                hotel_name = hotel.get(
                    "name",
                    hotel.get(
                        "hotel",
                        "Hotel"
                    )
                )

                minutes = hotel.get(
                    "minutes",
                    ""
                )

                price_min = hotel.get(
                    "price_min",
                    ""
                )

                price_max = hotel.get(
                    "price_max",
                    ""
                )

                stars = hotel.get(
                    "stars",
                    ""
                )

                distance = hotel.get(
                    "distance",
                    ""
                )

            else:

                hotel_name = str(hotel)
                minutes = ""
                price_min = ""
                price_max = ""
                stars = ""
                distance = ""

            hotel_details = []

            if stars:
                hotel_details.append(
                    f"{stars} stars"
                )

            if minutes:
                hotel_details.append(
                    f"{minutes} min from stadium"
                )

            elif distance:
                hotel_details.append(
                    str(distance)
                )

            if price_min and price_max:
                hotel_details.append(
                    f"{price_min} - {price_max} SAR/night"
                )

            elif price_min:
                hotel_details.append(
                    f"From {price_min} SAR/night"
                )

            if not hotel_details:

                hotel_details.append(
                    "Recommended accommodation"
                )

            with st.container(border=True):

                st.markdown(
                    f'<div class="section-label">'
                    f'HOTEL {index + 1}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="hotel-name">'
                    f'{hotel_name}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="hotel-detail">'
                    f'{" · ".join(hotel_details)}'
                    f'</div>',
                    unsafe_allow_html=True
                )

else:

    st.info(
        "No hotel recommendations available."
    )


# =========================================================
# TRANSPORT
# =========================================================

st.write("")
st.write("")

with st.container(border=True):

    st.markdown(
        '<div class="section-label">05 · GETTING AROUND</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Transport</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.write(
        selected_stadium["transport"]
    )


# =========================================================
# TIMELINE
# =========================================================

st.write("")
st.write("")

st.markdown(
    '<div class="section-label">06 · YOUR ITINERARY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Match-day timeline</div>',
    unsafe_allow_html=True
)

st.write("")


# BEFORE MATCH

st.markdown(
    '<div class="timeline-box">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="timeline-label">BEFORE THE MATCH</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="timeline-title">Activities</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="timeline-detail">'
    'Explore the recommended activities for your match date.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


# FOOD

st.markdown(
    '<div class="timeline-label">FOOD</div>',
    unsafe_allow_html=True
)

food_timeline = (
    food_results[0]
    if food_results
    else food_preference
)

st.markdown(
    f'<div class="timeline-title">'
    f'{food_timeline}'
    f'</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="timeline-detail">'
    f'{food_type}'
    f'</div>',
    unsafe_allow_html=True
)

st.write("")


# MATCH

st.markdown(
    f'<div class="timeline-label">'
    f'{selected_match["time"]}'
    f'</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="timeline-title">'
    f'{selected_match["match"]}'
    f'</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="timeline-detail">'
    f'{selected_stadium["name"]}'
    f'</div>',
    unsafe_allow_html=True
)

st.write("")


# HOTEL

if selected_hotels:

    first_hotel = selected_hotels[0]

    if isinstance(first_hotel, dict):

        first_hotel_name = first_hotel.get(
            "name",
            first_hotel.get(
                "hotel",
                "Recommended hotel"
            )
        )

    else:

        first_hotel_name = str(
            first_hotel
        )

else:

    first_hotel_name = "Recommended hotel"


st.markdown(
    '<div class="timeline-label">AFTER THE MATCH</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="timeline-title">'
    f'{first_hotel_name}'
    f'</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="timeline-detail">'
    'Your recommended place to stay.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# BACK
# =========================================================

st.write("")
st.write("")

if st.button(
    "← EDIT MY MATCH DAY",
    use_container_width=True
):

    st.switch_page(
        "pages/planner.py"
    )