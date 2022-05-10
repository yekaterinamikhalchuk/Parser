from django.views import generic
from parser.models import News
from .filters import ParserFilter
from .forms import ParserForm


class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'
    paginate_by = 7
    queryset = News.objects.order_by('create_date')
    form_class = ParserForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return ParserFilter(self.request.GET, queryset=queryset).qs



