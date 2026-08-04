import gradio as gr
from chatbot import shop_easy_reply


def chat(message, history):
    if not message.strip():
        return history

    answer = shop_easy_reply(message)

    history = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": answer}
    ]

    return history


with gr.Blocks(title="ShopEasy Customer Support") as demo:

    gr.Markdown("# ShopEasy Customer Support Chatbot")
    gr.Markdown(
        "Ask about orders, delivery, returns, refunds, payments, or products."
    )

    chatbot = gr.Chatbot(label="ShopEasy Support")

    with gr.Row():
        message = gr.Textbox(
            placeholder="Type your question here...",
            label="Your message"
        )

        send = gr.Button("Send")

    clear = gr.Button("Clear")

    send.click(
        chat,
        inputs=[message, chatbot],
        outputs=chatbot
    ).then(
        lambda: "",
        outputs=message
    )

    message.submit(
        chat,
        inputs=[message, chatbot],
        outputs=chatbot
    ).then(
        lambda: "",
        outputs=message
    )

    clear.click(
        lambda: [],
        outputs=chatbot
    )


if __name__ == "__main__":
    demo.launch() 