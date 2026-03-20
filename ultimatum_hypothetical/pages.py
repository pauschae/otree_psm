from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from shared_utils import common_template_vars

APP_NAME = 'ultimatum_hypothetical'


class Decision(Page):
    form_model = 'player'
    form_fields = ['negative_reciprocity']

    def vars_for_template(self):
        return common_template_vars(
            self.player,
            Constants,
            APP_NAME,
            endowment=Constants.endowment,
        )


page_sequence = [Decision]
