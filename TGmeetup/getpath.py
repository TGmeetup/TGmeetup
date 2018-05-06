#!/usr/bin/env python3
# coding=utf-8
import subprocess
from pathlib import Path


class GetPath():

    def get_mydir(self):
        cmd = "echo $HOME"
        output = subprocess.check_output(cmd, shell=True)
        myhome = str(output.splitlines()).split("'")[1]
        my_dir = Path(myhome + "/.config/TGmeetup")
        if(my_dir.is_dir()):
            return str(my_dir)
        else:
            return None
