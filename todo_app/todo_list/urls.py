from django.urls import path
from . import views

urlpatterns = [
    path('delete/<list_id>', views.delete_items, name='delete_item'),
    path('strike/<list_id>/', views.strike, name='strike'),
    path('board/<board_id>/', views.BoardListView.as_view(), name='board'),
    path('boards', views.BoardsListView.as_view(), name='boards'),
    # path('deleteboard/<board_id>', views.deleteboard, name='deleteboard'),
    path('deleteboard/<int:pk>', views.BoardDeleteView.as_view(), name='deleteboard'),
    path('additem/', views.additem, name='additem'),
    path('addboard/', views.BoardCreateView.as_view(), name='addboard'),
    path('addboard/', views.BoardCreateView.as_view(), name='addboard'),
    path('board/<int:pk>/update', views.BoardUpdateView.as_view(), name='updateboard')

	# path('uncross/<list_id>', views.uncross, name='uncross'),
    # path('uncross/<list_id>', views.uncross, name='uncross'),
    # path('', views.home, name='home'),
    # path('delete/<int:pk>', views.ItemDeleteView.as_view(), name='delete_item'),
    #path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    # path('logout', views.logout, name='logout'),
    # path('board/<board_id>/', views.board, name='board'),
    # path('addboard', views.addboard, name='addboard'),
]
