import factory
from faker import Faker
from blog.models import *

fake = Faker()

class TypeReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TypeReview
    name = fake.sentence()
    slug = fake.slug

class TagReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TagReview
    tag = fake.sentence()
    slug = fake.slug

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = fake.sentence()
    slug = name


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review
    title = fake.sentence()
    slug = ''
    text = fake.text()
    images = fake.file_extension(category='image')
    category = factory.SubFactory(CategoryFactory)
    tags = factory.SubFactory(TagReviewFactory)
    type = factory.SubFactory(TypeReviewFactory)
    is_published = 'True'
    time_create = fake.date()
    time_update = fake.date()