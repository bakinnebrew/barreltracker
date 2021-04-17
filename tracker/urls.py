from django.urls import path

from . import views

app_name = "tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("add_barrel", views.add_barrel, name="add_barrel"),
    path("load_account", views.load_account, name="load_account"),
    path("build_barrels/<str:build_view>",
         views.build_barrels, name="build_barrels"),
    path("single_barrel_load/<int:barrel_id>",
         views.single_barrel_load, name="single_barrel_load"),
    path("archive_barrel/<int:barrel_id>",
         views.archive_barrel, name="archive_barrel"),
    path("unarchive_barrel/<int:barrel_id>",
         views.unarchive_barrel, name="unarchive_barrel"),
    path("delete_barrel/<int:barrel_id>",
         views.delete_barrel, name="delete_barrel"),
    path("bookmark_barrel/<int:barrel_id>",
         views.bookmark_barrel, name="bookmark_barrel"),
    path("unbookmark_barrel/<int:barrel_id>",
         views.unbookmark_barrel, name="unbookmark_barrel"),
    path("filter/<str:filter_params>/<str:filter_params2>/<str:filter_params3>",
         views.filter, name="filter"),
    path("edit_account/", views.edit_account, name="edit_account"),
    path("load_notes/<int:barrel_id>", views.load_notes, name="load_notes"),
    path("add_note/<int:barrel_id>", views.add_note, name="add_note"),
    path("start_alerts/<int:barrel_id>",
         views.start_alerts, name="start_alerts"),
    path("stop_alerts/<int:barrel_id>", views.stop_alerts, name="stop_alerts"),
    path("load_alerts", views.load_alerts, name="load_alerts"),
    path("read_alerts", views.read_alerts, name="read_alerts"),
    path("remove_alert/<int:alert_id>", views.remove_alert, name="remove_alert"),
    path("submit_changes_to_barrel/<int:barrel_id>", views.submit_changes_to_barrel,
         name="submit_changes_to_barrel"),
    path("submit_barrel", views.submit_barrel, name="submit_barrel")
]
