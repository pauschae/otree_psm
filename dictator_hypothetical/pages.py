from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from shared_utils import app_number

APP_NAME = 'dictator_hypothetical'


class Altruism(Page):
    form_model = 'player'
    form_fields = ['altruism_hypothetical']

    def vars_for_template(self):
        return common_template_vars(
            self.player,
            Constants,
            APP_NAME,
            endowment_str="{:,}".format(Constants.endowment),
            endowment=Constants.endowment,
            part_index=app_number(self.player, APP_NAME)
        )


page_sequence = [Altruism]
