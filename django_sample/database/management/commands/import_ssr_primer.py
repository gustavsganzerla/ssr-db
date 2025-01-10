from django.core.management.base import BaseCommand
import os
from database.models import Ssr_primers


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type = str)

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r') as f:
            vetor_dados= f.readlines()
            vetor_dados = [line3.strip() for line3 in vetor_dados]
            for line in vetor_dados:
                aux = line.split(',')

                if len(aux) == 20:

                    Ssr_primers.objects.create(
                        sequence = aux[1],
                        standard = aux[2],
                        motif = aux[3],
                        repeat = aux[5],
                        start = aux[6],
                        end = aux[7],
                        length = aux[8],
                        product = aux[9],
                        forward = aux[10],
                        tm_forward = aux[11],
                        gc_forward = aux[12],
                        stability_forward = aux[13],
                        reverse = aux[14],
                        tm_reverse = aux[15],
                        gc_reverse = aux[16],
                        stability_reverse = aux[17],
                        clade = aux[18],
                        subclade = aux[19],


                )
        self.stdout.write(self.style.SUCCESS('ISSR data imported successfully'))