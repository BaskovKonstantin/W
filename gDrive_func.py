from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



def oAuth_console():

    ga = GoogleAuth()
    ga.CommandLineAuth()

    return ga

def make_copy(gAuth_source, gAuth_target, filename):




    file_source = get_file_by_name(gAuth_source, filename)
    file_source.GetContentFile(filename)

    drive = GoogleDrive(gAuth_target)

    file_target = drive.CreateFile({'title': filename})
    file_target.SetContentFile(filename)
    file_target.Upload()
    file_target.InsertPermission(
        {
        'type': 'anyone',
        'value': 'anyone',
        'role': 'writer'
        }
    )
    print('FILE TARGET ',file_target)

    file_source = None
    file_target = None
    pass

def get_file_by_name(gAuth, filename):

    drive = GoogleDrive(gAuth)
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file in fileList:
        if file['title'] == filename:

            file_id = file['id']
            file = drive.CreateFile(
            {'id': file_id})
            return file

def download_file(gAuth, username, filename):

    drive = GoogleDrive(gAuth)
    file = get_file_by_name(gAuth, filename)
    patch = str(username) + '/' + str(filename)
    print(patch)
    print(file)
    file.GetContentFile(patch)


def file_list(gAuth):

    drive = GoogleDrive(gAuth)
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file in fileList:
        print(f"Title: {file['title']} ID: {file['id']} LINK: {file['alternateLink']}")


def set_all_permission(googleFile):

    googleFile.InsertPermission(
        {
        'type': 'anyone',
        'value': 'anyone',
        'role': 'writer'
        }
    )

def upload_file(gAuth, name):

    drive = GoogleDrive(gAuth)
    file = drive.CreateFile({'title': name})
    file.SetContentFile(name)
    file.Upload()
    file.InsertPermission(
        {
        'type': 'anyone',
        'value': 'anyone',
        'role': 'writer'
        }
    )
    file = None

def get_link_per_name(gAuth, name):

    drive = GoogleDrive(gAuth)
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

    for file in fileList:
        # print(file)
        if (file['title'] == name):
            return file['alternateLink']

    return None