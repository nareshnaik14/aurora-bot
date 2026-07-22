import streamlit as st
from openai import OpenAI

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Aurora PG College Career Assistant",
    page_icon="🎓",
    layout="wide"
)

# ------------------------------
# OpenAI API Key
# ------------------------------
api_key = st.secrets.get("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY not found in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

# ------------------------------
# Sidebar
# ------------------------------
# ------------------------------
# Sidebar - API Key
# ------------------------------
with st.sidebar:

    st.title("🎓 Aurora PG College")

    st.markdown("### 🔑 OpenAI API Key")

    api_key = st.text_input(
        "Enter your OpenAI API Key",
        type="password",
        placeholder="sk-xxxxxxxxxxxxxxxxxxxxxxxx"
    )
with st.sidebar:
    st.title(" 🌐 Language")
    st.markdown("---")

    language = st.selectbox(
        "Choose Language",
        ["English", "Hinglish", "తెలుగు"]
)

with st.sidebar:

    st.title("🎓 Aurora PG College specifications")

    st.markdown("---")

    option = st.radio(
        "📌 Quick Navigation",
        [
            "🏠 Home",
            "💼 Career Domains",
            "📄 Resume Tips",
            "🎯 Interview Tips",
            
           
        ]
    )

with st.sidebar:

    st.title("📞 Contact Aurora PG College")

    st.subheader("🏫 College Address")

    st.write("""
    Aurora PG College

    nampally,

    Hyderabad,

    Telangana - 500001
    """)

    st.subheader("📞 Phone")

    st.write("""
    Admission Office: +91-XXXXXXXXXX

    Placement Cell: +91-XXXXXXXXXX
    """)

    st.subheader("📧 Email")

    st.write("""
    admissions@aurora.edu.in

    placements@aurora.edu.in
    """)

    st.subheader("🌐 Website")

    st.write("https://www.aurora.edu.in")

    st.subheader("🕒 Office Hours")

    st.write("""
    Monday - Saturday

    9:00 AM – 5:00 PM
    """)


    st.markdown("---")

    if option == "🏠 Home":
        st.success("Welcome to Aurora PG College Career Assistant.")
        st.write(
            """
            This aurora pg college helps students with:

            ✅ Career Guidance

            ✅ Placements

            ✅ Resume Building

            ✅ Mock Interview Preparation

            ✅ Government Jobs

            ✅ IT Jobs

            ✅ Higher Studies
            """
        )

    elif option == "💼 Career Domains":
        st.subheader("Popular Career Options")

        st.write("""
        • Software Developer

        • Data Scientist

        • AI & Machine Learning

        • Cyber Security

        • Cloud Computing

        • Testing

        • Business Analyst

        • Government Jobs

        • Banking

        • Digital Marketing
        """)

    elif option == "📄 Resume Tips":
        st.subheader("Resume Checklist")

        st.write("""
        ✔ Professional Summary

        ✔ Technical Skills

        ✔ Projects

        ✔ Certifications

        ✔ Education

        ✔ Achievements

        ✔ Contact Information
        """)

    elif option == "🎯 Interview Tips":
        st.subheader("Interview Preparation")

        st.write("""
        • Practice HR Questions

        • Learn Aptitude

        • Prepare Technical Questions

        • Improve Communication

        • Practice Mock Interviews

        • Research the Company
        """)


    elif option == "ℹ️ aurora pg college":
        st.info(
            """
            Aurora PG College Career Assistant

            Version: 1.0

            Powered by OpenAI GPT

            Designed for placement preparation,
            internships, career guidance,
            resume support and interview practice.
            """
        )




# ------------------------------
# Main Page
# ------------------------------

st.title("🎓 Aurora PG College Career Assistant")

st.write(
    """
    Your personalised career assistant for aurora pg students.
Welcome!

Ask anything related to:

• Placements

• IT Jobs

• Government Jobs

• Resume Building

• Interview Preparation

• Internships

• Coding

• Higher Studies
"""
)


# ------------------------------
# Chat History
# ------------------------------

translations = {
    "English": {
        "title": "🎓 Aurora PG College Career Assistant",
        "welcome": "Welcome!",
        "ask": "Ask about placements, careers, interviews, internships...",
        "home": "🏠 Home",
        "resume": "📄 Resume Tips",
        "interview": "🎯 Interview Tips"
    },

    "Hinglish": {
        "title": "🎓 Aurora PG College Career Assistant",
        "welcome": "Welcome!",
        "ask": "Placement, career ya interview ke baare mein puchiye...",
        "home": "🏠 Home",
        "resume": "📄 Resume Tips",
        "interview": "🎯 Interview Tips"
    },

    "తెలుగు": {
        "title": "🎓 ఆరోరా పీజీ కాలేజ్ కెరీర్ అసిస్టెంట్",
        "welcome": "స్వాగతం!",
        "ask": "ప్లేస్‌మెంట్స్, కెరీర్, ఇంటర్వ్యూల గురించి అడగండి...",
        "home": "🏠 హోమ్",
        "resume": "📄 రెజ్యూమ్ సూచనలు",
        "interview": "🎯 ఇంటర్వ్యూ సూచనలు"
    }
}

txt = translations[language]

st.title(txt["title"])
st.write(txt["welcome"])

#user_input = st.chat_input(txt["ask"])


if "messages" not in st.session_state:
    
    st.session_state.messages = [

        {
            "role": "system",
            "content": (
                "You are the Placement and Career Assistant for Aurora PG College. "
                "Help students with placements, internships, resume building, coding, "
                "communication skills, interview preparation, higher education, "
                "government jobs, aptitude preparation, and career planning. "
                "Respond using simple English and when suitable, use Hinglish. "
                "Provide practical, realistic, and student-friendly guidance."
            ),
        }
    ]

# ------------------------------
# Display Chat
# ------------------------------
for msg in st.session_state.messages:

    if msg["role"] == "system":
        continue

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ------------------------------
# User Input
# ------------------------------
user_input = st.chat_input(
    "Ask about placements, careers, interviews, internships..."
)

if user_input:

    """st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )"""

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):

        placeholder = st.empty()
        placeholder.write("🤖 Thinking...")

        try:

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=st.session_state.messages
            )

            ai_reply = response.choices[0].message.content

            placeholder.write(ai_reply)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": ai_reply
                }
            )

        except Exception as e:

            placeholder.error(f"Error: {e}")
