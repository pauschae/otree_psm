from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
from shared_utils import common_template_vars


class WillingnessToAct(Page):
    form_model = 'player'
    form_fields = ['forego_future', 'punish_unfair', 'punish_unfair_others', 'give_free']

    def vars_for_template(self):
        return common_template_vars(self.player, Constants, 'willingness_to_act')


page_sequence = [
    WillingnessToAct,
]
