from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.settings import api_settings

from app.serializers import VideoDetailSerializer, VideoListSerializer
from app.models import Video


class VideoViewSet(mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    """Get and list videos"""
    serializer_action_classes = {
        "list": VideoListSerializer,
        "retrieve": VideoDetailSerializer,
    }
    queryset = Video.objects.all()
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )
    filter_fields = ("publishing_date", "live_broadcast", "channel")
    ordering_fields = ("publishing_date", "live_broadcast")
    search_fields = ("title")

    def get_serializer_class(self):
        return self.serializer_action_classes[self.action]
    
    def list(self, request, *args, **kwargs):
        queryset = Video.objects.filter().order_by('-publishing_date')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk, format=None):
        video = Video.objects.get(
            pk=pk,
        )
        serializer = self.get_serializer(video, context={"request": request})
        return Response(serializer.data)
