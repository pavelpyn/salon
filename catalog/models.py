from django.db import models


# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Каталог услуг'
        verbose_name_plural = 'Каталог услуг'

    def __str__(self):
        return self.name


class Service(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    price_man = models.DecimalField('Мужская стрижка, стоимость работы без материалов', max_digits=10,
                                    decimal_places=2, blank=True, null=True)
    price_man_material = models.DecimalField('Мужская стрижка, расходные материалы', max_digits=10,
                                             decimal_places=2, blank=True, null=True)
    price_man_all = models.DecimalField('Мужская стрижка, стоимость работы', max_digits=10, decimal_places=2,
                                        blank=True, null=True)
    price_1 = models.DecimalField('Цены(до 15 см)', max_digits=10, decimal_places=2, blank=True, null=True)
    price_nm_1 = models.DecimalField('Цены без расходных материалов1', max_digits=10, decimal_places=2, blank=True,
                                     null=True)
    price_2 = models.DecimalField('Цены(от 15 до 25 см)', max_digits=10, decimal_places=2, blank=True, null=True)
    price_nm_2 = models.DecimalField('Цены без расходных материалов2', max_digits=10, decimal_places=2, blank=True,
                                     null=True)
    price_3 = models.DecimalField('Цены(от 25 до 40 см)', max_digits=10, decimal_places=2, blank=True, null=True)
    price_nm_3 = models.DecimalField('Цены без расходных материалов3', max_digits=10, decimal_places=2, blank=True,
                                     null=True)
    price_4 = models.DecimalField('Цены(от 40 см и выше)', max_digits=10, decimal_places=2, blank=True, null=True)
    price_nm_4 = models.DecimalField('Цены без расходных материалов4', max_digits=10, decimal_places=2, blank=True,
                                     null=True)
    gender = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        index_together = ('id', 'slug')


    def __str__(self):
        return self.name
