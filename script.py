import sys, os, subprocess, os.path

class git_script:
    def __init__(self, dir_path):
        self.dir_path = dir_path
    
    def git_func(self):
        os.mkdir(dir_path)
        os.chdir(dir_path)
        os.system('hub init && touch README.md && git add .git* && git commit -m "Initial commit"')
        os.system('sudo hub -o create ' + repo_name) 

repo_name = input('Repository name: ')
dir_path = os.path.join("/home/shub/Downloads/Projects/" , repo_name) #change the dir path to wherever you'd like to place the repo directories
final_path = git_script(dir_path)
final_path.git_func()

