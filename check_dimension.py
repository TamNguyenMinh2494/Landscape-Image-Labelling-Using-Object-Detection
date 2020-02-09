import cv2
import os
import shutil

DIR_ANNO = "BCS_OUT";
DIR = "BCS"

#Backup

#shutil.copy(DIR_ANNO,DIR_ANNO+"_backup")

countDeletion = 0

files = os.listdir(DIR)
for file in files:
    img = cv2.imread(DIR+"/"+file, cv2.IMREAD_UNCHANGED)
    deleted = False
    try:
        if img.shape[2] == 5:
            print("Error: "+file)
            deleted = True
            countDeletion +=1
    except:
        print("Except: "+file)
        deleted = True
        countDeletion+=1
    if deleted:
        try:
            os.unlink(DIR_ANNO+"/"+file[:-3]+"xml")
            print("Delete "+file[:-3]+"xml")
            print(str(countDeletion)+"/"+str(len(files)))
        except:
            print("Cannot delete "+file[:-3]+"xml")