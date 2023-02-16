import csv


def import_data(path: str):
    if '.csv' in path:
        with open(path) as file:
            archive = csv.DictReader(file, delimiter=',', quotechar='"')
            return list(archive)
    else:
        raise ValueError('Arquivo inválido')


print(import_data('src/aqr.csv'))
