from allauth.account.models import EmailAddress
from allauth.account.adapter import get_adapter

from django.contrib import messages
from django.shortcuts import redirect, render


# def error_404_view(request, exception):
#     return render(request, 'frontend/error404.html')


def resend_email(request):
    return render(request, 'account/resend_verification.html')


def resend_verfication(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            email_address = EmailAddress.objects.get(
                email__iexact=email, verified=False, user__is_active=True,
                email=email,
            )
            get_adapter(request).add_message(
                request,
                messages.INFO,
                "account/messages/" "email_confirmation_sent.txt",
                {"email": email},
            )
            email_address.send_confirmation(request)
        except EmailAddress.DoesNotExist:
            pass
    # redirect("named_url") or even better use here named url
    return redirect("/accounts/confirm-email/")