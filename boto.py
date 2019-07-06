"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
from logic import *

# afraid = [anxious,apprehensive,frightened,nervous,scared,shocked,suspicious,timid,abashed,aghast,alarmed,aroused,blanched,cowardly,cowed,daunted,discouraged,disheartened,dismayed,distressed,disturbed,faint-hearted,frozen,have cold feet,horrified,in awe,intimidated,panic-stricken,perplexed,perturbed,petrified,rattled,run scared,scared stiff,scared to death,spooked,startled,stunned,terrified,terror-stricken,timorous,trembling,upset,worried]
# bored = [disinterested,fatigued,tired,dull,blasé,inattentive,sick and tired,spiritless,turned off]
# confused = [baffled,befuddled,bewildered,dazed,disorganized,distracted,muddled,perplexed,perturbed,puzzled,abashed,addled,discombobulated,disconcerted,flummoxed,flustered,gone,misled,nonplussed,stumped,thrown,unscrewed,unzipped,at a loss,at sea,at sixes and sevens,come apart,fouled up,glassy-eyed,mixed up,not with it,out to lunch,punch-drunk,punchy,screwy,shook up,shot to pieces,slaphappy,spaced out,taken aback,thrown off balance,unglued]
# crying = [howl,lament,sob,bawl,bawling,bewailing,blubber,blubbering,howling,keening,lamentation,mourning,snivel,snivelling,sobbing,sorrowing,tears,wailing,weep,whimpering,yowl,shedding tears,the blues]
# dancing = [disco,rock,samba,tango,waltz,Charleston,bob,boogie,caper,careen,cavort,conga,flit,foxtrot,frolic,gambol,hop,hustle,jig,jitter,jitterbug,jive,jump,leap,one-step,prance,promenade,rhumba,shimmy,skip,spin,step,strut,sway,swing,tap,tread,trip,twist,two-step,whirl,boogie down,bunny hop,cut a rug,foot it,get down,hoof it,rock n' roll,trip the light fantastic]
# dog = [pup,puppy,bitch,cur,doggy,hound,mongrel,mutt,pooch,stray,tyke,bowwow,fido,flea bag,man's best friend,tail-wagger]
# excited = [agitated,annoyed,delighted,disturbed,eager,enthusiastic,hysterical,nervous,passionate,thrilled,animated,aroused,awakened,charged,discomposed,disconcerted,inflamed,moved,piqued,provoked,roused,ruffled,stimulated,stirred,wired,aflame,beside oneself,feverish,fired up,frantic,high,hot,hot and bothered,hyperactive,in a tizzy,juiced up,jumpy,keyed up,on edge,on fire,overwrought,steamed up,tumultous/tumultuous,wild,worked up,zipped up]
# giggling = [cackle,chuckle,guffaw,snicker,chortle,hee-haw,snigger,titter,twitter,teehee]
# heartbroke = [agony,anguish,bitterness,despair,grief,heartache,pain,remorse,sorrow,suffering,torment,woe,affliction,bale,care,desolation,distress,heartsickness,regret,rue,torture,broken heart,heavy heart]
# inlove = [affection,appreciation,devotion,emotion,fondness,friendship,infatuation,lust,passion,respect,taste,tenderness,yearning,adulation,allegiance,amity,amorousness,amour,ardor,attachment,case,cherishing,crush,delight,devotedness,enchantment,enjoyment,fervor,fidelity,flame,hankering,idolatry,inclination,involvement,like,partiality,piety,rapture,regard,relish,sentiment,weakness,worship,zeal,ardency,mad for,soft spot]
# laughing = [chuckle,giggle,grin,howl,roar,scream,shriek,snicker,snort,whoop,burst,cachinnate,chortle,convulsed,crow,fracture,guffaw,titter]
# money = [bill,capital,cash,check,fund,pay,payment,property,salary,wage,wealth,banknote,bankroll,bread,bucks,chips,coin,coinage,dough,finances,funds,gold,gravy,greenback,loot,pesos,resources,riches,roll,silver,specie,treasure,wad,wherewithal,almighty dollar,hard cash,legal tender,medium of exchange]
# no = [nay,nix,never,not]
# ok = [okay,OK,acceptance,affirmation,approbation,approval,assent,authorization,benediction,blessing,consent,endorsement,favor,go-ahead,permission,sanction,say-so,yes]
# takeoff = [departure,liftoff,ascent,climb,hop,jump,launch,rise]
# waiting = [await,delay,expect,hang,linger,remain,stand by,stay,stick around,watch]


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps(boto_message(user_message))


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000, reloader=True)

if __name__ == '__main__':
    main()
