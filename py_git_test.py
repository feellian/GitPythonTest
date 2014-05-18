__author__ = 'sibuser'
import subprocess
from git import *
import os
import sys
import shutil


def run_bash(bash_command):
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    return process.communicate()[0]


class GitTest():
    def __init__(self):
        self.git_path = os.environ['HOME'] + '/git-boots-test'
        if os.path.exists(self.git_path):
            self.__remove_folder(self.git_path)

        os.mkdir(self.git_path)
        os.chdir(self.git_path)

        self.create_file('test.txt', 'test')

        self.git = Git(self.git_path)
        self.git.init()
        self.add('test.txt').commit('First commit')

    def add(self, filename):
        self.git.add(filename)
        return self

    def commit(self, message):
        self.git.commit('-m "' + str(message) + '"')
        return self

    def clean(self):
        pass
        run_bash('rm -rf ' + self.git_path)
        return self

    @staticmethod
    def __remove_folder(folder_name):
        shutil.rmtree(folder_name)

    def create_file(self, name=None, text=''):
        with open(name, 'w') as f:
            f.write(str(text) + '\n')
        return self
