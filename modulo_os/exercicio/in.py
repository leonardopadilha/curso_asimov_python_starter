import os

cwd = os.getcwd()
# print(cwd)

full_list = os.listdir(cwd)
# print(full_list)

files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]
# print(files_list)

types = list(set([i.split('.')[1] for i in files_list]))
# print(types)

for file_type in types:
  os.mkdir(file_type)

for file in files_list:
  from_path = os.path.join(cwd, file)
  to_path = os.path.join(cwd, file.split('.')[-1], file)

  os.replace(from_path, to_path)