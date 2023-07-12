from django.db import models

# Create your models here.

#About
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"
    
    def __str__(self) -> str:
        return "About me"
    


#Service
class Service(models.Model):
    name = models.CharField(max_length=100000, verbose_name="Service name")
    description = models.TextField(verbose_name="About Service")
    
    def __str__(self) -> str:
        return self.name
    


#Recent work
class RecentWork(models.Model):
    title = models.CharField(max_length=100000, verbose_name="Work title")
    image = models.ImageField(upload_to="works")
    website = models.CharField(max_length=100000, verbose_name="Website Address", null=True)
    def __str__(self) -> str:
        return self.title



# #Client
# class Client(models.Model):
#     name = models.CharField(max_length=100000, verbose_name="Client name")
#     description = models.TextField(verbose_name="Client say")
#     image = models.ImageField(upload_to="clients", default="default.png")

#     def __str__(self) -> str:
#         return self.name