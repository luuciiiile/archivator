import glob
import os
import time
import shutil
from datetime import datetime


def deplace_file(fichier):
    """
    move the file from his original place to the to_archive directory
    :param fichier: the file to move
    :return: nothing
    """
    # if directory does not exist, create it
    if not os.path.exists('maurituri_te_salutant'):
        os.mkdir('maurituri_te_salutant')

    tail, head = os.path.split(fichier)
    src = fichier
    dest = 'maurituri_te_salutant/' + head

    shutil.move(src, dest)


def ave_cesar(fichier):
    """
    with the last modification date, define if the file need to go to the archive directory or not.
    :param fichier: file to be analyzed
    :return: nothing
    """
    # take the file metadata, extract the last modification date and the current date
    metadata = os.stat(fichier)
    file_time = time.localtime(metadata.st_mtime)
    current_time = datetime.now()

    # extract the year from the file and the current time
    current_year = current_time.year
    file_year = file_time.tm_year

    # extract the month from the file and the current time
    current_month = current_time.month
    file_month = file_time.tm_mon

    # if the file had been modified last year but at the end of the year, and we are at the beginning of the year,
    # check if there is a 3 months difference
    if current_year - file_year == 1:
        if (current_month == 3 and file_month >= 11) or (current_month == 2 and file_month >= 10) \
                or (current_month == 1 and file_month >= 9) or (current_month == 4 and file_month == 12):
            deplace_file(fichier)
    # if the file had been modified in another year, move it to the archive directory
    if current_year != file_year:
        deplace_file(fichier)
    # if the file had been modified the current year, if there is a 3 months difference, move it
    else:
        if (current_month - file_month) > 3:
            deplace_file(fichier)



# Press the green button in the gutter to run the script.
def search_for_file():
    """
    Recursively search in the current directory for all the files, including in subdirectories
    :return: a list of all the paths of all the files in the current directory.
    """
    listfichier = []
    for repertoire, sous_repertoire, fichier in os.walk('.'):
        for name in fichier:
            listfichier.append(os.path.join(repertoire, name))
    return listfichier


if __name__ == '__main__':
    maurituri = search_for_file()
    for potential in maurituri:
        ave_cesar(potential)
