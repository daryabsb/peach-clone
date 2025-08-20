from core.models import Journal

def export_journals_to_excel():
    # Get your queryset (you can filter as needed)
    journals = Journal.objects.all().select_related('dr_account', 'cr_account')
    
    # Call the export function
    return Journal.export_to_excel(journals, 'Journals.xlsx')


def run():
    export_journals_to_excel()
