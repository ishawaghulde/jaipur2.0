
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse

from polls.models import login_user, feedback1_routes, feedback1_text
from polls.serializers import employeeSerializer, feedbackRoutesSerializer, feedbackTextSerializer
from rest_framework import status
from django.shortcuts import render, redirect  
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['PUT','POST', ])
def Review(request):
    try:
        
        update_route=feedback1_routes.objects.get(route_name= request.data['route_name'])
       
        if feedback1_routes.objects.filter(route_name= request.data['route_name']).exists(): 
              serializer= feedbackRoutesSerializer(update_route)
              update_data=serializer.data
              updatez= int(update_data['no_of_reviews'])+1
              update_data['illumination']= ((int(update_data['illumination'])*int(update_data['no_of_reviews']))+int(request.data['illumination']))/updatez
              update_data['overall_safety']= ((int(update_data['overall_safety'])*int(update_data['no_of_reviews']))+int(request.data['overall_safety']))/updatez
              update_data['road_condition']= ((int(update_data['road_condition'])*int(update_data['no_of_reviews']))+int(request.data['road_condition']))/updatez
              update_data['hazardous_contruction']= ((int(update_data['hazardous_contruction'])*int(update_data['no_of_reviews']))+int(request.data['hazardous_contruction']))/updatez
              update_data['no_of_reviews']= int(update_data['no_of_reviews'])+1
              
              sum_rating= int(request.data['illumination'])+int(request.data['overall_safety'])+int(request.data['road_condition'])+int(request.data['hazardous_contruction'])/4
              if sum_rating>2.5:
                  update_data['danger_score']= update_data['danger_score']+ ((sum_rating/4)*update_data['danger_score'])
              else:
                  update_data['danger_score']= update_data['danger_score']- ((sum_rating/4)*update_data['danger_score'])
                

              data={}
              serializer= feedbackRoutesSerializer(update_route, data=update_data)
              if serializer.is_valid():
                 serializer.save()
                 data["success"]="update successful"
                 return Response(data= data)
              return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    except feedback1_routes.DoesNotExist:

            serializer= feedbackRoutesSerializer(data=request.data)
            if serializer.is_valid():
              serializer.save()
              return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def show(request):
    try:
        blog_post = feedback1_routes.objects.all()
    except feedback1_routes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer= feedbackRoutesSerializer(blog_post, many= True)
        return Response(serializer.data)
