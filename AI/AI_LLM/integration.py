from .company_analysis import analyze_company
from .email_generator import generate_email
from .lead_scoring import calculate_score
from .meeting_summary import generate_summary
from .dashboard import get_dashboard_stats


class SalesGenieAI:

    @staticmethod
    def analyze_company(data):
        return analyze_company(data)

    @staticmethod
    def generate_email(data):
        return generate_email(data)

    @staticmethod
    def calculate_score(data):
        return calculate_score(data)

    @staticmethod
    def generate_summary(data):
        return generate_summary(data)

    @staticmethod
    def dashboard():
        return get_dashboard_stats()