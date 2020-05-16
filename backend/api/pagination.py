from math import ceil

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomTvInfoPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': ceil(self.page.paginator.count / self.page_size),
            'limit': self.page_size,
            'results': data
        })
