from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    # 작성자
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 게시글 제목
    title = models.CharField(max_length=200)
    # 게시글 내용
    text = models.TextField()
    # 게시글 작성 시각
    created_date = models.DateTimeField(default=timezone.now)
    # 게시글 게시 시각
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # 현재 시각을 저장
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # 제목을 보여줌
        return self.title
