from django.db import models
from django.utils.translation import gettext_lazy as _


class Menu(models.Model):
    title = models.CharField(_("Menu"), max_length=200)
    text = models.TextField(_("Text"))
