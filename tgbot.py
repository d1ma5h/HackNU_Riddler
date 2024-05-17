import telebot
import pandas as pd
from datetime import datetime
from collections import defaultdict

TOKEN = '6432827107:AAGNbJFmioxEkoU3xovtm52tjunqiDuTQEE'
bot = telebot.TeleBot(TOKEN)

EXCEL_FILE_PATH = 'C:\\Users\\fsfs1\\Downloads\\bot\\teams.xlsx'

questions = [
    "Расшифруйте сообщение:\nQYYN VEMU YX IYEB DBOKCEBO REXD!",
    "Допустим, светофор работает по следующему расписанию: z̵̡̢̧̨̢̨̡̡̡̧̢̧̡̢̨̡̢̡̡̛̛̛̛̝͓͔̤͇̹̻͍̯̪͉̩̦̰̟͍͖͍̰̻̜̤̝͔͇̺̠̰̜̳̦̦͇͕̗̺͖̜̝̟̮̟͉̥̱̫̤̝͉͈͍̪̻̯̖̺͓̤̭̙͉̮̣̙̱͉͙͚͍̘̲̫̭͎̲͈͖̰̩̭͎̮̗̠̞̩̥̙̝̝̺̞̠̲̯͔͕͇̘̯̺͈͖̭̮̹̝̰̪̗̗̼͇̻͓̲̠̞͙̬̯͎̘̪͎̙̖͇͚̤̫̙̜̤͕̯̳̬̪̗͔̙̜̜̰̫̻͈̳͖͉͇̻͓̪̭̞͈̖̪̼̳̞̠̙̙̤̼̙͖̟̖͎̣̗̹͈͖̝̳̦̞̞̮̯̙͕̺̥̩͈͋̐́̆͒̌́̑̀̒͑́͌͒́̎̅̅͑̈́̇͒̽̈́̏̍̎͆͆͛̉̃̄̀̽́͊̉̃̅͘̚͜͜͜͜͜͠͝ͅͅͅͅa̸̡̡̧̡̢̨̡̨̨̨̧̨̡̛̭̲̠͚͓̭̞̠̜̲̲̞͇̼̦̼̼̝̤̞͚͉̪̯̱̬͓͙͍̫͓̬̱̱̗̖̭͕̣̞̺̜̙͙͎̖̥͔̝̯̝̼̹̯͙̦̰̜͔͓͍͖̞̬͎̳̳̗̖̖͚̩͚͈̩̗̟̼͈̮͙̭̼͕̮̲͖̻͕͚̲̺͕̮̬̖̜̻̤̳̬͕̮̣̱̰̭̯̼͔̯̼̦̜̣͍̣̱̻̜̗̩͈͚͇̞̼̭̝͎̣͚͂̓̒͂̓̄̋́̈̏͗̏́̈́̃͑́̏̾͐̀͂̾̓́͐͐̅͌̈́́͗͐̀̈̈́̍̿͒̏͋̈́̒̍́̎̿̎̑̈́͐̃̎̑̓̂̅̍̎̓͌̀̉͌̾̓͒̌͌̋͛̅̂͒͐̒̇̿̊̌̀͐́̈́̄̌͗͗̏̾̒̽̓̓̈̎́͐̊̍͊̽͋̿̿̉̀̈́̈́̉̌̒̍̀͗͆̍̌̔͆̈̈́̍͛̽̉̃̓̄̎̈́̋̍̎̉̀̌̍͌̀͌̈́̏̿͑̒̈́̉̅͌͊̏͌̽̈́̚̕̕͘͘͘̚̕͘͘̚̚̚̚͘͜͜͜͜͠͠͝͠͠ͅͅz̶̨̨̧̢̧̢̢̢̢̧̡̧̛̛̛̛̛̛̛̫̪̙͔̖͔͇̠̬̤̳͎̺̫̮̱͇͓̫̣̞͔̪͍͔̣̗͕̻̫̯̜͎͍͈̫̮͓͈͉̘̖͚̮͉̮͍̝̗̘͍̯̖̱̣̗̬̱͖͓̙̭̲̫͉͈͇̲̠͕̬̮̣̫̻͉͇̠͖̥͎̰̰̰̟͕̖̘̭̻̺̝͉͍̹̥̣̟̮͍̬̦͖͚͚̤̗̭̪̼͚͍͖͓̼̤̭̹̬͕̞̼̱̘̪̫͇̻͎̞̣͔̥͍̗̩͖͇̠̺̤͖̭̲͙̩̦̫̘̦͎̈̊́̔̂̓̐̈́́̃̿̎̽̒̆̉̔̾̐̔̂̊͗̀̌̀͂̅̅́̓͌̈̇͋̏͐͛̐͌̋̒̂̏̉̈̀̈́̄́̀͒̈́̍̄̒̐̂́͗̽̃͐̔̇̂̒͗̏̍̎̏̃͑̀̆́͒̐́̊́̑̊̓͆̒̔̑̀̽͂̈́̎̋͐̎͗͐͐͒̊̆͌̂͛̀̂͐͒́̄̆̂̓̈́̊́͗́̄̆̉͐̓̏̎̿͑̌̿̾̈́̏̈́̀̈́̑̔̾͌̓̔͊̀̀̋̌̇̈́̅̐̊̋́̏̃̆͐̀̎͊́͆̏̎̊̎̋͐̈́́̊̌̋̾͌̍̾̈́͑̆̋̈̂̋́̍̉̊͂̏̋̂̇̉͊̿͗̅̕̚͘̚̕̕͜͜͜͜͜͜͝͠͝͝͝͠͝͠͝͝͠͠͠͠͝͝͠͠͝͝͝͝͝ͅͅͅͅͅͅͅͅͅначала горит красный сигнал в течение 24 секунд, затем красный вместе с жёлтым — 10 секунд, после чего загорается зелёный на 15 секунд, и, наконец, жёлтый сигнал в течение 10 секунд. Этот цикл повторяется непрерывно. Необходимо выяснить, как долго каждый из сигналов был активен, если светофор проработал в общей сложности 200 секунд.\nОтвет в виде X, Y, Z",
    "Найдите три целых числа x, y, z такие, что их кубы в сумме дают 42 \nОтвет в виде X, Y, Z",
    "Игрок выбирает одну из трех дверей, за одной из которых находится приз. Ведущий, который знает, где находится приз, открывает одну из оставшихся дверей, за которой приза нет, и предлагает игроку изменить свой выбор. Какова вероятность выигрыша, если игрок решит изменить свой выбор? \nОтвет в виде дроби",
    "Представьте, что у вас есть бинарное дерево поиска. e̸̢̡̤̺̅̌̆̀̑̊̈́̒͑͆͂̈̆̀̿͒̏̔͊̌̎́̆͗͑̈́͐͗́͊̋̏̈́͐̈́͆͌̇̽́̊̇̽̀̽̏̔̊̇̋̈́̔̍̈́̔̽̄̂̿̄̄̾͂̇̇̀͌̇̆̅̋̍̃̕̚̚̕͘͝͝͝͠͝͝͝͠͝ͅ ̴̢̢̨̧̧̡̨̡̨̡̧̢̭̖͕̺̩̱̣̩̭̘̝̲̤͙͉̻̳̫̲̤͉͍͕̫̯̻̹̣̦͙͎̼͉̱͔͉̤̟̪̩̺͓̬̝͉̠̥̦̦͎̤̽̌͌͗̿͆̄͋͒̈̄͊̍̂͊̾̀̚͘̕͜͜͝͠ͅͅͅͅy̶̢̨̨̡̡͍̮̤̭̠̳̙̭̱̦̖̩̻̫̼̘̮̖̼͎̱͎̺͕̬͓̠̞̮̻͚͈̺̞̤͔̙̺̣̦͆̅́̇͛̓̅̄̃̒̽͗̚Какое минимальное количество узлов должно быть в таком дереве, чтобы глубина дерева была равна 5?",
    "57 цифр числа Пи после запятой",
    "Какое минимальное a̵̢̢̢̡̢̨̡̨͈̖̰͕̰̩̪͚̟̦͇̥̭̺͍͖͙̱̗̤̪̱̝̺͖̬̝̼͎͈̺̺̗̥̘̻̥̙̯͇̲͎̦̜̬̠̺̮̬̦͓͙̞̝͓̺͎͉̯̹̭̫̗̼̠̣͎̮̳̙̯̱̪̘͖̭͉̙̙͔̳͓̹̼̦̥͓͍̦̫̻͎̭̙͙̣͕̩̖̮̮̫͖̙͖̻͇͔̰̺̳̼̦̪̠̋͜͜͜͜ͅż̴̡̡̢̨̛͓͇͖̝̺̜͎̳̥̹̠̟̬͙̮̟̳̹̠̺͔̱͙̬̗̻̱͖̹̻̺͉͉͕͖͈͇̯̮͚̭̯̝̩̩͎̺͇̦̣̩̮̱̗͎̘͚̖͓͍͚̮̺̍̑̀̽̅͐̏̿̓̈́͑̉̇́̆́͂̎̑̈̍̾̾̈́̈́̆̿̈̋͐̏̿̾̿̐̏̎̈́͌̿́̇̄̎͗̍̿̆͌̈̿̈̚̚̚͘̕̚͘̕͝͝͠ͅколичество ходов необходимо, чтобы решить задачу о Ханойской башне с помощью 6 дисков?",
    "Evirfg Funzve Nqyrzna: \nmhJdAfXXAc+gXCsi9yYmhDUTDHLrInUkc01BupX9bO3n6wFtZHxB3asGngAWlfcPEv62ytJul/Z3a8zm7NcERnApic6FsIJfOXo8ptZ1TwbUq7wap6AbBalYD2dcm0VAguv+5DvP4+AkAn9xFOIbKuhPxaZBmm5w1J9IXfFI+O8=",
    "- .-. -.-- / -- --- .-. . --..-- / --. ..- -.-- ... ....- -- -... --.. --. --.- ....- - -.-. -- --.. - --. .- ..--- - .. --- .--- --.. --. --.- ...-- ... -.-- .. -... -..- --. . -..- -.. .. -- -... ... --. -.-- ..--- -.. --.- -- .--- .-- --. ..- ..--- -.. -- -- -... -..- --. ....- -...- -...- -...- -...- -...- -...- \nОтвет на английском языке",
    "Write d̷̨̨̩̭̰̦̟͈͖̗͚̖̎̆̀͊͑́̕own the 'year' of study ǒ̶͖͓̭͇̞̑̕f you̷͓͇̠̯͎͇͎͓̺̼͌̃̏̏́̈́͂͛̅̇͝ͅr team captain in The MAGIKAL ALPHABET"
]

answers = [
    "GOOD LUCK ON YOUR TREASURE HUNT!",
    "125, 60, 45",
    "-80538738812075974, 80435758145817515, 12602123297335631",
    "2/3",
    "6",
    "141592653589793238462643383279502884197169399375105820974",
    "63",
    "Hello, World!",
    "Stella",
    ""
]

def load_valid_team_codes(filename):
    df = pd.read_excel(filename, engine='openpyxl')
    valid_codes = df[df.iloc[:, 34] == 1].iloc[:, 35].tolist()
    return valid_codes

valid_team_codes = load_valid_team_codes(EXCEL_FILE_PATH)

def load_team_info(filename):
    df = pd.read_excel(filename, engine='openpyxl')
    valid_teams = df[df.iloc[:, 34] == 1][['team_code', 'captian_year']]
    team_info = valid_teams.set_index('team_code')['captian_year'].to_dict()
    return team_info

team_info = load_team_info(EXCEL_FILE_PATH)

chat_state = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id in chat_state and chat_state[chat_id].get('completed', False):
        bot.send_message(chat_id, "Вы уже завершили квест! Если хотите начать заново, используйте команду /restart.")
        return
    elif chat_id in chat_state:
        bot.send_message(chat_id, "Квест уже начат! Продолжите отвечать на вопросы.")
        return

    chat_state[chat_id] = {
        'authenticated': False,
        'team_code': None,
        'current_question': 0,
        'start_time': datetime.now(),  
        'question_start_time': datetime.now(), 
        'completed': False  
    }
    bot.send_message(chat_id, "Добро пожаловать! Введите код своей команды, чтобы начать квест")



@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    chat_id = message.chat.id
    if not chat_state[chat_id]['authenticated']:
        if message.text.strip() in valid_team_codes:
            chat_state[chat_id] = {'authenticated': True, 'team_code': message.text.strip(), 'current_question': 0}
            send_question(message)
        else:
            bot.reply_to(message, "Неверный код. Попробуйте еще раз")
    else:
        process_answer(message, message.text.strip())

def send_question(message):
    chat_id = message.chat.id
    chat_state[chat_id]['question_start_time'] = datetime.now()
    question_index = chat_state[chat_id]['current_question']
    if question_index < len(questions):
        formatted_question = questions[question_index]
        if question_index == 1 or question_index == 2: 
            formatted_question = formatted_question.replace("Ответ в виде X, Y, Z", "*Ответ в виде X, Y, Z*")
        elif question_index == 3:  
            formatted_question = formatted_question.replace("Ответ в виде дроби", "*Ответ в виде дроби*")
        elif question_index == len(questions) - 1: 
            formatted_question = formatted_question.replace("Ответ на английском языке", "*Ответ на английском языке*")

        bot.send_message(chat_id, f"Задание {question_index + 1}:\n{formatted_question}", parse_mode='Markdown')

def process_answer(message, answer):
    chat_id = message.chat.id
    question_index = chat_state[chat_id]['current_question']
    question_end_time = datetime.now()
    question_duration = question_end_time - chat_state[chat_id]['question_start_time']

    if question_index == len(questions) - 1:  
        team_code = chat_state[chat_id]['team_code']
        captain_year = team_info.get(team_code, '').lower()
        
        year_to_number = {
            'first': '69912',
            'found': '66354',
            'second': '153654',
            'third': '28994',
            'forth': '66928'
        }
        
        correct_answer = year_to_number.get(captain_year, '')
        
        if answer == correct_answer:
            total_time = datetime.now() - chat_state[chat_id]['question_start_time']
            bot.send_message(chat_id, f"Вы успешно завершили квест! Время выполнения: {total_time}")
            bot.send_animation(chat_id, 'https://i.pinimg.com/originals/f8/3d/cf/f83dcf0c379de146ef962251952577ab.gif')
            print(f"Team {team_code} completed the quest in {total_time}, last question took {question_duration}")
            return  
        else:
            bot.reply_to(message, "Неправильно, попробуйте еще раз!")
            print(f"Team {team_code} incorrect answer on last question, took {question_duration}, message: {answer}")
            return  
            
    if answer.lower() == answers[question_index].lower():
        bot.reply_to(message, "Правильный ответ! Переходим к следующему заданию")
        chat_state[chat_id]['current_question'] += 1
        print(f"Team {chat_state[chat_id]['team_code']} took {question_duration} for question {question_index + 1}")
        send_question(message)
    else:
        bot.reply_to(message, "Неправильно, попробуйте еще раз!")
        print(f"Team {chat_state[chat_id]['team_code']} incorrect answer on question {question_index + 1}, took {question_duration}")

def handle_correct_answer(chat_id, question_index, message):
    if question_index == len(questions) - 1:
        end_time = datetime.now()
        total_time = end_time - chat_state[chat_id]['start_time']
        chat_state[chat_id]['completed'] = True
        bot.send_message(chat_id, "Вы успешно завершили квест!")
        bot.send_animation(chat_id, 'https://i.pinimg.com/originals/f8/3d/cf/f83dcf0c379de146ef962251952577ab.gif')
        print(f"Team {chat_state[chat_id]['team_code']} completed the quest in {total_time}, message {message}")
    else:
        bot.reply_to(message, "Правильный ответ! Переходим к следующему заданию")
        chat_state[chat_id]['current_question'] += 1
        send_question(message)

def log_correct_answer(team_code, question_number, timestamp):
    print(f"Team {team_code} || question {question_number} || time {timestamp}")

bot.polling(none_stop=True)
