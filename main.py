from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from console import console_start
import gDrive_func


if __name__ == "__main__":
    gAuth_srv_drive = GoogleAuth()
    gAuth_srv_drive.LocalWebserverAuth() ###Основной гугл драйв
    console_start(gAuth_srv_drive)

