from django.core.management.base import BaseCommand
from phrasebook.models import Language


def add_lang(lang):
    if Language.objects.filter(english_name=lang.english_name).count() == 0:
        lang.save()
        print(lang.english_name + " has been saved, id: " + str(lang.id))
    else:
        print(lang.english_name + " already exists in the database.")


def setup_langs():
    add_lang(Language(
        name="Français",
        english_name="French",
        flag_name="fra",
        color="#2222FF",
        hello="Bonjour"
    ))

    add_lang(Language(
        name="Svenska",
        english_name="Swedish",
        flag_name="swe",
        color="#0000FF",
        hello="Hej"
    ))

    add_lang(Language(
        name="Deutsch",
        english_name="German",
        flag_name="ger",
        color="#424242",
        hello="Hallo"
    ))

    add_lang(Language(
        name="Espagnol",
        english_name="Spanish",
        flag_name="spa",
        color="#ffe91d",
        hello="Hola"
    ))


class Command(BaseCommand):
    args = ""
    help = "Setup the Languages to be stored in the database"

    def handle(self, *args, **options):
        setup_langs()
