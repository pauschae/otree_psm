from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from shared_utils import app_number

APP_NAME = 'ultimatum_hypothetical'


class Decision(Page):
    form_model = 'player'
    form_fields = ['negative_reciprocity']

    def vars_for_template(self):
        return dict(
            endowment=Constants.endowment,
            part_index=app_number(self.player, APP_NAME)
        )


page_sequence = [Decision]
