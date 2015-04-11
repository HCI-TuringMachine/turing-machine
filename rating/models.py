from django.db import models

# Create your models here.
class Requestor(models.Model):
	reqid = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	pay = models.PositiveSmallIntegerField()
	fair = models.PositiveSmallIntegerField()
	fast = models.PositiveSmallIntegerField()
	comm = models.PositiveSmallIntegerField()
	num_of_reports = models.PositiveIntegerField()
	joined_date = models.DateTimeField(default=None)

class Worker(models.Model):
	workerid = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	joined_date = models.DateTimeField(default=None)

class RequestorRating(models.Model):
	requestor = models.ForeignKey(Requestor)
	worker = models.ForeignKey(Worker)
	vote = models.PositiveSmallIntegerField()

class WorkerRating(models.Model):
	worker = models.ForeignKey(Worker)
	requestor = models.ForeignKey(Requestor)
	vote = models.PositiveSmallIntegerField()
