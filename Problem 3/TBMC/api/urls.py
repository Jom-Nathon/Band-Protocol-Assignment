from django.urls import path
from . import views

urlpatterns = [
    path("broadcast", views.PostPayloadView.as_view(), name="broadcast"),
    path("check/<str:tx_hash>/", views.GetTransactionView.as_view(), name="check_transaction")
]