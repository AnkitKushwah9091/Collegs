from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LikeModel(models.Model):
    class Meta:
        ordering = []
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        db_table = "PHOTOS_LIKES"
        unique_together = (('user', 'photo'),)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ForeignKey("PhotoModel",on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class CommentModel(models.Model):
    class Meta:
        ordering = []
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "PHOTOS_COMMENTS"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(auto_now=True)
    content = models.TextField()
    photo = models.ForeignKey("PhotoModel", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class PhotoAlbumModel(models.Model):
    class Meta:
        ordering = []
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        db_table = "PHOTOS_ALBUMS"

    name = models.CharField(max_length=30,default="Untitled")
    description = models.TextField(max_length=100,blank=True,null=True)
    cover_photo = models.ImageField(upload_to="",blank=True, null=True)
    location = models.CharField(max_length=50,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class PhotoModel(models.Model):
    class Meta:
        ordering = []
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        db_table = "PHOTOS"

    def post_photo_path(self,filename):
        file_name,extention = filename.split(".")
        filename = file_name+"."+extention
        return 'profile/{0}/posts/{1}'.format(self.user.username, filename)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    album = models.ForeignKey('PhotoAlbumModel',on_delete=models.CASCADE)
    caption = models.TextField(max_length=250,blank=True,null=True)
    photo = models.ImageField(upload_to=post_photo_path,blank=True, null=True)  
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def get_like_count(self):
        return LikeModel.objects.all(photo=self).count()

    @property
    def get_comment_count(self):
        return CommentModel.objects.all(photo=self).count()
