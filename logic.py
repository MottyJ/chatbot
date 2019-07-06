import firstAPI

bad_words = ["4r5e","5h1t","5hit","a55","anal","anus","ar5e","arrse","arse","ass","ass-fucker","asses","assfucker","assfukka","asshole","assholes","asswhole","a_s_s","b!tch","b00bs","b17ch","b1tch","ballbag","balls","ballsack","bastard","beastial","beastiality","bellend","bestial","bestiality","bi+ch","biatch","bitch","bitcher","bitchers","bitches","bitchin","bitching","bloody","blow job","blowjob","blowjobs","boiolas","bollock","bollok","boner","boob","boobs","booobs","boooobs","booooobs","booooooobs","breasts","buceta","bugger","bum","bunny fucker","butt","butthole","buttmuch","buttplug","c0ck","c0cksucker","carpet muncher","cawk","chink","cipa","cl1t","clit","clitoris","clits","cnut","cock","cock-sucker","cockface","cockhead","cockmunch","cockmuncher","cocks","cocksuck ","cocksucked ","cocksucker","cocksucking","cocksucks ","cocksuka","cocksukka","cok","cokmuncher","coksucka","coon","cox","crap","cum","cummer","cumming","cums","cumshot","cunilingus","cunillingus","cunnilingus","cunt","cuntlick ","cuntlicker ","cuntlicking ","cunts","cyalis","cyberfuc","cyberfuck ","cyberfucked ","cyberfucker","cyberfuckers","cyberfucking ","d1ck","damn","dick","dickhead","dildo","dildos","dink","dinks","dirsa","dlck","dog-fucker","doggin","dogging","donkeyribber","doosh","duche","dyke","ejaculate","ejaculated","ejaculates ","ejaculating ","ejaculatings","ejaculation","ejakulate","f u c k","f u c k e r","f4nny","fag","fagging","faggitt","faggot","faggs","fagot","fagots","fags","fanny","fannyflaps","fannyfucker","fanyy","fatass","fcuk","fcuker","fcuking","feck","fecker","felching","fellate","fellatio","fingerfuck ","fingerfucked ","fingerfucker ","fingerfuckers","fingerfucking ","fingerfucks ","fistfuck","fistfucked ","fistfucker ","fistfuckers ","fistfucking ","fistfuckings ","fistfucks ","flange","fook","fooker","fuck","fucka","fucked","fucker","fuckers","fuckhead","fuckheads","fuckin","fucking","fuckings","fuckingshitmotherfucker","fuckme ","fucks","fuckwhit","fuckwit","fudge packer","fudgepacker","fuk","fuker","fukker","fukkin","fuks","fukwhit","fukwit","fux","fux0r","f_u_c_k","gangbang","gangbanged ","gangbangs ","gaylord","gaysex","goatse","God","god-dam","god-damned","goddamn","goddamned","hardcoresex ","hell","heshe","hoar","hoare","hoer","homo","hore","horniest","horny","hotsex","jack-off ","jackoff","jap","jerk-off ","jism","jiz ","jizm ","jizz","kawk","knob","knobead","knobed","knobend","knobhead","knobjocky","knobjokey","kock","kondum","kondums","kum","kummer","kumming","kums","kunilingus","l3i+ch","l3itch","labia","lmfao","lust","lusting","m0f0","m0fo","m45terbate","ma5terb8","ma5terbate","masochist","master-bate","masterb8","masterbat*","masterbat3","masterbate","masterbation","masterbations","masturbate","mo-fo","mof0","mofo","mothafuck","mothafucka","mothafuckas","mothafuckaz","mothafucked ","mothafucker","mothafuckers","mothafuckin","mothafucking ","mothafuckings","mothafucks","mother fucker","motherfuck","motherfucked","motherfucker","motherfuckers","motherfuckin","motherfucking","motherfuckings","motherfuckka","motherfucks","muff","mutha","muthafecker","muthafuckker","muther","mutherfucker","n1gga","n1gger","nazi","nigg3r","nigg4h","nigga","niggah","niggas","niggaz","nigger","niggers ","nob","nob jokey","nobhead","nobjocky","nobjokey","numbnuts","nutsack","orgasim ","orgasims ","orgasm","orgasms ","p0rn","pawn","pecker","penis","penisfucker","phonesex","phuck","phuk","phuked","phuking","phukked","phukking","phuks","phuq","pigfucker","pimpis","piss","pissed","pisser","pissers","pisses ","pissflaps","pissin ","pissing","pissoff ","poop","porn","porno","pornography","pornos","prick","pricks ","pron","pube","pusse","pussi","pussies","pussy","pussys ","rectum","retard","rimjaw","rimming","s hit","s.o.b.","sadist","schlong","screwing","scroat","scrote","scrotum","semen","sex","sh!+","sh!t","sh1t","shag","shagger","shaggin","shagging","shemale","shi+","shit","shitdick","shite","shited","shitey","shitfuck","shitfull","shithead","shiting","shitings","shits","shitted","shitter","shitters ","shitting","shittings","shitty ","skank","slut","sluts","smegma","smut","snatch","son-of-a-bitch","spac","spunk","s_h_i_t","t1tt1e5","t1tties","teets","teez","testical","testicle","tit","titfuck","tits","titt","tittie5","tittiefucker","titties","tittyfuck","tittywank","titwank","tosser","turd","tw4t","twat","twathead","twatty","twunt","twunter","v14gra","v1gra","vagina","viagra","vulva","w00se","wang","wank","wanker","wanky","whoar","whore","willies","willy","xrated","xxx"]
first_message = True
user_name = "Jesus"

def boto_message(user_message):
    if first_message:
        return process_first_message(user_message)
    else: 
        return check_for_bad_words(user_message)

def process_first_message(user_message):
    global first_message
    global user_name
    if any(word in bad_words for word in user_message.lower().split(" ")):
        return {"animation": "no", "msg": "I hope you don't kiss your mother with that filthy mouth! Let's start again! What's your name?"} 
    else:
        first_message = False
        user_name = user_message
        return {"animation": "inlove", "msg": "It's a pleasure to meet you %s!" % user_name}

def check_for_bad_words(user_message):
    if any(word in bad_words for word in user_message.lower().split(" ")):
        return {"animation": "no", "msg": "I hope you don't kiss your mother with that filthy mouth! Try again."}
    else:
        return check_puncuation(user_message)

def check_puncuation(user_message):
    if user_message[-1] is not "!" and user_message[-1] is not "?" and user_message[-1] is not ".":
        return {"animation": "confused", "msg": user_name + ", I’m not an English school teacher, but I’m also not a mind reader. If you’d like to talk to me, please use punctuation at the end of your questions or statements!"}
    elif user_message[-1] is "!":
        return process_exclamation(user_message)
    elif user_message[-1] is "?":
        return process_question(user_message)
    else:
        return process_statement(user_message)

def process_exclamation(user_message):
    if any(word in user_message for word in ["dance", "dancing"]):
        return {"animation": "dancing", "msg": "I like to move it move it! I like to move it move it!"}
    else:
        return {"animation": boto_animation(user_message), "msg": user_name + ", that's the best thing I've heard all day! Tell me more!"}

def process_question(user_message):
    if any(word in user_message for word in ["old", "age"]):
        return {"animation": "crying", "msg": "I'm just a baby! I can barely even answer you!"}
    else:
        new_user_message = user_message.replace(" ", "+")
        return {"animation": boto_animation(user_message), "msg": "https://www.google.com/search?q=" + new_user_message}

def process_statement(user_message):
    if any(word in user_message for word in ["leave", "go", "bye"]):
        return {"animation": "takeoff", "msg": "I'll catch you on the flippity flip!'"}
    elif any(word in user_message for word in ["joke"]):
        return new_joke()
    else:
        return {"animation": boto_animation(user_message), "msg": user_name + ", thanks for letting me know. How does that make you feel?"}

def boto_animation(user_message):
    afraid = ["afraid","anxious","apprehensive","frightened","nervous","scared","shocked","suspicious","timid","abashed","aghast","alarmed","aroused","blanched","cowardly","cowed","daunted","discouraged","disheartened","dismayed","distressed","disturbed","faint-hearted","frozen","have cold feet","horrified","in awe","intimidated","panic-stricken","perplexed","perturbed","petrified","rattled","run scared","scared stiff","scared to death","spooked","startled","stunned","terrified","terror-stricken","timorous","trembling","upset","worried"]
    bored = ["bored","disinterested","fatigued","tired","dull","blasé","inattentive","sick and tired","spiritless","turned off"]
    confused = ["confused","baffled","befuddled","bewildered","dazed","disorganized","distracted","muddled","perplexed","perturbed","puzzled","abashed","addled","discombobulated","disconcerted","flummoxed","flustered","gone","misled","nonplussed","stumped","thrown","unscrewed","unzipped","at a loss","at sea","at sixes and sevens","come apart","fouled up","glassy-eyed","mixed up","not with it","out to lunch","punch-drunk","punchy","screwy","shook up","shot to pieces","slaphappy","spaced out","taken aback","thrown off balance","unglued"]
    crying = ["cry","crying","howl","lament","sob","bawl","bawling","bewailing","blubber","blubbering","howling","keening","lamentation","mourning","snivel","sniveling","sobbing","sorrowing","tears","wailing","weep","whimpering","yowl","shedding tears","the blues"]
    dancing = ["dance","dancing","disco","rock","samba","tango","waltz","Charleston","bob","boogie","caper","careen","cavort","conga","flit","foxtrot","frolic","gambol","hop","hustle","jig","jitter","jitterbug","jive","jump","leap","one-step","prance","promenade","rhumba","shimmy","skip","spin","step","strut","sway","swing","tap","tread","trip","twist","two-step","whirl","boogie down","bunny hop","cut a rug","foot it","get down","hoof it","rock n' roll","trip the light fantastic"]
    dog = ["dog","pup","puppy","cur","doggy","hound","mongrel","mutt","pooch","stray","tyke","bowwow","fido","flea bag","man's best friend","tail-wagger"]
    excited = ["excited","agitated","annoyed","delighted","disturbed","eager","enthusiastic","hysterical","nervous","passionate","thrilled","animated","aroused","awakened","charged","discomposed","disconcerted","inflamed","moved","piqued","provoked","roused","ruffled","stimulated","stirred","wired","aflame","beside oneself","feverish","fired up","frantic","high","hot","hot and bothered","hyperactive","in a tizzy","juiced up","jumpy","keyed up","on edge","on fire","overwrought","steamed up","tumultuous","wild","worked up","zipped up"]
    giggling = ["giggle","giggling","cackle","chuckle","guffaw","snicker","chortle","hee-haw","snigger","titter","twitter","teehee"]
    heartbroke = ["heartbreak","agony","anguish","bitterness","despair","grief","heartache","pain","remorse","sorrow","suffering","torment","woe","affliction","bale","care","desolation","distress","heartsickness","regret","rue","torture","broken heart","heavy heart"]
    inlove = ["love","in love","affection","appreciation","devotion","emotion","fondness","friendship","infatuation","lust","passion","respect","taste","tenderness","yearning","adulation","allegiance","amity","amorousness","amour","ardor","attachment","case","cherishing","crush","delight","devotedness","enchantment","enjoyment","fervor","fidelity","flame","hankering","idolatry","inclination","involvement","like","partiality","piety","rapture","regard","relish","sentiment","weakness","worship","zeal","ardency","mad for","soft spot"]
    laughing = ["laugh","laughing","chuckle","giggle","grin","howl","roar","scream","shriek","snicker","snort","whoop","burst","cachinnate","chortle","convulsed","crow","fracture","guffaw","titter"]
    money = ["money","bill","capital","cash","check","fund","pay","payment","property","salary","wage","wealth","banknote","bankroll","bread","bucks","chips","coin","coinage","dough","finances","funds","gold","gravy","greenback","loot","pesos","resources","riches","roll","silver","specie","treasure","wad","wherewithal","almighty dollar","hard cash","legal tender","medium of exchange"]
    ok = ["ok","okay","acceptance","affirmation","approbation","approval","assent","authorization","benediction","blessing","consent","endorsement","favor","go-ahead","permission","sanction","say-so","yes"]
    takeoff = ["takeoff","departure","liftoff","ascent","climb","hop","jump","launch","rise"]
    waiting = ["wait","waiting","await","delay","expect","hang","linger","remain","stand by","stay","stick around","watch"]
    if any(word in afraid for word in user_message.lower().split(" ")):
        return "afraid"
    if any(word in bored for word in user_message.lower().split(" ")):
        return "bored"
    if any(word in confused for word in user_message.lower().split(" ")):
        return "confused"
    if any(word in crying for word in user_message.lower().split(" ")):
        return "crying"
    if any(word in dancing for word in user_message.lower().split(" ")):
        return "dancing"
    if any(word in dog for word in user_message.lower().split(" ")):
        return "dog"
    if any(word in excited for word in user_message.lower().split(" ")):
        return "excited"
    if any(word in giggling for word in user_message.lower().split(" ")):
        return "giggling"
    if any(word in heartbroke for word in user_message.lower().split(" ")):
        return "heartbroke"
    if any(word in inlove for word in user_message.lower().split(" ")):
        return "inlove"
    if any(word in laughing for word in user_message.lower().split(" ")):
        return "laughing"
    if any(word in money for word in user_message.lower().split(" ")):
        return "money"
    if any(word in ok for word in user_message.lower().split(" ")):
        return "ok"
    if any(word in takeoff for word in user_message.lower().split(" ")):
        return "takeoff"
    if any(word in waiting for word in user_message.lower().split(" ")):
        return "waiting"
    else:
        return "confused"