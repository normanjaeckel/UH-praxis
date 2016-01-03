from django.db import models


class Section(models.Model):
    """
    Model for a section on the homepage.
    """
    class Meta:
        ordering = ('weight', 'title',)
        verbose_name = 'Abschnitt'
        verbose_name_plural = 'Abschnitte'

    title = models.CharField(
        'Titel',
        max_length=255,
    )
    content = models.TextField(
        'Inhalt',
        help_text='HTML-Tags sind erlaubt.',
    )
    weight = models.IntegerField(
        'Gewichtung',
        default=0,
        help_text=(
            'Je größer die Zahl, desto weiter unten/hinten erscheint der '
            'Abschnitt.'),
    )

    def __str__(self):
        return self.title
