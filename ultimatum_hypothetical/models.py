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
Question to Measure "Negative Reciprocity Quantitative" in Preference Survey Module (Hypothetical Ultimatum Game)
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_hypothetical'
    players_per_group = None
    num_rounds = 1

    # prize from the lottery
    endowment = 100


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    negative_reciprocity = models.IntegerField(
        label='',
        min=0, max=Constants.endowment
    )
