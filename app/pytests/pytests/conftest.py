import pytest
from pytest_factoryboy import register

from factories import (TypeReviewFactory, TagReviewFactory,
                        CategoryFactory, ReviewFactory)

register(TagReviewFactory)
register(TypeReviewFactory)
register(CategoryFactory)
register(ReviewFactory)



