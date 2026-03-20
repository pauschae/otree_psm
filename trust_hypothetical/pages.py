from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from shared_utils import app_number

APP_NAME = 'trust_hypothetical'

APP_NAME = 'trust_hypothetical'


def base_template_vars(player, page_number):
    return common_template_vars(
        player,
        Constants,
        APP_NAME,
        endowment=Constants.endowment,
        rate=Constants.rate,
        max_endowment=Constants.max_endowment,
        other_transfer=Constants.other_transfer,
        page=self.subsession.round_number,
        part_index=app_number(self.player, APP_NAME),
        currency=Constants.currency,
        instructions=Constants.instructions_template,
        page=page_number,
    )


class Instructions(Page):
    pass


class Introduction(Page):

    form_model = 'player'

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return base_template_vars(self.player, self.subsession.round_number)

    def before_next_page(self):
        return self.player.compute_endowment(),


class Receiver(Page):

    form_model = 'player'
    form_fields = ['transfer']

    # only display from round 1 to 4
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number <= Constants.num_rounds - 1

    def vars_for_template(self):
        return base_template_vars(self.player, self.subsession.round_number) | dict(
            other_endowment=self.participant.vars['other_endowment'],
            final_endowment=self.participant.vars['final_endowment'],
            other_transfer=self.participant.vars['other_transfer']
        )

    def before_next_page(self):
        return self.player.increase_other_transfer(), self.player.compute_endowment()


class Sender(Page):

    form_model = 'player'
    form_fields = ['transfer']

    # only display instruction in round 5
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds


page_sequence = [Introduction, Receiver, Sender]
