#from apply.views import delete  이거 뭐땜에 넣은거더라....?.?
from django.db import models

# Create your models here.
class Apply(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=3)
    say = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = "apply_img/", default='null') # 미디어파일을 받을 파일?폴더?명을 적어준것

    def __str__(self):
        return self.name

    # def summary(self):
    #     return self.say[:10]
   