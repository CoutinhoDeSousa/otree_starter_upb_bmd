from otree.api import *


doc = """
Simple trust game for VHB Course
"""


class C(BaseConstants):
    NAME_IN_URL = 'trustgame_vhb'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(10)
    MULTIPLIER = 3
    INSTRUCTIONS_TEMPLATE = '' # Todo: Name of the instruction Page (hint same folder)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=cu(0),
        max=C.ENDOWMENT,
        doc="""Amount sent by Player 1""",
        label="How much do you want to send to participant B?",
    )
    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by Player 2""", label="How much do you want to send back?"
    )


class Player(BasePlayer):
    pass


# FUNCTIONS
def sent_back_amount_choices(group: Group):
    return currency_range(0, group.sent_amount * C.MULTIPLIER, 1)


def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount


# PAGES
class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        pass # Todo: Only if Player 1


class WaitForP1(WaitPage):
    pass


class SendBack(Page):
    form_model = 'group'
    form_fields = [] # todo: Which FormFields do we have here?

    @staticmethod
    def is_displayed(player: Player):
        pass # todo: only display if you are the second player

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [WaitPage] ## Todo , right sequence