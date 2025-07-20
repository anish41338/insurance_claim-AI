def classify_claim(parsed_doc: dict) -> dict:
    """
    Dummy classification logic based on keywords.
    Replace this with trained ML later.
    """
    text = parsed_doc.get("raw_text", "").lower()

    if "fire" in text:
        category = "Property"
        priority = "High"
    elif "car accident" in text or "vehicle" in text:
        category = "Auto"
        priority = "Medium"
    elif "hospital" in text or "medical" in text:
        category = "Health"
        priority = "High"
    else:
        category = "General"
        priority = "Low"

    return {
        "category": category,
        "priority": priority,
        "summary": text[:200]
    }
