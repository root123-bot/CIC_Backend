from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PostMedia)
admin.site.register(RawPost)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(PostLike)
admin.site.register(CommentLike)
admin.site.register(ReplyLike)
admin.site.register(DeviceAuthModel)
admin.site.register(DeviceNotificationToken)