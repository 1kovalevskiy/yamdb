from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from artworks.models import Title
from users.models import User


class Review(models.Model):
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='review')
    text = models.TextField(verbose_name='text')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='author-review')
    score = models.PositiveIntegerField(
        default=5,
        validators=(
            MaxValueValidator(
                10,
                message='Введите целое число от 1 до 10'
            ),
            MinValueValidator(
                1,
                message='Введите целое число от 1 до 10')
        ),
        null=True,
        verbose_name='review-score',
    )
    pub_date = models.DateTimeField(verbose_name='date_published',
                                    auto_now_add=True,
                                    db_index=True)

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ('-pub_date',)
        constraints = (
            models.UniqueConstraint(fields=('title', 'author'),
                                    name='pair_unique'),
        )

    def __str__(self):
        return ('Review(title= ' + str(self.title) + ', '
                'author= ' + str(self.author) + ', '
                'text= ' + self.text[:250] + ')')


class Comment(models.Model):
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='comment-review')
    text = models.TextField(verbose_name='text')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='comment-author')
    pub_date = models.DateTimeField(verbose_name='date_published',
                                    auto_now_add=True,
                                    db_index=True)

    class Meta:
        def __str__(self):
            return ('Comment(review= ' + str(self.review) + ', '
                    'author= ' + str(self.author) + ', '
                    'text= ' + self.text[:250] + ')')
