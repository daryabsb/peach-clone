from django.urls import path
from .views import (
    CompanyList,
    # OwnerList,
    # AccountList,
    # AccountSubList,
    # ItemList
)

app_name = "companies"
urlpatterns = [
    path("", CompanyList.as_view(), name="company-list"),
    # path("owners", OwnerList.as_view(), name="owners-list"),
    # path("accounts", AccountList.as_view(), name="account-list"),
    # path("category", AccountSubList.as_view(), name="category-list"),
    # path("items", ItemList.as_view(), name="items-list"),
]
