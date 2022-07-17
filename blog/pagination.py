from rest_framework.pagination import PageNumberPagination

class CommonPageNumberPagination(PageNumberPagination):
    page_size = 2  # 每页显示的数据条数
    page_query_param = 'page'  # 页码的参数名
    page_size_query_param = 'size'  # 每页显示条数的参数名
    max_page_size = 2  # 最大显示条数，只有size参数有值才会生效