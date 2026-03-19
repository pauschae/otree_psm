from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
from shared_utils import common_template_vars

APP_NAME = 'self_assessment'


class SelfAssessment(Page):
    form_model = 'player'
    form_fields = ['favor_return', 'unjust_revenge', 'people_best_intent']

    def vars_for_template(self):
        return common_template_vars(self.player, Constants, APP_NAME)


class RiskAssessment(Page):
    form_model = 'player'
    form_fields = ['risk_assessment']

    def vars_for_template(self):
        return common_template_vars(self.player, Constants, APP_NAME)


page_sequence = [
    SelfAssessment,
    RiskAssessment,
]
