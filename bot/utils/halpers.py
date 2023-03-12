# Функция для удаления лишних пробелов и знаков препинания
def preprocess_text(text):
    return ' '.join(text.split())
