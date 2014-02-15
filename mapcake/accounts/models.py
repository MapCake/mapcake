from django.db import models


from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

# Create your models here.
class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    # organization = models.CharField(_('Organization Name'), max_length=255, blank=True, null=True, help_text=_('Name of your organization'))
    # profile = models.TextField(_('Profile'), null=True, blank=True)
    # position = models.CharField(_('Position Name'), max_length=255, blank=True, null=True, help_text=_('Your role or position'))
    telephone = models.CharField(_('telephone'), max_length=255, blank=True, null=True, help_text=_('Telephone number'))
    # fax = models.CharField(_('Facsimile'),  max_length=255, blank=True, null=True, help_text=_('Telephone number of a facsimile'))
    street = models.CharField(_('address'), max_length=255, blank=True, null=True, help_text=_('Physical address'))
    city = models.CharField(_('city'), max_length=255, blank=True, null=True, help_text=_('City'))
    area = models.CharField(_('administrative area'), max_length=255, blank=True, null=True, help_text=_('State, province of the location'))
    zipcode = models.CharField(_('postal code'), max_length=255, blank=True, null=True, help_text=_('ZIP or other postal code'))
    country = models.CharField(max_length=3, blank=True, null=True, help_text=_('Country'))
    # keywords = TaggableManager(_('keywords'), blank=True, help_text=_('commonly used word(s) or formalised word(s) or phrase(s) used to describe the subject (space or comma-separated'))
