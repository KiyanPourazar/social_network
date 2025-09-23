from django.contrib import admin

from .models import Post, PostFile

class PostFileInlineAdmin(admin.TabularInline):
    extra = 0
    model = PostFile
    fields = ('file',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'is_active', 'created_at')
    inlines = [PostFileInlineAdmin]
    # actions = None
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_add_permission(self, request, obj=None):
    #     return False
    #

# @admin.register(PostFile)
# class PostFileAdmin(admin.ModelAdmin):
#     pass