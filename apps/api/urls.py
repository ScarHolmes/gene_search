from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.render_search),
	url(r'^api/perform_search/$', views.perform_search),
	# url(r'^api/load_data/$', views.upload_info),
	url(r'^api/type_ahead/$', views.type_ahead),
	url(r'^api/purge_db/$', views.purge_db),
]