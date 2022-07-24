import os
import sys 
print(sys.argv)

dir_path = sys.argv[1]
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        print("file:", path)
    else:
        print("papka:", path)