from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, Http404


from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TutorialSerializer

    def perform_create(self, serializer):
        serializer.validated_data['created_by'] = self.request.user
        return super().perform_create(serializer)

    def get_queryset(self):
        return Tutorial.objects.filter(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.soft_delete()
            return  JsonResponse(
                status=204,
                data={
                    "status": True,
                    "message": "Successfully Deleted Tutorial",
                    "data": {},
                    "issues": None
                }
            )
        except Http404:
            return JsonResponse({'success': False})
            



