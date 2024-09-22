from csv import reader
import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "vcx.settings"
)  # Replace with your actual project name
django.setup()

from vcx.api.models import Author  # Now import your model after django.setup()


def convert_to_authors(csv_file):
    try:
        with open(csv_file, newline="", encoding="utf-8") as file:
            csv_reader = reader(file)
            next(csv_reader)  # pula o cabeçalho
            authors = []
            for row in csv_reader:
                if row:  # Verifica se a linha não está vazia
                    authors.append(Author(name=row[0]))  # primeira coluna
                print(row[0])

            Author.objects.bulk_create(authors)
            return "Authors added"

    except Exception as e:
        print(e)


convert_to_authors("test.csv")
