from django.conf.urls import url

import blog.views

urlpatterns = [
    url(r'^$', blog.views.home, name='home'),
    url(r'^tag/(?P<tag>[^\.]+)$', blog.views.home, name="posts_by_tag"),
    url(r'^(?P<slug>[^\.]+)$', blog.views.single_post, name="single_post"),
]
