from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from discount_scrapper.serializers import CourseSerializer
from discount_scrapper.services import CourseService


class DiscountViewset(viewsets.ViewSet):

    def list(self, request):
        all_course = CourseService.list_course()
        
        return Response(CourseSerializer(all_course, many=True).data)

    def retrieve(self, request, pk=None):
        all_course = CourseService.get_course(id=pk)
        
        return Response(CourseSerializer(all_course).data)
