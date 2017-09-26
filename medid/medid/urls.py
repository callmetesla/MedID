
from django.conf.urls import url,include
from django.contrib import admin
from . import views
#Mappint to account app
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'account/',include('account.urls'))

]
