from django.test import TestCase
from .models import News, Comments
# Create your tests here.


class TestNewsModel(TestCase):
    def test_has_comments_true(self):
        info = News(title="Hello World?", content="I started learning coding when I was ...")
        info.save()
        comment = Comments(news=info, content="Man... thats some bulshit")
        comment.save()
        self.assertIs(True, info.has_comment())

    def test_has_comments_false(self):
        info = News(title="Hello World?", content="I started learning coding when I was ...")
        info.save()
        self.assertIs(False, info.has_comment())

class TestIndexView(TestCase):
    # test for news to be in ascending order in "" page
    def test_index_for_ascending(self):
        new1 = News(title="1 ever new", content="I am happy to announce the launch of news app")
        new2 = News(title="2 new", content="Consistency is the key!")
        new3 = News(title="3 time a charm", content="I like it here")
        new1.save()
        new2.save()
        new3.save()
        response = self.client.get("/news/")

    # test for detail page to be exact


    
    # test for comments in detail page to be in descending order
