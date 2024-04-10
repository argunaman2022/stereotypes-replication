from otree.api import *
import random

doc = '''
This is the main survey app. It contains
1. Main survey 
2. One attention check.
- You can additionally calculate payoffs and save them at a participant field.
'''
# TODO:scoring of each game (missing: change detection)
#TODO: bonus calculations piece rate vs tournament results.
class C(BaseConstants):
    NAME_IN_URL = 'Study_Name'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Bonus_fee_max = 0.1 #TODO: adjust bonus fee
    Participation_fee = 0.1 #TODO: adjust participation fee
    Piece_rate = 0.1 #USD per correct answer #TODO: fix
    Tournament_rate = 0.2 #USD per correct answer #TODO: fix
    
    # Paths
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"

    Return_redirect = "https://www.wikipedia.org/" #TODO: adjust redirect
    
    Math_memory_template_path = "_templates/global/Math_memory.html"
    Visual_memory_template_path = "_templates/global/Visual_memory.html"
    Quiz_template_path = "_templates/global/Quiz.html"
    SpotTheDifference_template_path = "_templates/global/Change_Detection.html"
    SpotTheDifference_template_Tournament_path = "_templates/global/Change_Detection_Tournament.html"
    
    Round_length = 3660
    Timer_text = "Time left to complete this round:"
    
    
    # Game explanation texts
    MathMemory_text_Math = '''
    For this round you will be given <b>2 minutes</b> to solve as many <b>Math task problems</b> as you can.
    You will see a box with 12 cells. Behind each cell is a simple addition of two one-digit numbers (e.g. 1+2).
    Your task is to find the matching pairs by clicking on the corresponding cells.
    When you find a matching pair, these cells will disappear.
    Once you finish one box, a next box will appear. In total, there are at maximum 4 boxes.
    Each pair found counts as one problem correctly solved!
    <br><br>
    We expect that those with stronger <b>math skills</b> will perform better.
    <br><br>
    An example problem is depicted below. In this picture, 1+2 and 3+0 are matching pairs, since they both equal 3.
    Clicking on these two cells leads to a correct solution 
    '''
    MathMemory_text_Memory = '''
    For this round you will be given <b>2 minutes</b> to solve as many <b>Memory task problems</b> as you can.
    You will see a box with 12 cells. Behind each cell is a simple addition of two one-digit numbers (e.g. 1+2).
    Your task is to find the matching pairs by clicking on the corresponding cells.
    When you find a matching pair, these cells will disappear.
    <br>
    We expect that those with stronger <b>memory skills</b> will perform better.
    Once you finish one box, a next box will appear. In total, there are at maximum 4 boxes.
    Each pair found counts as one problem correctly solved!
    <br><br>
    An example problem is depicted below. In this picture, 1+2 and 3+0 are matching pairs, since they both equal 3.
    Clicking on these two cells leads to a correct solution 
    '''
    
    Visual_memory_text = '''
    For this round you will be given <b>2 minutes</b> to solve as many <b>Visual task problems</b> as you can.
   You will see a box with 12 cells.
   Behind each cell is a picture of an animal.
   There are 6 identical animals in these 12 cells.
   Your task is to find these matching pairs by clicking on the corresponding cells.
   When you find a matching pair, these cells will disappear.
   Once you finish one box, a next box will appear. In total, there are at maximum 4 boxes.
    Each pair found counts as one problem correctly solved!
    <br><br>
    An example problem is depicted below.
    In this picture, the second cell on the first column and the third cell on the second column fprm a matching pair,
    since they both have a picture of an owl.
    Clicking on these two cells leads to a correct solution 
    '''
    
    Quiz_text = '''
    For this round you will be given <b>2 minutes</b> to solve as many <b>Quiz task problems</b> as you can.
    There will be a maximum of 40 multiple-choice questions.
    These questions are from various domains such as Art, Languages, Geography, Technology, History, etc.
    You have to choose the one correct answer out of 4 options.
    These answers become clickable only after 4 seconds of having seen the question.
    For each question, you have a maximum of 10 seconds to answer. If you do not answer within these 10 seconds, the next question will be displayed.
    Each correctly answered question counts as one problem correctly solved!
    <br><br>
    An example problem is depicted below. Here, the correct answer is "F. Scott Fitzgerald"
    '''
    SpotTheDifference_text = '''
    For this round you will be given <b>2 minutes</b> to solve as many <b>Spot-The-Difference task problems</b> as you can. 
    In this task, you will see two pictures. 
    The picture on the left and the picture on the right are very similar but there are a 10 differences.
    Your task is to find these differences and click on them on the <b>right picture</b>.
    You can place at most 10 marks and you can change or remove them at any time. Once you have placed all your marks, you can submit your answers.
    Each correctly marked difference counts as one problem solved. 
    <br><br>
    An example is depicted below. 
    In this example, three differences are marked: on the right picture the bridge and the third kid are missing, and the first kid has a different shirt. 
    '''
       
    # Game explanation pics
    MathMemory_pic = 'pics/MathMemory_pic.png'
    Visual_memory_pic = 'pics/VisualMemory_pic.png' 
    Quiz_pic = 'pics/Quiz_pic.png' 
    SpotTheDifference_pic = 'pics/ChangeDetection_pic.png' 
    
    ## Piece rate vs Tournament
    #TODO: this doesn't work well with some tasks because of the wording of the tasks i.e. in math memory you don't "solve" problems
    Piece_rate_text = f'''<strong>Round 1. Payment information</strong>:
    If this round is randomly chosen to determine your bonus payment,
    then you will receive <strong>{Piece_rate}</strong> USD per problem you solve correctly in this round. 
    Your payment is not influenced by the performance of others in your group.
    Wrong answers do not decrease your payment. We call this payment scheme the <strong>"Piece-rate"</strong> payment, please remember this.'''
    
    Tournament_text = f'''<strong>Round 2. Payment information</strong>: If this round is chosen to determine your bonus payment,
        then you will receive either:
        <ul>
            <li> <strong>{Tournament_rate}</strong> USD per correctly solved problem in this round,
    if you answer more problems correctly than any of the other 5 people in your group in this round. 
            <li> <strong>0</strong> USD per correctly solved problem,
    if anyone else in your group answers more problems correctly than you in this round.
    We call this payment scheme the <strong>"Tournament"</strong> payment, please remember this.
        </ul>
        This round will start when you click "Continue". You will be given 2 minutes in total.
    Throughout the round, a timer will display the remaining time.
        '''
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
    game1_Competition_Choice = models.BooleanField(choices = [[True, 'Tournament Rate'], [False, 'Piece Rate']],
                                                   label='For this round, I choose')
    ## Second Game
    game2_Piece_rate = models.IntegerField(initial=0) #correct answers
    game2_Tournament = models.IntegerField(initial=0) 
    game2_Competition_Choice = models.BooleanField(choices = [[True, 'Tournament Rate'], [False, 'Piece Rate']],
                                                label='For this round, I choose')

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
        
def get_game_text(player, game2, Tournament_for_Change_detection=False):
    if game2 == 'VisualMemory':
        game2_explanation_text = C.Visual_memory_text
        game2_explanation_pic = C.Visual_memory_pic
        game2_path = C.Visual_memory_template_path
    elif game2 == 'Quiz':
        game2_explanation_text = C.Quiz_text
        game2_explanation_pic = C.Quiz_pic
        game2_path = C.Quiz_template_path
    elif game2 == 'SpotTheDifference':
        game2_explanation_text = C.SpotTheDifference_text
        game2_explanation_pic = C.SpotTheDifference_pic
        game2_path = C.SpotTheDifference_template_path
        if Tournament_for_Change_detection:
            game2_path = C.SpotTheDifference_template_Tournament_path
    
    return game2_explanation_text, game2_explanation_pic, game2_path
 
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
          

class Page1_G1_R1_E(MyBasePage):
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
    
class Page2_G1_R1(MyBasePage):
    extra_fields = ['game1_Piece_rate'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    timeout_seconds = C.Round_length
    timer_text = C.Timer_text
    
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
        
        variables['Game_path'] = C.Math_memory_template_path
        return variables
    
    @staticmethod
    def js_vars(player):
        game1, _, Treatment_math_or_memory = get_game(player)
        return dict(
            game_name = game1,
            game_field_name = 'id_game1_Piece_rate',
        )

class Page3_G1_R1_R(MyBasePage):
    extra_fields = []
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)

        # players score in previous round
        variables['game1_score'] = player.game1_Piece_rate
        variables['Treatment'] = player.participant.Treatment   
        return variables

class Page4_G1_R2_E(MyBasePage):
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
        
        variables['Game_path'] = C.Math_memory_template_path
        return variables

class Page5_G1_R2(MyBasePage):
    extra_fields = ['game1_Tournament']
    form_fields = MyBasePage.form_fields + extra_fields
    
    timeout_seconds = C.Round_length
    timer_text = C.Timer_text
    
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
        
        variables['Game_path'] = C.Math_memory_template_path
        return variables
    
    @staticmethod
    def js_vars(player):
        game1, _, Treatment_math_or_memory = get_game(player)
        return dict(
            game_name = game1,
            game_field_name = 'id_game1_Tournament',
        )

class Page6_G1_R2_R(MyBasePage):
    extra_fields = [] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)

        # players score in previous round
        variables['game1_score'] = player.game1_Tournament
        variables['Treatment'] = player.participant.Treatment   
        return variables
    
class Page7_G2_R1_E(MyBasePage):
    extra_fields = [] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory = get_game(player)
        
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2)
        
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game2_explanation_text
        variables['Game_explanation_pic'] = game2_explanation_pic
        
        variables['Game_path'] = game2_path
        return variables
    

        
class Page8_G2_R1(MyBasePage):
    extra_fields = ['game2_Piece_rate']
    form_fields = MyBasePage.form_fields + extra_fields
    
    timeout_seconds = C.Round_length
    timer_text = C.Timer_text
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory = get_game(player)
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2)
                
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game2_explanation_text
        variables['Game_explanation_pic'] =  game2_explanation_pic
        
        variables['Game_path'] =game2_path 
        return variables

    @staticmethod
    def js_vars(player):
        _, game2, Treatment_math_or_memory = get_game(player)
        return dict(
            game_name = game2,
            game_field_name = 'id_game2_Piece_rate',
        )
    
class Page9_G2_R1_R(MyBasePage):
    extra_fields = [] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        variables = MyBasePage.vars_for_template(player)
        variables['Prev_Score'] = player.game1_Tournament
        return variables
    
        
class Page10_G2_R2_E(MyBasePage):
    extra_fields = []
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory = get_game(player)
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2)
                
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game2_explanation_text
        variables['Game_explanation_pic'] =  game2_explanation_pic
        
        variables['Game_path'] =game2_path 
        return variables
    
class Page11_G2_R2(MyBasePage):
    extra_fields = ['game2_Tournament'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    timeout_seconds = C.Round_length
    timer_text = C.Timer_text
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory = get_game(player)
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2, Tournament_for_Change_detection=True)
                
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game2_explanation_text
        variables['Game_explanation_pic'] =  game2_explanation_pic
        variables['Game_path'] =game2_path 
        
        
        return variables
    
    @staticmethod
    def js_vars(player):
        _, game2, Treatment_math_or_memory = get_game(player)
        return dict(
            game_name = game2,
            game_field_name = 'id_game2_Tournament',
        )
    
class Page12_G2_R2_R(MyBasePage):
    extra_fields = [] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):

        variables = MyBasePage.vars_for_template(player)
        variables['prev_score'] = player.game2_Tournament
        
        return variables
    
class Page13_G1_Choice(MyBasePage):
    extra_fields = ['game1_Competition_Choice'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory = get_game(player)
                
        variables = MyBasePage.vars_for_template(player)
        variables['game1_name'] = game1
        variables['Game_explanation_pic'] =  C.MathMemory_pic
        variables['Prev_Score'] = player.game1_Piece_rate
        
        return variables
    
class Page14_G2_Choice(MyBasePage):
    extra_fields = ['game1_Competition_Choice'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory = get_game(player)
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2)
                
        variables = MyBasePage.vars_for_template(player)
        variables['game2_name'] = game1
        variables['Game_explanation_pic'] =  game2_explanation_pic
        variables['Prev_Score'] = player.game2_Piece_rate
        return variables
    
    
page_sequence = [
    Page1_G1_R1_E, Page2_G1_R1, Page3_G1_R1_R,
    Attention_check_2,
    Page4_G1_R2_E, Page5_G1_R2, Page6_G1_R2_R,
    Page7_G2_R1_E, Page8_G2_R1, Page9_G2_R1_R,
    Page10_G2_R2_E, Page11_G2_R2, Page12_G2_R2_R,
    Page13_G1_Choice, Page14_G2_Choice
    ]
