from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import FeedItem


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedItem
        fields = '__all__'


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeedItem.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['GET'])
    def me(self, request, pk=None):
        serializer = PostSerializer(FeedItem.objects.filter(user=request.user),
                                    many=True,
                                    context=self.get_serializer_context())
        return Response(
            serializer.data,
            status=200
        )

    @action(detail=False, methods=['GET'])
    def followed(self, request, pk=None):
        posts = FeedItem.objects.filter(user__registered_user__in=request.user.registered_user.tracking.all())
        serializer = PostSerializer(posts, many=True, context=self.get_serializer_context())
        return Response(
            serializer.data,
            status=200
        )
