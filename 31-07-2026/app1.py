import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
from chatbot import shop_easy_reply

st.set_page_config(page_title="ShopEasy AI Support", page_icon="🛍️", layout="wide")

st.markdown("""
<style>
.main{background:#f4f7fb;}
.block-container{padding-top:1.5rem;padding-bottom:2rem;}
.hero{
background:linear-gradient(90deg,#2563eb,#7c3aed);
padding:25px;border-radius:18px;color:white;margin-bottom:20px;
box-shadow:0 8px 20px rgba(0,0,0,.15);
}
.card{
background:white;
padding:18px;
border-radius:15px;
box-shadow:0 2px 12px rgba(0,0,0,.08);
height:100%;
}
.footer{
text-align:center;
color:#666;
padding:20px;
}
.stButton>button{
width:100%;
border-radius:10px;
font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages=[]
if "start" not in st.session_state:
    st.session_state.start=datetime.now()

# Sample data used for the Visualization Features section
@st.cache_data
def get_sample_data():
    categories = ["Order Tracking", "Delivery", "Returns", "Refunds", "Payments", "Products"]
    np.random.seed(42)
    data = pd.DataFrame({
        "Category": categories,
        "Tickets": np.random.randint(20, 120, size=len(categories))
    })
    return data

viz_data = get_sample_data()

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shopping-bag.png", width=70)
    st.title("ShopEasy")
    page=st.radio("Navigation",["🏠 Home","📊 Visualizations","ℹ️ About"])

    st.markdown("---")
    st.subheader("Support Areas")
    st.markdown("""
📦 Order Tracking

🚚 Delivery

↩️ Returns

💰 Refunds

💳 Payments

🛒 Products
""")

    users=sum(1 for m in st.session_state.messages if m["role"]=="user")
    bots=sum(1 for m in st.session_state.messages if m["role"]=="assistant")

    st.markdown("---")
    st.metric("👤 User Messages",users)
    st.metric("🤖 Bot Replies",bots)

    rating=st.slider("⭐ Rate",1,5,5)
    st.caption(f"{rating}/5")

    st.info(f"Started : {st.session_state.start.strftime('%H:%M:%S')}")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages=[]
        st.rerun()

if page=="ℹ️ About":
    st.markdown('<div class="hero"><h1>🛍️ ShopEasy Customer Support</h1><p>Professional Streamlit chatbot demo.</p></div>',unsafe_allow_html=True)
    st.markdown("""
### Technologies
- Python
- Streamlit
- Rule-Based Chatbot

### Features
- Chat Interface
- Sidebar Dashboard
- Quick FAQs
- Order Tracking
- Download Chat
- Visualization Dashboard
- Media & Status Widgets
- Modern UI
""")
    st.stop()

if page=="📊 Visualizations":
    st.markdown('<div class="hero"><h1>📊 Support Ticket Visualizations</h1><p>Native, Matplotlib, and Plotly views of ticket volume by category.</p></div>',unsafe_allow_html=True)

    st.header("Visualization Features")

    st.dataframe(viz_data, use_container_width=True)

    # Visualize the sample data with native, Matplotlib, and Plotly charts
    st.subheader("📈 Native Line Chart")
    st.line_chart(viz_data.set_index("Category")["Tickets"])

    st.subheader("📊 Native Bar Chart")
    st.bar_chart(viz_data.set_index("Category")["Tickets"])

    st.subheader("🌄 Native Area Chart")
    st.area_chart(viz_data.set_index("Category")["Tickets"])

    st.subheader("🧮 Matplotlib Chart")
    fig, ax = plt.subplots()
    ax.plot(viz_data["Category"], viz_data["Tickets"], marker="o", color="#7c3aed")
    ax.set_xlabel("Category")
    ax.set_ylabel("Tickets")
    ax.set_title("Ticket Volume by Category")
    plt.xticks(rotation=30)
    st.pyplot(fig)

    st.subheader("⚡ Plotly Chart")
    fig2 = px.bar(viz_data, x="Category", y="Tickets", color="Category",
                  title="Support Tickets by Category")
    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # ---------------- Media Features ----------------
    st.header("🎬 Media Features")
    st.caption("Uncomment and point to real files to enable these — placeholders shown below.")

    mcol1, mcol2, mcol3 = st.columns(3)

    with mcol1:
        st.markdown("**🖼️ Image**")
        # st.image("image.png")
        st.image("https://img.icons8.com/fluency/240/shopping-bag.png", caption="Sample product image", width=200)

    with mcol2:
        st.markdown("**🎵 Audio**")
        # st.audio("audio.mp3")
        st.caption("Upload an audio file to preview it here.")
        audio_file = st.file_uploader("Upload audio", type=["mp3", "wav", "ogg"], key="audio_uploader")
        if audio_file:
            st.audio(audio_file)

    with mcol3:
        st.markdown("**🎥 Video**")
        # st.video("video.mp4")
        st.caption("Upload a video file to preview it here.")
        video_file = st.file_uploader("Upload video", type=["mp4", "mov", "avi"], key="video_uploader")
        if video_file:
            st.video(video_file)

    st.divider()

    # ---------------- Status Features ----------------
    st.header("📶 Status Features")

    st.subheader("⏳ Progress Bar")
    if st.button("▶️ Run Progress Demo"):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
        st.success("Progress complete!")

    st.subheader("🔄 Spinner")
    if st.button("▶️ Run Spinner Demo"):
        with st.spinner("Processing..."):
            time.sleep(2)
        st.success("Done!")

    st.subheader("📭 Placeholder / Empty Container")
    placeholder = st.empty()
    placeholder.write("Temporary Message")
    if st.button("🔁 Refresh Placeholder"):
        placeholder.write(f"Updated at {datetime.now().strftime('%H:%M:%S')}")

    st.subheader("💹 Metric")
    scol1, scol2, scol3 = st.columns(3)
    scol1.metric("Revenue", "₹10 Lakhs", "+20%")
    scol2.metric("Active Orders", "342", "-5%")
    scol3.metric("Customer Satisfaction", "94%", "+2%")

    st.stop()

st.markdown("""
<div class="hero">
<h1>🛍️ ShopEasy AI Customer Support</h1>
<p>Helping customers 24×7 with Orders, Delivery, Returns, Refunds and Payments.</p>
</div>
""", unsafe_allow_html=True)

m1,m2,m3=st.columns(3)
m1.metric("👤 Users",users)
m2.metric("🤖 Replies",bots)
m3.metric("⭐ Rating",rating)

st.write("")

c1,c2,c3=st.columns(3)

with c1:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.subheader("⚡ FAQs")
    faq=st.selectbox("Quick Questions",[
        "",
        "Where is my order?",
        "Return Policy",
        "Refund",
        "Delivery",
        "Payment Methods",
        "Do you accept UPI?"
    ])
    if faq:
        with st.spinner("🤖 Fetching answer..."):
            time.sleep(0.8)
        st.success(shop_easy_reply(faq))
    st.markdown("</div>",unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.subheader("📦 Track Order")
    oid=st.text_input("Order ID",placeholder="ORD1234")
    if st.button("Track Order"):
        if oid:
            with st.spinner("Checking order..."):
                time.sleep(0.8)
            st.success(shop_easy_reply(oid))
        else:
            st.warning("Enter Order ID")
    st.markdown("</div>",unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.subheader("⚡ Quick Actions")
    for label,query in [("↩️ Return","return"),("💰 Refund","refund"),
                        ("🚚 Delivery","delivery"),("💳 Payment","payment")]:
        if st.button(label):
            st.info(shop_easy_reply(query))
    st.markdown("</div>",unsafe_allow_html=True)

st.divider()

left,right=st.columns([2,1])

with left:
    st.subheader("💬 Chat Assistant")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt=st.chat_input("💬 Ask ShopEasy anything...")

    if prompt:
        st.session_state.messages.append({"role":"user","content":prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.spinner("🤖 ShopEasy AI is checking your request..."):
            time.sleep(1)
            reply=shop_easy_reply(prompt)

        st.session_state.messages.append({"role":"assistant","content":reply})

        with st.chat_message("assistant"):
            st.write(reply)

with right:
    with st.expander("💡 Sample Questions",expanded=True):
        for q in [
            "Hi","Where is my order?","ORD1234","Refund",
            "Return Policy","Delivery","Payment Failed","UPI"
        ]:
            st.code(q)

    with st.expander("📜 Policies"):
        st.success(shop_easy_reply("return"))
        st.info(shop_easy_reply("refund"))

    with st.expander("⬇️ Download Chat"):
        text=""
        for m in st.session_state.messages:
            text+=f'{m["role"].capitalize()}: {m["content"]}\n\n'
        st.download_button("📄 Download",text,"ShopEasy_Chat.txt","text/plain")

st.markdown('<div class="footer">Made with ❤️ using Streamlit | © 2026 ShopEasy Demo</div>',unsafe_allow_html=True)