from django.db import models
from datetime import datetime

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50, null=False)
    job = models.CharField(max_length=50, null=False)
    hiredate = models.DateTimeField(default=datetime.now) # 입사일자
    sal = models.IntegerField(null=False, default=0) # 급여

    # 급여인상 메서드
    def update_sal(self, sal):
        self.sal = sal