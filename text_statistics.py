def create_bag_of_words(text):
    bag_of_words = {}
    for word in text.split():
        if word not in bag_of_words:
            bag_of_words[word] = 0
        bag_of_words[word] = bag_of_words[word] + 1

    return bag_of_words


def delete_stop_signs(text, stop_signs):
    for stop_sign in stop_signs:
        text = text.replace(stop_sign, "")
    return text


def create_bag_of_words_without_stop_sings(text, stop_signs=None):
    if stop_signs is None:
        stop_signs = [".", ",", "!", "?", "(", ")", ":", ";", "\"]

    text_without_stop_signs = delete_stop_signs(text, stop_signs)
    return create_bag_of_words(text_without_stop_signs)


