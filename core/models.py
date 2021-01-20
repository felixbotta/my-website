from django.db import models


class Skill(models.Model):
    name = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição', blank=True)
    experience = models.CharField('Experiência', max_length=5, blank=True)
    img = models.ImageField(upload_to='skills/image', verbose_name='Imagem', null=True, blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['created_at']
    



