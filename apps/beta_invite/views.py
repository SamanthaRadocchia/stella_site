"""
Views for signing up to beta. 
"""

from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db import IntegrityError

from beta_invite.forms import SignupForm
from beta_invite.models import BetaInviteProfile


def signup(request, success_url='/thankyou/'):
    """
    Creates a new BetaUser that only has an email address and registration key. Once they are
    deemed ready to join the Beta, they can be emailed a link to register unique to them. 
    """
    if request.method == 'POST':
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                new_beta_user = BetaInviteProfile.objects.create_invite_profile(email=form.cleaned_data['email'])
            except IntegrityError: # This means they already signed up because emails are unique
                return render_to_response('static/stella_already-registered.html')
            return HttpResponseRedirect(success_url)
    else:
        form = SignupForm()
        
    # Need to add the form elements for login
    context = RequestContext(request)
    # The extra forms will not be included for now because I'm not bothered 
    # to augment the contrib.auth.views to such an extent. Can be dealt with later.
    return render_to_response('registration/stella_login.html',
                              { 'form': AuthenticationForm(),
                                'form_signup': form},
                              context_instance=context)
