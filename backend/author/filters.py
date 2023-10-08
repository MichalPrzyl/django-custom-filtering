from django_filters import rest_framework as filters
from django.db.models import ForeignKey
# models
from author.models import Author



class AuthorFilter(filters.FilterSet):
    # created_dt__gt = filters.DateFilter(lookup_expr='gt', field_name='created_dt')
    class Meta:
        model = Author
        fields = [field.name for field in model._meta.fields] + ['']
        # fields = ['created_dt']
