from django_filters import rest_framework as filters
from django.db.models import ForeignKey
# models
from article.models import Article



# class ArticleFilter(filters.FilterSet):
#     # name = filters.CharFilter(lookup_expr='icontains')
#     # author__first_name = filters.CharFilter(lookup_expr='icontains')
#     created_dt = filters.DateFilter(lookup_expr='iexact', field_name='created_dt')
#     created_dt__gt = filters.DateFilter(lookup_expr='gt', field_name='created_dt')
#     # author__date_of_birth__year = filters.DateFilter(lookup_expr='gt')
#     author__date_of_birth__year = filters.NumberFilter()
#     class Meta:
#         model = Article
#         # fields = [field.name for field in model._meta.fields] + ['']
#         fields = ['created_dt']

class MyFilterBackend(filters.DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)
        # merge filterset kwargs provided by view class
        print(f"\033[94mkwargs\033[0m: {kwargs}")
        print(f"\n==============================\nupdating\n")
        if hasattr(view, 'get_filterset_kwargs'):
            kwargs.update(view.get_filterset_kwargs())
        
        kwargs['queryset'] = kwargs['queryset'].filter(author__first_name='Kinga')
        print(f"\033[94mkwargs\033[0m: {kwargs}")
        # kwargs['MP-attribuet'] = 'hello world'
        return kwargs
    pass