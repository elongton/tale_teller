from django.db import models

# Create your models here.
class User_input(models.Model):

	DEVELOPMENTAL_EDITING = 'DE'
	LINE_EDITING = 'LE'
	COPY_EDITING = 'CE'
	CREATIVE_CONSULTING = 'CC'
	
	EDITING_CHOICES = (
		(DEVELOPMENTAL_EDITING, 'Developmental Editing'),
		(LINE_EDITING, 'Line Editing'),
		(COPY_EDITING, 'Copy Editing'),
		(CREATIVE_CONSULTING, 'Creative Consulting'),

	)

	name = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	services_desired = models.CharField(max_length = 2,
										  choices = EDITING_CHOICES,
										  default = DEVELOPMENTAL_EDITING)
										  
	message = models.TextField()
	sample_upload = models.FileField(upload_to = '%Y_%m_%d')
	
	def __unicode__(self):
		return self.name