from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(max_length=255, verbose_name="Nombre clave", unique=True)
    name = models.CharField(max_length=255, verbose_name="Red social")
    url = models.URLField(verbose_name="Enlace", max_length=255, blank= True, null=True)
    created = models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de modificación", auto_now=True)
    
    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["name"]
        
    def __str__(self):
        return self.name
    