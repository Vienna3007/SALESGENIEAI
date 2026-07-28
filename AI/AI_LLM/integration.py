from .sales_pipeline import process_company
from .meeting_summary import generate_summary
from .dashboard import get_dashboard_stats


class SalesGenieAI:

    @staticmethod
    def process_company(company):
        return process_company(company)

    @staticmethod
    def meeting_summary(request):
        return generate_summary(request)

    @staticmethod
    def dashboard(leads):
        return get_dashboard_stats(leads)