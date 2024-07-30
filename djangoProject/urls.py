from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoProject.settings import MEDIA_URL, MEDIA_ROOT

def send_email(request):
    email = request.POST['email']
    subject = 'django tema'
    msg = 'Django grupadan xabar'
    start = time()
    send_mail(subject, msg, EMAIL_HOST_USER, [email])
    end = time()

    return JsonResponse()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('apps/', include('apps.urls', namespace='apps')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)  

                    
