import django_filters
from manager.models import SavedPassword


class PSManagerFilter(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(
        fields=(
            ('created', 'created'),
        ),
    )

    class Meta:
        model = SavedPassword
        fields = [
            'user',
            'username',
            'password',
            'website',
            'note'
        ]
