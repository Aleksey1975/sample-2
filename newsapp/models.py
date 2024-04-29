from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author}'

    def update_rating(self):
        ratPost = self.posts.aggregate(ratingPost=Sum('rating'))
        rPost = 0
        if self.posts.exists():
            rPost += ratPost.get('ratingPost') * 3

        ratCommentByAuthor = self.author.comments_from_users.aggregate(ratingCommentByAuthor=Sum('rating'))
        rCommentByAuthor = 0
        if self.author.comments_from_users.exists():
            rCommentByAuthor += ratCommentByAuthor.get('ratingCommentByAuthor')

        author_posts = self.posts.all()
        rPostsAuthor = 0
        for post in author_posts:
            if post.comments_to_posts.exists():
                r = post.comments_to_posts.aggregate(rComment_to_post=Sum('rating'))
                rPostsAuthor += r.get('rComment_to_post')

        self.rating = rPost + rCommentByAuthor + rPostsAuthor
             
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    article = 'AR'
    news = 'NE'
    POSTS = [
        (article, 'Статья'),
        (news, 'Новость'),
    ]
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='posts')
    type_of = models.CharField(max_length=2, choices=POSTS, default=news)
    time_created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.type_of}  {self.title}'

    def like(self):
        self.rating = F('rating') + 1
        self.save()

    def dislike(self):
        self.rating = F('rating') - 1
        self.save()


class PostCategory(models.Model):           
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_to_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_from_users')
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'Комментарий {self.user}'

    def like(self):
        self.rating = F('rating') + 1
        self.save()


    def dislike(self):
        self.rating = F('rating') - 1
        self.save()

