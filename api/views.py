from django.shortcuts import get_object_or_404, render
from .models import CategoryMenu, FoodType
from .serializer import CategoryMenuSerializer, FoodTypeSerializer
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status


class FoodTypeViewset(viewsets.ViewSet):
    queryset = FoodType.objects.all()

    def list(self,request):
        serializer = FoodTypeSerializer(self.queryset,many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def create(self,request):
        seralizer = FoodTypeSerializer(data=request.data)
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
        serializer = FoodTypeSerializer(foodType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,pk):
        foodType = get_object_or_404(FoodType,pk=pk)
        foodType.delete()
        return Response({"status":"success","data":"food type  deleted"})


class CategoryMenuviewset(viewsets.ViewSet):
    queryset = CategoryMenu.objects.all()

    def list(self, request):
        """
        This will return list of objects.
        """
        serializer = CategoryMenuSerializer(self.queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def create(self, request):
        """
        This will create an endpoint for POST request.
        """
        serializer = CategoryMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
        
 
    def retrieve(self, request, pk=None):
        """
        Returns a single object
        """
        category = get_object_or_404(self.queryset, pk=pk)
        serializer = CategoryMenuSerializer(category)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
 
    def update(self, request, pk):
        category = CategoryMenu.objects.get(pk=pk)
        serializer = CategoryMenuSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
 
    def partial_update(self, request,pk):
        category = CategoryMenu.objects.get(pk=pk)
        serializer = CategoryMenuSerializer(category, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
 
    def destroy(self, request,pk):
        category = get_object_or_404(CategoryMenu,pk=pk)
        category.delete()
        return Response({"status":"success","data":"Item Deleted"})