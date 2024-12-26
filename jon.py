file_path = 'path/to/your/file.txt'
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
