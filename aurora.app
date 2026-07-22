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
with st.sidebar:

    st.title("🎓 Aurora PG College")

    st.markdown("---")

    option = st.radio(
        "📌 Quick Navigation",
        [
            "🏠 Home",
            "💼 Career Domains",
            "📄 Resume Tips",
            "🎯 Interview Tips",
            "💻 Coding Platforms",
            "📚 Learning Resources",
            "ℹ️ About App"
        ]
    )

    st.markdown("---")

    if option == "🏠 Home":
        st.success("Welcome to Aurora PG College Career Assistant.")
        st.write(
            """
            This AI assistant helps students with:

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

    elif option == "💻 Coding Platforms":
        st.subheader("Practice Coding")

        st.write("""
        🔹 LeetCode

        🔹 HackerRank

        🔹 CodeChef

        🔹 GeeksforGeeks

        🔹 Codeforces
        """)

    elif option == "📚 Learning Resources":
        st.subheader("Learning Platforms")

        st.write("""
        📘 Coursera

        📘 Udemy

        📘 freeCodeCamp

        📘 NPTEL

        📘 YouTube

        📘 Kaggle
        """)

    elif option == "ℹ️ About App":
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

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

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
