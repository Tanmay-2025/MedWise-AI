def calculate_risk(answers):

    score = 0
    flags = []

    # Question 1
    if answers[1] == "Pharmacy without prescription":
        score += 3
        flags.append("Self-medication")

    elif answers[1] == "Leftover antibiotics":
        score += 3
        flags.append("Used leftover antibiotics")

    elif answers[1] == "Friend or family member":
        score += 4
        flags.append("Used antibiotics from another person")

    # Question 2
    if answers[2] == "Cold or flu":
        score += 3
        flags.append("Used antibiotics for viral infection")

    elif answers[2] == "Fever without consulting a doctor":
        score += 2
        flags.append("Possible self-medication")

    elif answers[2] == "Not sure":
        score += 1
        flags.append("Uncertain antibiotic use")

    # Question 3
    if answers[3] == "No":
        score += 3
        flags.append("Stopped antibiotic course early")

    # Question 4
    if answers[4] == "Yes":
        score += 2
        flags.append("Shared antibiotics")

    # Question 5
    if answers[5] == "Keep for future use":
        score += 2
        flags.append("Stored leftover antibiotics")

    elif answers[5] == "Give to someone else":
        score += 3
        flags.append("Shared leftover antibiotics")

    if score <= 3:
        level = "Low"

    elif score <= 8:
        level = "Moderate"

    else:
        level = "High"

    return {
        "score": score,
        "level": level,
        "flags": flags
    }