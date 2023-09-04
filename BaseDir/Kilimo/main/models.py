from django.db import models
from django.contrib.auth import get_user_model
from Kilimo.officer.models import OfficerProfile

# Create your models here.
# all media of post will be stored in this model like images, videos, audio, document etc
class PostMedia(models.Model):
    media = models.FileField(upload_to='post_media/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# post consist of "paragram" then media, it can have, we can track it when he tried to save
# it a, just like u did in add review...
class Paragraphs(models.Model):
    paragraph = models.TextField()
    rawpost = models.ForeignKey('RawPost', on_delete=models.CASCADE, related_name="paragraphs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# how it will work we'll take it as content if you have as many as many paragraphs, we should assume 
# the "content" is first paragraph, we'll ask the user if he want to add another paragraph
# this will be posted by researcher to officer
class RawPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)
    media = models.ManyToManyField(PostMedia, blank=True)
    date_posted= models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title
    
    
# this will be posted by officer
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    media = models.ManyToManyField(PostMedia, blank=True)
    date_posted= models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    raw_post = models.OneToOneField(RawPost, on_delete=models.CASCADE, related_name="post")
    author = models.ForeignKey(OfficerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    commented_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)
    commented_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    reply = models.TextField()
    replied_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    replied_at = models.DateTimeField(auto_now_add=True)
    replied_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reply
    
class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    liked_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    liked_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title
    
class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
    liked_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    liked_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment.comment
    
class ReplyLike(models.Model):
    reply = models.ForeignKey(CommentReply, on_delete=models.CASCADE, related_name="likes")
    liked_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    liked_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reply.reply

class DeviceAuthModel(models.Model):
    modelId = models.CharField(max_length=255)
    pin = models.CharField(max_length=255)


class DeviceNotificationToken(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="notificationToken")
    deviceNotificationToken = models.CharField(max_length=255)
