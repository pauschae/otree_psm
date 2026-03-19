from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Luca Congiu & Salvatore Nunnari (Bocconi University)'

doc = """
Question to Measure "Altruism Quantitative" in Preference Survey Module (Hypothetical Dictator Game)
"""


class Constants(BaseConstants):
    name_in_url = 'dictator_hypothetical'
    players_per_group = None
    num_rounds = 1

    endowment = 1_000


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    altruism_hypothetical = models.IntegerField(
        min=0, max=Constants.endowment,
        label=''
    )

