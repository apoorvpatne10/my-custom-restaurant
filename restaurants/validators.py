from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


def clean_email(self):
    email = value
    if ".edu" in email:
        raise forms.ValidationError("We don't accept edu emails.")
    # return email


CATEGORIES = ['Mexican', 'Asian', 'American', 'Thai']


def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{value} not a valid category")
    # value = cat
