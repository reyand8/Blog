import pytest
from faker import Faker
from factories import *
from blog.models import *



def test_review_instance(db, review_factory):
    review = review_factory.create()
    item =  Review.objects.all().count()
    print(review.title, item)
    assert True