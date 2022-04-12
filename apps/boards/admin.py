from django.contrib import admin

from apps.boards.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass
    # list_display_links = ['user']
    # list_display = ['pk', 'user', 'policy_type', 'updated_at']
    # raw_id_fields = ['user'] # 관리자페이지에서 foreignkey 등록할때 밑으로 리스트 나오는게 아니라 검색으로 찾을 수 있게 해준다.
    # search_fields = ['user__username'] # text만 찾을 수 있는데, user는 fk이므로 객체이다. 그러므로 __username으로 접근
    # ordering = ['-updated_at']
