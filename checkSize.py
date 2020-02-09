from xml.dom import minidom
import xml
import os
list_annotations = os.listdir("./Annotations")
# print(list_annotations)
def checkSize(anno_file):
    file_name = "./Annotations/"+anno_file
    doc = xml.dom.minidom.parse(file_name)
    path = doc.getElementsByTagName("width")[0]
    checkSize = int(path.firstChild.data)
    if(checkSize == 0):
        print(anno_file)
        try:
            os.remove(file_name)
            print("Deleted file "+anno_file)
        except:
            print("File is not exist: "+anno_file)
for anno_dir in list_annotations:
  checkSize(anno_dir)