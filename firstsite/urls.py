from django.contrib import admin
from django.urls import path
import one.views
import two.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',one.views.home,name='home'),
    path('one/book/',one.views.book,name='book'),
    path('one/<int:one_id>',one.views.detail,name='detail'),
    path('one/new/',one.views.new,name='new'),
    path('one/create/',one.views.create,name='create'),

    path('two/movie/',two.views.movie, name='movie'),
    path('two/<int:two_id>',two.views.detailm,name='detailm'),
    path('two/movie/newm/',two.views.newm,name='newm'),
    path('two/movie/createm/',two.views.createm,name='createm'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
