from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def about(request):
    return HttpResponse("This page is about django!")


def comments(request):
    return HttpResponse("This page is for comments")


def create(request):
    return HttpResponse("On this page you can create article")


def update(request):
    return HttpResponse("On this page you can update existing article")


def delete(request):
    return HttpResponse("On this page you can delete existing article")


def add_topic(request):
    return HttpResponse("You can add page to your favorites")


def remove_topic(request):
    return HttpResponse("You can remove article from your favorites")


def subscribe(request):
    return HttpResponse("Subscribe on topic")


def unsubscribe(request):
    return HttpResponse("Unsubscribe from topic")


def password(request):
    return HttpResponse("Here you can change your password")


def change_data(request):
    return HttpResponse("Here you can change your data")


def deactivate(request):
    return HttpResponse("Deactivate your account")


def register(request):
    return HttpResponse("Here you can register")


def login(request):
    return HttpResponse("Here you can login")


def logout(request):
    return HttpResponse("Here you can logout")


def username(request, pk):
    return HttpResponse(f"You're name is {pk}")
