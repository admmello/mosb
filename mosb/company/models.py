from django.db import models


class Company(models.Model):
    cnpj = models.CharField(max_length=14, verbose_name='CNPJ', blank=True, null=True)
    name = models.CharField(max_length=150, verbose_name='nome')
    address = models.CharField(max_length=250, verbose_name='endereço', blank=True, null=True)
    logo = models.ImageField(verbose_name='logo', upload_to='companiesLogo', blank=True, null=True)
    status = models.BooleanField(default=True, verbose_name='ativo', blank=True)

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'

    def __str__(self):
        return self.name