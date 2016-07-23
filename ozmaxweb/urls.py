from django.conf.urls import url, include
from django.contrib import admin

import blog.urls
import ckeditor_uploader.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include(ckeditor_uploader.urls)),
    url(r'^blog/', include(blog.urls)),
]
