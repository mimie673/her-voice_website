# chatbot_ui.py  (100% working on Streamlit free tier)
import streamlit as st
import random

# ────── Custom CSS (pink theme) ──────
st.set_page_config(page_title="Her Voice GBV Chat", layout="centered")

st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #FF69B4, #FF1493, #FF6B9D);}
    .title-text {font-size: 3rem; color: white; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);}
    .subtitle-text {font-size: 1.5rem; color: white; text-align: center;}
    .chat-container {background: white; padding: 1.5rem; border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.1); height: 500px; overflow-y: auto; border: 3px solid #FF69B4;}
    .user-message {background:#FF69B4; color:white; padding:12px; border-radius:18px 18px 0 18px; max-width:80%; margin-left:auto; margin-bottom:10px;}
    .bot-message {background:#f0f0f0; color:#333; padding:12px; border-radius:18px 18px 18px 0; max-width:80%; margin-right:auto; margin-bottom:10px; border-left:4px solid #FF69B4;}
    .emergency {background:#FF4444; color:white; padding:1rem; border-radius:15px; text-align:center; margin:1rem 0;}
</style>
""", unsafe_allow_html=True)

# ────── Dataset of reassuring responses (no heavy model needed) ──────
RESPONSES = {
    "physical": [
        "I'm so sorry you're going through this. Your safety comes first. If you're in danger right now, call **997** immediately. "
        "You can also go to any police station and ask for the Victim Support Unit. Take photos of injuries and keep a secret diary of dates. "
        "You deserve to live without fear. Would you like me to guide you to a safe shelter?",
        "This is never your fault. You can get a **Protection Order** from the magistrate court for free. "
        "Call Women’s Legal Resources Centre on **01 771 222** – they help women get these orders quickly. "
        "You are strong for reaching out."
    ],
    "emotional": [
        "The insults and control are emotional abuse – it’s just as serious as physical violence. "
        "His words do NOT define your worth. Try writing down 3 things you love about yourself every day. "
        "You can talk to a counsellor free on **116** (toll-free, 24/7). You are worthy of respect.",
        "Feeling worthless is exactly what emotional abuse does. It’s meant to keep you small. "
        "You are not crazy, you are not overreacting. Many women have felt exactly like you and have rebuilt their confidence. "
        "Would you like daily affirmations or steps to set boundaries?"
    ],
    "default": [
        "Thank you for trusting me. Whatever you're facing, you don’t have to go through it alone. "
        "You can call the **GBV Helpline 116** anytime – it’s free and confidential. "
        "You can also submit an anonymous report on our website. Your voice matters.",
        "I'm here to listen without judgment. Tell me a little more and I’ll give you the exact steps you need."
    ]
}

def get_response(user_input: str) -> str:
    user_input = user_input.lower()
    if any(word in user_input for word in ["hit", "beat", "slap", "physical", "hurt"]):
        return random.choice(RESPONSES["physical"])
    if any(word in user_input for word in ["insult", "shout", "worthless", "control", "emotional"]):
        return random.choice(RESPONSES["emotional"])
    return random.choice(RESPONSES["default"])

# ────── Main App ──────
st.markdown('<h1 class="title-text">💖 Her Voice GBV Chat</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">You are safe here. Talk to me anytime.</p>', unsafe_allow_html=True)

# Emergency box (only once)
if "show_emergency" not in st.session_state:
    st.session_state.show_emergency = True

if st.session_state.show_emergency:
    st.markdown('<div class="emergency">🚨 EMERGENCY: Police 997 | Ambulance 998 | GBV Helpline 116</div>', unsafe_allow_html=True)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-message">You: {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">Her Voice: {msg["content"]}</div>', unsafe_allow_html=True)

# Input
if prompt := st.chat_input("Type your message here..."):
    st.session_state.show_emergency = False
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

# Quick buttons
st.markdown("### 💬 Common questions")
cols = st.columns(3)
with cols[0]:
    if st.button("He hits me"):
        st.session_state.messages.append({"role": "user", "content": "My husband hits me"})
        st.session_state.messages.append({"role": "assistant", "content": random.choice(RESPONSES["physical"])})
        st.rerun()
with cols[1]:
    if st.button("He insults me daily"):
        st.session_state.messages.append({"role": "user", "content": "He insults me everyday"})
        st.session_state.messages.append({"role": "assistant", "content": random.choice(RESPONSES["emotional"])})
        st.rerun()
with cols[2]:
    if st.button("I need help anonymously"):
        st.session_state.messages.append({"role": "user", "content": "How can I report anonymously?"})
        st.session_state.messages.append({"role": "assistant", "content": "You can use the 'Get Started' button on our homepage → it takes you to a completely anonymous reporting form. No name, no phone number needed."})
        st.rerun()

st.markdown("<br><br><p style='text-align:center; color:white;'>💖 You are strong. You are not alone. 💖</p>", unsafe_allow_html=True)