from django.db import models


# Create your models here.

class QCSSC(models.Model):
    qihao = models.CharField('期号', max_length=10)
    wan = models.CharField('万', max_length=1)
    qian = models.CharField('千', max_length=1)
    bai = models.CharField('百', max_length=1)
    shi = models.CharField('十', max_length=1)
    ge = models.CharField('个', max_length=1)

    def __str__(self):
        return '期号：' + self.qihao + '----' + self.wan + '-' + self.qian + '-' + self.bai + '-' + self.shi + '-' + self.ge
