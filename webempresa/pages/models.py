from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    created = models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de modificación", auto_now=True)
    
    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ["order","title"]
        
    def __str__(self):
        return self.title
    