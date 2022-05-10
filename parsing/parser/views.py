from django.views import generic
from parser.models import News, Url
from .filters import ParserFilter
from .forms import ParserForm, CreateForm


class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'
    paginate_by = 7
    queryset = News.objects.order_by('create_date')
    form_class = ParserForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return ParserFilter(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ParserFilter(self.request.GET, queryset=self.get_queryset())
        return context


class UrlCreateView(generic.CreateView):
    template_name = 'url_create.html'
    form_class = CreateForm

    model = Url
    # fields = ['news_type', 'post_title', 'post_text', 'categories']

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['link'] = Url.objects.get(user_id=self.request.user.id)
    #     return initial



