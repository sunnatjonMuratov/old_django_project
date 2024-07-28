from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

from apps.views import Main
from djangoProject.settings import MEDIA_URL, MEDIA_ROOT

def send_email(request):
    email = request.POST['email']
    subject = 'django tema'
    msg = 'Django grupadan xabar'
    start = time()
    send_mail(subject, msg, EMAIL_HOST_USER, [email])
    end = time()

    return JsonResponse()

app_name = 'myapp'


urlpatterns = [
    path('', Main.as_view(), name='index_view')
    path('detail/<int:id>/', views.detail, name='detail'),
]

