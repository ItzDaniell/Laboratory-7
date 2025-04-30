from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from blog.models import Category, Tag, Post, Comment
import random
from datetime import timedelta


class Command(BaseCommand):
    """Command to seed the database with sample data"""
    help = 'Seeds the database with sample data for development and testing'
    
    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            self.stdout.write('Creating superuser... 👤')
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
        
        # Create regular user if it doesn't exist
        if not User.objects.filter(username='user').exists():
            self.stdout.write('Creating regular user... 👤')
            User.objects.create_user(
                username='user',
                email='user@example.com',
                password='user123'
            )
        
        # Create categories
        self.stdout.write('Creating categories... 📂')
        categories = [
            ('Programming', 'Posts about programming languages and software development.'),
            ('Data Science', 'Articles related to data analysis, machine learning, and statistics.'),
            ('Web Development', 'Content about web technologies, frameworks, and best practices.'),
            ('DevOps', 'Topics covering deployment, infrastructure, and operations.'),
            ('Career', 'Career advice, industry insights, and professional development.'),
        ]
        
        for name, description in categories:
            Category.objects.get_or_create(
                name=name,
                defaults={
                    'slug': slugify(name),
                    'description': description
                }
            )
        
        # Create tags
        self.stdout.write('Creating tags... 🏷️')
        tags = [
            'Python', 'JavaScript', 'Django', 'React', 'Docker',
            'APIs', 'Database', 'Security', 'Testing', 'Performance',
            'Git', 'Frontend', 'Backend', 'Cloud', 'Mobile'
        ]
        
        created_tags = []
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={'slug': slugify(tag_name)}
            )
            created_tags.append(tag)
        
        # Get users
        admin_user = User.objects.get(username='admin')
        regular_user = User.objects.get(username='user')
        
        # Create posts
        self.stdout.write('Creating posts... 📝')
        post_data = [
            {
                'title': 'Getting Started with Django ORM',
                'content': '',
            }
        ]
