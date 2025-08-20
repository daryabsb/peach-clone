from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    name = 'src.transactions'

    def ready(self):
        # import transactions.signals
        pass
