from django.db import models
from django.core.validators import FileExtensionValidator


class Ourguards(models.Model):
    Ourguards_person = models.CharField(max_length=150)
    Ourguards_post = models.CharField(max_length=150, blank=True)
    Ourguards_img = models.ImageField(
        upload_to='ourguards/images/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    Ourguards_file = models.FileField(
        upload_to='ourguards/files/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Ourguards_person} ({self.Ourguards_post})"

    class Meta:
        ordering = ['-created_at']
