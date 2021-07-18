from django.contrib import admin
from django.urls import path, include

# bu settings faylini o'zi sal boshqachorq usulda yuklash
from django.conf import settings

# bu static fayllarni yonalishini urlda korsatish uchun ishlatiladigan funksiya
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# shu yerda media fayllarga murojat qanday bolishi korsatish kerak

# har qanaqa media faylni templateda korstaish uchun media prefix qoshiladi

# agar siz qolda media deb yozib qoysez media faylizi papkasi ozgarishi mumkinu

# get_media_prefix degan funksiya automatik tarzda topib beradi ozi