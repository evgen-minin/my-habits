from rest_framework.pagination import PageNumberPagination


class HabitsPagination(PageNumberPagination):
    """
    Пагинация для списка привычек.

    Параметры:
    - page_size: Количество элементов на странице.
    - page_size_query_param: Параметр запроса для указания количества элементов на странице.
    - max_page_size: Максимальное количество элементов на странице.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
