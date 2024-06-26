from otree.api import *

doc = """
Your app description
"""
class C(BaseConstants):
    NAME_IN_URL = 'Results'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    # Prolific links:
    Completion_redirect = "https://app.prolific.com/submissions/complete?cc=CJVUV8Y1"
    Reject_redirect = "https://app.prolific.com/submissions/complete?cc=C13ABF98"
    Return_redirect = "https://app.prolific.com/submissions/complete?cc=CWE4UX3Q"

    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    blur_event_counts = models.StringField(initial=0, blank=True) # logs how often user clicked out of the page 



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
        return {'hidden_fields': ['blur_event_counts'], #hide the browser field from the participant, see the page to see how this works. #user_clicked_out
                'Instructions': C.Instructions_path} 

#%% Pages
class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.Allowed
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        if player.participant.Allowed:
            bonus_message = player.participant.bonus_message
            variables['bonus_message'] = bonus_message
            
        return variables

class Failed_screening(MyBasePage):
    'This page is displayed if the player failed the comprehension checks'
    @staticmethod
    def is_displayed(player: Player):
        return not player.participant.Comprehension_passed 

    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        failure_message = '''Unfortunately you did not successfuly pass the comprehension check. Because of this we cannot use your data. 
                                We do not want to reject you because of this, so we ask you to <strong>return the study on Prolific</strong>. '''
        # Add or modify variables specific to ExtendedPage
        variables['failure_message'] = failure_message
        return variables

    @staticmethod
    def js_vars(player):
        return dict(
            completion_link = C.Return_redirect
        )

class Failed_attention(MyBasePage):
    @staticmethod
    def is_displayed(player: Player):
        return not player.participant.Attention_passed  # player failed both attention checks
    @staticmethod
    def js_vars(player):
        return dict(
            completion_link = C.Failure_redirect
        )

page_sequence = [Results, Failed_screening, Failed_attention]
