from django.urls import path
from .views import CreateAccountView, MyAccountView

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('my-account/', MyAccountView.as_view(), name='myAccount')
]