import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db

class TestHomeView:
    class TestPublicationHomeView:
        def test_reverse_resolve(self):
            assert reverse('publication:home') == '/'
            assert resolve('/').view_name == 'publication:home'

        def test_status_code(self, client):
            response = client.get(reverse('publication:home'))
            assert response.status_code == 200

class TestTopicViews:
    class TestTopicListView:
        def test_reverse_resolve(self):
            assert reverse('publication:list_topic') == '/topic/list/'
            assert resolve('/topic/list/').view_name == 'publication:list_topic'

        def test_status_code(self, client):
            response = client.get(reverse('publication:list_topic'))
            assert response.status_code == 200


    class TestTopicCreateView:
        def test_reverse_resolve(self):
            assert reverse('publication:create_topic') == '/topic/create/'
            assert resolve('/topic/create/').view_name == 'publication:create_topic'

        def test_status_code(self, client):
            response = client.get(reverse('publication:create_topic'))
            assert response.status_code == 200

    class TestTopicUpdateView:
        def test_reverse_resolve(self, topic):
            url = reverse('publication:update_topic', kwargs={'slug': topic.slug})
            assert url == f'/topic/{topic.slug}/update/'

            view_name = resolve(f"/topic/{topic.slug}/update/").view_name
            assert view_name == 'publication:update_topic'

        def test_status_code(self, client, topic):
            response = client.get(reverse('publication:update_topic', kwargs={'slug': topic.slug}))
            assert response.status_code == 200


    class TestTopicDeleteView:
        def test_reverse_resolve(self, topic):
            url = reverse('publication:delete_topic', kwargs={'slug': topic.slug})
            assert url == f'/topic/{topic.slug}/delete/'

            view_name = resolve(f"/topic/{topic.slug}/delete/").view_name
            assert view_name == 'publication:delete_topic'

        def test_status_code(self, client, topic):
            response = client.get(reverse('publication:delete_topic', kwargs={'slug': topic.slug}))
            assert response.status_code == 200

class TestPostViews:
    class TestPostListView:
        def test_reverse_resolve(self):
            assert reverse('publication:list_post') == '/post/list/'
            assert resolve('/post/list/').view_name == 'publication:list_post'

        def test_status_code(self, client):
            response = client.get(reverse('publication:list_post'))
            assert response.status_code == 200

    class TestPostDetailView:
        def test_reverse_resolve(self, post):
            url = reverse('publication:detail_post', kwargs={'slug': post.slug})
            assert url == f'/post/{post.slug}/'

            view_name = resolve(f"/post/{post.slug}/").view_name
            assert view_name == 'publication:detail_post'

        def test_status_code(self, client, post):
            response = client.get(reverse('publication:detail_post', kwargs={'slug': post.slug}))
            assert response.status_code == 200

    class TestPostCreateView:
        def test_reverse_resolve(self):
            assert reverse('publication:create_post') == '/post/create/'
            assert resolve('/post/create/').view_name == 'publication:create_post'

        def test_status_code(self, client):
            response = client.get(reverse('publication:create_post'))
            assert response.status_code == 200

    class TestPostUpdateView:
        def test_reverse_resolve(self, post):
            url = reverse('publication:update_post', kwargs={'slug': post.slug})
            assert url == f'/post/{post.slug}/update/'

            view_name = resolve(f"/post/{post.slug}/update/").view_name
            assert view_name == 'publication:update_post'

        def test_status_code(self, client, post):
            response = client.get(reverse('publication:update_post', kwargs={'slug': post.slug}))
            assert response.status_code == 200

    class TestPostDeleteView:
        def test_reverse_resolve(self, post):
            url = reverse('publication:delete_post', kwargs={'slug': post.slug})
            assert url == f'/post/{post.slug}/delete/'

            view_name = resolve(f"/post/{post.slug}/delete/").view_name
            assert view_name == 'publication:delete_post'

        def test_status_code(self, client, post):
            response = client.get(reverse('publication:delete_post', kwargs={'slug': post.slug}))
            assert response.status_code == 200


 