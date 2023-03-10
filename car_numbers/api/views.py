from random import choices, randint

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CarNumer
from .serializers import CarNumerSerializer

LETTERS = 'ABEKMHOPCTYX'


def gen_number_plate():
    letters = ''.join(choices(LETTERS, k=3))
    numbers = randint(1, 999)
    return f'{letters[0]}{numbers:03d}{letters[1]}{letters[2]}'


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_plate(request, amount=1):
    if request.method == 'GET':
        plates = []
        for _ in range(amount):
            plates.append(gen_number_plate())

        data = {"generated_plate": plates}
        return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_plate(request, id=None):
    if request.method == 'GET':
        number = CarNumer.objects.get(id=id)
        serializer = CarNumerSerializer(number)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_plate(request):
    if request.method == 'POST':
        serializer = CarNumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
