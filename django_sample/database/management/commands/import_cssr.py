from django.core.management.base import BaseCommand
import os
from database.models import Cssr


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

                if len(aux) == 14:

                    Cssr.objects.create(
                        sequence = aux[2],
                        start = aux[3],
                        end = aux[4],
                        motif = aux[5],
                        complexity = aux[6],
                        length = aux[7],
                        gap = aux[8],
                        component = aux[9],
                        structure = aux[10],
                        clade = aux[11],
                        subclade = aux[12],
                        type = aux[13]
                )
        self.stdout.write(self.style.SUCCESS('CSSR data imported successfully'))