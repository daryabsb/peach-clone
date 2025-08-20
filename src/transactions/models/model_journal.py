from django.db import models
from src.finances.models import AccountSub
from django.apps import apps

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



MODEL_CHOICES = (
    ('Purchase', 'PURCHASE'),
    ('Sale', 'SALE'),
    ('Payment', 'PAYMENT'),
    ('Receive', 'RECEIVE'),
)



class Journal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    dr_account = models.ForeignKey(
        AccountSub, on_delete=models.CASCADE, related_name='debit_account')
    cr_account = models.ForeignKey(
        AccountSub, on_delete=models.CASCADE, related_name='credit_account')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    sender_model = models.CharField(max_length=10, null=True, blank=True)

    model_id = models.PositiveIntegerField(null=True, blank=True)

    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f'Dr: {self.dr_account}-{self.amount} --- Cr: {self.cr_account}-{self.amount}'
        return f'{self.created} - {self.dr_account}'

    @property
    def get_transaction(self):
        transaction_model = apps.get_model('transactions', self.sender_model)
        transaction = transaction_model.objects.get(id=self.object_id)
        return transaction

    @property
    def get_output(self):
        output = self.dr_account.main.account_section
        if output == 'Assets' or output == 'Liability' or output == 'Equity':
            print(self.dr_account.main.account_section)
            return 'balance'
        else:
            return 'income'

    @classmethod
    def export_to_excel(cls, queryset, filename=None):
        """
        Exports Journal queryset to Excel
        Args:
            queryset: Journal queryset to export
            filename: Custom filename (optional)
        Returns:
            Tuple of (file_data, filename) for further handling
        """
        import os
        from django.conf import settings
        EXPORT_DIR = os.path.join(settings.BASE_DIR, 'journal_exports')
        os.makedirs(EXPORT_DIR, exist_ok=True)
    
        filename = f"journal_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        filepath = os.path.join(EXPORT_DIR, filename)

        if not filename:
            filename = f"journal_export_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Journal Entries"
        
        # Column headers
        headers = [
            'ID', 'Created Date', 'Debit Account', 'Credit Account', 
            'Sender Model', 'Model ID', 'Description', 'Amount', 'Updated Date'
        ]
        
        # Write headers
        for col_num, header in enumerate(headers, 1):
            ws.cell(row=1, column=col_num, value=header)
        
        # Write data rows
        for row_num, journal in enumerate(queryset, 2):
            ws.cell(row=row_num, column=1, value=journal.id)
            ws.cell(row=row_num, column=2, value=journal.created.strftime('%Y-%m-%d %H:%M'))
            ws.cell(row=row_num, column=3, value=str(journal.dr_account))
            ws.cell(row=row_num, column=4, value=str(journal.cr_account))
            ws.cell(row=row_num, column=5, value=journal.sender_model or '')
            ws.cell(row=row_num, column=6, value=journal.model_id or '')
            ws.cell(row=row_num, column=7, value=journal.description or '')
            ws.cell(row=row_num, column=8, value=float(journal.amount))
            ws.cell(row=row_num, column=9, value=journal.updated.strftime('%Y-%m-%d %H:%M'))
        
        # Auto-adjust column widths
        for col_num in range(1, len(headers) + 1):
            column_letter = get_column_letter(col_num)
            ws.column_dimensions[column_letter].width = 20
        
        # Save to bytes buffer instead of HttpResponse
        buffer = BytesIO()
        wb.save(filepath)
        buffer.seek(0)
        
        return filepath
