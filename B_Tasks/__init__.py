from otree.api import *
import random

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''

class C(BaseConstants):
    NAME_IN_URL = 'Study_Name'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"

    Return_redirect = "https://www.wikipedia.org/" #TODO: adjust redirect
    
    Math_memory_template_path = "_templates/global/Math_memory.html"
    Visual_memory_template_path = "_templates/global/Visual_memory.html"
    Quiz_template_path = "_templates/global/Quiz.html"
    ChangeDetection_template_path = "_templates/global/Change_Detection.html"
    
    Round_length = 3660
    Timer_text = "Time left to complete this round:"
    
    
    # Game explanation texts
    #TODO: add the other game explanation texts.
    MathMemory_text_Math = 'This is a Math game. [PLACEHOLDER]'
    MathMemory_text_Memory = 'This is a Memory game. [PLACEHOLDER]'
    
    
    # Game explanation pics
    #TODO: add the other game example pics
    MathMemory_pic = 'pics/MathMemory_pic.png'
    
    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):   
    # Attention check 2, 1 was in introduction 
    Attention_2 = models.BooleanField(choices=[
            [True, 'I disagree.'],
            [False, 'I think both are possible.'],
            [False, 'I agree.'],], 
        label= 'A 20 year old man can eat 500kg meat and 2 tons of vegetables in one meal.', widget=widgets.RadioSelect)
            
            
    # Scores and trials from each game. There are 6 games but each player plays only 2. See treatment for the order.
    ## First game
    game1_Piece_rate = models.IntegerField(initial=0) #correct answers
    game1_Tournament = models.IntegerField(initial=0) 
    game1_Competition_Choice = models.BooleanField(choices = [[True, 'Tournament'], [False, 'Piece Rate']],
                                                   label='Which of the following do you choose? [WORDING]',)
    ## Second Game
    game2_Piece_rate = models.IntegerField(initial=0) #correct answers
    game2_Tournament = models.IntegerField(initial=0) 
    game2_Competition_Choice = models.BooleanField(choices = [[True, 'Tournament'], [False, 'Piece Rate']],
                                                label='Which of the following do you choose? [WORDING]',)

    ## Extra fields for certain tasks
    #TODO: ensure this is called only in math memory and write js code to save the values
    Math_memory_attempts = models.IntegerField(initial=0) # logs the number of attempts in the math memory game
    #TODO: ensure this is called only in Quiz and write js code to save the values
    Quiz_correct_wrong = models.StringField(blank=True) # logs the correct and wrong answers in the quiz
    
    # Whether the player clicked out of the page
    blur_event_counts = models.StringField(initial=0) # logs how often user clicked out of the page #TODO: ensure that this is added to all the pages

 
#%% Functions
def get_game(player):
    Treatment = player.participant.Treatment
    # split treatment based on _
    First_part, Second_part = Treatment.split('_')[0], Treatment.split('_')[1]
    Treatment_math_or_memory = First_part
    
    Game1 = 'MathMemory'

    return Game1, Second_part, Treatment_math_or_memory
        
 
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
                'Instructions': C.Instructions_path,
                'Treatment': player.participant.Treatment,} 
  
# Pages
class Attention_check_2(MyBasePage):         
    extra_fields = ['Attention_2']
    form_fields = MyBasePage.form_fields + extra_fields
    
    def before_next_page(player: Player, timeout_happened=False):
        if (not player.Attention_2 and not player.participant.vars['Attention_1']):
            player.participant.vars['Allowed'] = False
            player.participant.vars['Attention_passed'] = False
            
class Page1(MyBasePage):
    extra_fields = []
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory = get_game(player)
        
        if Treatment_math_or_memory == 'Math':
            game1_explanation_text = C.MathMemory_text_Math
        elif Treatment_math_or_memory=='Memory':
            game1_explanation_text = C.MathMemory_text_Memory
        game1_explanation_pic = C.MathMemory_pic
        
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game1_explanation_text
        variables['Game_explanation_pic'] = game1_explanation_pic
        return variables
    
class Page2(MyBasePage):
    extra_fields = ['game1_Piece_rate'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    timeout_seconds = C.Round_length
    timer_text = C.Timer_text
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        return variables
    
    @staticmethod
    def js_vars(player):
        return dict(
            game_name = 'Card',
            game_field_name = 'id_game1_Piece_rate',
        )
    

            
  # add back  Page3, Page4, Page5, Page6, Page7, Page8, Page9, Page10, Page11, Page12, Page13, Page14, Page15,
page_sequence = [
    Page1, Page2, 
    Attention_check_2,
    ]
