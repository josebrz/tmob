from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Redirect
from ..redis_conection import get_value_from_redis
from .common import ActionBasedPermission


class RedirectViewSet(viewsets.ViewSet):
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        'AllowAny': ['get_resource',]
    }

    @action(detail=False, methods=['GET'])
    def get_resource(self, request):
        key = request.query_params.get('key')
        if not key:
            return Response(
                'key not supplied',
                status.HTTP_400_BAD_REQUEST
            )
        is_cached, value = get_value_from_redis(key)
        if is_cached:
            return Response(
                {
                    "key": key,
                    "value": value
                },
                status.HTTP_200_OK
            )
        return Response(
            'Not Found',
            status.HTTP_404_NOT_FOUND
        )

