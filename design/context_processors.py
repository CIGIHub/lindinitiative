
from . import models


def design(request):
    design = models.Design.objects.filter(default=True).first()

    if design is None:
        return dict()

    return dict(
        design=design
    )
