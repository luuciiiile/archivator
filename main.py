import os
import time
import shutil
from _datetime import datetime


def deplace_file(fichier):
    if os.path.exists('maurituri_te_salutae'):
        print("hello")
        os.mkdir('maurituri_te_salutae')
    tail, head = os.path.split(fichier)
    src = fichier
    dest = 'maurituri_te_salutae/' + head
    shutil.move(src, dest)


def select_maurituri(fichier):
    metadata = os.stat(fichier)
    file_time = time.localtime(metadata.st_mtime)
    actual_time = datetime.now()

    actual_year = actual_time.year
    file_year = file_time.tm_year

    actual_month = actual_time.month
    file_month = file_time.tm_mon

    if actual_year - file_year == 1:
        if (actual_month == 3 and file_month >= 11) or (actual_month == 2 and file_month >= 10) \
                or (actual_month == 1 and file_month >= 9) or (actual_month == 4 and file_month == 12):
            deplace_file(fichier)
    if actual_year != file_year:
        deplace_file(fichier)
    else:
        if (actual_month - file_month) > 3:
            deplace_file(fichier)
    print(actual_time.month)
    print(file_time.tm_mon)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    select_maurituri('GPA.pdf')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
