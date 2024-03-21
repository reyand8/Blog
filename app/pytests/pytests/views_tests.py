import pytest
from django.urls import reverse
from blog.models import Category, TagReview


@pytest.mark.django_db
def test_homepage_url(client):
    response = client.get('')
    assert response.status_code == 200

@pytest.mark.django_db
def test_homepage_url(client):
    response = client.get('addreview')
    assert response.status_code == 200

@pytest.mark.django_db
def test_homepage_url(client):
    response = client.get('contact')
    assert response.status_code == 200

@pytest.mark.django_db
def test_homepage_url(client):
    response = client.get('about')
    assert response.status_code == 200


@pytest.fixture()
def setup(client):
    Category.objects.create(name='newdjango', slug='newdjango')
    TagReview.objects.create(tag='newdjango1', slug='newdjango1')

@pytest.mark.usefixtures('setup')
@pytest.mark.django_db
def test_category_url(client):
    url = reverse('category', args=['newdjango'])
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.usefixtures('setup')
@pytest.mark.django_db
def test_homepage_url(client):
    url = reverse('tag', args=['newdjango1'])
    response = client.get(url)
    assert response.status_code == 404