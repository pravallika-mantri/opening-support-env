def grade_classification(true_label, predicted):
    return 1.0 if true_label == predicted else 0.0


def grade_response(text):
    text = text.lower()

    if "sorry" in text and "refund" in text:
        return 1.0
    elif "sorry" in text:
        return 0.6
    return 0.0


def grade_resolution(text):
    return 1.0 if "resolved" in text else 0.0