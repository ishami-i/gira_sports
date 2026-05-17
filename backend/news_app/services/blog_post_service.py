from ..models.blog_post import blog_post

# Service functions for blog posts

def get_all_blog_posts():
    """
    Get all blog posts.
    """
    return blog_post.objects.all().order_by("-published_at")

# upload a new blog post
def upload_blog_post(title, slug, content, author):
    """
    Upload a new blog post.
    """
    new_blog_post = blog_post(
        title=title,
        slug=slug,
        content=content,
        author=author
    )
    new_blog_post.save()
    return new_blog_post

# update a blog post
def update_blog_post(blog_post_id, title=None, slug=None, content=None, status=None):
    """
    Update a blog post.
    """
    try:
        blog_post_to_update = blog_post.objects.get(id=blog_post_id)
        if title:
            blog_post_to_update.title = title
        if slug:
            blog_post_to_update.slug = slug
        if content:
            blog_post_to_update.content = content
        if status:
            blog_post_to_update.status = status
        blog_post_to_update.save()
        return blog_post_to_update
    except blog_post.DoesNotExist:
        return None