from django.shortcuts import render


def login_view(request):
    print(request.headers)
    return render(request, "login.html", {})

def create_an_account_view(request):
    print(request.headers)
    return render(request, "create_an_account.html", {})
