from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from common.models import TimeStampedModel
from common.helpers import generate_slug

class Blog(TimeStampedModel):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog, self).save(*args, **kwargs)