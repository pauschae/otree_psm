from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from shared_utils import common_template_vars

APP_NAME = 'pos_reciprocity'


class Reciprocity(Page):
    form_model = 'player'
    form_fields = ['reciprocity']

    def vars_for_template(self):
        return common_template_vars(
            self.player,
            Constants,
            APP_NAME,
            stranger_cost=Constants.stranger_cost,
            cheap_present=Constants.cheap_present,
            expensive_present=Constants.expensive_present,
        )


page_sequence = [Reciprocity]
