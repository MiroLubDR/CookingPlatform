from django.core.exceptions import ValidationError


def rude_words_validator(value):
    error_text = 'check your text for swear words'
    swear_words = {
'arse' : 'arse','ass':'ass','asshole':'asshole',

'bastard':'bastard','bitch':'bitch','bollocks':'bollocks','brotherfucker':'brotherfucker','bugger':'bugger','bullshit': 'bullshit',

'child-fucker':'child-fucker','cocksucker':'cocksucker','crap':'crap','cunt':'cunt',

'damn':'damn',

'effing':'effing',

'fatherfucker':'fatherfucker','frigger':'frigger','fuck':'fuck',

'goddamn': 'goddamn','godsdamn':'godsdamn',

'hell':'hell','holyshit':'holyshit','horseshit':'horseshit',

'motherfucker':'motherfucker','nigga':'nigga',

'piss':'piss','prick':'prick','shit':'shit','sisterfucker':'sisterfucker','slut':'slut','whore':'whore'

    }

    for word in value.split(' '):
        if word.lower() in swear_words:
            raise  ValidationError(error_text)