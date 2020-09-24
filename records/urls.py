from django.urls import path 
from .views import HomeView ,DashboardView, EntryDetailView, AddEntryView,UpdateEntryView,DeleteEntryView


urlpatterns = [
    
       path('' , HomeView.as_view() , name="home"),
       path('dashboard' , DashboardView.as_view() , name="dashboard"),
       path('transaction/<int:pk>' , EntryDetailView.as_view() , name="entrydetail"),
       path('add_entry/' , AddEntryView.as_view() , name="addentry"),
       path('edit_entry/<int:pk>' , UpdateEntryView.as_view() , name="editentry"),
       path('entry/<int:pk>/remove' , DeleteEntryView.as_view() , name="delentry"),
]
