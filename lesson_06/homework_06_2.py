is_str_correct: bool = False

while not is_str_correct:
    provided_word: str = input("Provide your word please: ").lower()

    if provided_word.find("h") != -1:
        is_str_correct = True

