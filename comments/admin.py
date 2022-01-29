from django.contrib import admin

from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "product",
        "is_accept",
        "time",
    ]

    class Meta:
        model = Comment
