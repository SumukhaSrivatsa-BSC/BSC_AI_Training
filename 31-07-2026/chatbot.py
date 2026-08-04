from policies import (
    RETURN_POLICY,
    REFUND_POLICY,
    DELIVERY_INFO,
    PAYMENT_METHODS,
    ORDER_STATUS
)


def get_order_status(order_id):
    order_id = order_id.upper()

    if order_id in ORDER_STATUS:
        status = ORDER_STATUS[order_id]
        return f"Your order {order_id} has been {status.lower()}."

    return "I could not find that order ID. Please check the order ID."


def shop_easy_reply(message):
    text = message.lower().strip()

    # Greeting
    if text in ["hi", "hello", "hey"]:
        return "Welcome to ShopEasy! How can I help you today?"

    # Order tracking
    if "where is my order" in text or "track my order" in text:
        return "Please provide your order ID."

    if text.upper().startswith("ORD"):
        return get_order_status(text)

    # Return
    if "return" in text:
        return RETURN_POLICY

    # Refund
    if "refund" in text:
        return REFUND_POLICY

    # Delivery
    if "delivery" in text or "how long" in text:
        return DELIVERY_INFO

    # Payments
    if "upi" in text:
        return "Yes, UPI is available."

    if "cash on delivery" in text or "cod" in text:
        return "Yes, Cash on Delivery (COD) is available."

    if "credit card" in text:
        return "Yes, Credit Card payment is available."

    if "debit card" in text:
        return "Yes, Debit Card payment is available."

    if "payment" in text and "failed" in text:
        return "Please check your payment details and try again. If the problem continues, please contact customer support."

    if "payment" in text:
        return "Available payment methods are: " + PAYMENT_METHODS

    # Products
    if any(word in text for word in ["laptop", "phone", "product", "products"]):
        return "ShopEasy has a range of products. Please tell me which product you are looking for."

    # Customer support
    if "contact" in text or "customer support" in text:
        return "Please contact ShopEasy customer support for further assistance."

    # Unknown question
    return (
        "Sorry, I could not understand your question. "
        "I can help with orders, delivery, returns, refunds, payments, and products."
    )