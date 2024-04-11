from otree.api import *
#TODO: calculate payoffs and stuff

doc = """
Your app description
"""
class C(BaseConstants):
    NAME_IN_URL = 'Pilot'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    # Prolific links, gotten from the study page on prolific
    Completion_redirect = 'https://www.wikipedia.org/' #TODO: adjust redirect
    Failure_redirect = 'https://www.wikipedia.org/' #TODO: adjust redirect
    Return_redirect = 'https://www.wikipedia.org/' #TODO: adjust redirect

    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    blur_event_counts = models.StringField(initial=0) # logs how often user clicked out of the page #TODO: ensure that this is added to all the pages
    Pilot1 = models.StringField(label='How much difficulty did you have in understanding the general instructions?',
                                choices=['No difficulty at all', 'Some difficulty', 'Moderate difficulty', 'A lot of difficulty'],
                                widget=widgets.RadioSelectHorizontal
                )
    Pilot2 = models.StringField(label='How much difficulty did you have in understanding the instructions of the first game?',
                                choices=['No difficulty at all', 'Some difficulty', 'Moderate difficulty', 'A lot of difficulty'],
                                widget=widgets.RadioSelectHorizontal
                )

    Pilot4 = models.StringField(label='How much difficulty did you have in understanding the instructions of the second game?',
                                choices=['No difficulty at all', 'Some difficulty', 'Moderate difficulty', 'A lot of difficulty'],
                                widget=widgets.RadioSelectHorizontal
                )
    Pilot5 = models.StringField(label='How difficult do you think the first game will be for other Prolific participants?',
                                choices=['Not difficult at all', 'Somewhat difficult', 'Moderately difficult', 'Very difficult'],
                                widget=widgets.RadioSelectHorizontal
                )
    Pilot6 = models.StringField(label='How difficult do you think the second game will be for other Prolific participants?',
                                choices=['Not difficult at all', 'Somewhat difficult', 'Moderately difficult', 'Very difficult'],
                                widget=widgets.RadioSelectHorizontal
                )
    Pilot7 = models.StringField(label='How much fun/engaging was the first game for you?',
                                choices=['Not fun at all', 'Somewhat fun', 'Moderately fun', 'Very fun'],
                                widget=widgets.RadioSelectHorizontal
                )
    Pilot8 = models.StringField(label='How much fun/engaging was the second game for you?',
                                choices=['Not fun at all', 'Somewhat fun', 'Moderately fun', 'Very fun'],
                                widget=widgets.RadioSelectHorizontal
                )

    Pilot3 = models.StringField(label='How much difficulty did you have in understanding the two payment schemes (Tournament vs Piece-rate)?',
                            choices=['No difficulty at all', 'Some difficulty', 'Moderate difficulty', 'A lot of difficulty'],
                            widget=widgets.RadioSelectHorizontal
            )

# PAGES

#%% Base Pages
class MyBasePage(Page):
    'MyBasePage contains the functions that are common to all pages'
    form_model = 'player'
    form_fields = ['blur_event_counts']
    
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed 
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'hidden_fields': ['bullshit'], #hide the browser field from the participant, see the page to see how this works. #user_clicked_out
                'Instructions': C.Instructions_path} 

#%% Pages

class Pilot(MyBasePage):
    form_model = 'player'
    form_fields = ['Pilot1', 'Pilot3','Pilot2',  'Pilot4', 'Pilot5', 'Pilot6', 'Pilot7', 'Pilot8', ]
    

page_sequence = [Pilot]
