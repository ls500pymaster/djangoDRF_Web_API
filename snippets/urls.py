from django.urls import path
from snippets.views import snippet_detail, snippet_list

urlpatterns = [
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
]