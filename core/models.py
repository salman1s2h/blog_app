from django.db import models
from django.conf import settings

# Create your models here.

class Tag(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
      return self.name

    
class Category(models.Model):
    
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Post(models.Model):

    # id = models.AutoField(primary_key=True, db_column='id')
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(upload_to='', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="blog_post_like")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,blank=True, null=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,null=True)#new added


    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return 'Comment by {}'.format(self.name)
    

class Like(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)

    comment = models.OneToOneField(Comment, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='requirement_comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment.comment)[:30]