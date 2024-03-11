from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Homepage.as_view(), name='home'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us, name='contact'),
    path('addreview/', views.AddReview.as_view(), name='addreview'),
    path('review/<slug:review_slug>/', views.ShowReview.as_view(), name='review'),
    path('category/<slug:category_slug>/', views.ReviewCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagReviewList.as_view(), name='tag'),
    path('update/<slug:slug>/', views.UpdateReview.as_view(), name='update_review'),
]