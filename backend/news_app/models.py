from django.db import models

# Create your models here.
# the users table will be like this:
class users(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password_harsh = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # role will be foreign key from role table
    role = models.ForeignKey('role', on_delete=models.CASCADE)

# the role table which is either editor, chief editor, admin, or viewer, other will be added through development
class role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

# category of the news article like sports, fixtures, scores, transfers, and other will be added through development
class category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

# table for news article
class news_article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='draft')  # draft, published, archived
    # the author will be foreign key from users table
    author = models.ForeignKey(users, on_delete=models.CASCADE)
    # the category will be foreign key from category table
    category = models.ForeignKey(category, on_delete=models.CASCADE)

# table for comments on news article
class comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # the author will be foreign key from users table
    author = models.ForeignKey(users, on_delete=models.CASCADE)
    # the news article will be foreign key from news_article table
    news_article = models.ForeignKey(news_article, on_delete=models.CASCADE)

# table for blog posts by community members
class blog_post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='draft')  # draft, published, archived
    # the author will be foreign key from users table
    author = models.ForeignKey(users, on_delete=models.CASCADE)

# table for forum post by community members
class forum_post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='draft')  # draft, published, archived
    # the author will be foreign key from users table
    author = models.ForeignKey(users, on_delete=models.CASCADE)

# table for forum post comments by community members
class forum_comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # the author will be foreign key from users table
    author = models.ForeignKey(users, on_delete=models.CASCADE)
    # the forum post will be foreign key from forum_post table
    forum_post = models.ForeignKey(forum_post, on_delete=models.CASCADE)


