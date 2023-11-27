from django.shortcuts import render


def create_account_view(request):
    print(request.headers)
    return render(request, "create_account.html", {})
