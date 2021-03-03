from django.urls import path
from .views import index, BookView, Tweete, loginform, logoutfunc,register;


urlpatterns = [
    path("greet/", index, name="index"),
    # path("namaste/", SayNamaste.as_view(), name="view"),
    path("booksdb/", BookView.as_view(), name="books"),
    path("tweetie/", Tweete, name="tweetie" ),
    path("login/", loginform, name="login"),
    path("logout/", logoutfunc ,name="logout"),
    path("register/", register, name="register"),

]
