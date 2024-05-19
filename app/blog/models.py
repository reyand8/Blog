from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Review.Status.PUBLISHED)


class TypeReview(models.Model):
    slug = models.SlugField(unique=True, max_length=20, db_index=True)
    name = models.CharField(unique=True, max_length=20, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('type_review', kwargs={'type_slug': self.slug})

    class Meta:
        verbose_name ='Type'
        verbose_name_plural = 'Types'
        ordering = ['name']


class Category(models.Model):
    slug = models.SlugField(unique=True, max_length=20, db_index=True)
    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class TagReview(models.Model):
    slug = models.SlugField(unique=True, max_length=50, db_index=True)
    tag = models.CharField(max_length=60, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['tag']


class Review(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Not Publish'
        PUBLISHED = 1, 'Publish'


    slug = models.SlugField(unique=True, max_length=50, db_index=True)
    type = models.ForeignKey('TypeReview', default=True, on_delete=models.PROTECT)
    title = models.CharField(unique=True, max_length=50, db_index=True)
    text = models.CharField(max_length=3500,
                            validators=[
                               MinLengthValidator(20, message="Your text must contain at "
                                                              "least 20 characters"),
                               MaxLengthValidator(3500, message="Your text must contain no more "
                                                              "than 3500 characters"),
                           ])
    images = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True, default=None)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    tags = models.ForeignKey('TagReview',
                             blank=True,
                             verbose_name='Tags',
                             on_delete=models.PROTECT,
                             related_name='tags')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Publish')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.SET_NULL,
                               related_name='reviews',
                               null=True,
                               default=None)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review',
                       kwargs={'review_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Review, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['id']