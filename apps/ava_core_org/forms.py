from django.forms import ModelForm

from apps.ava_core_org.models import *


class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation



#class OrganisationUnitForm(ModelForm):
#     class Meta:
#         model = OrganisationUnit
#         fields = ('name','office','unittype','parent')
#
# OrganisationUnitFormSet = inlineformset_factory(Organisation,OrganisationUnit)
# EmployeeFormSet = inlineformset_factory(Organisation,Employee)
