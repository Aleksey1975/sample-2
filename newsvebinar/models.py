from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When

#
# class Author(models.Model):
#     authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
#     ratingAuthor = models.IntegerField(default=0)
#
#     def update_rating(self):
#         postRat = self.post_set.aggregate(postRating=Sum('rating'))
#         pRat = 0
#         pRat += postRat.get('postRating')
#
#         commentRat = self.authorUser.post_set.aggregate(commentRating=Sum('rating'))
#         cRat = 0
#         cRat += commentRat.get('commentRating')
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=64, unique=True)
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class Post(models.Model):
#     NEWS = 'NE'
#     ARTICLE = 'AR'
#     CATEGORY_CHOICES = (
#         (NEWS, 'Новость'),
#         (ARTICLE, 'Статья')
#     )
#     categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     dateCreation = models.DateTimeField(auto_now_add=True)
#     postCategory = models.ManyToManyField(Category, through='PostCategory')
#     title = models.CharField(max_length=128)
#     text = models.TextField()
#     rating = models.IntegerField(default=0)
#
#     def preveiw(self):
#         return f'{self.text[:123]}...'
#
#     def like(self):
#         self.rating = F('rating') + 1
#         self.save()
#
#     def dislike(self):
#         self.rating = F('rating') - 1
#         self.save()
#
#
# class PostCategory(models.Model):
#     postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
#     categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
#
# class Comment(models.Model):
#     commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
#     commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     dateCreation = models.DateTimeField(auto_now_add=True)
#     rating = models.IntegerField(default=0)
#
#
#     def like(self):
#         self.rating = F('rating') + 1
#         self.save()
#
#     def dislike(self):
#         self.rating = F('rating') - 1
#         self.save()
#
#
#
