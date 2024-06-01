from django.urls import path

from miner.apps import MinerConfig
from miner.views import InfoDetailView, get_point

app_name = MinerConfig.name

urlpatterns = [
    path("detail_info/<int:pk>/", InfoDetailView.as_view(), name="detail_info"),
    path("get_point/<int:pk>/", get_point, name="get_point"),
]
