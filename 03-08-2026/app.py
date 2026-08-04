import streamlit as st
from transformers import pipeline
from datetime import datetime


# ---------------- Page Setup ----------------

st.set_page_config(
    page_title="AI Text Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------- Styling ----------------

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    font-size: 17px;
    margin-bottom: 20px;
}

.chat-box {
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #cccccc;
    margin-bottom: 15px;
    word-wrap: break-word;
}

.answer-box {
    max-height: 350px;
    overflow-y: auto;
    white-space: pre-wrap;
}

.footer {
    text-align: center;
    margin-top: 30px;
    padding: 15px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- Load Hugging Face Model ----------------

@st.cache_resource
def load_model():

    model_name = "Qwen/Qwen2.5-0.5B-Instruct"

    model = pipeline(
        "text-generation",
        model=model_name
    )

    return model


# ---------------- Generate Answer ----------------

def generate_answer(question, temperature, max_length):

    question_lower = question.lower().strip()

    # Simple responses for common conversation questions
    if question_lower in ["hi", "hello", "hey", "hii", "hiii"]:
        return (
            "Hello! 👋 I am your AI Text Assistant. "
            "How can I help you today?"
        )

    if question_lower in [
        "who are you",
        "who are you?",
        "what are you",
        "what are you?"
    ]:
        return (
            "I am an AI Text Assistant. I can answer questions, "
            "explain concepts, and help you understand different topics."
        )

    if question_lower in [
        "how are you",
        "how are you?"
    ]:
        return (
            "I'm doing well! 😊 Ask me anything and I'll try "
            "to help you with a clear answer."
        )

    model = load_model()

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI assistant. "
                "Answer questions accurately and clearly. "
                "Use simple English when possible. "
                "Do not make up facts. "
                "For explanations, give enough detail to make "
                "the concept easy to understand."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    result = model(
        messages,
        max_new_tokens=max_length,
        temperature=temperature,
        do_sample=True,
        top_p=0.9,
        repetition_penalty=1.1
    )

    answer = result[0]["generated_text"][-1]["content"]

    return answer.strip()


# ---------------- Session State ----------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "clear_request" not in st.session_state:
    st.session_state.clear_request = False


# ---------------- Sidebar ----------------

with st.sidebar:

    st.header("⚙️ Model Settings")

    max_length = st.slider(
        "Maximum output length",
        30,
        250,
        120,
        10
    )

    temperature = st.slider(
        "Creativity / Temperature",
        0.1,
        1.5,
        0.7,
        0.1
    )

    st.divider()

    st.header("ℹ️ About the App")

    st.write(
        "AI Text Assistant is a Streamlit application "
        "that uses a lightweight Hugging Face instruction "
        "model to answer user questions."
    )

    st.write("**Model:** Qwen/Qwen2.5-0.5B-Instruct")

    st.write("**Developer:** N Rithika Mary")

    st.write("**Version:** 1.0")

    st.divider()

    if st.button(
        "🗑️ Clear Chat History",
        use_container_width=True
    ):

        st.session_state.clear_request = True


    if st.session_state.clear_request:

        st.warning(
            "Are you sure you want to clear the chat history?"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("Yes, Clear"):

                st.session_state.chat_history = []

                st.session_state.clear_request = False

                st.rerun()

        with col2:

            if st.button("Cancel"):

                st.session_state.clear_request = False

                st.rerun()


# ---------------- Main Page ----------------

st.markdown(
    '<div class="main-title">🤖 AI Text Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask a question and get a response from a Hugging Face AI model.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- Question Input ----------------

left_col, right_col = st.columns([2, 1])

with left_col:

    question = st.text_area(
        "Enter your question",
        placeholder="Example: Explain machine learning in simple words.",
        height=140,
        max_chars=1000
    )

with right_col:

    st.info(
        "💡 Tip\n\n"
        "Keep your question clear and specific "
        "for a better response."
    )

    st.caption("Maximum input length: 1000 characters")


# ---------------- Generate Button ----------------

generate = st.button(
    "✨ Generate AI Response",
    type="primary",
    use_container_width=True
)


if generate:

    if not question.strip():

        st.warning(
            "Please enter a question before generating a response."
        )

    elif len(question) > 1000:

        st.warning(
            "Your question is too long. "
            "Please keep it within 1000 characters."
        )

    else:

        try:

            with st.spinner("Generating AI response..."):

                answer = generate_answer(
                    question.strip(),
                    temperature,
                    max_length
                )

            current_time = datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

            st.session_state.chat_history.append(
                {
                    "time": current_time,
                    "question": question.strip(),
                    "answer": answer
                }
            )

        except Exception as error:

            st.error(
                "Something went wrong while generating the answer."
            )

            st.caption(
                f"Error details: {error}"
            )


# ---------------- Conversation History ----------------

st.divider()

st.subheader("💬 Conversation History")


if len(st.session_state.chat_history) == 0:

    st.info(
        "No conversation yet. Ask a question above to start."
    )

else:

    for item in reversed(st.session_state.chat_history):

        st.markdown(
            f"""
            <div class="chat-box">

            <b>🕒 {item['time']}</b>

            <br><br>

            <b>🙋 Question:</b><br>
            {item['question']}

            <br><br>

            <div class="answer-box">

            <b>🤖 AI Response:</b><br>
            {item['answer']}

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ---------------- Download History ----------------

    history_text = ""

    for item in st.session_state.chat_history:

        history_text += (
            "Time: " + item["time"] + "\n"
            "Question: " + item["question"] + "\n"
            "Answer: " + item["answer"] + "\n"
            + "-" * 60
            + "\n\n"
        )

    st.download_button(
        "⬇️ Download Chat History",
        data=history_text,
        file_name="chat_history.txt",
        mime="text/plain",
        use_container_width=True
    )


# ---------------- Footer ----------------

st.markdown(
    """
    <div class="footer">
        Developed by <b>N Rithika Mary</b>
        | AI Text Assistant v1.0
    </div>
    """,
    unsafe_allow_html=True
) 