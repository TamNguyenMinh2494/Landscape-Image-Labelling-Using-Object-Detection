import os
import cv2
with open("./predefined_classes.txt", "r", encoding="UTF-8") as file:
    code = ""
    pbtxt = ""
    classes = file.readlines()
    for i in range(len(classes)):
        code += "if row_label == '"+classes[i].strip()+"':\n"
        code += "\treturn "+str(i+1)+"\n"
        pbtxt += "item {\n\tname:\""+classes[i].strip()+"\"\n\tid:"+str(i+1)+"\n}\n"
    output = open("code.py", "w", encoding="UTF-8")
    output.write(code)
    output.close()
    output = open("label_map.pbtxt", "w", encoding="UTF-8")
    output.write(pbtxt)
    output.close()
        
