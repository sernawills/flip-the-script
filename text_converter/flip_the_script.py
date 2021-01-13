import re

list_m_f = u"""maleS femaleS, maleness femaleness, 
himself herself, his her, his hers, he she, him her,
Mr Mrs, Mister Missus, Ms Mr, Master Miss, Master Mistress, 
uncleS auntS, nephewS nieceS, sonS daughterS, grandsonS granddaughterS, stepsonS stepsisterS,
brotherS sisterS, man woman, men women, boyS girlS, paternal maternal, paternity maternity,
grandfatherS grandmotherS, GodfatherS GodmotherS, GodsonS GoddaughterS, 
fiancéS fiancéeS, fianceS fianceeS, husband wife, husbands wives, 
fatherS motherS, bachelorS spinsterS, groomS brideS, widowerS widowS, 
KnightS DameS, Sir Madam, Sir DameS, KingS QueenS, DukeS DuchessES, PrinceS PrincessES, 
MarquessES MarchionessES, EarlS CountessES, ViscountS ViscountessES, ladS lassES, sir madamS, 
gentleman lady, gentlemen ladies, Lord Lady, Lords Ladies, dude lady, dudes ladies, 
BaronS BaronessES, baronetS baronetessES, stallionS mareS, ramS eweS, coltS fillieS, 
billy nanny, billies nannies, bullS cowS, godS goddessES, godheadS goddessheadS, 
godhood goddesshood, godliness goddessliness, godly goddessly, gramps grandma, heroS heroineS, 
undies nickers, sweat glow, jackarooS jillarooS, gigoloS hookerS, landlord landlady, landlords landladies, 
manservantS maidservantS, actorS actressES, CountS CountessES, 
EmperorS EmpressES, giantS giantessES, heirS heiressES, hostS hostessES, 
lionS lionessES, managerS manageressES, murdererS murderessES, 
priestS priestessES, poetS poetessES, shepherdS shepherdessES, 
stewardS stewardessES, tigerS tigressES, waiterS waitressES, 
fireman firewoman, firemen firewomen, policeman policewoman, 
policemen policewomen, congressman congresswoman, congressmen congresswomen, 
anchorman anchorwoman, anchormen anchorwomen, cameraman camerawoman, 
cameramen camerawomen, showman showwoman, showmen showwomen, barman barmaid, 
barmen barmaids, cockS henS, drakeS henS, dogS vixenS, tomS tibS, 
boarS sowS, buckS roeS, peacockS peahenS, gander goose, ganders geese, friarS nunS, 
archdukeS archduchessES, boyish girly, bro sis, bros sistas, deaconS deaconessES,
monkS nunS, bloke gal, boyfriendS girlfriendS, manly womanly, squireS damselS, 
boyhoodS girlhoodS, brotherhoodS sisterhoodS, grandpaS grandmaS, margraveS margravineS, 
matriar patriar, patriarchy matriarchy, matroniz patroniz, airman airwoman, airmen airwomen, 
alderman alderwoman, aldermen alderwomen, assemblyman assemblywoman, assemblymen assemblywomen, 
bogeyman bogeywoman, bogeymen bogeywomen, bondsman bondswoman, bondsmen bondswomen, businessman businesswoman, 
businessmen businesswomen, caveman cavewoman, cavemen cavewomen, chairman chairwoman, 
chairmen chairwomen, clergyman clergywoman, clergymen clergywomen, congressman congresswoman, 
congressmen congresswomen, councilman councilwoman, councilmen councilwomen, 
countrymen countrywomen, craftsman craftswoman, craftsmen craftswomen, 
daddy mommy, daddies mommies, dadS momS, papa mama, momma poppa, manhood womanhood, 
mankind womankind, manly womanly, doorman doorwoman, doormen doorwomen, fisherman fisherwoman, 
fishermen fisherwomen, foremen forewomen, freshman freshwoman, freshmen freshwomen, 
garbageman garbagewoman, garbagemen garbagewomen, guyS galS, handyman handywoman, handymen handywomen,
hangman hangwoman, hangmen hangwomen, henchman henchwoman, henchmen henchwomen, 
journeyman journeywoman, journeymen journeywomen, kinsman kinswoman, kinsmen kinswomen, 
klansman klanswoman, layman laywoman, laymen laywomen, madman madwoman, madmen madwomen,  
mailman mailwoman, mailmen mailwomen, mansplain ladysplain, marksman markswoman, 
marksmen markswomen, middleman middlewoman, middlemen middlewomen, milkman milkwoman, 
milkmen milkwomen, misandr misogyn, nobleman noblewoman, noblemen noblewomen,
ombudsman ombudswoman, ombudsmen ombudswomen, postman postwoman, postmen postwomen, 
repairman repairwoman, repairmen repairwomen, salesman saleswoman, salesmen saleswomen, 
sandman sandwoman, sandmen sandwomen, serviceman servicewoman, servicemen servicewomen, 
snowman snowwoman, spaceman spacewoman, spacemen spacewomen, spokesman spokeswoman, 
spokesmen spokeswomen, sportsmen sportswomen, statesman stateswoman, statesmen stateswomen, 
stepbrother stepsister, stepmother stepfather, stepsister stepbrother,
superman superwoman, supermen superwomen, unman unwoman, watchman watchwoman, 
watchmen watchwomen, weatherman weatherwoman, weathermen weatherwomen, 
whitemaleness whitefemaleness, workman workwoman, workmen workwomen, masculinity femininity, 
misandry misogyny, manliness womanliness, clergyman clergywoman, clergymen clergywomen,
headmasterS headmistressES, chauffeurS chauffeuseS, witchES wizardS, brother-in-law sister-in-law,
father-in-law mother-in-law, son-in-law daughter-in-law, schoolboy schoolgirl,
Englishman Englishwoman, DJ DJane, conductorS conductressES"""

plural_test_list = u"""brotherS sisterS, godS goddessES"""

# compile() function returns the specified source as a code object, ready to be executed.

def parse_switch_dict(pair_list):

  # raw string line separator
  re_nl = re.compile(r",[ \n]*") 

  # split strings from the pair_list, which in fact is a long string
  m_f = [tok.split(" ") for tok in re_nl.split(pair_list)] 

  # compile the strings with the plural form "S"
  re_plural = re.compile("E*S$") 

  # compile the strings with the plural form "ES"
  re_ES = re.compile("ES$")     

  # replace function
  def gender_plural(m,f):                         
    yield re_plural.sub("",m),re_plural.sub("",f)
    yield re_ES.sub("es",m),re_ES.sub("es",f)
    yield re_plural.sub("s",m),re_plural.sub("s",f)
  
  def gender_cap_plural(m,f):
    for m,f in gender_plural(m,f):
      yield m.capitalize(), f.capitalize()
      yield m,f
  
  def gender_switch_role_cap_plural(m,f):
    for m,f in gender_cap_plural(m,f):
      yield m,f
      yield f,m
  
  switch = {}

  for m,f in m_f:
    for xy,xx in gender_switch_role_cap_plural(m,f):
      if xy not in switch: 
        switch[xy]=xx

  return switch


switch = parse_switch_dict(list_m_f)

words = switch.keys()
 
words = "|".join(words)
 
re_word = re.compile(r"\b("+words+r")\b")
 
def flip_the_script(text):
  text = re_word.split(text)
  return "".join([ word+switch[gen] for word,gen in zip(text[::2],text[1::2])])+text[-1]

#text = input("Enter your text:")

#text=u'''We were discussing something, and I said, “An advanced computer user knows what she needs…”, [when] a male colleague, suddenly interrupted, “Are you saying men cannot be advanced computer users?” I thought he was joking and laughed, but then realised I was the only one laughing, and he was looking at me as if I were his personal enemy'.'''

#result = flip_the_script(text)

#print("This is your reverse gendered text: " + str(result))



