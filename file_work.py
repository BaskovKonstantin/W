import os

def scan_user_folder(username, filename):

    files_list = os.listdir(username)
    return files_list