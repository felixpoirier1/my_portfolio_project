from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.CharField(primary_key = True, max_length= 50)
    name = models.CharField(max_length= 50)
    technology = models.CharField(max_length= 20, null=True, blank=True)
    theme = models.CharField(max_length= 20, null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField()
    git_hub_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class FilePath(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    path = models.TextField()

    def __str__(self):
        return self.description

