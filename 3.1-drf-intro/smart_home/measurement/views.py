# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorsListSerializer, MeasurementSerializer


class SensorsListView(ListAPIView):
    # Список датчиков с краткой информацией о них
    queryset = Sensor.objects.all()
    serializer_class = SensorsListSerializer

    def post(self, request):
        new_sensor = SensorsListSerializer(data=request.data)
        if new_sensor.is_valid():
            new_sensor.save()

        return Response(request.data)


class SensorView(RetrieveAPIView):
    # Информация по конкретному датчику
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        # Изменение информации датчика
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.data)


class MeasurementView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        measurement = Measurement.objects.create(temperature=request.data['temperature'],
                                                 sensor=Sensor.objects.get(id=request.data['sensor']))
        new_measurement = MeasurementSerializer(data=request.data)
        if new_measurement.is_valid():
            new_measurement.save()
        return Response(request.data)

