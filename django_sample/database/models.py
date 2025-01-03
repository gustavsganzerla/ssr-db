from django.db import models

# Create your models here.
class Cssr(models.Model):
    #id	sequence	start	end	motif	complexity	length	gap	component	structure	clade	subclade	{type}
    id = models.BigAutoField(primary_key=True)
    sequence = models.CharField(max_length=200)
    start = models.IntegerField()
    end = models.IntegerField()
    motif = models.CharField(max_length=50)
    complexity = models.IntegerField()
    length = models.IntegerField()
    gap = models.IntegerField()
    component = models.CharField(max_length=50)
    structure = models.CharField(max_length=50)
    clade = models.IntegerField()
    subclade = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.sequence}, {self.start}, {self.end}, {self.motif}, {self.complexity}, {self.length}, {self.gap}, {self.component}, {self.structure}, {self.clade}, {self.subclade}"
    


class Issr(models.Model):
    #id	sequence	standard	motif	{type}	start	end	length	match	subsitution	insertion	deletion	score	clade	subclade
    id = models.BigAutoField(primary_key=True)
    sequence = models.CharField(max_length=200)
    standard = models.CharField(max_length=50)
    motif = models.CharField(max_length=50)
    start = models.IntegerField()
    end = models.IntegerField()
    length = models.IntegerField()
    match = models.IntegerField()
    subsitution = models.IntegerField()
    insertion = models.IntegerField()
    deletion = models.IntegerField()
    score = models.FloatField()
    clade = models.IntegerField()
    subclade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sequence}, {self.standard}, {self.motif}, {self.start}, {self.end}, {self.length}, {self.match}, {self.subsitution}, {self.insertion}, {self.deletion}, {self.score}, {self.clade}, {self.subclade}"


class Ssr(models.Model):
    #id	sequence	standard	motif	{type}	repeat	start	end	length	clade	subclade
    id = models.BigAutoField(primary_key=True)
    sequence = models.CharField(max_length=200)
    standard = models.CharField(max_length=50)
    motif = models.CharField(max_length=50)
    repeat = models.IntegerField()
    start = models.IntegerField()
    end = models.IntegerField()
    length = models.IntegerField()
    clade = models.IntegerField()
    subclade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sequence}, {self.standard}, {self.motif}, {self.repeat}, {self.start}, {self.end}, {self.length}, {self.clade}, {self.subclade}"
    

class Vntr(models.Model):
    #id	sequence	motif	{type}	repeat	start	end	length	clade	subclade
    id = models.BigAutoField(primary_key=True)
    sequence = models.CharField(max_length=200)
    motif = models.CharField(max_length=50)
    repeat = models.IntegerField()
    start = models.IntegerField()
    end = models.IntegerField()
    length = models.IntegerField()
    clade = models.IntegerField()
    subclade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sequence}, {self.motif}, {self.repeat}, {self.start}, {self.end}, {self.length}, {self.clade}, {self.subclade}"

