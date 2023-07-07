import os
import shutil

from_dir = "D:/pythonprojects/project_111"
to_dir = "C:/Users/dell/OneDrive/Pictures/Documents/Desktop/class_112(2)"

list_of_file = os.listdir(from_dir)
# print(list_of_file)

for file_name in list_of_file:
    name,extension = os.path.splitext(file_name)
    # print(name)
    # print(extension)
    if extension == "":
        continue
    if extension in [".gif",".png",".jfif",".jpg",".jpeg"]:
        path1 = from_dir + '/'+ file_name
        path2 = to_dir + '/' + "image_files"
        path3 = to_dir + '/' + "image_files" +'/' + file_name

        if os.path.exists(path2):
            print("moving "+ file_name + "....")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("moving "+ file_name + "....")
            shutil.move(path1,path3) 



