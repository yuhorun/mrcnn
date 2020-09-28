import os

path = r"D:\标注\413-would\mrcnn\dataset\surgery\train\JPEGImages\2020-04-13T22.06.58.jpg"

(filepath, tempfilename) = os.path.split(path)
(filename, extension) = os.path.splitext(tempfilename)

print(filepath)