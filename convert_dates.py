import json
import re
from datetime import datetime

# Укажите путь к вашему исходному и конечному файлам JSON
input_file = 'fixtures/Сотрудники.json'
output_file = 'fixtures/Сотрудники.json'

# Функция для преобразования даты
def convert_date(date_str):
    try:
        # Попробуем распарсить дату в формате DD.MM.YYYY
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        # Вернем дату в формате YYYY-MM-DD
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return date_str  # Вернем исходную строку, если формат неверный

# Откройте исходный файл
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Преобразуем даты в правильный формат
for record in data:
    for field, value in record.items():
        if isinstance(value, str) and re.match(r'\d{2}\.\d{2}\.\d{4}', value):
            record[field] = convert_date(value)

# Сохраните обновленный файл
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Файл успешно обновлен и сохранен как {output_file}")





