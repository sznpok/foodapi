from django.shortcuts import get_object_or_404, render
from .models import CategoryMenu, FoodType, Orders,SubCategoryMenu, Table, TableType
from .serializer import CategoryMenuSerializer, FoodTypeSerializer,SubCategoryMenuSerializer, TableSerializer, TableTypeSerializer,OrderSerialzer
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
        serializer = CategoryMenuSerializer(self.queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = CategoryMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
        
 
    def retrieve(self, request, pk=None):
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
 
    def destroy(self, request,pk):
        category = get_object_or_404(CategoryMenu,pk=pk)
        category.delete()
        return Response({"status":"success","data":"Item Deleted"})



class SubCategoryMenuviewset(viewsets.ViewSet):
    queryset = SubCategoryMenu.objects.all()

    def list(self, request):
        serializer = SubCategoryMenuSerializer(self.queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = SubCategoryMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
        
 
    def retrieve(self, request, pk=None):
        sub_category = get_object_or_404(self.queryset, pk=pk)
        serializer = SubCategoryMenuSerializer(sub_category)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
 
    def update(self, request, pk):
        sub_category = SubCategoryMenu.objects.get(pk=pk)
        serializer = SubCategoryMenuSerializer(sub_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
 
    def destroy(self, request,pk):
        sub_category = get_object_or_404(SubCategoryMenu,pk=pk)
        sub_category.delete()
        return Response({"status":"success","data":"Item Deleted"})


class Tableviewset(viewsets.ViewSet):
    queryset = Table.objects.all()

    def list(self, request):
        serializer = TableSerializer(self.queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
        
 
    def retrieve(self, request, pk=None):
        table = get_object_or_404(self.queryset, pk=pk)
        serializer = TableSerializer(table)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
 
    def update(self, request, pk):
        table = Table.objects.get(pk=pk)
        serializer = TableSerializer(table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
 
    def destroy(self, request,pk):
        table = get_object_or_404(Table,pk=pk)
        table.delete()
        return Response({"status":"success","data":"Item Deleted"})


class TableTypeviewset(viewsets.ViewSet):
    queryset = TableType.objects.all()

    def list(self, request):
        serializer = TableTypeSerializer(self.queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = TableTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
        
 
    def retrieve(self, request, pk=None):
        tableType = get_object_or_404(self.queryset, pk=pk)
        serializer = TableTypeSerializer(tableType)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
 
    def update(self, request, pk):
        tableType = TableType.objects.get(pk=pk)
        serializer = TableTypeSerializer(tableType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
 
    def destroy(self, request,pk):
        tableType = get_object_or_404(TableType,pk=pk)
        tableType.delete()
        return Response({"status":"success","data":"Item Deleted"})\

class Orderviewset(viewsets.ViewSet):
    queryset = Orders.objects.all()

    def list(self, request):
        serializer = OrderSerialzer(self.queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = OrderSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
        
 
    def retrieve(self, request, pk=None):
        order = get_object_or_404(self.queryset, pk=pk)
        serializer = OrderSerialzer(order)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
 
    def update(self, request, pk):
        order = Orders.objects.get(pk=pk)
        serializer = OrderSerialzer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status = status.HTTP_201_CREATED)

        else:
            return Response({"status":"error","data":serializer.errors},status = status.HTTP_400_BAD_REQUEST)
 
    def destroy(self, request,pk):
        order = get_object_or_404(Orders,pk=pk)
        order.delete()
        return Response({"status":"success","data":"Item Deleted"})
