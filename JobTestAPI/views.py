from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import *
from .serializers import *


######### API 4 CARS
class APIGetOneCar(APIView):
    def get(self, request, pk):
        cars = Cars.objects.filter(id=pk)
        serializer = CarsSer(cars, many=True)
        return Response(serializer.data)


class APICars(APIView):
    def get(self, request):
        cars = Cars.objects.all()
        serializer = CarsSer(cars, many=True)
        return Response(serializer.data)


    def post(self, request):
        cars = request.data.get('car')
        serializer = CarsSer(data=cars)

        if serializer.is_valid(raise_exception=True):
            cars_saved = serializer.save()
        return Response({
            "Car saved"
        })

    def put(self, request, pk):
        PrevObj = get_object_or_404(Cars.objects.all(), pk=pk)
        newData = request.data.get('car')
        serializer = CarsSer(instance=PrevObj, data=newData, partial=True)
        if serializer.is_valid(raise_exception=True):
            car_saved = serializer.save()
        return Response({
            "success": "Car '{}' updated successfully".format(pk)
        })

    def delete(self, request, pk):
        car = get_object_or_404(Cars.objects.all(), pk=pk)
        car.delete()
        return Response({
            "message": "Car with id `{}` has been deleted.".format(pk)
        }, status=204)


#############API 4 DEALERS
class APIOneDealer(APIView):
    def get(self, request, pk):
        dealer = Dealer.objects.filter(id=pk)
        serializer = DealerSer(dealer, many=True)
        return Response(serializer.data)


class APIDealer(APIView):
    def get(self, request):
        dealer = Dealer.objects.all()
        serializer = DealerSer(dealer, many=True)
        return Response(serializer.data)

    def post(self, request):
        dealer = request.data.get('dealer')
        serializer = DealerSer(data=dealer)

        if serializer.is_valid(raise_exception=True):
            dealer_saved = serializer.save()
        return Response({
            "Dealer saved"
        })

    def put(self, request, pk):
        PrevObj = get_object_or_404(Dealer.objects.all(), pk=pk)
        newData = request.data.get('dealer')
        serializer = DealerSer(instance=PrevObj, data=newData, partial=True)
        if serializer.is_valid(raise_exception=True):
            dealer_saved = serializer.save()
        return Response({
            "success": "Dealer '{}' updated successfully".format(pk)
        })

    def delete(self, request, pk):
        dealer = get_object_or_404(Dealer.objects.all(), pk=pk)
        dealer.delete()
        return Response({
            "message": "Dealer with id `{}` has been deleted.".format(pk)
        }, status=204)


#######API 4 COMPARING
class APIOneComparing(APIView):
    def get(self, request, pk):
        compares = Comparing.objects.filter(id=pk)
        serializer = ComparinSer(compares, many=True)
        return Response(serializer.data)


class APIComparing(APIView):
    def get(self, request):
        compares = Comparing.objects.all()
        serializer = ComparinSer(compares, many=True)
        return Response(serializer.data)

    def post(self, request):
        compares = request.data.get('compares')
        serializer = ComparinSer(data=compares)

        if serializer.is_valid(raise_exception=True):
            compare_saved = serializer.save()
        return Response({
            "Compare saved"
        })

    def put(self, request, pk):
        PrevObj = get_object_or_404(Comparing.objects.all(), pk=pk)
        newData = request.data.get('compares')
        serializer = ComparinSer(instance=PrevObj, data=newData, partial=True)
        if serializer.is_valid(raise_exception=True):
            compare_saved = serializer.save()
        return Response({
            "success": "Compare '{}' updated successfully".format(pk)
        })

    def delete(self, request, pk):
        compare = get_object_or_404(Comparing.objects.all(), pk=pk)
        compare.delete()
        return Response({
            "message": "Compare with id `{}` has been deleted.".format(pk)
        }, status=204)

class OptionalDelete(APIView):
    def post(self, request):
        companyname = DealerSer(Dealer.objects.filter(CompanyName=request.data.get('CompanyName')), many=True).data[0]['id']
        print(companyname)
        modelname = CarsSer(Cars.objects.filter(ModelName=request.data.get('ModelName'), BrandName=request.data.get('BrandName')), many=True).data[0]['id']
        print(companyname, modelname)
        MyObject = get_object_or_404(Comparing.objects.filter(DealerId=companyname, CarId=modelname))
        MyObject.delete()

        return Response({
            "message": "Compare with `{}` has been deleted.".format(request.data.get('CompanyName'))
        }, status=204)
