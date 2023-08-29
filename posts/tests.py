from django.test import TestCase
from django.contrib.auth.models import User

from . import models


# Create your tests here.

class BlogTests(TestCase):
    TITLE = 'Blog test title1'
    BODY = 'Test body text....'
    USER = 'test_user1'
    PWD = 'password1'

    @classmethod
    def setUpTestData(cls):
        # Create a user
        test_user1 = User.objects.create_user(
            username=cls.USER,
            password=cls.PWD
        )
        test_user1.save()

        # Create a blog post
        test_post = models.Post.objects.create(
            author=test_user1,
            title=cls.TITLE,
            body=cls.BODY
        )
        test_post.save()

    def test_blog_content(self):
        post = models.Post.objects.get(pk=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'

        self.assertEqual(expected_author, self.USER)
        self.assertEqual(expected_title, self.TITLE)
        self.assertEqual(expected_body, self.BODY)


