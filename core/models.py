from django.db import models


class ModelProvider(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=255)
    provider = models.ForeignKey(ModelProvider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WorkloadRunner(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Workload(models.Model):
    enw = models.CharField(max_length=255, help_text='Enwiro environment name')
    workload_runner = models.ForeignKey(WorkloadRunner, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.enw
