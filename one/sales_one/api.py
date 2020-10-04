from . import models
from . import serializers
from rest_framework import viewsets, permissions


class InvoiceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Invoice class"""

    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoiceItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the InvoiceItem class"""

    queryset = models.InvoiceItem.objects.all()
    serializer_class = serializers.InvoiceItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReceiveViewSet(viewsets.ModelViewSet):
    """ViewSet for the Receive class"""

    queryset = models.Receive.objects.all()
    serializer_class = serializers.ReceiveSerializer
    permission_classes = [permissions.IsAuthenticated]


