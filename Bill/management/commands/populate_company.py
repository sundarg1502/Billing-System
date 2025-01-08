from django.core.management.base import BaseCommand
from Bill.models import Company

class Command(BaseCommand):
    def handle(self, *args, **options):
            Company.objects.all().delete()
            c_name = [
            "sri prasanna metal products",
            "Vanitha fireworks Industries",
            "Varshini fireworks",
            "Mori fireworks",
            "Sun moon industries",
            "Starwell fancy pyrolink",
            "Sri Thangavel chakravarthy fireworks",
            "Sri venkat vishva Metal",
            "Jairam fireworks industries",
            "Muthu Agencies",
            "Mariya Chemicals",
            "Shri Vahini Distributors",
            "Sri Paul Sticks",
            "Sri Nataraja trading company",
            "Sri Muthuraj Agency",
            ]
            
            mesh_30 = [750, 0, 0,0, 750, 0, 0, 700, 0, 750,0, 800,0,0,760]
            mesh_40 = [810,0, 850, 940, 810, 950, 810,0, 810, 810,0,0,0,900, 810]
            mesh_60 = [900,0,0,0, 850,0,0, 875,0,0, 900,0, 950,0,0]
            mesh_80 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 1050, 0]
            mesh_150 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
            mesh_30_40 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
            mesh_40_60 = [0, 1050, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
            mesh_60_80 = [0, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
            mesh_80_100 = [0, 400, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
            GSTIN = [
                "33AJHPM8551G1Z4",
                "33AAFFTT2327Q1ZW",
                "None",
                "33AAZFM9758L1Z4",
                "33ABBPT2662B1Z2",
                "33AENE62370C1Z7",
                "33ABYES1068DIZZ",
                "33AMGPM3134B12R",
                "33AAQEJ0261J1ZC",
                "33DVPPS3619C1ZG",
                "33ALXPA4909LIZR",
                "33ADTPH7673L1ZU",
                "33AERPA4149P1Z4",
                "33AANFS1973R1ZD",
                "33BMEPT2350R1ZL",
            ]
            TO = [
                "1243 Ganagiri road, Sivakasi-626189",
                "3-AA Maruthu pandiyar mettu street, Sivakasi Tamilnadu-626123",
                "1/150,1/151, Sangaranatham, Sankaranatham, Virudhunagar, Tamilnadu, 626203",
                "1319 Ganagiri road, Sivakasi-626189",
                "60 Gandhi road, Sivakasi-626123",
                "524/1, Anaikuttam village, Sivakasi Virudhunagar-626189",
                "No.1/184 Kangarsevel village, Sivakasi-626131 Tamilnadu",
                "460 B1 Virdhunagar road, Sivakasi",
                "K.S.A Rajadurai nagar, 2/665G Vilampatti road, Sivakasi west Virudhunagar, Tamilnadu-626123",
                "3/1429/16 Sattur road, Iswariya Nagar, Sivakasi",
                "3/666/1, Ponbalaji Nagar, Viswanatham village, Sattur road, Sivakasi, Virudhunagar-626189",
                "87, Gandhi road, Sivakasi",
                "No 2/1877, P.S.R Nagar, Sasi Nagar (Opp), Sivakasi-626123",
                "167 Chairman P.K.S.A Arumugam road, Sivakasi",
                "3/642-H Sattur road, Sivagamypuram Colony, Viswanatham, Sivakasi-626189",
            ]
            for name,add,gst,m30,m40,m60,m80,m150,m3040,m4060,m6080,m80100 in zip(c_name,TO,GSTIN,mesh_30,mesh_40,mesh_60,mesh_80,mesh_150,mesh_30_40,mesh_40_60,mesh_60_80,mesh_80_100):
                  Company.objects.create(c_name=name,toAddress=add,mesh_30=m30,mesh_40=m40,mesh_60=m60,mesh_80=m80,mesh_150=m150,mesh_30_40=m3040,mesh_40_60=m4060,mesh_60_80=m6080,mesh_80_100=m80100,gstIN=gst)

            self.stdout.write("Company Registered In the database")