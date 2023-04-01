from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='test', email='test@gmail.com', password='123456'
        )
        cls.post = Post.objects.create(
            title='test title',
            body='test body',
            author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, 'test title')
        self.assertEqual(self.post.body, 'test body')
        self.assertEqual(self.post.author.username, 'test')
        self.assertEqual(str(self.post), 'test title')
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_url_exist_at_correct_location_listview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_exist_at_correct_location_detailview(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detailview(self):
        response = self.client.get(
            reverse('post_detail', kwargs={'pk': self.post.pk}))
        no_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test title')
        self.assertTemplateUsed(response, 'detailPage.html')

    def test_post_createView(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_updateView(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")

    def test_post_deleteView(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
