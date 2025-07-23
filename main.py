import streamlit as st

st.set_page_config(page_title="Vote Shaykhah – Let’s Make This Journey Better", layout="centered")

# ----- Force Light Mode Styling -----
st.markdown("""
    <style>
        body, .main, .block-container {
            background-color: white !important;
            color: black !important;
        }
        header, .st-emotion-cache-1avcm0n {
            background-color: white !important;
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
            color: white;
        }
        .stRadio > div {
            background-color: #f7f5fa;
            padding: 0.5rem;
            border-radius: 10px;
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

# ----- EXTRACURRICULARS SECTION -----
st.header("🪩 What I’ve Been Involved In")

# Create a "matrix-style" aligned layout
cols = st.columns(3)

activities = [
    {
        "image": "technation.jpeg",
        "caption": "Technation – President",
        "description": "*Led 19+ events, workshops, and a hackathon*",
        "link": "[🔗 Technation on LinkedIn](https://www.linkedin.com/company/technation-clubb/)"
    },
    {
        "image": "tuwaiq.jpg",
        "caption": "Tuwaiq Academy – TA",
        "description": "*Mentored 25+ trainees through AI projects*",
        "link": "[🔗 Tuwaiq Academy](https://www.linkedin.com/school/tuwaiqacademy/)"
    },
    {
        "image": "GDSC.png",
        "caption": "GDSC – Co-lead",
        "description": "*Helped run 10+ university-wide tech events*",
        "link": "[🔗 GDSC ImamU](https://www.linkedin.com/company/gdsc-imamu/)"
    }
]

for col, act in zip(cols, activities):
    with col:
        st.image(act["image"], caption=act["caption"], use_column_width=True)
        st.markdown(act["description"])
        st.markdown(act["link"])

# ----- IDEAS SECTION -----
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

# ----- BADGE UNLOCK -----
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

