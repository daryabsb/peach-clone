from django.urls import path
from .views import (
    CompanyList,
    OwnerList,
    AccountList,
    AccountSubList,
    ItemList,
    PurchaseList,
    SaleList
)

app_name = "companies"
urlpatterns = [
    path("", CompanyList.as_view(), name="company-list"),
    path("owners", OwnerList.as_view(), name="owners-list"),
    path("accounts", AccountList.as_view(), name="account-list"),
    path("category", AccountSubList.as_view(), name="category-list"),
    path("items", ItemList.as_view(), name="items-list"),
    path("purchases", PurchaseList.as_view(), name="purchase-list"),
    path("sales", SaleList.as_view(), name="sale-list"),
    # path("category/<str:category>", MovieCategory.as_view(), name="movie-category"),
    # path("language/<str:lang>", MovieLanguage.as_view(), name="movie-language"),
    # path("search/", MovieSearch.as_view(), name="movie-search"),
    # path("year/<int:year>", MovieYear.as_view(), name="movie-year"),
    # path("<slug:slug>", MovieDetail.as_view(), name="movie-detail"),
]
