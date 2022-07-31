import datetime
import requests
from YA_disk import YaDisk

def create_folder_yandex():
    ya_token = 'AQAAAABBAA-fAADLW7Lioz_T00K0h8dHXQInC_Y'
    response = YaDisk(ya_token)
    folder_name = input('Введите имя папки: ')
    request_response = response.create_folder_yandex_(folder_name)
    if request_response:
        return(folder_name)
    else:
        return ('')

if __name__ == '__main__':
    name_ = create_folder_yandex()
    print(name_)