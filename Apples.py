import math

trees               = 333                                                                              #hoeveel bomen zijn er in totaal?
shadedTrees         = math.ceil(trees / 3 * 2)                                                         #hoeveel bomen staan er in de schaduw (afgerond naar boven)?
sunnyTrees          = math.ceil(trees / 3)                                                             #hoeveel in de zon?

shadeOutputModifier = 0.8                                                                              #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 146                                                                              #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = math.ceil(sunnyTreeOutput * shadeOutputModifier)                                 #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = sunnyTrees * sunnyTreeOutput                                                     #hoeveel appels geven alle zonnige bomen? 
shadedOutput        = shadedTrees * shadedTreeOutput                                                   #hoeveel appels geven alle schaduw bomen?
totalOutput         = sunnyOutput + shadedOutput                                                       #hoeveel appels zijn er in totaal?

owners              = 4                                                                                #met hoeveel mensen verdelen we de appels?

eatCount            = totalOutput % owners                                                             #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = totalOutput                                                                      #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = math.ceil(totalOutput / owners)                                                  #hoeveel appels mag ik verkopen?



print("In een boomgaard staan 333 appelbomen.")
print("2/3 deel (indien noodzakelijk afgerond naar boven) van de bomen staat in de")
print("schaduw van een berg en geeft hierdoor maar 80% van de appels in vergelijking")
print("met de bomen die in de zon staan.")
print("Een boom die in de zon staat geeft precies 146 Appels.")
print("De boomgaard is van mij en 3 vrienden en we verdelen alle appels eerlijk.")
print('\n')
print("Aantal bomen: " + str(trees))
print("Aantal bomen in de schaduw: " + str(shadedTrees))
print("Aantal bomen in de zon: " + str(sunnyTrees))
print("Aantal appels van een boom in de zon: " + str(sunnyTreeOutput))
print("Aantal appels van een boom in de schaduw: " + str(shadedTreeOutput))
print("Totaal aantal appels van alle bomen in de zon: " + str(sunnyOutput))
print("Totaal aantal appels van alle bomen in de schaduw: " + str(shadedOutput))
print("Totaal aantal appels van alle bomen: " + str(totalOutput))
print("Aantal eigenaren" + str(owners))
print("Aantal appels over: " + str(eatCount))
print("Aantal appels om te verkopen: " + str(sellableOutput))
print("Aantal appels die ik mag verkopen: " + str(cut))