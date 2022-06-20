import os
import shutil

html_files = []

for address, dirs, files in os.walk("my_project"):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(f"{address}/{file}"))

for path in html_files:
    path_lst = path.split("/")
    path_str = ("/").join(path_lst[0:-1])
    shutil.copytree(path_str, f"my_project/templates/{path_lst[-2]}", dirs_exist_ok=True)








