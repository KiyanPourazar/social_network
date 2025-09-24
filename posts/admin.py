from django.contrib import admin

from .models import Post, PostFile, Comment, Like

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

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_approved')
    list_filter = ('is_approved',)
    date_hierarchy = 'created_at'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_liked')
    list_filter = ('is_liked',)
    date_hierarchy = 'created_at'