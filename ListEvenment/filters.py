from .models import Evenment
import django_filters


class Evenment_filter(django_filters.FilterSet):
    class Meta:
        model = Evenment
        fields = ['porte',
                'type_evenment'
                ]
