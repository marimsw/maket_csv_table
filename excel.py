import pandas as pd

# Укажите имя файла Excel
filename = '/content/drive/MyDrive/Rabota/Задачи от 28_01_2025/export_maquette 2.0.xlsx'  # замените на имя вашего файла

# Загрузка данных из Excel
df = pd.read_excel(filename)

# Проверяем, есть ли как минимум две колонки
if df.shape[1] < 2:
    raise ValueError("Файл должен содержать как минимум две колонки.")

# Создаем новый DataFrame для хранения результатов
new_rows = []

# Проходим по каждой строке
for index, row in df.iterrows():
    # Получаем значение из первой колонки
    first_col_value = row[0]

    # Получаем значение из второй колонки и разбиваем его по запятой
    second_col_values = str(row[1]).split(',')

    # Добавляем новые строки в новый DataFrame
    for value in second_col_values:
        new_rows.append([first_col_value, value.strip()])  # Убираем лишние пробелы

# Создаем новый DataFrame из собранных строк
new_df = pd.DataFrame(new_rows, columns=[df.columns[0], df.columns[1]])

# Сохраняем новый DataFrame в новый Excel файл
new_df.to_excel('output_file.xlsx', index=False)  # замените на желаемое имя выходного файла

print("Данные успешно обработаны и сохранены в 'output_file.xlsx'.")
