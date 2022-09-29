
import os
import sys
import time
import json
import threading


class GitManager:
    def __init__(self, __dir_path=os.path.dirname(os.path.realpath(__file__))):
        self.__dir_path = __dir_path
        self.__folder_list = os.listdir(self.__dir_path)
        self.__repositories_list_name = "repositoriy_list.txt"
        self.__git_url = "ssh://qin@cq.qinyupeng.com:10022/Repositories/qin/"
        self._list_repositories()

    def _push(self):
        for folder_name in self.__folder_list:
            if os.path.isdir(self.__dir_path+'/'+folder_name):
                os.chdir(self.__dir_path+'/'+folder_name)
                print(f"Project:{'['+folder_name}]")
                os.system("pwd")
                os.system("git init")
                os.system(
                    f"git remote add cqhome {self.__git_url}/"+folder_name+".git")
                os.system("git add .")
                os.system("git commit -m \"new update\"")
                os.system("git push --set-upstream cqhome master")
                os.chdir(self.__dir_path)
                os.system("pwd")
                print("updated repositoriy:"+folder_name)

    def _git_list(self):
        repositoriy_list = []
        exist_repositoriy_list = []
        with open(f"{self.__dir_path}/repositoriy_list.txt", "r") as f:
            repositoriy_list = f.readlines()
        exist_repositoriy_list = os.listdir(self.__dir_path)
        for folder_name in exist_repositoriy_list:
            if folder_name.find(".") != -1:
                exist_repositoriy_list.remove(folder_name)
        new_repositoriy_list = list(
            set(repositoriy_list+exist_repositoriy_list))
        print(str(new_repositoriy_list))
        with open(f"{self.__dir_path}/repositoriy_list.txt", "w+") as f:
            f.seek(0)
            for line in new_repositoriy_list:
                if line != "\n" and line != "repositoriy_list.txt":
                    f.write(str(line))

    def _pull(self):
        with open(f"{self.__dir_path}/{self.__repositories_list_name}") as f:
            repositoriy_list = f.readlines()
        # folder_list = os.listdir(repositoriy_list)
        for repositoriy in repositoriy_list:
                repositoriy = repositoriy.replace("\n", "")
                # os.chdir(self.__dir_path+'/'+folder_name)
                print(f"[_pull]pulling[{repositoriy}]")
                # os.system("git init")
                os.system(f"git clone {self.__git_url}" +
                          repositoriy+".git")
                # os.system("git add .")
                # os.system("git commit -m \"new update\"")
                # os.system("git push git")
                # os.chdir(self.__dir_path)
                print("[_pull]Updated repositoriy:"+repositoriy)

    def _list_repositories(self):
        folder_list = []
        if os.path.isfile(f"{self.__dir_path}/{self.__repositories_list_name}"):
            with open(f"{self.__dir_path}/{self.__repositories_list_name}", "r") as f:
                folder_list = f.readlines()
        with open(f"{self.__dir_path}/{self.__repositories_list_name}", "a") as f:
            for folder_name in os.listdir(self.__dir_path):
                if os.path.isdir(self.__dir_path+'/'+folder_name):
                    if folder_name+"\n" not in folder_list:
                        f.write(folder_name+"\n")


if __name__ == '__main__':
    gm = GitManager()
    gm = gm._pull()
    # gm._push()
    # gm._list_repositories()
