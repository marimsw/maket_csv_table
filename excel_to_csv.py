import pandas as pd  
import csv

# Загрузка данных из Excel файла
file_path = '/content/output_file_modified.xlsx'
data = pd.read_excel(file_path)

# Извлечение данных из колонок
objects = data['OBJECTS'].tolist()
files = data['FILES'].tolist()

# Параметры для сохранения
save_dir = './'  # Укажите нужный путь для сохранения
output_csv = f"{save_dir}output4.csv"

# Создание и открытие CSV файла
with open(output_csv, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    # Запись заголовков в CSV файл
    writer.writerow(['file_name', 'categories'])  # Поменяли местами заголовки

    # Создание чанков по FILES
    chunk_size = 2  # Укажите размер чанка
    for i in range(0, len(files), chunk_size):
        chunk_files = files[i:i + chunk_size]
        chunk_objects = objects[i:i + chunk_size]

        # Запись данных в CSV файл
        for j in range(len(chunk_files)):
            category = chunk_objects[j]  # Первая колонка - category
            file_name = chunk_files[j]  # Вторая колонка - file_name
            writer.writerow([category, file_name])  # Поменяли порядок записи данных

print(f"Данные успешно сохранены в {output_csv}")
