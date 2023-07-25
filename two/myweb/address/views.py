from django.shortcuts import redirect, render
from address.models import Address

# redirect : 방향 전환, 작업 완료 => 새로운 작업
# render : 요청한 데이터를 화면을 만들어서 표시하는 작업, 화면(template) 생성
# urls.py views urls

def home(request):
            # 요청사항 내장객체
    items = Address.objects.order_by("name")
            # 테이블  모든레코드들         필드명
    return render(request, 'address/list.html', {'items': items, 'address_count': len(items)})
         # 화면으로 이동

def write(request):
    return render(request, "address/write.html")

def insert(request):
    addr = Address(name=request.POST['name'], tel=request.POST['tel'], email=request.POST['email'], address=request.POST['address'])
    addr.save() # 레코드 저장
    return redirect("/address") # 방향 전환 - 목록으로 이동

# <input type='text name='변수명'>
# request.POST['변수명']
# post 보낼때 get 받을때 (방식)

def detail(request):
    addr=Address.objects.get(idx=request.GET['idx'])
    return render(request, 'address/detail.html', {'addr': addr})

def update(request):
    addr = Address( idx=request.POST['idx'], name=request.POST['name'], tel=request.POST['tel'], email=request.POST['email'], address=request.POST['address'] )
    addr.save()
    return redirect("/address")

def delete(request):
    Address.objects.get(idx=request.POST['idx']).delete()
    return redirect("/address")

# CRUD
# CREATE    레코드 생성
# READ      열람
# UPDATE    수정
# DELETE    삭제

