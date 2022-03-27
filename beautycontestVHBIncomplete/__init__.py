from otree.api import *


doc = """
Your app description
"""
'''
Constant Variables
They dont change over the course of the experiment

'''

class C(BaseConstants):
    NAME_IN_URL = 'beautycontestVHBIncomplete'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3

    guess_max = 100
    jackpot = Currency(5)
    winner_payoff = c(1)
    fixed_payoff = c(0)

'''
For future experiments you can append subsessions to every model 
this goes here. For this experiment this class remains empty.
'''
class Subsession(BaseSubsession):
    pass

'''
Here you will calculate what is needed and 
set the payoff
'''
class Group(BaseGroup):
    group_average = models.FloatField()  # group average
    target_value = models.FloatField()  # target value (2/3 of group average)
    best_guess = models.FloatField()  # best Guess
    '''
    Don't change anything above 
    '''

    def set_payoffs(self):
        '''
        Calculate the average of all received numbers, calculate the target value, determine which player
        made the best guess and determine who is the winner

        get a list of the current player
        each player in the list has every attribute you are looking for
        for example:
            players[1].my_guess
            is the guess of the second player
            !!!! Notice : Python counts from 0 up !!!!
        at the beginning, is_winner is not initialized , you should set it to zero and
        only change it for the actual winner
        '''
        players = self.get_players()  # list of current players

        i = 0  # your counting variable for the while-loop, Feel free to delete it, if you do not need it




'''
Here are the variables per Player 
'''


class Player(BasePlayer):
    # Player variables

    '''
       you need to add the variables my_diff and total_wins. Think which models you need.
       '''

    is_winner = models.BooleanField(
        initial=False,
        doc="""
            True if player had the winning guess
            """
    )

    my_guess = models.FloatField(
        initial=None,
        min=0, max=C.guess_max,
        doc="""
            Each player guess: between 0-{}
            """.format(C.guess_max)
    )


# PAGES
class MyPage(Page):
    pass
'''
Registering all the pages you need for your experiment
First is the introduction page. Only displayed in the beginning
'''
class Introduction(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

#Page where participants type in their numbers
class Guess(Page):

    form_model = models.Player
    form_fields = ['my_guess']

#this is standard. no changes necessary
class StandardWaitPage(WaitPage):
     body_text = "Please wait for the other contestants"

#between the input and the result in this waiting page, the calculation takes place
#here the method you wrote should be executed
class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
       # self.group.<the name of your method>

    body_text = "Please wait for the other contestants"

#The results for every round
class ResultRounds(Page):
    '''
    Please name the 3 Variables for the ResultRounds.html as followed , otherwise the page will not work:
            'group_average'
            'target_value'
            'diff'
    use round(<variable>,2) to round it to 2 decimalpoints.


    '''
    def vars_for_template(self):
    return{
        #Insert here the variables
    }

#This is the final result screen
class Results(Page):
    def is_displayed(self):
        return self.subsession.round_number == C.NUM_ROUNDS

    '''
    Calculate total_payoff 
    for this you have to sum over every round and put it into the total_payoff variable
    when you enter the code below, it will return whatever is in total_payoff

    sum([p.payoff for p in self.player.in_all_rounds()]) # this comment sums up the payoff of each player 
    Please be sure the name of the variable is 'total_payoff' 
    '''

    def vars_for_template(self):
        return {
            # Insert here the total_payoff variable you want to pass on
        }


page_sequence = [Introduction,StandardWaitPage,Guess,ResultsWaitPage,ResultRounds,Results]
