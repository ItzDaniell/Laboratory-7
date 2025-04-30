from django.db import models
from django.db.models import Count
from django.utils import timezone

class PostManager(models.Manager):
    """Custom manager for Post model"""
    
    def published(self):
        """Return only published posts"""
        return self.filter(
            status='published',
            published_at__lte=timezone.now()
        )
    
    def drafts(self):
        """Return only draft posts"""
        return self.filter(status='draft')
    
    def by_category(self, category_slug):
        """Return posts for a specific category"""
        return self.published().filter(category__slug=category_slug)
    
    def by_tag(self, tag_slug):
        """Return posts with a specific tag"""
        return self.published().filter(tags__slug=tag_slug).distinct()
    
    def by_author(self, author_id):
        """Return posts by a specific author"""
        return self.published().filter(author_id=author_id)
    
    def with_comment_count(self):
        """Return posts with their comment counts"""
        return self.annotate(total_comments=Count('comments'))
    
    def recent_posts(self, count=5):
        """Return most recent posts"""
        return self.published().order_by('-published_at')[:count]
    
    def popular_posts(self, count=5):
        """Return posts with most comments"""
        return self.published().annotate(
            total_comments=Count('comments')
        ).order_by('-total_comments')[:count]
