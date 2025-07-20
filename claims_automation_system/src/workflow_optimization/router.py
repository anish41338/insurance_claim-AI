def route_claim(claim_info: dict) -> str:
    """
    Route claim based on priority/category.
    """
    priority = claim_info["priority"]
    category = claim_info["category"]

    if priority == "High":
        return f"Route to {category} Urgent Review Team"
    elif priority == "Medium":
        return f"Route to {category} Processing Queue"
    else:
        return "Route to General Inbox"
