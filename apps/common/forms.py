from django import forms
from django.conf import settings
from django.template.defaultfilters import striptags


class testAddress(object):
    def __init__(self,cleaned_data):
        self.fieldmap = [
            ('address1','Address1'),
            ('address2','Address2'),
            ('city','City'),
            ('state','State'),
            ('zip_code','Zip5')
        ]
        self.address1 = cleaned_data['address1']
        self.address2 = cleaned_data['address2']
        self.city = cleaned_data['city']
        self.state = cleaned_data['state']
        self.zip_code = cleaned_data['zip_code']


class AjaxBaseForm(forms.BaseForm):
    def errors_as_json(self, strip_tags=False):
        error_summary = {}
        errors = {}
        for error in self.errors.iteritems():
            if self.prefix:
                errors.update({self.prefix + '-' + error[0] : unicode(striptags(error[1]) \
                    if strip_tags else error[1])})
            else:
                errors.update({error[0] : unicode(striptags(error[1]) \
                    if strip_tags else error[1])})
        error_summary.update({'errors' : errors })
        return error_summary


class AjaxModelForm(AjaxBaseForm, forms.ModelForm):
    """Ajax Form class for ModelForms"""


class AjaxForm(AjaxBaseForm, forms.Form):
    """Ajax Form class for Forms"""