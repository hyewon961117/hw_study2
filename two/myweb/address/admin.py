from django.contrib import admin
from address.models import Address

class AddressAdmin(admin.ModelAdmin):

    #화면에 출력할 필드 목록을 튜플로 지정
    list_display = ('name', 'tel', 'email', 'address')
    # 관리자 화면에 표시할 필드 목록

# 관리자 화면에 등록
admin.site.register(Address, AddressAdmin)