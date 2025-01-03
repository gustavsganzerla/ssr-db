from django.core.management.base import BaseCommand
import os
from database.models import Vntr


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

                if len(aux) == 11:
                    Vntr.objects.create( 
                        sequence = aux[2],
                        motif = aux[3],
                        repeat = aux[5],
                        start = aux[6],
                        end =aux[7],
                        length = aux[8],
                        clade = aux[9],
                        subclade = aux[10],
                )
        self.stdout.write(self.style.SUCCESS('VNTR data imported successfully'))