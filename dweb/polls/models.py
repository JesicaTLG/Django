from django.db import models

Class Question(model.Model):
    title= model.CharFiel(verbose_name= 'Titulo de la publicación ', max_Lengt=200)
    content = model.TexField(verbose_name='agrerga el contenido de la publicación')
    status = models.SmallIntegerField(verbose_name='indica el estado de la publicación')
    publishedDate = models.DataTimeField('especificar fecha de publiscación')
    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'    
