from typing import List, Dict

# Пример функции для чтения лог-файла и возврата его содержимого в виде списка строк
def read_log_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.readlines()

# Пример функции для фильтрации строк лог-файла по определенному критерию
def filter_log_entries(log_entries: List[str], keyword: str) -> List[str]:
    return [entry for entry in log_entries if keyword in entry]

# Пример функции для агрегации информации из лог-файла
def analyze_log_entries(log_entries: List[str]) -> Dict[str, int]:
    analysis_result = {}
    for entry in log_entries:
        # В этом примере просто подсчитываем количество вхождений каждого уникального слова
        words = entry.split()
        for word in words:
            analysis_result[word] = analysis_result.get(word, 0) + 1
    return analysis_result

# Пример использования функций
#dilnaz
log_file_path = 'C:/Users/mikas/Microsoft/Power BI Desktop Store App/WebView2/EBWebView/Default/Local Storage/leveldb/000003.log'
log_entries = read_log_file(log_file_path)
filtered_entries = filter_log_entries(log_entries, 'app')
analysis_result = analyze_log_entries(filtered_entries)
print(analysis_result)
