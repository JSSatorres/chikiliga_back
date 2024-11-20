
def remove_diacritics(text):
    try:
        text = text.encode('latin-1').decode('utf-8')
    except UnicodeEncodeError as e:

        return f"UnicodeEncodeError: {e}. Unable to process the given text."
    return text