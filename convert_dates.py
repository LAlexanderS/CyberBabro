import json
import re
from datetime import datetime

# Укажите путь к вашему исходному и конечному файлам JSON
input_file = 'fixtures/Переносы заявок по времени_updated.json'
output_file = 'fixtures/Переносы заявок по времени_final.json'

# Функция для преобразования формата времени
def convert_time_format(records):
    datetime_fields = ['time_edit']  # добавьте сюда любые другие поля, которые требуют преобразования формата
    for record in records:
        if 'fields' in record:
            for field in datetime_fields:
                if field in record['fields']:
                    value = record['fields'][field]
                    try:
                        # Проверка текущего формата и преобразование
                        if re.match(r'^\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}$', value):
                            datetime_obj = datetime.strptime(value, '%d.%m.%Y %H:%M:%S')
                            value = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
                        # Сохранение значения в правильном формате
                        record['fields'][field] = value
                    except ValueError:
                        print(f"Ошибка преобразования времени в записи: {record['pk']} поле: {field} значение: {value}")

# Откройте исходный файл
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Преобразование форматов времени
convert_time_format(data)

# Сохраните обновленный файл
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Файл успешно обновлен и сохранен как {output_file}")











