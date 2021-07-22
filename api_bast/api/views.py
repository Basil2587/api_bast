from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer
from .permissions import IsAdminUser


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
