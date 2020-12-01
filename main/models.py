from django.db import models
from django.utils import timezone
from django.urls import reverse

class image(models.Model):
	CHOICE =(
		('Dapartment', (('Biotechnology', 'Biotechnology'), ('Botany', 'Botany'), ('Chemestry', 'Chemestry'), ('Commerce', 'Commerce'), ('Computer Science', 'Computer Science'),
						('Economics', 'Economics'), ('Education', 'Education'), ('English', 'English'), ('History', 'History'), ('Mathematics', 'Mathematics'),
						('Physics', 'Physics'), ('Political Science', 'Political Science'), ('Socialogy', 'Socialogy'), ('Social Work', 'Social Work'), ('Zoology', 'Zoology'), ('PG', 'PG'))),
		('Clubs', (('AICUF', 'AICUF'), ('BSSM', 'BSSM'), ('Campus Ministry', 'Campus Ministry'), ('Cultural Club', 'Cultural Club'), ('Debating Society', 'Debating Society'),
						('Electoral Literacy Cell', 'Electoral Literacy Cell'), ('IT Club', 'IT Club'), ('Jesus Youth', 'Jesus Youth'), ('Maram Times', 'Maram Times'), ('Media Club', 'Media Club'),
						('Music Club', 'Music Club'), ('Nature Club', 'Nature Club'), ('NSS', 'NSS'), ('Poetry Club', 'Poetry Club'), ('Red Ribbon', 'Red Ribbon'), ('Rovers and Rangers', 'Rovers and Rangers'),
						('Science Club', 'Science Club'), ('Speech Club', 'Speech Club'), ('Sports Club', 'Sports Club'), ('Story Telling Club', 'Story Telling Club'), ('Women Cell', 'Women Cell'))),
		('Others', (('Sports Week', 'Sports Week'), ("Teachers Day", "Teachers Day"), ('Exams', 'Exams'), ('Others', 'Others')))
		)
	time = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=25, choices=CHOICE, default='Others')
	img = models.ImageField(upload_to='image')
	def date(self):
		return self.time.strftime('%b/%d/%y')
	def name(self):
		return self.title +" "+ str(self.id)
	
	def get_absolute_url(self):
		return reverse('upload')
