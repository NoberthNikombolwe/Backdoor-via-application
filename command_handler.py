# command_handler.py
import os
import subprocess

def execute_command(command):
    try:
        if command[:2] == "cd" and len(command) > 3:
            os.chdir(command[3:])

        task = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout, stderr = task.communicate()
        return stdout.decode() + stderr.decode()

    except Exception as e:
        return str(e)
