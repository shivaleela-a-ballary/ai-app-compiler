AMBIGUOUS_WORDS = [
    "something",
    "useful",
    "app",
    "platform",
    "system",
    "website"
]


def needs_clarification(prompt):

    prompt = prompt.lower()

    if len(prompt.split()) < 4:
        return True

    for word in AMBIGUOUS_WORDS:
        if prompt.strip() == word:
            return True

    if "something useful" in prompt:
        return True

    if "create an app" in prompt:
        return True

    return False


def clarification_questions():

    return [
        "What type of application do you want?",
        "Who are the users?",
        "What are the core features?",
        "Do you need authentication and roles?"
    ]