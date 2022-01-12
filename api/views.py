from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order


@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'Orders list':'/list/',
        'Create':'/create/',
        'Update status':'/update-status/',
        'Orders':'/orders/clients/<str:client_id>/?from=<date>&to=<date>/',
    }
    return Response(api_urls)
@api_view(['GET'])
def listOrder(request):
    orders=Order.objects.all()
    serializer=OrderSerializer(orders, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def createOrder(request):
    serializer=OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateOrder(request):
    pk=request.data['id']
    order=Order.objects.get(id=pk)
    if order.status=="accepted":
        if request.data['status']=="cancelled":
            return Response("Order can not be cancelled")
    serializer=OrderSerializer(instance=order, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def listOrderbyClient(request, client_id):
    start = request.GET.get('from')
    end = request.GET.get('to')
    if start and end:
        orders=Order.objects.filter(client=client_id, created__range=[start, end])
    else:
        orders = Order.objects.filter(client=client_id)
    serializer=OrderSerializer(orders, many=True)

    return Response(serializer.data)