import time
from django.db import transaction
from django.shortcuts import render
from transaction.models import Emp

def home(request):
    return render(request, 'transaction/index.html')

# 트랜잭션 처리 (1000개 중 하나라도 실패하면 실행 안됨)
@transaction.atomic()
def insert(request):
    start = time.time() # 시간측정
    Emp.objects.all().delete() # 모든 레코드 삭제
    for i in range(1, 1001): # 1~1000
        emp = Emp(empno=i, ename='name' + str(i), deptno=i)
        emp.save()

    end = time.time()
    runtime = end - start

    cnt = Emp.objects.count() # 레코드 수 카운트
    return render(request, 'transaction/index.html',
                  {'cnt': cnt, 'runtime': f'{runtime:.2f}초'})

def list(request):
    empList = Emp.objects.all().order_by('empno')
    return render(request, 'transaction/list.html',
                  {'empList': empList, 'empCount': len(empList)})

