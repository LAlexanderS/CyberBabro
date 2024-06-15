import json
import re
from datetime import datetime

# Укажите путь к вашему исходному и конечному файлам JSON
input_file = 'fixtures/Переносы заявок по времени_updated.json'
output_file = 'fixtures/Переносы заявок по времени_final.json'

# Функция для преобразования формата времени
def convert_time_format(records, field):
    for record in records:
        if 'fields' in record and field in record['fields']:
            value = record['fields'][field]
            try:
                # Проверка текущего формата и преобразование
                if re.match(r'^\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}$', value):
                    datetime_obj = datetime.strptime(value, '%d.%m.%Y %H:%M:%S')
                    value = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
                    print(f"Преобразовано значение для поля {field} в записи {record['pk']}: {value}")
                elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', value):
                    # если формат уже правильный, но без таймзоны, просто подтверждаем
                    datetime_obj = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                    value = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
                # Сохранение значения в правильном формате
                record['fields'][field] = value
            except ValueError:
                print(f"Ошибка преобразования времени в записи: {record['pk']} поле: {field} значение: {value}")

# Откройте исходный файл
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Преобразование форматов времени
convert_time_format(data, 'time_edit')

# Сохраните обновленный файл
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Файл успешно обновлен и сохранен как {output_file}")













