from django.urls import path
from .views import (
    CompanyList
)

app_name = "company"
urlpatterns = [
    path("", CompanyList.as_view(), name="company-list"),
    # path("category/<str:category>", MovieCategory.as_view(), name="movie-category"),
    # path("language/<str:lang>", MovieLanguage.as_view(), name="movie-language"),
    # path("search/", MovieSearch.as_view(), name="movie-search"),
    # path("year/<int:year>", MovieYear.as_view(), name="movie-year"),
    # path("<slug:slug>", MovieDetail.as_view(), name="movie-detail"),
]