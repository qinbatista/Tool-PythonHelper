
import os
import sys
import time
import json
import threading
class GameManager:
    def __init__(self):
        self.__dir_path = os.path.dirname(os.path.realpath(__file__))

    def _push(self):
        folder_list = os.listdir(self.__dir_path)
        for folder_name in folder_list:
            if folder_name.find(".")==-1 and folder_name.find("@")==-1:
                os.chdir(self.__dir_path+'/'+folder_name)
                print("----------------------------------")
                os.system("pwd")
                os.system("git init")
                os.system("git remote add git https://github.com/qinbatista/"+folder_name+".git")
                os.system("git add .")
                os.system("git commit -m \"new update\"")
                os.system("git push git")
                os.chdir(self.__dir_path)
                os.system("pwd")
                print("updated repositoriy:"+folder_name)

if __name__ == '__main__':
    gm = GameManager()
    gm._push()
