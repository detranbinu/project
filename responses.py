import random
from datetime import datetime

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there bud!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!timestamp':
        timestamp = datetime.now()
        a = timestamp.strftime('%H:%M:%S')
        return a

    if p_message == 'love u':
        return 'Im a bot not your lover, keep dreaming bud!'

    if p_message == 'ur mean':
        return 'And I would care why?'

    if p_message == 'rude':
        return 'Hmm, did I ask?'

    if p_message == 'yes':
        return 'so?'

    if p_message == 'hate u':
        return 'U created me so u hate yourself'

    if p_message == 'chill':
        return 'go cry kiddo!'

    if p_message == 'time':
        return 'type "!timestamps"'

    if p_message == 'date':
        return 'Type "time"'

    if p_message == 'find me gf':
        return 'Impossible task'

    if p_message == 'u suck':
        return 'u suck more (^_^)'

    if p_message == '!commands':
        return 'All command available right now: `"hello", "roll", "!timestamp", "love u", "ur mean", "rude", "yes", "hate u", "chill", "time", "date", "find me gf", "u suck"`'

    return ('I didn\'t understand what you wrote. Try typing "!commands" or search in https://www.google.com')
