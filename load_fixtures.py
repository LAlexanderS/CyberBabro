import os
import subprocess
import sys

# Список файлов фикстур
fixtures = [
    'fixtures/Наименование станций метро_updated.json',
    'fixtures/Метро время пересадки между станциями_updated.json',
    'fixtures/Метро время между станциями_updated.json',
    'fixtures/Сотрудники_updated.json',
    'fixtures/Заявки_updated.json',
    'fixtures/Неявка пассажира_updated.json',
    'fixtures/Отмены заявок_updated.json',
    'fixtures/Переносы заявок по времени_updated.json',
    
]

def load_fixtures():
    python_executable = sys.executable  # Получаем путь к текущему интерпретатору Python
    successful_fixtures = []
    failed_fixtures = []

    for fixture in fixtures:
        try:
            # Используем команду manage.py loaddata для загрузки каждой фикстуры
            subprocess.run([python_executable, 'manage.py', 'loaddata', fixture], check=True)
            print(f"Успешно загружен файл: {fixture}")
            successful_fixtures.append(fixture)
        except subprocess.CalledProcessError:
            print(f"Ошибка при загрузке файла: {fixture}")
            failed_fixtures.append(fixture)

    return successful_fixtures, failed_fixtures

if __name__ == '__main__':
    successful_fixtures, failed_fixtures = load_fixtures()

    if successful_fixtures:
        print("\nУспешно загруженные файлы:")
        for fixture in successful_fixtures:
            print(f"- {fixture}")
    else:
        print("\nНет успешно загруженных файлов.")

    if failed_fixtures:
        print("\nФайлы с ошибками:")
        for fixture in failed_fixtures:
            print(f"- {fixture}")
    else:
        print("\nНет ошибок при загрузке файлов.")
