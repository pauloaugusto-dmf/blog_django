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

class TestTopicView:
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