from otree.api import *
import random
import numpy as np

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
    
    Bonus_fee_max = 1.2 # max bonus fee is 1.2 USD
    Participation_fee = 1.2 # participation fee is 1.2 USD
    
    Piece_rate_Memory = 0.03 # Bonus_fee_max/36 #USD per correct answer 
    Piece_rate_SpotTheDifference = 0.12 #1.2/6 #USD per correct answer 
    Piece_rate_Quiz = 0.04 #1.2/30 #USD per correct answer 
    
    Tournament_rate_Memory = 6*Piece_rate_Memory #USD per correct answer 
    Tournament_rate_SpotTheDifference = 6*Piece_rate_SpotTheDifference #USD per correct answer 
    Tournament_rate_Quiz = 6*Piece_rate_Quiz #USD per correct answer 
    
    
    # Paths
    Instructions_path = "_templates/global/Instructions.html"
    Quit_study_text_path = "_templates/global/Quit_study_text.html"

    # Prolific links:
    Completion_redirect = "https://app.prolific.com/submissions/complete?cc=CJVUV8Y1"
    Reject_redirect = "https://app.prolific.com/submissions/complete?cc=C13ABF98"
    Return_redirect = "https://app.prolific.com/submissions/complete?cc=CWE4UX3Q"
    
        
    Math_memory_template_path = "_templates/global/Math_memory.html"
    Visual_memory_template_path = "_templates/global/Visual_memory.html"
    Quiz_template_path = "_templates/global/Quiz.html"
    SpotTheDifference_template_path = "_templates/global/Change_detection.html"
    SpotTheDifference_template_Tournament_path = "_templates/global/Change_detection_Tournament.html"
    
    Round_length = 120
    Timer_text = "Time left to complete this round:"
    
    
    # Game explanation texts
    MathMemory_text_Math = '''
    For this round you will be given <b>2 minutes</b> to solve as many <b>Math task problems</b> as you can.
    You will see a box with 12 cells. Behind each cell is a simple addition of two one-digit numbers (e.g. 1+2).
    Your task is to find the matching pairs by clicking on the corresponding cells.
    When you find a matching pair, these cells will disappear.
    Once you finish one box, another will appear.
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
    Once you finish one box, another will appear.
    Each pair found counts as one problem correctly solved!
    <br><br>
    An example problem is depicted below. In this picture, 1+2 and 3+0 are matching pairs, since they both equal 3.
    Clicking on these two cells leads to a correct solution 
    '''
    
    Visual_memory_text = '''
    For this round you will be given <b>2 minutes</b> to solve as many <b>Visual Memory problems</b> as you can.
   You will see a box with 12 cells.
   Behind each cell is a picture of an animal.
   There are 6 identical animals in these 12 cells.
   Your task is to find these matching pairs by clicking on the corresponding cells.
   When you find a matching pair, these cells will disappear.
   Once you finish one box, another will appear.
    Each pair found counts as one problem correctly solved!
    <br><br>
    An example problem is depicted below.
    In this picture, the second cell on the first column and the third cell on the second column fprm a matching pair,
    since they both have a picture of an owl.
    Clicking on these two cells leads to a correct solution 
    '''
    
    Quiz_text = '''
    For this round you will be given <b>2 minutes</b> to solve as many <b>Quiz task problems</b> as you can.
    There will be a maximum of 30 multiple-choice questions.
    These questions are from various domains such as Art, Languages, Geography, Technology, History, etc.
    You have to choose the one correct answer out of 4 options.
    These answers become clickable only after 4 seconds of having seen the question.
    For each question, you have a maximum of 10 seconds to answer. If you do not answer within these 10 seconds, the next question will be displayed.
    Each correctly answered question counts as one problem correctly solved!
    <br><br>
    An example problem is depicted below. Here, the correct answer is "F. Scott Fitzgerald"
    '''
    SpotTheDifference_text = '''
    For this round you will be given <b>2 minutes</b> to solve as many <b>SpotTheDifference task problems</b> as you can. 
    In this task, you will see two pictures. 
    The picture on the left and the picture on the right are very similar but there are 10 differences.
    Your task is to find these differences and click on them on the <b>right picture</b>.
    You can place at most 10 marks and you can change or remove them at any time.
    Each correctly marked difference counts as one problem solved. 
    <br><br>
    An example is depicted below. 
    In this example, three differences are marked: on the right picture the bridge and the third kid are missing, and the first kid has a different shirt 
    '''
       
    # Game explanation pics
    MathMemory_pic = 'https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/MathMemory_pic.png'
    Visual_memory_pic = 'https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/VisualMemory_pic.png' 
    Quiz_pic = 'https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/Quiz_pic.png' 
    SpotTheDifference_pic = 'https://raw.githubusercontent.com/argunaman2022/stereotypes-replication/master/_static/pics/ChangeDetection_pic.png'
    

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):   
    bonus_payoff = models.FloatField(initial=0)
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
    game1_Competition_Choice = models.BooleanField(choices = [[True, 'I choose to apply the Tournament-rate to my round 1 score.'],
                                                              [False, 'I choose to apply the Piece-rate to my round 1 score.']],
                                                   label='For round 3:')
    ## Second Game
    game2_Piece_rate = models.IntegerField(initial=0) #correct answers
    game2_Tournament = models.IntegerField(initial=0) 
    game2_Competition_Choice = models.BooleanField(choices = [[True, 'I choose to apply the Tournament-rate to my round 1 score.'],
                                                              [False, 'I choose to apply the Piece-rate to my round 1 score.']],
                                                   label='For round 3:')

    ## Extra fields for certain tasks
    Game1_attempts_R1 = models.IntegerField(initial=0) # logs the number of attempts in the math memory game
    Game1_attempts_R2 = models.IntegerField(initial=0) # logs the number of attempts in the math memory game
    #The Game2 attempts are only relevant in the visual memory game
    Game2_attempts_R1 = models.IntegerField(initial=0) # logs the number of attempts in the math memory game
    Game2_attempts_R2 = models.IntegerField(initial=0) # logs the number of attempts in the math memory game
    
    # Whether the player clicked out of the page
    blur_event_counts = models.StringField(initial=0, blank=True) # logs how often user clicked out of the page 

 
#%% Functions
def Payment_info(player, game):
    assert game in ['MathMemory', 'VisualMemory', 'Quiz', 'SpotTheDifference']
    ## Piece rate vs Tournament
    if game in ['MathMemory', 'VisualMemory']:
        Piece_rate = C.Piece_rate_Memory
        Tournament_rate = C.Tournament_rate_Memory
    elif game == 'Quiz':
        Piece_rate = C.Piece_rate_Quiz
        Tournament_rate = C.Tournament_rate_Quiz
    elif game == 'SpotTheDifference':
        Piece_rate = C.Piece_rate_SpotTheDifference
        Tournament_rate = C.Tournament_rate_SpotTheDifference
    return Piece_rate, Tournament_rate

def get_game(player):
    Treatment = player.participant.Treatment
    # split treatment based on _
    First_part, Second_part = Treatment.split('_')[0], Treatment.split('_')[1]
    Treatment_math_or_memory = First_part
    
    Game1 = 'MathMemory'
    
    Game1_Page_title = Treatment_math_or_memory + ' game'
    Game2_Page_title = Second_part + ' game'

    return Game1, Second_part, Treatment_math_or_memory, Game1_Page_title, Game2_Page_title
        
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
        _, _, Treatment_math_or_memory, Game1_title, _ = get_game(player)
        
        if Treatment_math_or_memory == 'Math':
            game1_explanation_text = C.MathMemory_text_Math
        elif Treatment_math_or_memory=='Memory':
            game1_explanation_text = C.MathMemory_text_Memory
        game1_explanation_pic = C.MathMemory_pic
        
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game1_explanation_text
        variables['Game_explanation_pic'] = game1_explanation_pic
        variables['Game_title'] = Game1_title
        variables['Payment_info'] = Payment_info(player, 'MathMemory')
        return variables
    
class Page2_G1_R1(MyBasePage):
    extra_fields = ['game1_Piece_rate','Game1_attempts_R1'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    timeout_seconds = C.Round_length
    timer_text = C.Timer_text
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        
        if Treatment_math_or_memory == 'Math':
            game1_explanation_text = C.MathMemory_text_Math
        elif Treatment_math_or_memory=='Memory':
            game1_explanation_text = C.MathMemory_text_Memory
        game1_explanation_pic = C.MathMemory_pic
        
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game1_explanation_text
        variables['Game_explanation_pic'] = game1_explanation_pic
        
        variables['Game_path'] = C.Math_memory_template_path
        variables['Game_title'] = Game1_title

        return variables
    
    @staticmethod
    def js_vars(player):
        game1, _, Treatment_math_or_memory, _, _ = get_game(player)
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
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)


        # players score in previous round
        variables['game1_score'] = player.game1_Piece_rate
        variables['Treatment'] = player.participant.Treatment   
        variables['Game_title'] = Game1_title
        return variables

class Page4_G1_R2_E(MyBasePage):
    extra_fields = [] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        
        if Treatment_math_or_memory == 'Math':
            game1_explanation_text = C.MathMemory_text_Math
        elif Treatment_math_or_memory=='Memory':
            game1_explanation_text = C.MathMemory_text_Memory
        game1_explanation_pic = C.MathMemory_pic
        
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game1_explanation_text
        variables['Game_explanation_pic'] = game1_explanation_pic
        
        variables['Game_path'] = C.Math_memory_template_path
        variables['Game_title'] = Game1_title
        return variables

class Page5_G1_R2(MyBasePage):
    extra_fields = ['game1_Tournament', 'Game1_attempts_R2']
    form_fields = MyBasePage.form_fields + extra_fields
    
    timeout_seconds = C.Round_length
    timer_text = C.Timer_text
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        
        if Treatment_math_or_memory == 'Math':
            game1_explanation_text = C.MathMemory_text_Math
        elif Treatment_math_or_memory=='Memory':
            game1_explanation_text = C.MathMemory_text_Memory
        game1_explanation_pic = C.MathMemory_pic
        
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game1_explanation_text
        variables['Game_explanation_pic'] = game1_explanation_pic
        
        variables['Game_path'] = C.Math_memory_template_path
        variables['Game_title'] = Game1_title
        return variables
    
    @staticmethod
    def js_vars(player):
        game1, _, Treatment_math_or_memory, _,_ = get_game(player)
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
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)

        # players score in previous round
        variables['game1_score'] = player.game1_Tournament
        variables['Treatment'] = player.participant.Treatment   
        variables['Game_title'] = Game1_title
        return variables
    
class Page7_G2_R1_E(MyBasePage):
    extra_fields = [] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2)
        
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game2_explanation_text
        variables['Game_explanation_pic'] = game2_explanation_pic
        
        variables['Game_path'] = game2_path
        variables['Game_title'] = Game2_title
        variables['Piece_rate'] = Payment_info(player, game2)[0]
        return variables
    

        
class Page8_G2_R1(MyBasePage):
    extra_fields = ['game2_Piece_rate', 'Game2_attempts_R1']
    form_fields = MyBasePage.form_fields + extra_fields
    
    timeout_seconds = C.Round_length
    timer_text = C.Timer_text
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2)
                
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game2_explanation_text
        variables['Game_explanation_pic'] =  game2_explanation_pic
        
        variables['Game_path'] =game2_path 
        variables['Game_title'] = Game2_title
        return variables

    @staticmethod
    def js_vars(player):
        _, game2, Treatment_math_or_memory, _, _ = get_game(player)
        return dict(
            game_name = game2,
            game_field_name = 'id_game2_Piece_rate',
        )
    
class Page9_G2_R1_R(MyBasePage):
    extra_fields = [] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        variables = MyBasePage.vars_for_template(player)
        variables['Prev_Score'] = player.game2_Piece_rate
        variables['Game_title'] = Game2_title
        return variables
    
        
class Page10_G2_R2_E(MyBasePage):
    extra_fields = []
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2)
                
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game2_explanation_text
        variables['Game_explanation_pic'] =  game2_explanation_pic
        variables['Game_title'] = Game2_title
        
        variables['Game_path'] =game2_path 
        variables['Tournament_rate'] = Payment_info(player, game2)[1]

        return variables
    
class Page11_G2_R2(MyBasePage):
    extra_fields = ['game2_Tournament', 'Game2_attempts_R2'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    timeout_seconds = C.Round_length
    timer_text = C.Timer_text
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2, Tournament_for_Change_detection=True)
                
        variables = MyBasePage.vars_for_template(player)
        variables['Game_explanation_text'] = game2_explanation_text
        variables['Game_explanation_pic'] =  game2_explanation_pic
        variables['Game_path'] =game2_path 
        variables['Game_title'] = Game2_title
        
        return variables
    
    @staticmethod
    def js_vars(player):
        _, game2, Treatment_math_or_memory, _, _ = get_game(player)
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
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        variables['prev_score'] = player.game2_Tournament
        variables['Game_title'] = Game1_title
        
        return variables
    
class Page13_G1_Choice(MyBasePage):
    extra_fields = ['game1_Competition_Choice'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
                
        variables = MyBasePage.vars_for_template(player)
        variables['game1_name'] = game1
        variables['Game_explanation_pic'] =  C.MathMemory_pic
        variables['Prev_Score'] = player.game1_Piece_rate
        variables['Game_title'] = Game1_title
        variables['Piece_rate'] = Payment_info(player, game2)[0]
        variables['Tournament_rate'] = Payment_info(player, game2)[1]

        return variables
    
class Page14_G2_Choice(MyBasePage):
    extra_fields = ['game2_Competition_Choice'] 
    form_fields = MyBasePage.form_fields + extra_fields
    
    @staticmethod
    def vars_for_template(player: Player):
        game1, game2, Treatment_math_or_memory, Game1_title, Game2_title = get_game(player)
        game2_explanation_text, game2_explanation_pic, game2_path  = get_game_text(player, game2)
                
        variables = MyBasePage.vars_for_template(player)
        variables['game2_name'] = game2
        variables['Game_explanation_pic'] =  game2_explanation_pic
        variables['Prev_Score'] = player.game2_Piece_rate
        variables['Game_title'] = Game2_title
        variables['Piece_rate'] = Payment_info(player, game2)[0]
        variables['Tournament_rate'] = Payment_info(player, game2)[1]
        return variables
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened=False):
        participant = player.participant
        # choose 1 of the 6 rounds randomly as the bonus_relevant_round
        bonus_relevant_round = np.random.choice([1, 2, 3, 4, 5, 6])
        
        game2 = participant.Treatment.split('_')[1]
        if game2== 'VisualMemory':
            game2_piece_rate = C.Piece_rate_Memory
            game2_tournament_rate = C.Tournament_rate_Memory
        elif game2 == 'Quiz':
            game2_piece_rate = C.Piece_rate_Quiz
            game2_tournament_rate = C.Tournament_rate_Quiz
        elif game2 == 'SpotTheDifference':
            game2_piece_rate = C.Piece_rate_SpotTheDifference
            game2_tournament_rate = C.Tournament_rate_SpotTheDifference

        participant.bonus_relevant_round = bonus_relevant_round
        # if round is G1R1 or G2R1 multiply that with the piece rate with the number of correct solutions in those rounds
        # if round is G1R2 or G2R2 ex post matching based on win status
        # if round is G1R3 or G2R3 multiply that with the piece rate if the player has chosen Piece rate in these rounds,
        # else ex post matching based on win status
        if bonus_relevant_round == 1:
            participant.bonus_payoff = round(player.game1_Piece_rate*C.Piece_rate_Memory, 2)
            participant.score = player.game1_Piece_rate
            participant.bonus_message = f'''Round {bonus_relevant_round} was randomly selected to be the bonus-relevant round.
            In this round you completed {participant.score} questions correctly.
            As a result your bonus payment is {participant.bonus_payoff}$ = {participant.bonus_payoff/C.Piece_rate_Memory} * {C.Piece_rate_Memory}$.'''
        elif bonus_relevant_round == 2:
            participant.score = player.game1_Tournament
            participant.bonus_message = f'''Round {bonus_relevant_round} was randomly selected to be the bonus-relevant round.
            In this round you completed {participant.score} questions correctly. As a result,
            Once all the participants have finished, you will earn {round(participant.score*C.Tournament_rate_Memory,2)}$ if you have answered more questions correctly than the other 5 people in your group.'''
        elif bonus_relevant_round == 3:
            participant.bonus_payoff = round(player.game2_Piece_rate*game2_piece_rate, 2)
            participant.score = player.game2_Piece_rate
            participant.bonus_message = f'''Round {bonus_relevant_round} was randomly selected to be the bonus-relevant round.
            In this round you completed {participant.score} questions correctly.
            As a result your bonus payment is {participant.bonus_payoff}$ = {participant.score} * {game2_piece_rate}$.'''
        elif bonus_relevant_round == 4:
            participant.score = player.game2_Tournament
            participant.bonus_message = f'''Round {bonus_relevant_round} was randomly selected to be the bonus-relevant round.
            In this round you completed {participant.score} questions correctly. As a result,
            Once all the participants have finished, you will earn {round(participant.score*game2_tournament_rate,2)}$ if you have answered more questions correctly than the other 5 people in your group.'''            
        elif bonus_relevant_round == 5 and player.game1_Competition_Choice:
            participant.score = player.game1_Piece_rate
            participant.bonus_message = f'''Round {bonus_relevant_round} was randomly selected to be the bonus-relevant round.
            In round 1 of Game 1 you completed {participant.score} questions correctly and you chose to apply Tournament rate to your round 1 performance.
            Once all the participants have finished, you will earn {round(participant.score*C.Tournament_rate_Memory,2)}$ if you have answered more questions correctly than the other 5 people in your group in this round.'''            
        elif bonus_relevant_round == 5 and not player.game1_Competition_Choice:
            participant.bonus_payoff = round(player.game1_Piece_rate*C.Piece_rate_Memory, 2)
            participant.score = player.game1_Piece_rate
            participant.bonus_message = f'''Round {bonus_relevant_round} was randomly selected to be the bonus-relevant round.
            In round 1 of Game 1 you completed {participant.score} questions correctly and you chose to apply Piece-rate to your round 1 performance.
            As a result your bonus payment is {participant.bonus_payoff}$ = {participant.bonus_payoff/C.Piece_rate_Memory} * {C.Piece_rate_Memory}$..'''            
        elif bonus_relevant_round == 6 and player.game2_Competition_Choice:
            participant.score = player.game2_Piece_rate
            participant.bonus_message = f'''Round {bonus_relevant_round} was randomly selected to be the bonus-relevant round.
            In round 1 of Game 2 you completed {participant.score} questions correctly and you chose to apply Tournament rate to your round 1 performance. As a result,
            Once all the participants have finished, you will earn {round(participant.score*game2_tournament_rate,2)}$ if you have answered more questions correctly than the other 5 people in your group in this round.'''            
        elif bonus_relevant_round == 6 and not player.game2_Competition_Choice:
            participant.bonus_payoff = round(player.game2_Piece_rate*game2_piece_rate, 2)
            participant.score = player.game2_Piece_rate
            participant.bonus_message = f'''Round {bonus_relevant_round} was randomly selected to be the bonus-relevant round.
            In round 1 of Game 2 you completed {participant.score} questions correctly and you chose to apply Piece-rate to your round 1 performance.
            As a result your bonus payment is {participant.bonus_payoff}$ = {participant.bonus_payoff/game2_piece_rate} * {game2_piece_rate}$..'''      
                    

        

page_sequence = [
    Page1_G1_R1_E, Page2_G1_R1, Page3_G1_R1_R,
    Attention_check_2,
    Page4_G1_R2_E, Page5_G1_R2, Page6_G1_R2_R,
    Page7_G2_R1_E, Page8_G2_R1, Page9_G2_R1_R,
    Page10_G2_R2_E, Page11_G2_R2, Page12_G2_R2_R,
    Page13_G1_Choice, Page14_G2_Choice,
    ]
