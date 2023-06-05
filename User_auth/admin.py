from django.contrib import admin
from .models import PDF_Detail, Comment

class PDF_DetailAdmin(admin.ModelAdmin):
    list_display =  ('pdf_title', 'user')

admin.site.register(PDF_Detail, PDF_DetailAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('pdf_for', 'by_user', 'comment')

admin.site.register(Comment, CommentsAdmin)