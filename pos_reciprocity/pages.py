from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from shared_utils import app_number

APP_NAME = 'pos_reciprocity'


class Reciprocity(Page):
    form_model = 'player'
    form_fields = ['reciprocity']

    def vars_for_template(self):
        return dict(
            stranger_cost=Constants.stranger_cost,
            cheap_present=Constants.cheap_present,
            expensive_present=Constants.expensive_present,
            part_index=app_number(self.player, APP_NAME)
        )


page_sequence = [Reciprocity]
