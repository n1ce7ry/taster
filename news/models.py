from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "News"


    def __str__(self):
        return self.title
