from django.db import models

from core.base.models.model_base import DateTimeModel


class Board(DateTimeModel):
    title = models.CharField(max_length=255, verbose_name='제목')
    content = models.TextField(verbose_name='본문 내용')
