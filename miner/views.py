from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from miner.models import Info, Achievement


class InfoDetailView(DetailView):
    """
    Представление детального просмотра информации
    """

    model = Info
    extra_context = {
        "title": "Поинты",
        "description": "Нажимай и прибавляй 1 поинт себе в копилку!",
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["achievements"] = Achievement.objects.order_by("task")
        return context_data


def get_point(request, pk):
    """
    Функция блокировки и разблокировки пользователей сайта
    :param pk:
    """
    info = get_object_or_404(Info, pk=pk)
    info.amount += 1
    info.save()
    return redirect(reverse("miner:detail_info", args=[pk]))
