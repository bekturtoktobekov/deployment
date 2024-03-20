from rest_framework.decorators import api_view
from . import serializers, models
from rest_framework.response import Response

@api_view(['GET'])
def get_product(request):
    directors = models.Product.objects.all()
    data = serializers.ProductSerializers(directors, many=True).data
    return Response(data=data)



@api_view(['GET'])
def test(request):
    context = {
        'integer': 100,
        'string': 'hello world',
        'boolean': True,
        'list': [
            1, 2, 3
        ]
    }
    return Response(data=context)