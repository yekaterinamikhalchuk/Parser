from django.forms import SelectDateWidget
from django_filters import FilterSet, DateFilter, ChoiceFilter, CharFilter
from .models import News


class ParserFilter(FilterSet):
    update_date = DateFilter(field_name='update_date',
                               lookup_expr='gt',
                               label='Updated after',
                               widget=SelectDateWidget)
    create_date = DateFilter(field_name='create_date',
                             lookup_expr='gt',
                             label='Created after',
                             widget=SelectDateWidget)
    country = ChoiceFilter(label='Country')
    
    class Meta:
        model = News
        fields = (
            'update_date',
            'domain',
            'link',
            'create_date',
            'update_date',
            'country')
