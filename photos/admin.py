from django.contrib import admin
from .models import PhotoModel,PhotoAlbumModel,LikeModel,CommentModel
# Register your models here.
@admin.register(PhotoModel)
class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'album' ,'caption','date_created','date_modified']
    
 

@admin.register(PhotoAlbumModel)
class PhotoAlbumModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description' ,'location','date_created','date_modified']


@admin.register(LikeModel)
class LikeModelAdmin(admin.ModelAdmin):
    list_display = ['id','photo','user','date_liked']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['id','photo','user','content','date_commented']

