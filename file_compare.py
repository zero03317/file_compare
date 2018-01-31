#-*- coding:UTF-8 -*-
import hashlib
import os
from deepdiff import DeepDiff

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def wait():
    raw_input("Press Enter to exit...")
    exit(1)

def dict_compare(d1, d2):
    result=DeepDiff(d1,d2)
    print result
    if result=={}:
        print "file compare success!!"
        return True
    else:
        print"file compare fail!!!!!"
        print result
        return False


#print md5("C:\Users\N269-01\Desktop\iometer.txt")
def gene_dic(path):
    for dirPath, dirNames, fileNames in os.walk(path):
        diction_result={}
        lengther=0
        for f in fileNames:
            result=os.path.join(dirPath, f)
            #print result
            md5_result=md5(result)
            diction_result[f]=md5_result
            lengther +=1
            print "Data size:"+str(lengther)



        return diction_result


try:
    print "Please input source path (example:C:\\f1)"
    source_path=raw_input()
    if os.path.isdir(source_path):
        print "source path correct"
    else:
        print "path no exists pls try again"
        wait()
    print "Please input destination path (example : W:\\f1)"
    des_path=raw_input()
    if os.path.isdir(des_path):
        print "destination path correct"
    else:
        print "path no exists pls try again"
        wait()
    source=gene_dic(source_path)
    des=gene_dic(des_path)
    result=dict_compare(source,des)
    print result
    wait()
except Exception as error:
    print error
    wait()