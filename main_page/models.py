from django.db import models

class WorkPost(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    #author : 추후 작성
    
    url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return f'[{self.pk}] {self.title}'
