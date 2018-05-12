from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'add_expense'

urlpatterns=[
    url(r'^home/',views.home,name='home'),
    ]