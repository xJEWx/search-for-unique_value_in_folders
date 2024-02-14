import os

# Функция для поиска уникального значения в файле rule
def find_value_in_file(file_path, unique_value):
    with open(file_path, 'r') as file:
        for line in file:
            if unique_value in line:
                return unique_value

# Функция для перебора папок и файлов
def search_folders(root_folder, unique_value):
    found = False
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file == "file.txt":
                file_path = os.path.join(root, file)
                value = find_value_in_file(file_path, unique_value)
                if value:
                    print("Уникальное значение '{}' найдено в файле:".format(unique_value), file_path)
                    print("Значение:", value)
                    found = True
                    break
        if found:
            print("В папке", root, "найдено уникальное значение")
            return True
    return False


def main():
    root_folder = "C:/path/"
    prefix = "" # если есть начальный префикс файла
    folders_to_check = [folder for folder in os.listdir(root_folder) if folder.startswith(prefix)]
    unique_value = input("Введите уникальное значение для поиска: ")
    result = False
    for folder in folders_to_check:
        full_folder_path = os.path.join(root_folder, folder)
        if search_folders(full_folder_path, unique_value):
            result = True
    if not result:
        print("Ничего не найдено")

if __name__ == "__main__":
    main()
