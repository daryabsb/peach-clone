from django.urls import path
from .views import IncomeStatementView

app_name = "statements"
urlpatterns = [
    path("income", IncomeStatementView.as_view(), name="income-list"),
    # path("purchases/add/", CreatePurchase.as_view(), name="purchase-add"),

]
