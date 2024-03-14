from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .forms import AddReviewForm
from .models import Review, TagReview
from .utils import DataMixin


class Homepage(DataMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'reviews'
    title_page = 'Home'
    cat_selected = 0

    def get_queryset(self):
        return Review.published.all().select_related('category')

def about_us(request):
    return render(request, 'blog/about.html',
                  {'title': 'About us'})

def contact_us(request):
    return render(request, 'blog/contact.html',
                  {'title': 'Contact us'})


class ShowReview(DataMixin, DetailView):
    template_name = 'blog/review_details.html'
    context_object_name = 'review'
    slug_url_kwarg = 'review_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['review'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Review.published, slug=self.kwargs[self.slug_url_kwarg])


class AddReview(LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'blog/add_review.html'
    form_class = AddReviewForm
    title_page = 'Add review'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        return super().form_valid(form)


class UpdateReview(PermissionRequiredMixin, DataMixin, UpdateView):
    template_name = 'blog/add_review.html'
    model = Review
    form_class = AddReviewForm
    success_url = reverse_lazy('home')
    title_page = 'Update review'
    permission_required = 'blog.update_review'


class ReviewCategory(DataMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'reviews'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['reviews'][0].category
        return self.get_mixin_context(context,
                                      title='Category ' + cat.name,
                                      category_selected = cat.pk)

    def get_queryset(self):
        return Review.published.filter(category__slug=self.kwargs['category_slug'],
                                     is_published=True).select_related('category')


class TagReviewList(DataMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'reviews'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagReview.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Tag: ' + tag.tag)

    def get_queryset(self):
        return Review.published.filter(
            tags__slug=self.kwargs['tag_slug']).select_related('tags')


class TypeReviewList(DataMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'reviews'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        types_review = context['reviews'][0].type
        return self.get_mixin_context(context,
                                      title='Type ' + types_review.name)

    def get_queryset(self):
        return Review.published.filter(
            type__slug=self.kwargs['type_slug']).select_related('type')

def page_not_found(request, exception):
    return render(request, 'blog/NotFound.html', status=404)
