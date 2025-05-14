import os

def list_files(startpath, exclude_dirs=None, exclude_files=None, indent_char="    "):
    if exclude_dirs is None:
        # Додано більше типових каталогів для виключення
        exclude_dirs = [
            '.git', '__pycache__', 
            '.venv', 'venv', 'env',  # Типові назви віртуальних середовищ
            'node_modules', 
            'site-packages', # Важливо для виключення встановлених бібліотек
            'google-cloud-sdk', 
            'reports', 'screenshots',
            '.pytest_cache',
            'dist', 'build', '*.egg-info' # Типові каталоги для збірки
        ]
    if exclude_files is None:
        exclude_files = ['.DS_Store', '*.pyc', '*.log', '*.zip', '*.tar.gz']
    
    # Нормалізуємо startpath для коректного порівняння
    normalized_startpath = os.path.normpath(startpath)

    for root, dirs, files in os.walk(startpath, topdown=True):
        # Виключаємо непотрібні каталоги
        # dirs[:] = ... модифікує список dirs "на місці", щоб os.walk не заходив у ці каталоги
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Обчислюємо рівень вкладеності
        # Спочатку отримуємо відносний шлях від startpath до поточного root
        relative_path = os.path.relpath(root, startpath)
        if relative_path == ".": # Якщо це сам startpath
            level = 0
        else:
            level = relative_path.count(os.sep) + 1
            
        indent = indent_char * (level)
        
        # Виводимо назву поточного каталогу (крім самого startpath, який вже виведено)
        if normalized_startpath != os.path.normpath(root):
            print(f"{indent}{os.path.basename(root)}/")
        
        subindent = indent_char * (level + 1)
        for f_name in files:
            if f_name not in exclude_files and not f_name.endswith(('.pyc', '.log', '.zip', '.tar.gz')):
                print(f"{subindent}{f_name}")

if __name__ == '__main__':
    project_path = '.'  # Запускаємо з поточного каталогу
    
    # Виводимо назву кореневого каталогу проєкту
    # os.path.abspath('.') дасть повний шлях, наприклад /workspaces/auto-report-generator
    # os.path.basename(...) візьме останню частину, тобто auto-report-generator
    print(f"{os.path.basename(os.path.abspath(project_path))}/")
    
    list_files(project_path)
