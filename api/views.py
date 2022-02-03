from django.shortcuts import get_object_or_404, render
from .models import FoodType
from .serializer import FoodTypeSeralizer
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status


class FoodTypeViewset(viewsets.ViewSet):
    queryset = FoodType.objects.all()

    def list(self,request):
        serializer = FoodTypeSeralizer(self.queryset,many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def create(self,request):
        seralizer = FoodTypeSeralizer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response({
                "status":"success",
                "data":seralizer.data,
                
            },
            status= status.HTTP_201_CREATED
            )
        else:
            return Response({"status":"error","data":seralizer.errors},status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        foodType = FoodType.objects.get(pk=pk)
        serializer = FoodTypeSeralizer(foodType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,pk):
        foodType = get_object_or_404(FoodType,pk=pk)
        foodType.delete()
        return Response({"status":"success","data":"food type  deleted"})