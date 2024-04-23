def remove_spaces(text):
    """Функция для удаления пробелов из строки."""
    return text.replace(" ", "")

def to_lower_case(text):
    """Функция для приведения строки к нижнему регистру."""
    return text.lower()

str1 = "Пример Текста Для Обработки"

result = map(to_lower_case(remove_spaces, str1))

print(list(result))