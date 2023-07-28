from django.shortcuts import render, redirect
from memo.models import Memo

def home(request):
               # 테이블 전체 select * from memo_memo order by idx desc
    memoList = Memo.objects.order_by("-idx")
                            # -필드명 => 내림차순 정렬
    return render(request, 'memo/list.html', {'memoList': memoList, 'memoCount': len(memoList)})
             # 탬플릿 생성

def insert_memo(request):
    memo = Memo( writer=request.POST['writer'], memo=request.POST['memo'] )
    memo.save()
    # insert into memo_memo values(?,?)
    return redirect("/memo")
            # 레코드 저장이 완료되면 목록으로

def detail_memo(request):
    row=Memo.objects.get(idx=request.GET['idx'])
                            # 글번호
                    # select * from memo_memo where idx=?
    return render(request, 'memo/detail.html', {'row': row})

def update_memo(request):
    memo = Memo( idx=request.POST['idx'],
                 writer=request.POST['writer'],
                 memo=request.POST['memo'])
    memo.save()
    # update memo_memo set writer=?, memo=? where idx=?
    return redirect("/memo")
            # 목록으로 이동

def delete_memo(request):
    Memo.objects.get(idx=request.POST['idx']).delete()
                        # 삭제할 글번호
    return redirect("/memo")
            # 목록으로 이동

# urls.py           views.py             templates
# url-function  화면준비, 데이터처리         화면출력