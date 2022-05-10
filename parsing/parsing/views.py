from django.views import generic
from parser.models import News
# 
# 
# class HomePageView(generic.ListView):
#     template_name = 'home.html'
#     context_object_name = 'articles'
#     paginate_by = 10
#     form_class = ParserForm
#     
#     def get_queryset(self):
#         return News.objects.all()