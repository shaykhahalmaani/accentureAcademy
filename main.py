import streamlit as st
import random

st.set_page_config(page_title="Vote Shaykhah – Let’s Make This Journey Better", layout="centered")

# ----- Custom Styling -----
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2 {
            color: #A100FF;
        }
        .stButton>button {
            background-color: #A100FF;
            color: white;
            font-weight: 600;
            border-radius: 8px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #7a00cc;
        }
        .extracurricular-grid {
            display: flex;
            justify-content: space-around;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 1rem;
        }
        .extracurricular-item {
            width: 250px;
            text-align: center;
        }
        .extracurricular-item img {
            width: 100%;
            border-radius: 8px;
        }
        .extracurricular-item a {
            text-decoration: none;
            font-size: 0.9rem;
            color: #A100FF;
        }
    </style>
""", unsafe_allow_html=True)

# ----- HEADER -----
st.title("💡 Vote Shaykhah – Let’s Make This Journey Better")
st.image("header.gif", use_container_width=True)
st.markdown("---")

# ----- INTRO -----
st.header("👋 Hi, I’m Shaykhah")
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
Hi! I’m Shaykhah — a Cloud Technology Associate with a strong background in AI, student leadership, and real-world projects.

I’ve led communities, built solutions, and mentored tech talent — and now, I’d love to represent **you** in the Accenture Academy Student Council.

My goal? A council that’s not just symbolic, but actually *useful* — with events, energy, and ideas that make this journey better for all of us.
""")
with col2:
    st.image("me.jpeg", width=180)

st.markdown("""
<a href="https://www.linkedin.com/in/shaykha-almaani/" target="_blank" style="text-decoration: none;">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="20" style="vertical-align: middle; margin-right: 5px;">
    Let's connect on LinkedIn!
</a>
""", unsafe_allow_html=True)
st.markdown("---")

# ----- EXTRACURRICULARS -----
st.header("🪩 What I’ve Been Involved In")
cols = st.columns(3)

with cols[0]:
    st.image("technation.jpeg", caption=None, use_container_width=True)
    st.markdown("**Technation – President**", unsafe_allow_html=True)
    st.markdown("Led 19+ events, workshops, and a hackathon")
    st.markdown('[🔗 Technation on LinkedIn](https://www.linkedin.com/company/technation-clubb/)')

with cols[1]:
    st.image("tuwaiq.jpg", caption=None, use_container_width=True)
    st.markdown("**Tuwaiq Academy – TA**", unsafe_allow_html=True)
    st.markdown("Mentored 25+ trainees through AI projects")
    st.markdown('[🔗 Tuwaiq Academy](https://www.linkedin.com/school/tuwaiqacademy/)')

with cols[2]:
    st.image("GDSC.png", caption=None, use_container_width=True)
    st.markdown("**GDSC – Co-lead**", unsafe_allow_html=True)
    st.markdown("Helped run 10+ university-wide tech events")
    st.markdown('[🔗 GDSC ImamU](https://www.linkedin.com/company/gdsc-imamu/)')

# ----- IDEAS -----
st.markdown("---")
st.header("🎯 What I’d Love to Bring to Council")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("ideas.gif", width=250)

with st.expander("🔔 Ring the Bell! (Family Feud Style Face-Off)"):
    st.markdown("""
Two teams. One buzzer. Quick-fire questions and plenty of fun.

A fast-paced trivia game inspired by *Family Feud* to energize and bond teams across the Academy.
""")

with st.expander("🏆 Ace of the Week – Kahoot Challenge"):
    st.markdown("""
Weekly Kahoot quizzes to celebrate participation, learning, and a little healthy rivalry.

Top scorers get shoutouts and optional digital badges!
""")

with st.expander("🌍 Global Day Events – Do Good, Together"):
    st.markdown("""
I’d love to bring meaning into our moments — with light activities tied to global days:

- **Clean Air Day (Sep 7)** – Focus with friends in the *Forest* app 🌱  
- **Humanitarian Day (Aug 19)** – Join a local charity or give time digitally  
- **Charity Day (Sep 5)** – A donation drive or awareness boost  

Simple actions, big collective impact.
""")

# ----- BADGE -----
st.markdown("---")
st.header("🏅 Supporter Badge")

if st.button("🎖️ Unlock Your Badge"):
    st.balloons()
    st.success("You just earned the 💡 I Voted Shaykhah badge!")
    st.image("badge.png", caption="🗳️ Show your support!", use_container_width=False)

    with open("badge.png", "rb") as file:
        st.download_button(
            label="⬇️ Download Your Badge",
            data=file,
            file_name="I_Voted_Shaykhah.png",
            mime="image/png"
        )

# ----- CONTACT -----
st.markdown("---")
st.header("📬 Say Something")
msg = st.text_area("Send a thought, suggestion, or just say hi!")
if st.button("Send"):
    st.success("Thanks! I’ll read every message 💌")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("contact.gif", width=250)

# ----- FOOTER -----
st.markdown("""---  
Made with 💜 by [Shaykhah Almaani](https://www.linkedin.com/in/shaykha-almaani/)
""")


