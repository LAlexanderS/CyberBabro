import json

# Укажите путь к вашему исходному и конечному файлам JSON
input_file = 'fixtures/Неявка пассажира.json'
output_file = 'fixtures/Отмены заявок_updated.json'

# Укажите имя вашего приложения и модели
app_name = 'applications'
model_name = 'NO'

# Откройте исходный файл
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создаем новую структуру данных
updated_data = []
for idx, record in enumerate(data, start=1):
    new_record = {
        'model': f'{app_name}.{model_name}',
        'pk': idx,
        'fields': record
    }
    updated_data.append(new_record)

# Сохраните обновленный файл
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(updated_data, file, ensure_ascii=False, indent=4)

print(f"Файл успешно обновлен и сохранен как {output_file}")




