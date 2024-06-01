from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {"blank": True, "null": True}


class Info(models.Model):
    user = models.ForeignKey("users.User", verbose_name=_("user"), on_delete=models.CASCADE, related_name="info",
                             **NULLABLE)
    amount = models.IntegerField(verbose_name=_("amount"))
    per_second = models.IntegerField(default=1, verbose_name=_("point_per_second"))

    class Meta:
        verbose_name = _("information")
        verbose_name_plural = _("information")

    def __str__(self):
        return str(self.user)


class Achievement(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    task = models.IntegerField(verbose_name=_("task"))
    info = models.ManyToManyField(Info, verbose_name=_("info"), related_name="achievement")

    class Meta:
        verbose_name = _("achievement")
        verbose_name_plural = _("achievements")

    def __str__(self):
        return self.name
