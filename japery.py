import random
from ursina import *
from ursina.prefabs.health_bar import HealthBar

tt = 0
def update():
    global tt, show_text, time_left, player_number
    if player_number != player_hot_seat:
        Player_unhot_seat()
    else:
        tt += 1
        if tt >= 10:
            tt = 0
            time_left.value -= 1
        Player_hot_seat()
        if time_left.value < 0:
            if player_number < 4:
                player_number += 1
            else:
                player_number = 1

app = Ursina()
questions = [
    "What are you currently doubting in your life?","What is your best shower thought?","What do you think is the most valuable resource?",'What’s the flavor of gum you wish existed?',
    "What's your story about breaking the law?","What's your favorite form of entertainment?","What type of exercise do you like most?",'If your life was a sitcom, which one it would be?',
    'If you could change one thing about your family, what would it be?','What is your favorite spice?',"for What is your favorite spice?",'What is something you never shared with me?',
    "What's the story behind your favorite memento?",'Are you currently going through any type of phase?',"What is your opinion on social media?","Which is your favorite day of the week?",
    'What was the last big mistake you made?',"What do you do in secret that you're proud of?","Can you describe your personal style?","What do you regret doing in life?",
    "What's your favorite room in your house and why?",'What situation is sure to make you cry?',"Where was your secret hiding place as a child?","When does life hits different for you?",
    'What is your opinion on tattoos?','Do you have a favorite brand?',"What's simply too difficult?","What destination is at the top of your list to visit?",
    "What's the story about the last time you cried?",'What would your dream day look like?',"Where do you draw the line?","How do you usually react if you receive bad service?",
    'What is something you feel is unacceptable that is still being done today?',"What app or website completely changed your life?","How well do you think you understand yourself?",
    'Do you name inanimate objects?','What do you see happening in your future?',"What mode of transportation have you never tried?","What's the strangest thing you've ever found?",
    'What would be the best thing about losing your hearing?','What was your last "ah-ha" moment?',"What part of your body currently doesn't feel 100%?","What is your favorite spice?",
    "What's your close call story?",'Can you explain love?','What is it that motivates yourself the most?',"Do you believe in Reincarnation?","What is the one random word you always say?"]
player_hot_seat = random.randint(1,4)
player_number = 1
class Answer(Button):
    def __init__(self, position=(0,0,0),text = ''):
        super().__init__()
        self.parent = scene
        self.position = position
        self.model = 'circle'
        self.highlight_color = color.black
        self.text = text
        self.scale = 1
        self.collider = 'mesh'
        self.z = 1

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if self.text == '':
                    global question_text,player_number
                    time_left.value = 100
                    question_text.text = random.choice(questions)
                    player_number += 1
                if self.text != 'QA':
                    player_number += 1
                    Audio('Buzzer Sound Effect.mp4')
                else:
                    if len(user_field.text) > 0:
                        questions.append(user_field.text + '?')
                        user_field.text = ""
                    else:
                        user_field.text = ""
                        print_on_screen("question needs to be longer",position = (-0.16,0.01))

def Player_unhot_seat():
    player_text = Text(text = 'Player: {}'.format(player_number),y = 0.43,x = -0.07)
    user_field = InputField(y=-.35,text = 'Post a question',x = 0)

    answer1 = Answer(position = (-2,0),text = 'Lie')
    answer1.color = color.red
    answer3 = Answer(position = (0,2),text = 'QA')
    answer3.color = color.orange
    answer2 = Answer(position = (2,0),text = 'Truth')
    answer2.color = color.blue

show_text = False
time_left = HealthBar(max_value = 100,scale = (1.6,0.02),y = 0.38)
question_text = Text(text=random.choice(questions), y=0.3, x=-0.8, scale=1.5)
def Player_hot_seat():
    global show_text
    if show_text == False:
        player_text = Text(text = 'Player: {}'.format(player_number),y = 0.43,x = -0.04)
        show_text = True
    answer1 = Answer(position = (0.3,0),text = '')
    answer1.color = color.red
app.run()
