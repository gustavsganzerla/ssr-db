from django.core.management.base import BaseCommand
import os
from database.models import Ssr


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

                if len(aux) == 12:
                    Ssr.objects.create(
                        sequence = aux[2],
                        standard = aux[3],
                        motif = aux[4],
                        repeat = aux[6],
                        start = aux[7],
                        end = aux[8],
                        length = aux[9],
                        clade = aux[10],
                        subclade = aux[11],
                )
        self.stdout.write(self.style.SUCCESS('SSR data imported successfully'))