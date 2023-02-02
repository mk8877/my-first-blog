from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)#文字数が制限されたテキストの定義
    text = models.TextField()#長いテキスト用
    creatrd_date = models.DateTimeField(default=timezone.now)#日付と時間のフィールド
    published_date = models.DateTimeField(blank=True,null=True)#     ,,

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title