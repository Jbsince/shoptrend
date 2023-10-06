
from django.urls import path, include
from . import views
app_name='todoapp'

urlpatterns = [
    path('', views.add, name='home'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetails'),
    path('cbvedit/<int:pk>/',views.Taskupdateview.as_view(),name='cbvedit'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),

]

