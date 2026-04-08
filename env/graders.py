def grade_classification(message, action_content):
    if "charged twice" in message.lower() and action_content == "billing":
        return 1.0
    return 0.0


def grade_response(response_text):
    text = response_text.lower()
    if "refund" in text and "sorry" in text:
        return 1.0
    elif "refund" in text:
        return 0.7
    return 0.0


def grade_resolution(action_history):
    actions = [a["action_type"] for a in action_history]

    if "classify" in actions and "reply" in actions:
        return 1.0
    return 0.0