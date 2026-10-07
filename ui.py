"""TAKTIK shared theme: clean, readable, interactive."""

import base64
import streamlit as st
from pathlib import Path


_A = Path(__file__).resolve().parent / "assets"

_f = next(iter(sorted(_A.glob("*ogo*"))), None) if _A.exists() else None

_LOGO = ""

if _f:
    _LOGO = (
        "url(data:image/jpeg;base64,"
        + base64.b64encode(_f.read_bytes()).decode()
        + ")"
    )


_CSS = """
<style>

html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: #040D09 !important;
}

.stApp {
    background:
        radial-gradient(
            circle at 85% 10%,
            rgba(94,53,150,.38),
            transparent 34%
        ),
        radial-gradient(
            circle at 5% 75%,
            rgba(0,122,61,.42),
            transparent 38%
        ),
        #040D09 !important;

    color: #fff !important;
}


/* ---------------------------------
   GLOBAL DECORATION
--------------------------------- */

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;

    background:
        repeating-linear-gradient(
            45deg,
            rgba(203,161,53,.035) 0 1px,
            transparent 1px 38px
        ),
        repeating-linear-gradient(
            -45deg,
            rgba(203,161,53,.035) 0 1px,
            transparent 1px 38px
        );

    z-index: 0;
}


/* ---------------------------------
   STREAMLIT CONTENT
--------------------------------- */

[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.block-container {
    position: relative;
    z-index: 2;
}


/* ---------------------------------
   HIDE STREAMLIT DEFAULT UI
--------------------------------- */

#MainMenu,
footer,
[data-testid="stToolbar"],
[data-testid="stHeader"] {
    display: none !important;
}


/* ---------------------------------
   TEXT
--------------------------------- */

.block-container {
    text-shadow: 0 2px 16px rgba(0,0,0,.75);
}

.eye,
.lab,
.sel,
.num,
.card small,
.stat small,
.sum span,
.steps,
.live,
.ready,
.foot,
.ft,
.chip span,
.tag {

    font-size: 14px !important;
    color: #F0CF6E !important;
    letter-spacing: 3px !important;
}


.desc,
.sub,
.meta,
.dt,
.card p,
.stat p,
.plan p,
.sum div,
.vs + .meta {

    font-size: 18px !important;
    color: rgba(255,255,255,.92) !important;
    line-height: 1.7;
}


.sub {
    font-size: 20px !important;
}

.ar {
    font-size: 44px !important;
    color: #fff !important;
}

.nm {
    font-size: 25px !important;
    color: #fff;
}

.stat h4 {
    font-size: 27px !important;
}

.card h3 {
    font-size: 36px !important;
}

.vs {
    font-size: 40px !important;
}

.ev b {
    font-size: 17px !important;
}

.chip b {
    font-size: 34px !important;
}

.sec {
    font-size: 40px !important;
}

.pr {
    font-size: 28px !important;
}

.stars {
    font-size: 18px !important;
}


/* ---------------------------------
   CARDS
--------------------------------- */

.chip,
.card,
.stat,
.food,
.hot,
.ev,
.sum {

    background: rgba(5,14,10,.66) !important;

    backdrop-filter: blur(18px);

    border: 1px solid
        rgba(203,161,53,.35) !important;
}


/* ---------------------------------
   STAGE
--------------------------------- */

.stage {
    background: rgba(0,0,0,.2) !important;
}


/* ---------------------------------
   PLAN
--------------------------------- */

.plan {
    background:
        linear-gradient(
            135deg,
            rgba(74,37,116,.78),
            rgba(0,108,53,.70)
        ) !important;
}


/* ---------------------------------
   SELECTBOX
--------------------------------- */

div[data-baseweb="select"] * {
    font-size: 19px !important;
    color: #fff !important;
}

div[data-baseweb="select"] > div {

    background: rgba(5,14,10,.75) !important;

    min-height: 62px !important;

    border:
        1.5px solid
        rgba(203,161,53,.55) !important;

}


/* ---------------------------------
   RADIO
--------------------------------- */

div[role="radiogroup"] label {

    background:
        rgba(5,14,10,.70) !important;

}

div[role="radiogroup"] p {

    font-size: 19px !important;
    font-weight: 800;

}


/* ---------------------------------
   BUTTONS
--------------------------------- */

div.stButton > button p {

    font-size: 16px !important;
    font-weight: 900;

}


/* ---------------------------------
   LOGO
--------------------------------- */

.brand {

    font-size: 0 !important;

    width: 200px;
    height: 74px;

    border-radius: 18px;

    background:
        #fff
        __LOGO__
        center / contain
        no-repeat;

    box-shadow:
        0 8px 30px rgba(0,0,0,.45),
        0 0 0 2px rgba(203,161,53,.7);

}


/* ---------------------------------
   GOLD
--------------------------------- */

.gold {

    filter:
        drop-shadow(
            0 4px 18px rgba(0,0,0,.6)
        );

}


/* ---------------------------------
   STREAMLIT ZERO HEIGHT IFRAMES
--------------------------------- */

iframe[height="0"] {
    display: none !important;
}

</style>
"""


_CSS = _CSS.replace("__LOGO__", _LOGO)


def theme():
    st.markdown(
        _CSS,
        unsafe_allow_html=True
    )