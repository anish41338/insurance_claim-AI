def check_policy_compliance(claim_info: dict) -> dict:
    """
    Very basic compliance logic.
    Extend this with real business rules engine.
    """
    allowed_categories = {"Property", "Health", "Auto"}

    compliant = claim_info['category'] in allowed_categories
    notes = "Approved" if compliant else "Excluded by policy."

    return {
        "compliant": compliant,
        "notes": notes
    }
