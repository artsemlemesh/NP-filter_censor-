from datetime import datetime, date
from django_filters import FilterSet
from .models import News

class NewsFilter(FilterSet):
    class Meta:
        model = News
        fields = {
            'name': ['icontains'],
            'description': ['icontains'],
            'publish_date': ['month']
        }