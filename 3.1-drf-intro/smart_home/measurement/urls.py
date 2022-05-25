from django.urls import path
from measurement.views import SensorView, SensorsListView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsListView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
