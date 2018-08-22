from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Slugged


class BaseBlockCategory(Slugged):
    """Base Category"""

    slug = models.CharField(max_length=2000, blank=True, null=True)
    level = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        abstract = True


class BlockCategory(BaseBlockCategory):
    """Block Category
    """
    class Meta:
        verbose_name = _('Block category')
        verbose_name_plural = _('Block categories')
