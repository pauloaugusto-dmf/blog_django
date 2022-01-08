from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from datetime import datetime, timezone

from users.models import User


class Topic(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "topic"
        verbose_name_plural = "topics"

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="title")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True)
    alt = models.CharField(max_length=200, blank=True, default="")
    article = models.TextField()
    like = models.ManyToManyField(User, blank=True, related_name="blog_posts_like")
    dislike = models.ManyToManyField(
        User, blank=True, related_name="blog_posts_dislike"
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("publication:detail_post", kwargs={"slug": self.slug})

    def get_sum_likes(self):
        likes = self.like.count()
        return likes

    def get_sum_dislikes(self):
        dislikes = self.dislike.count()
        return dislikes

    def get_time(self):
        return format_data(self)


class Comment(TimeStampedModel):
    user = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE, default=None
    )
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE, default=None
    )
    text = models.TextField()

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.text

    def get_time(self):
        return format_data(self)


def format_data(date):
    # TODO refactor
    now = datetime.now(timezone.utc) - date.created
    if now.days == 0:
        now = str(now).split(":")
        if now[0] == "0":
            if now[1] == "00":
                return "Nesse momento"
            else:
                return (
                    f"Há {now[1]} minutos atrás"
                    if now[1] != "01"
                    else f"Há {now[1]} minuto atrás"
                )
        else:
            return (
                f"Há {now[0]} horas atrás"
                if now[0] != "1"
                else f"Há {now[0]} hora atrás"
            )
    else:
        return (
            f"Há {now.days} dias atrás"
            if now.days != "1"
            else f"Há {now.days} dia atrás"
        )
