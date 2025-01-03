from django.core.management.base import BaseCommand
import os
from database.models import Issr


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type = str)

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r') as f:
            vetor_dados= f.readlines()
            vetor_dados = [line3.strip() for line3 in vetor_dados]
            for line in vetor_dados:
                aux = line.split('\t')

                if len(aux) == 16:

                    Issr.objects.create(
                        sequence = aux[2],
                        standard = aux[3],
                        motif = aux[4],
                        start = aux[6],
                        end = aux[7],
                        length = aux[8],
                        match = aux[9],
                        subsitution = aux[10],
                        insertion = aux[11],
                        deletion = aux[12],
                        score = aux[13],
                        clade = aux[14],
                        subclade = aux[15]
                )
        self.stdout.write(self.style.SUCCESS('ISSR data imported successfully'))