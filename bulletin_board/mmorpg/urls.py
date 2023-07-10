from django.urls import path
from django.views.generic import TemplateView

from mmorpg.views import Posts, PostDetail, PostCreate, PostEdit, PostDelete, Profile, CommentCreate, Comments, \
    CommentDetail, confirm_comment, reject_comment, Search

urlpatterns = [
    path('', Posts.as_view(), name='posts'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('profile/', Profile.as_view(), name='profile'),
    path('filter/', Search.as_view(), name='filter'),
    path('<int:pk>/comment/', CommentCreate.as_view(), name='comment_create'),
    path('comments/', Comments.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('comments/<int:pk>/confirm/', confirm_comment, name='confirm_comment'),
    path('comments/<int:pk>/reject/', reject_comment, name='reject_comment'),
    path('accept/', TemplateView.as_view(template_name='accept.html')),
]
