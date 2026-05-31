import streamlit as st

st.set_page_config(
    page_title="planing  date with aynaz ❤️",
    page_icon="❤️",
    layout="centered"
)

# -----------------------------
# Session State
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "question"

if "no_count" not in st.session_state:
    st.session_state.no_count = 0

if "drink" not in st.session_state:
    st.session_state.drink = None

if "day" not in st.session_state:
    st.session_state.day = None

if "time" not in st.session_state:
    st.session_state.time = None

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(180deg,#fff5f8,#cf007f);
}

.main-title{
    text-align:center;
    color:#ff4f8b;
    font-size:55px;
    font-weight:bold;
    margin-top:50px;
}

.subtitle{
    text-align:center;
    font-size:24px;
    margin-bottom:30px;
}

.heart{
    text-align:center;
    font-size:60px;
}

.summary-box{
    background:#cd00cf;
    padding:30px;
    border-radius:20px;
    text-align:center;
    font-size:24px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# PAGE 1
# -----------------------------
if st.session_state.page == "question":

    messages = [
        "Will you be my tiramisu? 🍰",
        "Are you sure? 🥺",
        "Really sure? 😢",
        "Think again 😭",
        "Please? 💔",
        "Last chance 😭",
        "Don't break my heart 💔",
        "Only Yes remains 😎"
    ]

    current_message = messages[
        min(st.session_state.no_count, len(messages)-1)
    ]

    st.markdown(
        '<div class="heart">💌</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="main-title">{current_message}</div>',
        unsafe_allow_html=True
    )

    yes_size = min(
        1.0 + (st.session_state.no_count * 0.15),
        2.5
    )

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown(
            f"""
            <style>
            div[data-testid="stButton"] button {{
                height:60px;
                font-size:{20 * yes_size}px;
                border-radius:30px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        yes = st.button(
            "Yes ❤️",
            use_container_width=True
        )

        if st.session_state.no_count < 7:
            no = st.button(
                "No 😔",
                use_container_width=True
            )
        else:
            no = False

        if yes:
            st.session_state.page = "drink"
            st.rerun()

        if no:
            st.session_state.no_count += 1
            st.rerun()

# -----------------------------
# PAGE 2
# -----------------------------
elif st.session_state.page == "drink":

    st.markdown(
        '<div class="heart">❤️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-title">Great Choice!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Hot Chocolate or Tea?</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("☕ hot chocolate", use_container_width=True):
            st.session_state.drink = "Hot Chocolate ☕"
            st.session_state.page = "day"
            st.rerun()

    with col2:
        if st.button("🍵 Tea & tiramisu", use_container_width=True):
            st.session_state.drink = "Tea 🍵 & Tiramisu 🍰"
            st.session_state.page = "day"
            st.rerun()

# -----------------------------
# PAGE 3
# -----------------------------
elif st.session_state.page == "day":

    st.markdown(
        '<div class="main-title">📅 Choose a Day</div>',
        unsafe_allow_html=True
    )

    day = st.radio(
        "",
        [
            "Friday",
            "Saturday",
            "Sunday",
            "monday",
            "tuesday",
            "wednesday",
            "thursday"
        ]
    )

    if st.button("Next ➜", use_container_width=True):
        st.session_state.day = day
        st.session_state.page = "time"
        st.rerun()

# -----------------------------
# PAGE 4
# -----------------------------
elif st.session_state.page == "time":

    st.markdown(
        '<div class="main-title">🕒 Choose a Time</div>',
        unsafe_allow_html=True
    )

    selected_time = st.selectbox(
        "",
        [
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00"
        ]
    )

    if st.button("Confirm ❤️", use_container_width=True):
        st.session_state.time = selected_time
        st.session_state.page = "summary"
        st.rerun()

# -----------------------------
# PAGE 5
# -----------------------------
elif st.session_state.page == "summary":

    st.balloons()

    st.markdown(
        '<div class="main-title">🎉 babah babah datemun joor shod 😍 🎉</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="summary-box">

         eshiya getmamiz salina 😎 

        <br><br>

        ☕ Drink:
        {st.session_state.drink}

        <br><br>

        📅 Day:
        {st.session_state.day}

        <br><br>

        🕒 Time:
        {st.session_state.time}

        <br><br>

        🌹 Günleri sayıyorum 🥰

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("Start Over"):
        st.session_state.page = "question"
        st.session_state.no_count = 0
        st.session_state.drink = None
        st.session_state.day = None
        st.session_state.time = None
        st.rerun()
