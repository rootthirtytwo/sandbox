import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("Path with current filename:  ",os.path.abspath(__file__))
print("Directory of file: ",os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
print(os.path.join(BASE_DIR, 'folder_name'))

