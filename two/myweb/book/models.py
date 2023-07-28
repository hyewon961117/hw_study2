from django.db import models

class Book(models.Model):
            # 상위클래스
    idx = models.AutoField(primary_key=True)
    # 필드명 = 자료형.자동증가일련번호(식별자)
    title = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)