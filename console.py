import gDrive_func
from dbMongo import find_link
from dbMongo import find_user
from dbMongo import insert_user
from dbMongo import insert_link
from gDrive_func import upload_file
from gDrive_func import download_file
from gDrive_func import oAuth_console
from gDrive_func import make_copy
from gDrive_func import get_link_per_name
from gDrive_func import file_list
import os

def console_start(gAuth):
    print('Console starting')
    login_or_register(gAuth)

def parce_command(gAuth, username):

    commandDict = dict()
    commandDict = {
        'upload': upload,
        'get_link': get_link,
        'download': download,
        'copy_file': copy_file,
        'help': help,

    }

    print('Input command')
    command = input()

    commandDict[command](gAuth, username)

def help(*args):

    print('avalible command')
    print('upload - upload file to google drive')
    print('get_link - get link to download from google drive')
    print('download - download file from google drive')
    print('copy_file - copy file from source account to target account')
    print('help - help')

def copy_file(gAuth_source, username, filename = None):

    print('Log in to the account from where the copy will be made')
    gAuth_target = oAuth_console()

    if (filename == None):
        print('Input filename')
        filename = input()

    patch = str(username) + '/' + str(filename)
    if (os.path.exists(patch)):
        make_copy(gAuth_source, gAuth_target, filename)
        link = get_link_per_name(gAuth_target, filename)
        print('LINK: ', link)
        insert_link(username, filename, link)
        return 1
    else:
        print('Cannot upload not existed file')
        return None


def download(gAuth, username):

    print('Input filename')
    filename = input()

    link = get_link(gAuth, username, filename)
    if (link != 'None'):

        print('Download link:', link)

    else:
        print('Can\'t get download link please get your account to copy file on your disk')
        Copyed = copy_file(gAuth, username, filename)
        if (Copyed == None):
            print('Some trouble with copy file we download this file at your folder')
            download_file(gAuth, username, filename)



def get_link(gAuth, username, filename = None):

    if (filename == None):
        print('Input filename')
        filename = input()

    link = find_link(username, filename)
    print(link)

    return link


def upload(gAuth, username):

    print('Input filename')
    filename = input()

    patch = str(username) + '/' + str(filename)
    if (os.path.exists(patch)):
        upload_file(gAuth, patch)
        link = get_link_per_name(gAuth, filename)
        insert_link(username, filename, link)
    else:
        print('Cannot upload not existed file')

def login_or_register(gAuth):
    print('Input \"login\" or \"l\" for login '
          'Input \"register\" or \"r\"')
    command = input()

    username = ''
    if (command == 'login' or command == 'l'):
        username = login()
    elif (command == 'register' or command  == 'r'):
        username = register()

    file_list(gAuth)
    while True:
        try:
            parce_command(gAuth, username)
        except Exception as e:
            print(e)
def login():

    print('Input username: ')
    username = input()
    if (find_user(username) != None):
        print('Input password: (NOT ENABLED)')
        password = input()
    else:
        print('User already exist ')
        register()

    return username

def register():

    print('Input username: ')
    username = input()
    if ( find_user(username) == None ):
        print('Input password: ')
        password = input()
        insert_user(username,password)

        os.makedirs(username)
    else:
        print('User already exist ')
        login()

    return username
    pass