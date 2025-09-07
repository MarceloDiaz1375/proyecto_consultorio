from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pacientes
from .serializers import PacientesSerializer
# Create your views here.

class PacientesList(APIView):
    def get(self, request):
        pacientes = Pacientes.objects.all()
        serializer = PacientesSerializer(pacientes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PacientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)