from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.


class Article(models.Model):
    title = models.CharField(_("عنوان مقاله"), max_length=50)
    slug = models.SlugField(_("اسلاگ"), unique=True)
    author = models.ForeignKey(User, verbose_name=_(
        "نویسنده"), on_delete=models.CASCADE)
    content = models.TextField(_("محتوا"))
    publish = models.DateTimeField(_("تاریخ انتشار"), default=timezone.now)
    created = models.DateTimeField(_("تاریخ ایجاد"), auto_now_add=True)
    updated = models.DateTimeField(_("آپدیت مقاله"), auto_now=True)
    status = models.BooleanField(_("وضعیت"), default=False)

    def __str__(self):
        return self.title
