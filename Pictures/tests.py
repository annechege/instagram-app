from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='user', email='email')
        self.user.save()
        self.profile = Profile(image='image', bio='bio', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

class PostTest(TestCase):
    def setUp(self):
        self.post = Post(image='image',caption='caption',created_date='created_date')

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))


class CommentTest(TestCase):
    def setUp(self):
        self.comment = Comment(comment='comment', created_date='created_date')
        self.post = Post(image='image', caption='caption', created_date='created_date')
        self.post.save()
        self.user = User(username='user', email='email')
        self.user.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_save(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)
