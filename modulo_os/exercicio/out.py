import os

cwd = os.getcwd()
# print(cwd)

folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]
# print(folder_list)

for folder in folder_list:
  path = os.path.join(cwd, folder)

  files = os.listdir(path)
  for file in files:
    from_path = os.path.join(path, file)
    to_path = os.path.join(cwd, file)
    os.replace(from_path, to_path)
  os.rmdir(path)