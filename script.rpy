#Scenes
image mainmenu = "main_menu.jpg"

#Personnages
define jp = Character('Jean Plank', color="#c8ffc8")                                                            #Thomas
define trist = Character('Tristana, l\'enfant innocente', color="#c8ffc8")                                      #Bahar
define lulu  = Character('Lulu, une AUTRE enfant, ça commence à faire beaucoup là, non ?', color="#c8ffc8")     #?F
define cait = Character('La Représentante des Forces de l\'Ordre', color="#c8ffc8")                             #Dagga                 
define Rize = Character('Rize le \"sOrCieR\" qui aime bien les enfants', color="#c8ffc8")                       #Sacha
define fille = Character('La pickpocket aventureuse', color="#c8ffc8")                                          
define jinx = Character('Jinx', color="#c8ffc8")                                                                #Eva
define lee = Character('Lee le Voyant', color="#c8ffc8")                                                        #Styrale
define malade = Character('Un patient déjà bien mal en point', color="#c8ffc8")                                 #?H
define shen = Character('Le Médecin de l\'Hôpital', color="#c8ffc8")                                            #Sacha
define femme = Character('Une Honnête Citoyenne', color="#c8ffc8")                                              #?F
define garde = Character('Un Vigile qui ne fait, ma foi, que son travail', color="#c8ffc8")                     #Sacha
define general = Character('Le Géneral de la Garde', color="#c8ffc8")                                           #?H
define simon = Character('Un Opportuniste Avéré', color="#c8ffc8")                                              #Simon
define Haddock = Character('Haddock, connu comme Capitaine des Docks', color="#c8ffc8")                         #Grim
define martin = Character('Tobias, mais Martin c\'est bien aussi', color="#c8ffc8")                             #?H             (3)
define renaud = Character('Renaud, mais Martin c\'est bien aussi', color="#c8ffc8")
define contremaitre = Character('Le Contremaître du Navire', color="#c8ffc8")                                   #?H             (1)
define illaoi = Character('Illafloy, Incarnation de l\'Océan', color="#c8ffc8")                                 #Bahar
define marchand = Character('Un Marchand très banal', color="#c8ffc8")                                          #Chevre         (3)  #Sacha Renaud
define marchand2 = Character('Un autre Marchand tout aussi banal', color="#c8ffc8")                             #?H             (1)  #Fred Renaud
define capitaine_des_marchands = Character('Le Capitaine des Marchands', color="#c8ffc8")                       #?H
define tontonzil = Character('Le Vieux Con que, de son temps, c\'était pas comme ça', color="#c8ffc8")          
define inconnu = Character('???', color="#c8ffc8")                                                              
define wayne = Character('Wayne', color="#c8ffc8")                                                              #Desco-chan
define pere_jp = Character('Monsieur Plank', color="#c8ffc8")                                                   #?H
define marin = Character('Un Marin Audacieux', color="#c8ffc8")                                                 #Sacha          (2) #Chevre
define marin2 = Character('Un Marin Beaucoup Moins Audacieux', color="#c8ffc8")                                 #?H             (2)
define katarina = Character('Katarina', color="#c8ffc8")                                                        #?F
define pirate = Character('Une canaille au service de Katarina', color="#c8ffc8")                               #?H             (2) #Styrale Renaud
define patrick = Character('Un certain \"Patrick Balkany\"', color="#c8ffc8")                                   #Styrale
define Urgo = Character('Urgo le Boucher Exilé', color="#c8ffc8")                                               #Styrale
define fillette = Character('Une Fillette Apeurée', color="#c8ffc8")                                            
define vex = Character('La Sorcière Désoh Profonde', color="#c8ffc8")                                           #?F
define thresh = Character('Thresh le Moissonneur Nocturne', color="#c8ffc8")                                    #?H
define simon2 = Character('Un Opportuniste Confirmé', color="#c8ffc8")                                          #Simon
define illaoi_version_esprit = Character('La Gardienne des Promesses', color="#c8ffc8")                         

label start:

scene mainmenu

$ artefact = 0
$ censure = 0

menu:
    "Jouer à la version tout public":
        $ censure = 1

    "Jouer à la version non censurée ":
        $ censure = 0

#Scene 1

play music "music/music_libre.ogg"
scene libre
"Jean Plank venait de recupérer son indépendence et son visage."
"Cependant, malgré cette liberté recouvrée, il se rendit vite compte qu'il n'avait absolument aucune idée d'où aller."
"Se venger, oui, mais encore fallait-il savoir de qui."

scene jp_reflexion
"L'heure était à la reflexion."

#$renpy.sound.play("sound/sound_nuitambience.ogg", loop=True)
scene jp_reflexion2
"Et quand je dis l'heure, il ne s'agit point d'une image, notre bon capitaine mit très exactement 1 heure, 15 secondes et 12 centièmes à comprendre qu'il lui fallait quelqu'un pour lui indiquer le chemin."
"Quelqu'un qui savait tout."
"Quelqu'un capable de tout voir."

scene jp_revelation
#voice "doublages_jp4/scene1/scene1_jp1.ogg"
jp "J'ai trouvé ! Il me faut l'autre débile d'aveugle !"

"Sitôt crié, sitôt parti."

scene vers_village
$renpy.sound.play("sound/sound_forêtnuit.ogg", loop=True)
"Jean Plank s'éloigna des décombres en direction du temple de Lee."
"Il ne savait plus trop où il était situé mais heureusement, Jean Plank était un malin."
"Il se souvenait avoir pris la première à droite pour aller au village des Schtroumpfs."

#voice "doublages_jp4/scene1/scene1_jp2.ogg"
jp "Je vais retrouver ce village et prendre la première pas à droite !"
"S'exclama-t-il après un gros moment de réflexion."
"Il sortit alors son sextant, puis l'explosa par terre après s'être plaint que ça marchait qu'en mer et que, par conséquent, c'était de la merde."
"Il prit ensuite la direction du village en titubant, principalement parce qu'il était ivre mort, ce qui ralentissait considérablement son allure."

scene rize
play music "music/music_rize.ogg"
$renpy.sound.play("sound/sound_forêtambient.ogg", loop=True)

#voice "doublages_jp4/scene1/scene1_trist1.ogg"
trist "Tonton Rize, Tonton Rize ! Le braconnier est revenu !"

#voice "doublages_jp4/scene1/scene1_rize1.ogg"
Rize "Braconnier ? Va jouer ailleurs, je suis en plein examen médical là."

#voice "doublages_jp4/scene1/scene1_lulu1.ogg"
lulu "Oui c'est vrai ! Tonton Rize il a dit que j'étais malade et que du coup il devait m'examiner."

scene rize2

#voice "doublages_jp4/scene1/scene1_rize2.ogg"
Rize "Eeeeh mais qu'est-ce qu'il fait là l'autre débile, on l'avait pas enfermé ?! Vite Tristana, va me chercher le téléphone !"

#voice "doublages_jp4/scene1/scene1_trist2.ogg"
trist "Mais oncle Rize, il est dans ta poche !"

#voice "doublages_jp4/scene1/scene1_rize3.ogg"
Rize "Mais bordel !"

label cait:

play music "music/music_cait.ogg"
#play sound "sound/police.ogg"
scene police
"Quelques minutes plus tard, la maréchaussée venait se saisir de Jean Plank."

scene cait
#voice "doublages_jp4/scene1/scene1_cait1.ogg"
cait "Monsieur, veuillez me suivre sans faire d'histoires, je vous prie."
menu:
    "Hurler \"Silence, chienne de femme !\"":

        #voice "doublages_jp4/scene1/scene1_jp3.ogg"
        scene jpsilence
        jp "Silence, chienne de femme !"

        "Étonnamment, cela eût l'effet escompté."
        "L'agent de police, abasourdie, ne dit plus un mot."

        scene jparrogant
        "Puis, à la vue du sourire arrogant et satisfait qu'arborait Jean Plank, elle reprit ses esprits."
        "Elle sortit alors son taser à ours et, d'un geste rapide et précis, visa les couilles de notre bon capitaine, lequel s'effondra sur le sol en bavant."
        
        play music "music/music_prison.ogg"
        scene jppendu
        stop sound
        "Quand Jean Plank se réveilla, son procès était déjà terminé. La prison ayant été détruite et l'accusé ayant été ivre mort (et par conséquent inconscient) à la barre, il avait été décidé qu'il serait pendu à l'aube."
        "Malheureusement, Jean Plank n'eût pas la chance de tenir jusque-là."
        "La policière, aussi féministe que rancunière, n'avait pas vraiment apprécié les propos de Jean Plank."
        jump mort_tabasse_prison
    
    "Boire une lampée de Rhum":
        
        "Jean Plank regarda la donzelle d'un air mystérieux."
        scene jp_rhum_cait
        "D'un geste gracieux, il sortit alors sa bouteille de rhum pour en reprendre une généreuse lampée."
        "Il se racla la gorge."

        scene jp_discours_cait
        "C'est alors qu'il entreprit un discours engagé sur le fait que le remettre en prison n'avait pas de sens."
        "Parce qu'il n'y avait plus de prison."
        "Sa voix était charismatique."
        "Son discours était clair."
        "Ses arguments étaient pertinents."
        "Enfin ça, c'est ce qu'il croyait."
        "Médusée, l'agent de police venait de se décider à foutre un gros coup de taser à cet imbécile d'ivrogne quand un bruit venant d'une petite maison visiblement mal isolée attira son attention."
        #play sound bruit fermeture éclaire

        play music "music/music_rize_cait.ogg"
        #voice "doublages_jp4/scene1/scene1_lulu2.ogg"
        lulu "Tonton Rize, j'ai le droit de me rhabiller maintenant ?"

        #voice "doublages_jp4/scene1/scene1_rize4.ogg"
        Rize "Attends, j'ai pas fini mon examen !"

        scene cait2
        #voice "doublages_jp4/scene1/scene1_cait2.ogg"
        cait "Toi tu bouges pas d'ici, je reviens."
        #Tout ce passage sera en fondu sonore
        #bruit d'une porte qu'on détruit

        scene rize_cait
        stop sound
        #voice "doublages_jp4/scene1/scene1_cait3.ogg"
        cait "Police ouvrez cette porte !"

        #voice "doublages_jp4/scene1/scene1_rize5.ogg"
        Rize "Attendez c'est un malentendu ! Dis lui, toi !"

        scene rize_cait_lulu
        #voice "doublages_jp4/scene1/scene1_lulu3.ogg"
        lulu "Oui, c'est vrai que c'est pas mal tendu !"

        scene rize_cait
        #voice "doublages_jp4/scene1/scene1_rize6.ogg"
        Rize "Traîtrese !"
        #bruit de Rize a qui on met des menotes

        #voice "doublages_jp4/scene1/scene1_rize7.ogg"
        Rize "Elle était consentente ! Elle m'a piégé ! Elle m'a piégé, je vous dis ! Mais merde..."
        #Fin du passage en fondu sonore

scene rize_prison
"Jean Plank regarda la voiture partir avec à son bord Rize, qui semblait plutôt mécontent."

scene jp_bus
"En honnête pilleur sanguinaire qu'il était, il décida d'attendre le retour de la policière, comme promis."
"Trois jours plus tard, la maréchaussée n'était toujours pas revenue. Jean Plank décida donc qu'il était grand temps d'aller chez Lee."

scene jp_vitesse_eclair2
play music "music/music_vengeance_lulu.ogg"
#voice "doublages_jp4/scene1/scene1_jp4.ogg"
jp "Les traîtres méritent de brûler en enfer."

scene vengeance_lulu
$renpy.sound.play("sound/sound_feu.ogg", loop=True)
"Grommela-t-il en mettant le feu à la maison de Lulu avant de repartir."
jump scene2

label mort_tabasse_prison:
scene mort_tabasse_prison
"Ainsi rendit-elle une visite nocturne à Jean Plank afin de le tabasser à mort avant que l'aube ne pointe."
show ecran_game_over
play music "music/music_mort.ogg"
window hide
pause
hide ecran_game_over
stop music
jump cait

label scene2:

scene jp_sort_village
$renpy.sound.play("sound/sound_forêtambient.ogg", loop=True)
play music "music/music_repos.ogg"
"Voilà un moment que Jean Plank marchait."
"Il avait la gorge sèche et n'avait malheureusement plus rien à boire."

scene jp_repos_arbre
"Fatigué, il  se décida à faire une sieste sous un arbre qui trainait là."
"Il s'adossa contre le tronc et à la manière d'un véritable cowboy, abattit son tricorne sur ses yeux."
"C'était peu efficace, un tricorne n'étant pas prévu à cet effet."
"Plus fatigué qu'il ne le pensait, il tomba rapidement dans les bras de Morphée."#Font sonore : no homo

scene jp_volalatire
$renpy.sound.play("sound/sound_forêtnuit.ogg", loop=True)
"Il fut reveillé quelques instants plus tard par une désagréable sensation."
"Celle de se faire faire les poches."

scene jp_vitesse_eclair
"Il ouvrit les yeux, et analysa la situation en un éclair."
show jp_vitesse_eclair2
"Il ouvrit les yeux, et analysa la situation en un éclair."

scene jp_gifle_branche
"Plus rapide que son ombre, il se saisit de la gorge du voleur et lui administra une baffe magistrale."
"En entendant le craquement significatif d'une branche que l'on casse, Jean Plank se dit qu'il avait peut-être analysé la situation un peu trop vite."

show jp_vitesse_eclair
"Aussi décida-t-il de recommencer, un peu plus lentement cette fois."
show jp_vitesse_eclair2
"Genre à la vitesse de l'éclair mais en lent."

scene jp_branche
"Il s'était en effet saisi d'une branche."
"Devant lui, incrédule, une fille à l'air pas très net, la main toujours dans les affaires de Jean Plank."
"Elle était si stupéfaite de la stupidité du capitaine qu'elle ne réagit même pas lorsque ce dernier la saisit par le bras en hurlant."

#voice "doublages_jp4/scene2/scene2_jp1.ogg"
jp "Ha ha !"

scene jinx
"Jean Plank se releva, tenant toujours la fille par le bras."
"Qu'allait-il en faire à present ?"
"Il avait entendu parler d'une tradition étrangère dans laquelle on coupait une main aux voleurs."
"Jean Plank trouvait ça idiot parce qu'on pouvait continuer à voler, même avec une main en moins."

#voice "doublages_jp4/scene2/scene2_jp2.ogg"
jp "Mmhh, et si je tranchais la tête..."

"Décidément, Jean Plank était vraiment un malin."
"La fillette ne semblait pas trop perturbée par les projets meurtriers de notre bon capitaine."

scene jinx_grenade
"Au lieu de paniquer elle sortit juste une grenade qu'elle dégoupilla en rigolant."
"Jean Plank afficha alors son plus beau sourire."
"Il aimait les filles de caractère."

#voice "doublages_jp4/scene2/scene2_jp3.ogg"
jp "C'est comme le fromage !"

#voice "doublages_jp4/scene2/scene2_jinx1.ogg"
fille "Hein ?"

#voice "doublages_jp4/scene2/scene2_jp4.ogg"
jp "Très bien, tu es engagée !"

scene jp_jette_grenade
"Dit-il en arrachant la grenade des mains de la fillette pour la lancer au loin dans la forêt."

#voice "doublages_jp4/scene2/scene2_jinx2.ogg"
fille "Quoi mais comment ça ?! Mais non, mais lâche-moi !"

stop sound
$renpy.sound.play("sound/sound_feu.ogg", loop=True)
scene vers_lee_feu
#La ya un sprite avec la foret en feu derrière
"Jean Plank ne l'écoutait déjà plus. Motivé d'avoir trouvé un nouveau compagnon, il marchait désormais à grandes enjambées vers la demeure de Lee Sin, désormais accompagné de sa réticente camarade."


#Scene 3

play music "music/music_lee_jinx.ogg"
stop sound

scene cabanejp3
"Notre bon capitaine et sa suivante, obligée plus que dévouée, venaient d'arriver devant le cabanon de Lee."
"Jean Plank s'était arrêté devant la porte."
"Pensif, il regardait la grande croix que quelqu'un avait dessiné à même le sol."
"Après un moment, il passa finalement le palier en se demandant qui était l'idiot qui dessinait des croix sur le sol."

scene lee_attend
"D'un rapide coup d'œil, il vit que rien n'avait changé dans le cabanon."
"Son regard croisa alors celui du voyant tant recherché."
"Statique au fond de la pièce, Lee semblait attendre Jean Plank."

#voice "doublages_jp4/scene3/scene3_lee1.ogg"
lee "Bon retour, petit scarabée. As-tu trouvé tous les artefacts sacrés ?"

menu:
    "Adopter l'attitude de celui à qui on ne la fait pas.": #act like you see through the trick en VA
        show jp_artefacts
        "Dubitatif, Jean Plank prit alors l'attitude de celui à qui on ne la fait pas."
        "Voyant chez Jean Plank l'attitude du gars à qui on ne la fait pas, Lee changea de stratégie."
        hide jp_artefacts
    "Dire cordialement que vous n'avez rien trouvé.":
        jp "Vas te faire foutre, vieux chauve !"


lee  "Hmm, pas grave, tout le monde s'en fout de toute manière ! Je t'attendais !"

"Lee avait en effet l'air d'être au courant de la venue du capitaine."

#voice "doublages_jp4/scene3/scene3_jp1.ogg"
jp "Lucien est parti !"

#voice "doublages_jp4/scene3/scene3_lee2.ogg"
lee "Je sais, je vois tout !"

#voice "doublages_jp4/scene3/scene3_jinx1.ogg"
fille "Mais vous aller me lâcher oui ?!"

#voice "doublages_jp4/scene3/scene3_jp2.ogg"
jp "N..."

#voice "doublages_jp4/scene3/scene3_lee3.ogg"
lee "Laisse moi le plaisir de lui répondre, petit scarabée."

"Il se tourna vers la fille."

show lee_non
#voice "doublages_jp4/scene3/scene3_lee4.ogg"
lee "Mmhh, non !"

#voice "doublages_jp4/scene3/scene3_jinx2.ogg"
fille "Mais pourquoi ?!"

scene jp_crayon
play music "music/crayon.ogg"
#voice "doublages_jp4/scene3/scene3_jp3.ogg"
jp "Écoute petite, tu veux vivre ou mourir ?"
menu:
    "Heu vivre ?!":
        "Jean Plank prenait soin de son prochain."
        "Aussi prit-il en considération les désirs de la demoiselle."
        "Gentillement, il lui expliqua alors que si elle voulait vivre, elle n'avait pas 36 solutions."
    "Mourir":
        #voice "doublages_jp4/scene3/scene3_jp4.ogg"
        jp "Dans ce cas tu peux bien m'accorder ta vie !"

play music "music/music_lee_jinx.ogg"
scene jinx_realisation

"La fille, que désormais nous appellerons Jinx, parce que c'est son prénom et parce que c'est chiant de l'appeler \"la fille\", comprit alors qu'elle venait de se faire avoir."

scene jinx_ok

"Ainsi se décida-t-elle à vouer sa vie au capitaine et à ses objectifs, aussi stupides soient-ils."

scene lee_discute_jp

#voice "doublages_jp4/scene3/scene3_lee5.ogg"
lee "Bon, pourquoi venais-tu me consulter jeune chamois égaré ?"

#voice "doublages_jp4/scene3/scene3_jp5.ogg"
jp "Tu vois tout, espèce de vieux débris, tu devrais le savoir non ?"

#voice "doublages_jp4/scene3/scene3_lee6.ogg"
lee "Mmhh certes !"

#voice "doublages_jp4/scene3/scene3_lee7.ogg"
lee "Mais cela a tendance à limiter les interactions sociales avec les gens, du coup je fais semblant."

"Une fois de plus notre capitaine fut cloué par tant de sagesse."
"Vraiment, comment un simple aveugle pouvait-il devenir aussi sage ?"

#voice "doublages_jp4/scene3/scene3_lee8.ogg"
lee "Bon, suffit les éloges, formule ta requête je n'ai pas que ça à faire."

#voice "doublages_jp4/scene3/scene3_jp6.ogg"
jp "Je ne sais pas de qui me venger !"

#voice "doublages_jp4/scene3/scene3_lee9.ogg"
lee "De qui te venger pour quoi ?"

#voice "doublages_jp4/scene3/scene3_jp7.ogg"
jp "Quoi ?"

#voice "doublages_jp4/scene3/scene3_lee10.ogg"
lee "Quoi \"quoi\" ?"

show jinx_interruption

#voice "doublages_jp4/scene3/scene3_jinx3.ogg"
jinx "Grenouille !"

#voice "doublages_jp4/scene3/scene3_lee11.ogg"
lee "Toi sois gentille, tu fermes ta gueule."#La retouche pas celle là

hide jinx_interruption

#voice "doublages_jp4/scene3/scene3_jp8.ogg"
jp "Je dois me venger de celui qui a détruit ma demeure et tous mes biens."

#voice "doublages_jp4/scene3/scene3_lee12.ogg"
lee "Eh bien, fais le !"

#voice "doublages_jp4/scene3/scene3_jp9.ogg"
jp "Je ne sais malheureusement pas qui c'est !"

#voice "doublages_jp4/scene3/scene3_lee13.ogg"
lee "Mmhh, je vois, je vois."

#voice "doublages_jp4/scene3/scene3_lee14.ogg"
lee "Mais une telle requête nécessite un sacrifice aux dieux, en es-tu bien conscient ?"

"Jean Plank n'en était pas du tout conscient."

scene jp_sacrifice_jinx

"Mais, fin stratège, il se contenta de hocher la tête en souriant à Jinx."
"Cette dernière, voyant les dents pourries du capitaine, comprit alors qu'elle ne ferait plus long feu dans le récit."

scene lee_attend

#voice "doublages_jp4/scene3/scene3_lee15.ogg"
lee "Mmhh je vois que tu n'as malheureusement pas amené de sacrifice."

#voice "doublages_jp4/scene3/scene3_lee16.ogg"
lee "Pas de sacrifice, pas de prédiction."

play music "music/crayon.ogg"
show jp_crayon

#voice "doublages_jp4/scene3/scene3_jp10.ogg"
jp "Mais Lee..."

show lee_crayon
#voice "doublages_jp4/scene3/scene3_lee17.ogg"
lee "Quoi ?"

hide lee_crayon
#voice "doublages_jp4/scene3/scene3_jp11.ogg"
jp "Mais regarde !"

show lee_facepalm
#voice "doublages_jp4/scene3/scene3_lee18.ogg"
lee "..."

scene sacrifice_lee

play music "music/sacrifice_lee.ogg"
#voice "doublages_jp4/scene3/scene3_lee19.ogg"
lee "Très bien, j'ai compris !"

#voice "doublages_jp4/scene3/scene3_lee20.ogg"
lee "Je me suis engagé à faire cette prédiction, je vais donc te faire cette prédiction."

show jp_lee_interrogation
#voice "doublages_jp4/scene3/scene3_jp12.ogg"   #son venant de la droite
window hide
pause
hide jp_lee_interrogation

#voice "doublages_jp4/scene3/scene3_lee21.ogg"
lee "Comme tu n'as pas amené de sacrifice, je te propose de me sacrifier moi-même."

scene jp_chiot

"Jean Plank, dubitatif, pencha la tete sur le côté à la manière d'un chiot qui ne comprend pas."

show lee_couteau
voice "sound/chant_nordique.ogg"
"Lee sortit alors un couteau, et se trancha la gorge après avoir entonné les chants nordiques rituels."

show lee_tranche_gorge
#play sound "sound/lee_mort.ogg"
"Lee sortit alors un couteau, et se trancha la gorge après avoir entonné les chants nordiques rituels."
"Il se mit alors à convulser comme s'il était en transe."

scene lee_mort
"Puis s'effondra sur le sol dans une mare de sang."
"Jean Plank attendit quelques secondes, mais comme Lee ne disait plus rien, il finit par s'impatienter."

#voice "doublages_jp4/scene3/scene3_jp13.ogg"
jp "Alors ça vient ?!"

"Dit-il en mettant un coup dans les côtes de l'homme étendu sur le sol devant lui."
"Lee voulut alors lui faire part de sa vision mais malheureusement aucun son ne sortit de sa bouche."

scene lee_noir
"Usant ses dernières forces, il utilisa alors son propre sang pour orthographier un unique mot de 4 lettres sur le sol." #noir
"Puis il mourut."
"Jinx était abasourdie."
"Jean Plank observa attentivement les caractères sur le sol."
"Jinx était toujours abasourdie."

#voice "doublages_jp4/scene3/scene3_jp14.ogg"
jp "J'ai encore perdu mon temps !"
"Il se dirigea alors vers la porte."

scene lee_sortie
play music "music/sortie_lee.ogg"
#voice "doublages_jp4/scene3/scene3_jp15.ogg"
jp "Adieu, vieux débris."
"Dit-il en claquant la porte au nez de Jinx qui était juste derrière lui."

#Scene 4

scene exterieur_du_cabanon
$renpy.sound.play("sound/sound_forêtambient.ogg", loop=True)
play music "music/exterieur_du_cabanon.ogg"
"Jean Plank était embêté, il n'avait rien appris."

show porte_explose
"Il voulut se plonger dans ses pensées afin de trouver une solution mais fût interrompu par un énorme bruit."
#"Ce qui n'était finalment pas plus mal, ces pensée étant peu profonde il se serait surment fait mal XDDDDD PDTR" 

show porte_explose_jinx
"C'etait Jinx qui venait d'exploser la porte de Lee Sin à grands coups de roquette."
"En la regardant attentivement, Jean Plank crut alors déceler une pointe de colère dans ses yeux."

#voice "doublages_jp4/scene4/scene4_jinx1.ogg"
jinx "Refais ça et je jure que je te bousille, gros fils de pute !"

#voice "doublages_jp4/scene4/scene4_jp1.ogg"
jp "Hé là !"

"Jean Plank ne le prenait pas très bien."
"Certes il n'avait pas fait beaucoup de sport ces derniers temps, mais il n'était tout de même pas si gros que ça."
#crayon 

scene jp_crayon_gros
stop sound
play music "music/crayon.ogg"
#voice "doublages_jp4/scene4/scene4_jp2.ogg"
jp "Jinx..."

show jinx_crayon
#voice "doublages_jp4/scene4/scene4_jinx2.ogg"
jinx "Ose me claquer une porte au nez encore une fois et je jure que je te tranche la jugulaire avec un clou rouillé."

hide jinx_crayon
#voice "doublages_jp4/scene4/scene4_jp3.ogg"
jp "Je ne suis pas gros."

show jinx_crayon
#voice "doublages_jp4/scene4/scene4_jinx3.ogg"
jinx "J'en ai rien à foutre !"

scene ferme_en_feu
play music "music/ferme_en_feu.ogg"
$renpy.sound.play("sound/sound_feu.ogg", loop=True)
"Le problème ainsi réglé nos deux amis allèrent foutre le feu à la ferme d'à côté histoire de se détendre."
"La vue de cette immense brasier donna du baume au cœur à Jean Plank."
"Une agréable chaleur envahissait son corps tout entier."
"Tout à coup la chaleur devint beaucoup moins agréable."

scene cape_en_feu
"Jean Plank remarqua alors que sa veste avait pris feu."
"C'était Jinx qui s'était amusé à foutre le feu à ses habits."

scene jp_se_roule_par_terre
#voice "doublages_jp4/scene4/scene4_jp4.ogg"
jp "Quelle petite pitre, c'est beau la jeunesse !"

"Pensa-t-il alors qu'il se roulait par terre misérablement pour éteindre les flammes."

scene jp_jinx_dehors_lee
play music "music/jp_jinx_dehors_lee.ogg"
$renpy.sound.set_volume(0.50, delay=0, channel='sound')
"Le feu éteint et après avoir remercié Jinx pour cette bonne tranche de rigolade il voulut prendre 5 minutes pour réfléchir."

#voice "doublages_jp4/scene4/scene4_jinx4.ogg"
jinx "Bon du coup, je n'ai pas tout trop compris."

#voice "doublages_jp4/scene4/scene4_jinx5.ogg"
jinx "Quelqu'un a brulé ta demeure et tu cherches à te venger ?"

#voice "doublages_jp4/scene4/scene4_jp5.ogg"
jp "Oui, c'est ça !"

#voice "doublages_jp4/scene4/scene4_jinx6.ogg"
jinx "Depuis quand les pirates ont des demeures ?"

show jp_pasdereponse1
#J'aimerai bien un jp qui leve le doigt comme s'il allait dire un truc
jp "..."
show jp_pasdereponse2
jp "..."

show jp_jinx_dehors_lee_sourcils
"Jinx posait les questions qui fâchent."
"Jean Plank était fâché."
"Quel beau combo formaient nos deux compères."

#voice "doublages_jp4/scene4/scene4_jp6.ogg"
jp "Et ta sœur elle en a une de demeure ?"

#voice "doublages_jp4/scene4/scene4_jinx7.ogg"
jinx "Non."

hide jp_jinx_dehors_lee_sourcils
show jp_jinx_demeure
"Jean Plank avait appris quelque chose."
"Mais ça ne lui servait pas à grand-chose."

#voice "doublages_jp4/scene4/scene4_jp7.ogg"
jp "Quelqu'un a détruit ma demeure, je voulais me venger mais Saint Gède m'avait volé mon visage. J'ai donc mis ma vengeance de côté le temps de récupérer mon visage."

#voice "doublages_jp4/scene4/scene4_jp8.ogg"
jp "Maintenant je songe à la vengeance mais je ne sais pas de qui me venger."

#voice "doublages_jp4/scene4/scene4_jp9.ogg"
jp "Cela te convient-il ?"

#voice "doublages_jp4/scene4/scene4_jinx8.ogg"
jinx "Oui."

"Jinx satisfaite, Jean Plank put enfin prendre le temps de réfléchir."
"Un souvenir remonta alors à la surface."

#mettre la scene du 2 ou il dis captaine des doc  en version floue et noir et blanc
show flashback_capitainedocks
pause
show flashback_capitainedocks2
pause
hide flashback_capitainedocks2
hide flashback_capitainedocks
#voice "doublages_jp4/scene4/scene4_jp10.ogg"
jp "Jinx !"

#voice "doublages_jp4/scene4/scene4_jinx9.ogg"
jinx "Oui, c'est moi !"

#voice "doublages_jp4/scene4/scene4_jp11.ogg"
jp "Je sais de qui me venger."

scene jp_vers_son_destin
"Il n'en dit pas plus et d'un pas décidé, prit la direction de son destin, suivi de son acolyte quelque peu incrédule."

play music "music/jp_jinx_vers_haddock.ogg"
scene jp_jinx_vers_haddock
$ renpy.sound.set_volume(1.00, delay=0, channel='sound')
$renpy.sound.play("sound/sound_forêtambient.ogg", loop=True)
#voice "doublages_jp4/scene4/scene4_jinx10.ogg"
jinx "Où allons nous ?"

#voice "doublages_jp4/scene4/scene4_jp12.ogg"
jp "Chez le Capitaine des Docks."

#voice "doublages_jp4/scene4/scene4_jinx11.ogg"
jinx "Pourquoi ?"

#voice "doublages_jp4/scene4/scene4_jp13.ogg"
jp "J'ai eu une révélation."

show jinx_revelation
#voice "doublages_jp4/scene4/scene4_jinx12.ogg"
jinx "Ah, moi aussi !"

#voice "doublages_jp4/scene4/scene4_jp14.ogg"
jp "Ah ?"

#voice "doublages_jp4/scene4/scene4_jinx13.ogg"
jinx "Si les rouges-gorges avaient une tache violette à la place d'une tache rouge, on les appellerait les mauves-gorges."

jp "..."

"Jinx aimait les vérités."
hide jinx_revelation

#voice "doublages_jp4/scene4/scene4_jinx14.ogg"
jinx "Et où allons-nous ?"

show jp_colere_jinx

"Jean Plank dévisagea Jinx d'un air agressif."
"D'un mouvement stylé, il sortit alors sa carte et la posa sur une table environnante."

show jp_carte

#voice "doublages_jp4/scene4/scene4_jp915.ogg"
jp "Regarde, là ça ressemble un peu à la maison de Lee, donc comme est partis dans la direction opposée à la porte, nous on doit être à peu près là."

#voice "doublages_jp4/scene4/scene4_jp16.ogg"
jp "Je crois qu'Haddock habite à l'Est donc on doit aller vers la grosse tache jaune."

"Jinx, dubitative, n'était pas sûre que c'était de cette façon qu'on lisait une carte."
"Cependant, elle avait confiance en Jean Plank."
show ecran_noir
stop music
"A tort."

#Scene 5

scene perdus_desert
play music "music/perdus_desert.ogg"
#$renpy.sound.play("sound/sound_desertambience.ogg", loop=True)

"Deux jours plus tard, ils étaient perdus sans eau en plein désert."

show barils_explosion
"Fort heureusement, Jean Plank, expert en survie, eût le réflexe de faire exploser ses 12 derniers barils de poudre avant de s'évanouir à cause de la chaleur et la désydratation."
hide barils_explosion

stop sound
scene infirmerie_shurima
"Lorsqu'il se réveilla, il était dans ce qui semblait être une infirmerie."
"Ne voyant pas sa coéquipière, notre héros comprit instinctivement la triste nouvelle."

#voice "doublages_jp4/scene6/scene6_jp1.ogg"
jp "Morte... Pas de chance ça !"

"Jean Plank se sentait un peu patraque."
"Il ne savait pas de puis combien de temps il était allongé ici mais il lui semblait clair qu'il était victime d'un syndrome de sevrage."
"Il se mit alors en quête du flacon qui lui rendrait l'ivresse."

#voice "doublages_jp4/scene6/scene6_jp2.ogg"
jp "Toi là !"

scene jp_secoue_malade
"Hurla-t-il en empoignant un blessé."

#voice "doublages_jp4/scene6/scene6_jp3.ogg"
jp "Donne moi du rhum !"

#voice "doublages_jp4/scene6/scene6_peon1.ogg"
malade "Mais, mais... Mais enfin mais j'ai pas de rhum !"

"Une fois encore, la diplomatie avait échoué."

show shen_baffe
"Alerté par le bruit de la baffe magistrale que Jean Plank venait d'administrer, l'infirmier entra en hurlant."

#voice "doublages_jp4/scene6/scene6_shen1.ogg"
shen "Mais enfin vous êtes malade, qu'est-ce que vous foutez ?!"

show shen_jp
#voice "doublages_jp4/scene6/scene6_jp4.ogg"
jp "Je ne suis pas malade, je suis sobre !"

#voice "doublages_jp4/scene6/scene6_shen2.ogg"
shen "Mais j'en ai rien à foutre !"

show shen_malade
"Il se précipita alors sur le patient dont les blessures avaient été réouvertes."
"Jean Plank, de son coté, n'appréciait pas vraiment qu'on l'ignore."

#voice "doublages_jp4/scene6/scene6_jp5.ogg"
jp "Tu viens de me manquer de respect, vieillard !"

#voice "doublages_jp4/scene6/scene6_shen3.ogg"
shen "Mais bordel... Sécurité !"

show jp_tire_shen
play sound "sound/tirpistolet.ogg"
#voice "doublages_jp4/scene6/scene6_jp5.ogg"
jp "Personne ne me manque de respect !"

show jp_sort_infirmerie
"Il ajusta son manteau puis sortit triomphalement de l'infirmerie."
"Il le savait, il venait de remporter ce combat haut la main."
"(Le blessé survécut miraculeusement à ses blessures)"

play alder "sound/sound_village.ogg"
scene jp_shurima
"Une fois dehors, Jean Plank comprit, grâce à son exceptionnel esprit de déduction, qu'il était en ville."

if censure == 1:
    scene jp_fiora_galipette_censored
else:
    scene jp_fiora_galipette_uncensored
$ renpy.sound.set_volume(0.00, delay=0, channel='alder')
"Après avoir très poliment \"interrogé\" une passante..." #Scene de cul gratuite.png

show passante_explications
$ renpy.sound.set_volume(1.00, delay=0, channel='alder')
"...il apprit qu'il se trouvait désormais dans le coeur de Shurima, capitale de la région, située au centre du désert éponyme."
"Bien sûr, ces mots étaient trop compliqués pour le capitaine."

show passante_explications2
#voice "doublages_jp4/scene6/scene6_femme1.ogg"
femme "Toi être dans ville au milieu de mer de sable."

#voice "doublages_jp4/scene6/scene6_jp6.ogg"
jp "Une mer de sable ? Quelle drôle d'idée !"

show jp_shurima1

$ renpy.sound.set_volume(1.00, delay=0, channel='sound')
$renpy.sound.play("sound/musique_alder.ogg", loop=True)
$renpy.sound.set_pan(1,0)

"Curieux de découvrir cet étrange pays, notre capitaine se mit à déambuler dans les rues de la capitale."

show jp_shurima2

$renpy.sound.set_pan(0,0)

"Curieux de découvrir cet étrange pays, notre capitaine se mit à déambuler dans les rues de la capitale."

$renpy.sound.set_pan(-1,0)
show jp_shurima3
"Curieux de découvrir cet étrange pays, notre capitaine se mit à déambuler dans les rues de la capitale."

stop alder
stop sound
$renpy.sound.set_pan(0,0)
scene salle_artefact
play music "music/artefact.ogg"
"Après avoir ennuyé quelques passants, dont seulement 20\% de femmes, il finit par arriver dans une salle bien étrange."
"Elle était gigantesque et comportait en son centre un autel sur lequel reposait un bien mystérieux artefact."
menu: 
    "Aller pendre l'artefact":
        menu:
            "Eviter le piège":
                "Sentant le danger, Jean Plank se jeta sur le coté."
                "Il fit un roulé-boulé avant de s'étaler misérablement sur le sol."
                "Malheureusement pour lui, il n'y avait pas du tout de piège."
                "C'est donc désormais blessé dans son orgeuil et regardé par des gardes hilares qu'il se dirigea vers l'artefact."
            "Ne pas éviter le piège":
                "Jean Plank marcha calmement vers l'artefact."
        $ artefact = 1
        "Voyant qu'il s'approchait de plus en plus, un des garde se décida à intervenir."

        show garde_artefact
        #voice "doublages_jp4/scene6/scene6_garde1.ogg"
        garde "Halte ! Que faites-vous, étranger ?"
        #Scene confiance en soit/regard ténébreux

        #voice "doublages_jp4/scene6/scene6_jp7.ogg"
        jp "T'inquiète frère."
        "Le garde était incrédule."
        "Jean Plank avait répondu avec tant de charisme et d'assurance."
        "Jamais quelqu'un qui n'avait rien a foutre là n'aurait pu répondre de la sorte."

        show garde_excuses
        "Aussi s'écarta-t-il du chemin de Jean Plank en lui présentant des excuses."
        "Jean Plank s'approcha alors de l'autel."
        "L'artefact ressemblait VAGUEMENT à une orange."

        show jp_prend_artefact
        #voice "doublages_jp4/scene6/scene6_jp8.ogg"
        jp "Bien juteux !"
        "S'exclama-t-il en se saisissant de l'objet."

        show jp_prend_artefact2
        "C'est à ce moment précis que l'ambiance changea radicalement."
        "Une ombre se jeta sur la pièce alors que tout se mettait à trembler."
        "C'était comme si toute vie venait de quitter le monde."
        "Les gardes, bien que remplis de confiance envers le capitaine, ne purent s'empêcher d'être dubatifs."

        show garde_doute
        #voice "doublages_jp4/scene6/scene6_garde2.ogg"
        garde "C'est normal ça ?"
        #Je vois bien un Jean Plank qui court un peu commme shaco
        show fuite_artefact
        "Jean Plank ne put répondre, il était déjà loin."

    "Ne pas aller prendre l'artefact":
        "Jean Plank n'était intéressé."
        $ artefact = 0

        #voice "doublages_jp4/scene6/scene6_jp9.ogg"
        jp "Je ne suis pas intéressé."

        show sortie_artefact
        "Il sortit alors dignement de la pièce sous le regard intrigué des gardes, qui ne comprendraient jamais ce qu'il venait de se passer."

play music "music/simon.ogg"
if artefact == 1:
    show avant_simon_artefact
    $renpy.sound.play("sound/sound_villageinquiet.ogg", loop=True)
else:
    show avant_simon
    $renpy.sound.play("sound/sound_village.ogg", loop=True)

"Jean Plank voulait maintenant quitter la ville le plus rapidement possible."
"Il avait assez perdu de temps dans ce taudis."
"Il se dirigea donc vers la porte principale."
"Il allait la passer, mais une main se posa alors sur son épaule pour le retenir."

if artefact == 1:
    show simon_offre_artefact
else:
    show simon_offre

stop sound
play music "music/simon2.ogg"
#voice "doublages_jp4/scene6/scene6_simon1.ogg"
simon "Etranger, tu ne peux pas t'aventurer dans le désert sans monture, c'est du suicide !"

#voice "doublages_jp4/scene6/scene6_jp10.ogg"
jp "Et alors ?"

#voice "doublages_jp4/scene6/scene6_simon2.ogg"
simon "Eh bien, ce serait bête ! En plus tu passerais à coté d'une super opportunité !"

#voice "doublages_jp4/scene6/scene6_jp11.ogg"
jp "Je suis très intéressé."

#voice "doublages_jp4/scene6/scene6_simon3.ogg"
simon "Cela te coûterait seulement 300 pièces d'or !"
menu:
    "Je ne suis plus intéressé":
        "Jean Plank choisit de résister à son instinct de jeune opportuniste."

        #voice "doublages_jp4/scene6/scene6_jp12.ogg"
        jp "Au revoir !"
        if artefact ==1:
            "Dit-il en se retournant vers la porte de la ville, essayant tant bien que mal de se persuader que son choix était le bon."
        else :
            show sortie_shurima1
            "Dit-il en se passant la porte de la ville, essayant tant bien que mal de se persuader que son choix était le bon."
  
    "Payer":
        "Jean Plank le savait : dans la vie, il n'y avait que deux moyens de gagner gros."
        "Investir, et investir dans l'immobilier."
        "Aussi se décida-t-il à sortir 300 pièces d'or pour accéder à la super offre de ce généreux marchand."
        "Malheureusement, il n'avait pas 300 pièces d'or."
        if artefact ==1:
            "Anéanti, Jean Plank dût donc se résoudre à décliner cette super offre et se retourna vers la grande porte menant au désert."
        else :
            show sortie_shurima1
            "Anéanti, Jean Plank dût donc se résoudre à décliner cette super offre et passa la grande porte menant au désert."
    
    "Payer plutôt deux fois qu'une":
        "Jean Plank le savait, plus on investissait et plus ça rapportait gros."
        "Aussi se décida-t-il à sortir 600 pièces d'or pour accéder à la super offre de cet altruiste marchand."
        "Malheureusement, il ne possédait pas 600 pièces d'or."
        if artefact ==1:
            "Mentalement détruit, Jean Plank dût donc se résoudre à décliner cette super offre et se retourna vers la grande porte menant au désert."
        else :
            show sortie_shurima1
            "Mentalement détruit, Jean Plank dût donc se résoudre à décliner cette super offre et passa la grande porte menant au désert."


if artefact == 1:

    play music "music/general.ogg"
    #voice "doublages_jp4/scene6/scene6_general1.ogg"
    general "Il est là ! Arrêtez le, vite !"

    scene general
    "A peine trois secondes plus tard, tout un régiment de soldats s'alignait derrière un Jean Plank qui allait franchir le pas de la porte."

    #voice "doublages_jp4/scene6/scene6_general2.ogg"
    general "Attends, étranger ! Pitié, pas un pas de plus !"
    menu: 
        "Ma pitié est morte quand mon navire a coulé":
            "Jean Plank fit un pas en arrière puis se retourna."

            #voice "doublages_jp4/scene6/scene6_jp12.ogg"
            jp "Ma pitié est morte quand mon navire a coulé !"
        "Appuyer sa dominance de la situation":

            #voice "doublages_jp4/scene6/scene6_jp13.ogg"
            jp "C'est moi le capitrane !"
            "Oui, comme d'habitude, Jean Plank était ivre."

    #voice "doublages_jp4/scene6/scene6_general3.ogg"
    general "Etranger ! L'artefact que tu as pris..."

    show jp_general
    #voice "doublages_jp4/scene6/scene6_jp14.ogg"
    jp "Celui là ?"

    #voice "doublages_jp4/scene6/scene6_general4.ogg"
    general "Oui !"

    #voice "doublages_jp4/scene6/scene6_jp15.ogg"
    jp "Ce n'est pas une simple orange."

    #voice "doublages_jp4/scene6/scene6_general5.ogg"
    general "Ce n'est pas une orange tout court, sombre crétin !"

    #voice "doublages_jp4/scene6/scene6_general6.ogg"
    general "C'est le coeur de la cité !"

    #voice "doublages_jp4/scene6/scene6_general7.ogg"
    general "Au moment même où tu le sortiras, la cité sera condamnée !"

    "Jean Plank s'arrêta."
    "Son regard croisa celui du général."
    "Ils se devisagèrent intensement."

    #voice "doublages_jp4/scene6/scene6_jp16.ogg"
    jp "TU BLUFFES !"

    #General bouche bée
    "Le général était bouche bée."
    "Jamais de sa vie, il n'avait vu un connard pareil."
    "Le destin de Shurima et de ses 700 000 habitants était en jeu."
    "Il lui fallait une solution et maintenant !"

    scene sortie_shurima
    "Malheureusement, il était trop tard. Jean Plank venait de passer la porte."
    
    $renpy.sound.play("sound/sound_destructionshurima.ogg", loop=True)
    "Un bruit gigantesque se fit alors entendre."

    show sortie_shurima2
    "Le desert se mit alors à bouilloner. Des vagues de sable géantes surgirent alors du sol et, telles les flammes de l'enfer, s'abattirent sur la ville."
    "Visiblement, il ne bluffait pas."
    "Enfin bon, ce qui est fait est fait, que voulez-vous ?"
 #   "C'était le chaos. Tous les habitants paniquaient, couraient et hurlaient, horrifiés."
 #   "Au milieu de toute cette débacle, seul l'un d'entre eux restait impassible au milieu de tout ce chaos."
 #   "Rongé par le regret de ne pas avoir jouer au poker plus souvent, le général disparu avec sa ville."
    


#"La route était assez longue jusqu'à chez Haddock."
#"Cela ne dérangeait pas Jean Plank qui avait pris l'habitude de voyager et qui se sentait pousser des ailes à mesure qu'il approchait de son objectif."
#
#if artefact:  #ACHANGER
#    "En revanche, pour Jinx c'était une autre affaire."
#    "Extenué par le voyage, elle n'était plus capable de marcher."
#    "Mais ne pouvant se resoudre à abandonner le capitaine, elle avait trouvé une astucce pour continuer de suivre le capitaine malgré tout."
#    "Elle avait noué une de ses nates à un des pied du capitaine et se laissait trainer depuis 3 jours."
#    jinx "Ça tire un peu au début mais c'est comme boire du carburant; on s'y fait !"
#
#scene maisonhaddock
#if artefact:
#    "Mais ils touchaient enfin au but :"
#    "Après 3 semaines de voyage, ils étaient finalement parvenu à la maison d'Haddock."
#else:
#    "Mais il touchait enfin au but :"
#    "Après 3 semaines de voyage, il était finalement parvenu à la maison d'Haddock."
#"Jean Plank sentait l'excitation grandir en lui."
#"Enfin il y était."
#"Il courrut vers la petite porte en bois."
#"Petite porte qu'il détruisit d'un magistral coup de pied en hurlant."
#
#scene haddock
#
#play sound "sound/sound_violent_open_door.ogg"
#voice "doublages_jpvalhalla/audio_sc_7/7_jp2.ogg"
#
#jp "Haddock ! Tout le monde doit payer !"
#
#"Voyant sa porte voler en éclats, Haddock, qui était visiblement en train de déjeuner avec sa femme et sa fille, tourna la tête."
#
#voice "doublages_jpvalhalla/audio_sc_7/7_haddock1.ogg"
#Haddock "Tintin ?"
#
#voice "doublages_jpvalhalla/audio_sc_7/7_jp3.ogg"
#jp "Non, c'est pas Tintin !"
#
#label debut_fight_Haddock:
#
#scene fighthaddock
#play music "music/music_fighthaddock.ogg"
#
#voice "doublages_jpvalhalla/audio_sc_7/7_haddock2.ogg"
#Haddock "Alors que fais-tu chez moi ?!"
#
#"Dit Haddock en se levant brusquement de sa chaise."
#label fight_pass1:
#menu:
#    "Courir vers Haddock et le frapper":
#        "Jean Plank courut vers Haddock pour lui mettre une de ses fameuses baffes secrètes."
#        "Cependant il avait oublié qu'Haddock était à l'autre bout de la pièce."
#        menu :
#            "Courrir plus vite":
#                "Cependant j'en Plank était malin, si Hadock était plus loin, il n'avait qu'a courrir plus vite."
#                "Ce qu'il fit avec brio."
#                "Tel le bison qui traverse la savane, il traversa la pièce et se jetta sur Haddock."
#                label run_down_haddock:
#                scene chaise
#                "Ce dernier qui venait tout juste de se saisir d'une chaise, et se préparait à en foutre un coup à Jean Plank."
#                menu:
#                    "Reculer de peur de se prendre la chaise":
#                         "Aïe aïe aïe, mauvais choix."
#                         "Jean Plank recula si vite qu'il se congna contre un truc."
#                         "Vous ne saurez jamais quoi, mais il en mourru."
#                         jump end_tomb
#
#                    "La chaise n'existe que si tu as peur d'elle.":
#                        "Jean Plank navait pas peur des chaises"
#                        "Hadock, lui non plus n'avait encore jamais eu peur d'une chaise."
#                        "Cependant celle que Jean Plank venanit de lui arracher des mains semblait vraiment menaçante."
#                        "Pas autant que de courrir avec des ciseaux, mais vraiment pas loin."
#                        "Tétanisé par la peur, il ne pu que regarder le destin dans les yeux."
#                        "En l'occurance ,le destin avait quand même vachement la forme d'un tabouret."
#                        menu:
#                            "Faire attention à Milou, le chien de Tintin":
#                                "Jean Plank était méfiant. Il n'attaqua pas et chercha du regard ce fichu clébard."
#                                "Il y avait en effet un chien !"
#                                "Mais celui ci semblait empaillé depuis un moment."
#                                "Pas un danger pour notre héro en somme."
#                                "Par contre la femme d'haddock, qui avait profité de ce moment d'inattention se saisir d'un vase, en était un."
#                                menu:
#                                    "Eviter le coup de vase in-extremis":
#                                        "Malheureusement, il était trop tard pour éviter le vase."
#                                        "Jean Plank distrait par sa tentative d'esquive, se prit le vase de plein fouet et perdi connaissance."
#                                        jump fin_prison
#
#                                    "Prendre le coup de vase comme un brave":
#                                        "De toute façon il était trop tard pour l'éviter."
#                                        "Cependant la bravoure de Jean Plank fit en sorte qu'il s'en sorti sans perdre connaissance."
#                                        "Il lanca rapidement son tabouret sur la tronche de Haddock qui tomba lourdement au sol."
#                                        "Puis, suspectant la fille de preparer elle aussi un coup en traître, il se saisi de cette dernière pour la lancer sur la mère."
#                                        "Les deux etre humains de sexe feminin volèrent dans la pièce"
#                                        "Jean Plank hallllaaa verifier qu'elles ne lui causerait plus d'ennuit"
#                                        "Il prit une pause pour penser un peu à l'ocean" #Un Jean pank stylé avec la musique d'ultra vomit discretement en son sonnore
#                                        "Puis il retourna cogner sur hadock."
#                                        menu :
#                                            "Revérifier que la femme ne causera pas d'ennui":
#                                                "Jean Plank décida de suivre son instinct."
#                                                "Delaissant Haddock il HALLA se saisir de la femme. Il raprocha son visage du sien en soulevant son corp inerte par le col."
#                                                jp "TU FAIS SEMBLANT UN C'EST CA ?! TU CROIS QUE CA M'AMUSE ?!"
#                                                "Voyant qu'elle ne repondait pas, il lui mit une baffe titanesque qui l'envoya quelque mettre plus loin."
#                                                "Desormais serein, il retourna cogner sur haddock."
#
#                                            "Cogner sur Haddock mais avec le doute que la femme puisse quand même se relever et attaquer dans le dos en traître comme le font toutes les femmes":
#                                                "Jean Plank cogna Haddock, cependant, il le fit avec une lègère anxiété."
#                                                "Cela gachait un peu son plaisir."
#                                                "Il continua de congner de bon coeur malgrès tout."
#                                                "Le stress vous fait gagner \"Cheuveux blanc\""
#                                        jump fin_fight_haddock
#
#
#
#                            "Abbatre la chaise sur ce gredin !": #ACHANGER
#                                "Jean Plank abattu violamment ça chaise sur le crane de son enemie"
#                                "Sa fureux n'ayant d'egale que sa stupidité, la cervelle du capitaine des doc se répendie sur le sol sous les yeux horifiés de sa femme et sa fille."
#                                "Stylé dans la vengence, Jean Plank frappa chacune d'entre elle avant de les violer."
#                                "Ceci fait, il les frappa encore hisoire de marquer le coup."
#                                "Jean Plank était victorieux."
#                                "Cependant il regrettait un peu cette victoire trop facile."
#                                "Le scénariste aussi d'ailleur."
#                                "C'est pour cela que malgrès votre victoire, totale et incontestabe, vous n'aurez tout de même que l'ecran de défaite en récompense."
#                                jump end_false_vitory
#
#            "Courrir moin vite":
#                "Jean Plank ralenti le rythme afin d'avoir plus de teps pour anticiper la reaction d'Hadock"
#                "Mais plus il ralentissait, plus haddock avait le temps de preparer une contre offensive."
#                "Il se vait donc de ralentir encore."
#                "Mais haddock avait toujours plus de temps"
#                "Et Jean Plank devait toujours plus ralentir."
#                "et ..."
#                "Totalement ahuri par le fait que Jean Plank ne bougeait maintenant plus du tout, haddock fini par se lever pour aller à sa rencontre."
#                #scene crayon
#                haddock "Jean Plank tu es un attardé mental c'est ça ?"
#                jp "Bah n..."
#                #Scene flash back musique triste (peut-etre la faire en vidéo)
#                #ryse "mais vous etes totallement attardé"
#                #lucien "Attend tu sais pas compter ?"
#                #jp et pas lire non plus
#                "Le triste vérité atteignait enfin Jean Plank."
#                jp "Haddock,"
#                jp "PERSONNE NE ME TRAITE D'ATTARDE MENTAL."  #ACHANGER
#                "Jean Plank vennait de tirer au pistolet dans le crane de son ennemi, causant ainsi son décès précipité."
#                "La cervelle de son ennemi sur les murs, sa compagne tumefiée au sol et sa fille qui allait très bientot comprendre ce que celà impliquait d'etre une femme."
#                "(Car Jean Plank allait lui faire un exposé)"
#                "Jean Plank était indéniablement victorieux" #FINDU #ACHANGER
#                "Cependant il regratta longtemps cette victoire trop facile."
#                "Le scénariste aussi d'ailleur."
#                "C'est pour cela que malgrès votre victoire, totale et incontestabe, vous n'aurez tout de même que l'ecran de défaite en récompense"
#                jump end_false_vitory
#
#    "Les femmes et les enfants d'abord":
#        "D'accord mais la femme ou la fille ?"
#        menu:
#            "La femme !":
#                jump les_deux
#            "La fille !":
#                jump les_deux
#            "Les deux ?":
#                "Il n'y avait qu'une seulement manière de neutraliser ces deux puissants adversaires en un coup."
#                "Jean Plank se saisit de son pistolet d'une main et de son épé de l'autre."
#                "Puis, d'un agile mouvement il lança puissanment ses deux armes à travers la pièce."
#                "Mais Jean Plank n'était pas très bon lanceur et ne toucha absolument personne."
#                "L'égo de Jean Plank fut tout bonement anéhenti en réalisant cette effroyable vérité."
#                "Ayant perdu toute volonté de se battre et désomais dépressif, il alla lui même se rendre à la police."
#                "Seul et déprimé au fond de ça cellule il prit la resolution de ne plus jamais rien lancer."
#                jump fin_prison
#        label les_deux:
#        jp "GIBIER DE POTENCE ! C'EST HADDOCK QUE JE VEUX FRAPPER !"
#        "Hurla Jean Plank, en se précipitant sur Haddock."
#        jump run_down_haddock


#label end_tomb:
#label end_false_victory:
#label fin_prison:
#label fin_fight_haddock:
#
###############################################################################################################################################
############Fin du combat Haddock
###################################################################################################################################################
##label start:
#
#label fin_fight:
#stop sound
#scene finfighthaddock
#voice "doublages_jpvalhalla/audio_sc_7/7_jp4.ogg"
#jp "Tu vas casser ta pipe, vieux fou !"
#"Haddock n'était vraiment pas rassuré."
#"Pourquoi donc ce cinglé venait tout casser chez lui ?"
#
#if artefact:
#    "Et pourquoi son abrutie d'accolite était elle en train d'essayer de se pendre avec ses propres cheveux ?"
#    #voice "doublages_jpvalhalla/audio_sc_7/7_haddock3.ogg"
#    Haddock "Bachi-bouzouc ! Que faites vous ici ?!"
#
#    #voice
#    jinx "Un noeud coulant, c'est pour me pendre !"
#
#    "Haddock abassourdi ne comprenait rien."
#    "Le capitaine profita de ce moment d'égarement pour cogner Haddock de toutes ses forces."
#else:
#    voice "doublages_jpvalhalla/audio_sc_7/7_haddock3.ogg"
#    Haddock "Bachi-bouzouc ! Que fais tu ici ?!"
#
#    scene haddocklose
#
#    voice "doublages_jpvalhalla/audio_sc_7/7_jp5.ogg"
#    jp "Comme on se retrouve, enculé !"
#    play sound "sound/sound_poing.ogg"
#    "Cria le Capitaine en cognant Haddock de toutes ses forces."
#"Haddock s'éffondra sur le sol."
#voice "doublages_jpvalhalla/audio_sc_7/7_haddock4.ogg"
#Haddock "Mille milliards de mille sabords, ça ne va pas se passer comme ça !"
#"Hurla Haddock en se relevant !"
#play sound "sound/sound_poing2.ogg"
#"Malheureusement, un second coup lui signifia qu'il ferait mieux de rester à terre."
#
#voice "doublages_jpvalhalla/audio_sc_7/7_jp6.ogg"
#jp "Tu vas payer !"
#
#voice "doublages_jpvalhalla/audio_sc_7/7_haddock5.ogg"
#Haddock "Mais tonnerre de Brest, pourquoi ?"
#
#voice "doublages_jpvalhalla/audio_sc_7/7_jp7.ogg"
#jp "Vengeance !"
#
#play sound "sound/violent_coup_de_poing.ogg"
#"Cette fois Haddock ne put plus dire mot."
#if artefact:
#    "Et c'est avec l'image floue du visage de jinx devenant violet à mesure qu'elle étoufait, qu'il fini par s'évanouir"
#
#
#scene haddocksol
#play music "music/music_finfighthaddock.ogg"
#
#"Jean Plank contemplait son ennemi juré évanoui sur le sol."
#"Il aurait voulu l'achever mais était un peu embêté : il se rendait maintenant compte qu'il n'était pas sûr de la culpabilité d'Haddock."
#if artefact:
#    "Il aurait voulu demander son avis à Jinx mais cette dernière était dans le coma."
#    "Jean Plank qui, en essayant de la détacher avait glissé et c'était rattrapé en s'accrochant à elle, se demandait s'il n'avait pas une part de responsabilité."
#    "Aussi désida-t-il de ne pas l'insulter de vieille pute."
#    "Ça et le fait qu'elle n'était pas vieille."
#    "Il arreta de digressé et revins à Haddock"
#
#"C'est vrai qu'il n'avait pas beaucoup de preuves que c'était bel et bien lui qui avait brulé sa maison, excepté le retentissant \"TINTIN\" qui s'était fait entendre ce jour-ci."
#"D'autant qu'Haddock n'avait pas vraiment l'air de savoir ce qu'il faisait ici."
#"Non, décidément il lui fallait des aveux."
#"Jean Plank entreprit alors de le torturer en quête de réponses."
#
#scene torture
#
#"Aussi, à peine son ennemi réveillé, notre héros commença sa besogne."
#"Plusieurs heures de torture ne suffisant pas à le faire avouer, Jean Plank entreprit de violer la femme d'Haddock sous ses yeux."
#"Mais toujours aucun résultat."
#if artefact:
#    "Jinx, qui s'était reveillé entre temps, supposa que Jean Plank s'y était peut-être mal prit, et tenta elle aussi l'experience."
#    "Mais sans d'avantage de succès."
#"Ce n'est qu'après avoir inscrit sa fille sur TikTok sans obtenir aucun aveu que Jean Plank commença à vraiment croire qu'Haddock était innocent."
#"Mais si Haddock n'était pas coupable..."
#"Qui aurait été coupable ?"
#"Jean Plank se mit à réfléchir.... Qui donc aurait pu lui en vouloir ?"
#"Après une intense réflexion de plusieurs heures, il finit par perdre le compte passé la 49e personne."
#"Décidément, réfléchir ne menait à rien."
#"Au bout du rouleau et éreinté, il prit une lampée de rhum."
#if artefact:
#    "Il en proposa aussi Jinx et aux otages."
#if artefact:
#    "Il en proposa aussi à ses otages."
#"Décidément, même dans cette situation, Jean Plank avait un grand cœur."
#"Une fois le cerveau de Jean Plank bien désydraté à l'alcool, il eu une idée."
#"Il allait retrouner à Bilgwater, là ou sa deumeure avait cramé et y chercher des indices sur l'identité du vendale."
#"Ainsi commence les aventure de l'inspecteur Plank."


#Scene bateau.

play music "music/jp_theme.ogg"
$renpy.sound.play("sound/sound_mer.ogg", loop=True)
scene inspecteur_bateau
"Jean Plank était à nouveau en mer. Il avait dégoté un bateau et un équipage en utilisant son nouveau statut d'inspecteur."
"Si, si je vous assure."

$renpy.sound.set_volume(0.00, delay=0, channel='sound')
show inspecteur_badge
"Ivre mort, il avait ramassé un bout de carton et gardait une idée vague d'à quoi ressemblait le badge de Caitlyn." 
"Il avait donc réalisé une reproduction très fidèle, grâce à des crayons de couleur échangés à un gamin du coin contre sa ceinture et une pomme."
"Il était ensuite allé dans un pub très louche où il avait parié son badge contre un navire et des hommes face à un capitaine au moins aussi ivre que le nôtre."

show inspecteur_ciseaux
"Verdict avait été rendu, il avait gagné en faisant \"ciseau\" 37 fois d'affilée."

show inspecteur_ciseaux1
"Verdict avait été rendu, il avait gagné en faisant \"ciseau\" 37 fois d'affilée."

show inspecteur_ciseaux2
"Verdict avait été rendu, il avait gagné en faisant \"ciseau\" 37 fois d'affilée."

$renpy.sound.set_volume(1.00, delay=0, channel='sound')
scene inspecteur_bateau
"La mer était calme et un superbe vent arrière poussait le navire."
"Notre capitaine était de bonne humeur."
"Il avait même commencé à sympathiser avec l'équipage."

show tape_dans_le_dos
#voice "doublages_jp4/scene9/scene9_jp1.ogg"
jp "Haha !"

hide tape_dans_le_dos
"Cependant, la vie de Jean Plank ne pouvait pas être un long fleuve tranquille."

#voice "doublages_jp4/scene6/scene6_jp2.ogg"
jp "Martin !"

show inspecteur_bateau2
#voice "doublages_jp4/scene6/scene6_jp3.ogg"
jp "Martiiin !"

show tobias1
#voice "doublages_jp4/scene6/scene6_tobias1.ogg"
martin "Je vous ai déjà dit que je ne m'appelais pas Martin !"

#voice "doublages_jp4/scene6/scene6_jp4.ogg"
jp "Pourtant tu réponds."

"Le pauvre Tobias ne trouva rien à redire."

#voice "doublages_jp4/scene6/scene6_jp5.ogg"
jp "Martin ?"

#voice "doublages_jp4/scene6/scene6_tobias2.ogg"
martin "Tobias !"#da yo

#voice "doublages_jp4/scene6/scene6_jp6.ogg"
jp "As-tu déjà eu l'impression que le monde était comme dessiné par les événements que tu rencontres ?"

#voice "doublages_jp4/scene6/scene6_jp7.ogg"
jp "Est-ce un biais psychologique, ou la vie n'est-elle qu'un rêve et ce monde cessera d'exister à mon réveil ?"

#voice "doublages_jp4/scene6/scene6_jp8.ogg"
jp "Ou au contraire, tout continuera-t-il indéfiniment comme si notre existence toute entière n'avait pas vraiment d'importance dans le déroulement des événements de l'Univers ?"

#voice "doublages_jp4/scene6/scene6_jp9.ogg"
jp "Finalement est-ce que ce n'est pas cette impuissance à impacter radicalement notre monde que l'on nomme le destin ?"

"Mart... Tobias était un peu perdu."
"Il se demandait maintenant s'il ne préférait pas le capitaine quand il était ivre."

show tobias_rhum
"Aussi, il se décida à sortir l'alcool de sa cachette et à le rendre à Jean Plank."

hide tobias_rhum
#voice "doublages_jp4/scene6/scene6_jp10.ogg"
jp "Merci beaucoup."

show tobias2
"Quelque minutes plus tard, Tobias revint vers le capitaine pour vérifier que celui-ci était à nouveau lui même."

show tobias3
#voice "doublages_jp4/scene6/scene6_jp11.ogg"
jp "Je vois des tentacules !"

#voice "doublages_jp4/scene6/scene6_tobias3.ogg"
martin "Ahhh tant mieux !"

show tobias4
#voice "doublages_jp4/scene6/scene6_jp12.ogg"
jp "Non ! Je vois vraiment des tentacules."

play music "music/fight_illaoi.ogg" fadein(0.3)
show tobias5
#voice "doublages_jp4/scene6/scene6_tobias4.ogg"
"Tobias se retourna et, voyant les effroyables masses gélatineuses qui grimpaient le long du navire, il ne put s'empêcher de hurler."
menu:
    "Rassurer Tobias":
        
        #voice "doublages_jp4/scene6/scene6_jp13.ogg"
        jp "Et puis quoi encore ?"
    "Il va la fermer sa gueule ?!":
        
        #voice "doublages_jp4/scene6/scene6_jp14.ogg"
        jp "Mais il va la fermer sa gueule ?!"

show choix_illaoi        
"Hurla Jean Plank en tranchant violemment la gorge de Tobias."
label fight_illaoi:
scene choix_illaoi
"Jean Plank connaissait cette situation qui commençait un peu à l'agacer."
"Il allait devoir faire un choix."
menu:
    "Mater Illafloy":
        "Jean Plank savait comment faire."
        "Il avait séduit la donzelle une fois, il saurait la séduire une deuxième."
        show haubants
        "Agile malgré ses quelques kilos en trop, il grimpa rapidement dans les haubants."

        #voice "doublages_jp4/scene6/scene6_jp15.ogg"
        jp "Illafloy !"
        "Aucune réponse."

        #voice "doublages_jp4/scene6/scene6_jp16.ogg"
        jp "Je sais ce que tu veux !"

        "Toujours aucune réponse, mais l'équipage, comme rassuré par la voix puissante du capitaine, avait cessé de s'agiter. Tous levaient désormais des yeux pleins d'espoir vers le capitaine."

        show haubants_penis
        "Jean Plank, empli d'une fierté immense, sortit alors son énorme sexe qu'il montra à l'océan."
        
        #voice "doublages_jp4/scene6/scene6_jp17.ogg"
        jp "Regarde Jamy !"

        "En guise de réponse, un tentacule s'abattit sur la barre, tuant 3 marins."
        "Notre capitaine rengaina son sabre superbe et rejoignit rapidement le contremaître."

        show contremaitre
        #voice "doublages_jp4/scene6/scene6_jp18.ogg"
        jp "Bon bah j'aurais tout essayé, je n'ai rien à me reprocher."

        #voice "doublages_jp4/scene6/scene6_contremaitre1.ogg"
        contremaitre "Quoi ?"
        #play sound "sound/naufrage.ogg"
        stop music
        show naufrage
        window hide
        pause

        

    "Matter Illafloy":
        "Jeu de mot misérable, je sais."
        show jp_plonge_illaoi
        "Pris d'une soudaine et incontrôlable envie de revoir son seul amour, Jean Plank se jetta à l'eau."
        "Il nagea en direction des abysses avec conviction."
        "2 minutes plus tard, il était mort."
        play music "music/music_mort.ogg"
        show ecran_game_over
        window hide
        pause
        hide ecran_game_over
        stop sound
        play music "music/fight_illaoi.ogg"
        jump fight_illaoi

play music "music/illaoi.ogg"
"Le navire commençait à sombrer."
"Comme Jean Plank l'avait appris, un équipage sombre avec son navire."
show equipage_sombre
"Aussi avait-il fait le nécéssaire pour qu'aucun marin n'en réchappe."

show jp_mat
"A nouveau accroché au mât comme un idiot, il observait l'étendue d'eau devant lui avec résignation alors que le navire s'enfonçait lentement dans les profondeurs."
"Après quelques instants, il prit une grande inspiration et s'adressa à l'océan."

#voice "doublages_jp4/scene6/scene6_jp18.ogg"
jp "Illafloy !"

"Aucune réponse."
"Il réessaya."

#voice "doublages_jp4/scene6/scene6_jp19.ogg"
jp "Illafloy !?"

"Toujours rien..."
"Perdant patience, il tenta le tout pour le tout."

#voice "doublages_jp4/scene6/scene6_jp20.ogg"
jp "Illafloy, OMG, réponds-moi grosse p..."

show jp_illaoi
"Il s'accrocha au mât de toutes ses forces alors que la déésse de l'océan sortait de l'eau en une vague majestueuse."
"Jean Plank relâcha légèrement sa prise et adressa ses hommages à la déesse."

#voice "doublages_jp4/scene6/scene6_jp21.ogg"
jp "Illafloy..."

#voice "doublages_jp4/scene6/scene6_illaoi1.ogg"
illaoi "Jean Plank..."

#voice "doublages_jp4/scene6/scene6_jp22.ogg"
jp "Je vois que tu as pris du muscle."

#voice "doublages_jp4/scene6/scene6_illaoi2.ogg"
illaoi "Je vois que tu as pris des coups."

show jp_crayon
$renpy.sound.set_volume(0.00, delay=0, channel='music')
play alder "music/crayon.ogg"

#voice "doublages_jp4/scene6/scene6_jp23.ogg"
jp "Illafloy..."

show illaoi_crayon
#voice "doublages_jp4/scene6/scene6_illaoi3.ogg"
illaoi "Oui, Jean Plank ?"

hide illaoi_crayon
#voice "doublages_jp4/scene6/scene6_jp24.ogg"
jp "Je sais que tu m'en veux."

#voice "doublages_jp4/scene6/scene6_jp25.ogg"
jp "Je sais aussi que ce que j'ai fait est impardonnable."

#voice "doublages_jp4/scene6/scene6_jp26.ogg"
jp "Mais sincèrement..."

#voice "doublages_jp4/scene6/scene6_jp27.ogg"
jp "Détruire tous mes navires ?"

#voice "doublages_jp4/scene6/scene6_jp28.ogg"
jp "Ne penses-tu pas que ta quête de vengeance est un peu puérile ?"
$renpy.sound.set_volume(1.00, delay=0, channel='music')
$renpy.sound.set_volume(1.00, delay=0, channel='sound')
stop alder
hide jp_crayon

show illaoi_sourcil
"Illafloy haussa un sourcil, ni plus ni moins."
"A la vue de l'expression figée sur le visage d'Illafloy, Jean Plank comprit que ses excuses n'avaient peut-être pas fait mouche."
"La voie diplomatique ayant encore une fois echoué, Jean Plank se jura que dorénavant, il utiliserait systématiquement la force pour arriver à ses fins."

hide illaoi_sourcil
#voice "doublages_jp4/scene6/scene6_illaoi4.ogg"
illaoi "Très bien, Jean Plank."

#voice "doublages_jp4/scene6/scene6_illaoi5.ogg"
illaoi "Tu as raison, tout cela a assez duré."

#voice "doublages_jp4/scene6/scene6_illaoi6.ogg"
illaoi "Je vais arrêter de te harceler..."

#voice "doublages_jp4/scene6/scene6_illaoi7.ogg"
illaoi "Mais en échange, je vais te prendre ce que tu as de plus précieux."

#voice "doublages_jp4/scene6/scene6_jp29.ogg"
jp "Mon trésor ?"

#voice "doublages_jp4/scene6/scene6_illaoi8.ogg"
illaoi "Ton honneur !"

"Jean Plank ne savait pas dans quel univers elle avait vu que son honneur était précieux, mais il préféra garder le silence dans l'espoir de bénéficier de cette avantageuse transaction."

show jp_stonks
#voice "doublages_jp4/scene6/scene6_jp30.ogg"
jp "Très bien !"

show illaoi_papier
#voice "doublages_jp4/scene6/scene6_illaoi9.ogg"
illaoi "Signe ce papier."

#voice "doublages_jp4/scene6/scene6_jp31.ogg"
jp "Comment se fait-il qu'il ne soit pas trempé ?"

#voice "doublages_jp4/scene6/scene6_illaoi10.ogg"
illaoi "SIGNE CE FOUTU PAPIER !"#Elle sort les tentacules

"Jean Plank s'empressa de signer le contrat qui faisait d'Illafloy la détentrice légale de son honneur."

#voice "doublages_jp4/scene6/scene6_jp32.ogg"
jp "Et voilà !"

#voice "doublages_jp4/scene6/scene6_illaoi11.ogg"
illaoi "Tu es un idiot."

#voice "doublages_jp4/scene6/scene6_illaoi12.ogg"
illaoi "Au revoir, Jean Plank."

#voice "doublages_jp4/scene6/scene6_jp33.ogg"
jp "Au revoir, Illafloy..."

"Répondit-il une larme à l'oeil, assistant au spectacle de son seul amour qui disparaissait dans l'abîme, emportant au fond de l'océan l'honneur de notre bon capitaine."



#Scene 6
show jp_derive_marchand
play music "music/vayne_derive.ogg"
$renpy.sound.play("sound/sound_mouettes.ogg", loop=True)
"Voilà maintenant 3 jours que Jean Plank dérivait sur son radeau de fortune."
"Il n'était pas inquiet bien qu'il commençait à avoir un peu soif."

show jp_derive_bateau
"Le destin ayant notre capitaine à la bonne (ou la mort refusant de voir sa sale gueule), il n'eût plus à attendre très longtemps avant qu'un navire marchand ne croise son chemin."

#voice "doublages_jp4/scene7/scene7_marchand1.ogg"
marchand "Un homme à la mer !"

"Jean Plank se saisit de l'échelle qui lui était gracieusement tendue et monta sur le pont."

show marchands
$renpy.sound.play("sound/sound_mer.ogg", loop=True)
#voice "doublages_jp4/scene7/scene7_capitaine1.ogg"
capitaine_des_marchands "Eh bien, mon brave ! Vous avez eu une sacrée chance."

#voice "doublages_jp4/scene7/scene7_jp1.ogg"
jp "Ah ah."

#voice "doublages_jp4/scene7/scene7_marchand2.ogg"
marchand "Capitaine ?"

#voice "doublages_jp4/scene7/scene7_capitaine2.ogg"
capitaine_des_marchands  "Oui ?"

"Comment ça \"oui\" ?"

show capitrane
"Jean Plank empoigna le col du scélérat qui avait osé répondre à sa place."

play music "music/fight_marchands.ogg"
#voice "doublages_jp4/scene7/scene7_jp2.ogg"
jp "C'EST MOI LE CAPITRANE !"

#voice "doublages_jp4/scene7/scene7_marchand3.ogg"
marchand "Mais lâchez-le, pauvre abruti !"

show jp_baffe_marchand
jp "Personne ne me donne d'ordre !" #(bruit de baffe)

#bruit de sabre qu'on sort
show marchand_epee
#voice "doublages_jp4/scene7/scene7_marchand4.ogg"
marchand2 "Bon tu l'auras voulu, tocard !"

#bruit de pistolet 
show jp_tire_marchand
#voice "doublages_jp4/scene7/scene7_marchand5.ogg"
marchand "Argh il m'a tiré dessus le con !"

show jp_a_la_mer
#voice "doublages_jp4/scene7/scene7_marchand6.ogg"
capitaine_des_marchands "Foutez-le par dessus bord !"

play music "music/vayne_derive.ogg"
scene jp_derive
$renpy.sound.play("sound/sound_mouettes.ogg", loop=True)
"Voilà maintenant 4 jours que Jean Plank dérivait en faisant la planche."
"Les yeux fermés, il songeait à l'océan avec mélancolie."
"Avec les yeux ouverts, il y songeait aussi pas mal mais comme l'eau salée lui brûlait les yeux, mieux valait les garder fermés."

#voice "doublages_jp4/scene7/scene7_wayne1.ogg"
inconnu "Hep ?"

"L'océan faisait toute sorte de bruits, mais celui là était quand même très inhabituel."

#voice "doublages_jp4/scene7/scene7_wayne2.ogg"
inconnu "T'es mort ?"

show vayne_derive
$renpy.sound.play("sound/sound_port.ogg", loop=True)
"Jean Plank ouvrit les yeux."

#voice "doublages_jp4/scene7/scene7_wayne3.ogg"
inconnu "Ca fait deux jours que je te vois barboter. Qu'est-ce que tu fous ?"

"D'un rapide coup d'oeil, Jean Plank analysa la situation."

#voice "doublages_jp4/scene7/scene7_jp3.ogg"
jp "Je méditais !"

"C'était totalement con comme réponse, mais admettre qu'il avait perdu deux jours dans les docks ne lui aurait pas donné l'air plus malin."

show jp_sort_eau
"Avec quelques difficultés, il parvint à sortir de l'eau."
"Il n'était pas très en forme mais il était arrivé à bon port."
"Avec ses yeux vitreux, son teint blafard, sa dégaine titubante et son odeur de chien mouillé, notre bon vieux capitaine avait rarement été si misérable."
"Mais tel un vieux chien qu'on refuse d'euthanasier, il avait toujours un certain charme."

label choix_verre:
scene jp_sort_eau
#voice "doublages_jp4/scene7/scene7_wayne4.ogg"
inconnu "Allez viens, suis moi. Je t'offre un verre."

menu:
    "S'exécuter":
        "Ravi qu'on lui paye son alcool, Jean Plank lui emboîta le pas."
    "S'exécuter":
        #sound "sound/jp_cri.ogg"
        show jp_execution1
        "Jean Plank commença alors à hurler."
        "Il se mit ensuite à genoux."
        show jp_execution2
        #sound "sound/jpexecution.ogg"
        "Puis enfonça son sabre dans sa bedaine, toujours en continuant de beugler comme un âne."
        play music "music/music_mort.ogg"
        show ecran_game_over
        stop sound
        window hide
        pause
        hide ecran_game_over
        show jp_sort_eau
        play music "music/vayne_derive.ogg"
        $renpy.sound.play("sound/sound_port.ogg", loop=True)
        jump choix_verre


scene vayne_bar

stop music
play alder "music/young_edwin.ogg"
$renpy.sound.play("sound/sound_tavernsound.ogg", loop=True)
"Une fois nos deux protagonistes enfin arrivés au bar, l'inconnue ayant sorti Jean Plank de sa méditation en révéla un peu plus sur ses intentions."
"Elle s'appelait Wayne et était une chasseuse de primes à la recherche d'un certain \"Patrick Balkany\"."

show vayne_nego1
#voice "doublages_jp4/scene7/scene7_jp4.ogg"
jp "Escorte-moi jusqu'à chez moi et je te conduirai à l'homme que tu cherches."
"Jean Plank n'avait pas besoin d'escorte mais il aimait beaucoup négocier."

#voice "doublages_jp4/scene7/scene7_wayne5.ogg"
wayne "OK."

show vayne_nego2
"Quoi, comment ça \"OK\" ? Une négociation aussi simple n'avait rien d'intéressant."

#voice "doublages_jp4/scene7/scene7_jp5.ogg"
jp "Et en plus, tu payeras ma nuit à l'auberge !"

#voice "doublages_jp4/scene7/scene7_wayne6.ogg"
wayne "OK."

show vayne_nego3
"Mais bordel !"

#voice "doublages_jp4/scene7/scene7_jp6.ogg"
jp "Et aussi, tu vas coucher avec moi !"

#voice "doublages_jp4/scene7/scene7_wayne7.ogg"
wayne "OK."

stop alder
if censure == 1:
    scene jp_vayne_galipette_censored
else:
    scene jp_vayne_galipette
stop sound
play sound "sound/sound_bruit_cul.ogg"
#voice "doublages_jp4/scene7/scene7_jp7.ogg"
jp "Et merde !"

scene vayne_deception
stop sound
play music "music/vayne_deception.ogg"
"Jean Plank était vraiment très très très déçu."
"Et un peu dans la merde aussi, parce qu'il n'avait absolument aucune idée de qui était ce \"Patrick Balkany\"."
"Le lendemain, escorté par son escorte, il se rendit là où tout avait commencé."


show jp_vayne_chemin
"Sur le chemin, Jean essayait de penser à un plan pour debusquer Patrick Balkany."
show culdevayne
"Mais pour une quelconque raison, il n'arrivait pas à se concentrer."

scene ruinesjp4
play music "music/ruines_jp4.ogg"
#$renpy.sound.play("sound/sound_ruines.ogg", loop=True)
"Il arriva donc là où tout avait commencé, sans l'ombre d'une solution."
"Le paysage était toujours aussi ravagé."
"Absolument rien n'avait repoussé depuis son départ. Il y régnait une atmosphère oppressante, comme si une étrange magie était à l'oeuvre."
"Jean Plank était à la recherche d'un indice."

show jp_indice
#voice "doublages_jp4/scene7/scene7_wayne8.ogg"
wayne "Tu cherches quoi exactement ?"

#voice "doublages_jp4/scene7/scene7_jp8.ogg"
jp "UN INDICE !"

"Il fit le tour de ce qu'il restait de son domaine mais, rien n'apparut à notre héros."
"Les indices avaient probablement tous disparu dans les flammes."
"Il se retrouvait véritablement bloqué. Il essaya alors de se souvenir de ce que lui avait prédit Lee."
"Malheureusement, il n'avait pas dit grand chose."

#voice "doublages_jp4/scene7/scene7_jp9.ogg"
jp "Bon, je pense que je n'ai plus le choix..."
"Se résigna Jean Plank."

#voice "doublages_jp4/scene7/scene7_jp10.ogg"
jp "Je vais devoir apprendre à lire."

play music "music/zilean.ogg"
show zilean_ehtoi
#voice "doublages_jp4/scene7/scene7_patrick1.ogg"
#patrick "Eh toi là bas"
window hide
pause

"Une espèce de vieux débris venait de sortir Jean Plank de son intense réflexion."

show zilean_bougepas
#voice "doublages_jp4/scene7/scene7_patrick2.ogg"
#patrick "Bouge pas !"
window hide
pause

show zilean_boite
"Il boîtait de manière rapide vers nos deux protagonistes, un air sérieux sur son visage ridé."

show zilean_tonpere_blank
"Enfin arrivé au niveau de Jean Plank, il l'empoigna pas le col et colla son front (ridé) contre celui du capitaine pour le regarder droit dans les yeux."

show zilean_toi
#voice "doublages_jp4/scene7/scene7_patrick3.ogg"
#patrick "Toi !"
window hide
pause

show zilean_tonpere
#voice "doublages_jp4/scene7/scene7_patrick4.ogg"
#patrick "Espece de minable, ton père te détestait."
window hide
pause

hide zilean_tonpere
hide zilean_toi

show flashback_zilean
stop sound
$renpy.sound.set_volume(0.00, delay=0, channel='music')
play sound "sound/flashback.ogg"
play alder "music/melancolie.ogg"
"Jean Plank se replongea alors dans ses souvenirs."

show jp_malle
#voice "doublages_jp4/scene7/scene7_perejp1.ogg"
pere_jp "Et t'as pas intérêt à griffer l'intérieur ou je te jure que je t'étripe !"
#Re zoom sur les yeux du capitaine de fin de flash back

hide jp_malle
"Aucun doute, il avait raison."

$renpy.sound.set_volume(1.00, delay=0, channel='music')
$renpy.sound.set_volume(1.00, delay=0, channel='sound')
hide flashback_zilean
stop alder
"Jean Plank tourna alors la tête vers son acolyte."

show zilean_vayne
#voice "doublages_jp4/scene7/scene7_jp11.ogg"
#jp "Wayne..."
window hide
pause

show zilean_patrick
#voice "doublages_jp4/scene7/scene7_jp12.ogg"
#patrick "C'est lui Patrick Balkany."
window hide
pause

show zilean_connard
#voice "doublages_jp4/scene7/scene7_patrick5.ogg"
#patrick "Héé connard ! Comment tu connais mon nom ?"
window hide
pause

show zilean_collabos
#voice "doublages_jp4/scene7/scene7_patrick6.ogg"
#patrick "Lâche moi toi, lâche moi ! Bande de collabos !"
window hide
pause



#scene 8



scene bateau_vayne 
play music "music/voyage_vayne.ogg"
$renpy.sound.play("sound/sound_mouettes.ogg", loop=True)
"Quelques jours avaient passé, Jean Plank avait rapidement retrouvé un navire et un équipage grâce à la notoriété de sa nouvelle compagne."

show voyage_vayne
"Devant tous deux se rendre sur le continent, ils avaient décidé de faire un bout de chemin ensemble."
"Le voyage se passait étonnamment bien et les deux compagnons d'infortune voguaient dans le soleil couchant."
"Seul le vieux Patrick Balkany causait quelques torts."

$renpy.sound.play("sound/sound_mer.ogg", loop=True)
show patrick_insulte
#voice "doublages_jp4/scene8/scene8_patrick1.ogg"
patrick "De mon temps, les noirs sur les bateaux, ils portaient des chaînes !"

"Il s'était échappé 3 fois, avait mordu deux marins et insulté au moins la moitié de la totalité d'entre eux."
"Bref, les choses allaient bon train."

show longue_vue
#voice "doublages_jp4/scene8/scene8_marin1.ogg"
marin "Capitaine ! Navire en vue !"

#voice "doublages_jp4/scene8/scene8_patrick2.ogg"
patrick "L'écoutez pas, il ment, il est avec l'ennemi !"

#voice "doublages_jp4/scene8/scene8_patrick3.ogg"
patrick "C'est lui qui m'a balancé !"

show longue_vue_vayne
#voice "doublages_jp4/scene8/scene8_wayne1.ogg"
wayne "Hé toi ! Va donc m'enfermer ça dans la cale."

#voice "doublages_jp4/scene8/scene8_marin2.ogg"
marin2 "Très bien, madame."

show patrick_cale
#voice "doublages_jp4/scene8/scene8_patrick4.ogg"
patrick "Hééé touche à tes morts, toi ! Je vous enterrai tous !"

#voice "doublages_jp4/scene8/scene8_marin3.ogg"
marin2 "Mais il mord, le con ! Viens là, toi !"

#voice "doublages_jp4/scene8/scene8_patrick5.ogg"
patrick "JE VOUS ENTERRAI TOUS ! JE VOUS ENTERRAI TOUS !" #bruit de porte qui claque

show longue_vue_vayne_nopatrick
#voice "doublages_jp4/scene8/scene8_marin4.ogg"
marin "Capitaine ! C'est un navire pirate !"

show longue_vue_vayne_jp
#voice "doublages_jp4/scene8/scene8_jp1.ogg"
jp "Pirate ?"

#voice "doublages_jp4/scene8/scene8_jp2.ogg"
jp "Et alors ? Nous aussi, non ?"

show longue_vue_vayne_surprise
#voice "doublages_jp4/scene8/scene8_wayne1.ogg"
wayne "Comment ça ?"

#montage Jp avec la gueule d'Onisuka
window hide
pause

"Jean Plank venait de se rendre compte qu'il avait peut-être omis ce détail quand il s'était présenté à la chasseuse de primes."

play music "music/abordage_kata.ogg"

show jp_choc_pirates
#voice "doublages_jp4/scene8/scene8_jp3.ogg"
jp "Ahhh, des pirates ! Fuyons ! Fuyons !"
#bruit de porte qui souvre

show patrick_lache
#voice "doublages_jp4/scene8/scene8_patrick6.ogg"
patrick "Hé, toi ! Non seulement t'es moche mais en plus t'es lâche ! De mon temps on savait se battre !"

"Patrick Balkany avait visiblement échappé à son détenteur."

#voice "doublages_jp4/scene8/scene8_patrick7.ogg"
patrick "Bon, elles sont planquées où les armes sur ce rafiot ?"

"Dit-il en s'élançant dans la cale, bien determiné à trouver une solution définitive au problème."

show vayne_poursuite
#voice "doublages_jp4/scene8/scene8_wayne2.ogg"
wayne "On reparlera de tout ça, Jean !"

"Dit-elle en s'élançant à la poursuite de l'ancien maire de Levallois-Perret."

show jp_meduse
"Jean Plank, un peu médusé, se massa entre les sourcils."
"Ce \"Patrick Balkany\" n'était pas vraiment un cadeau."

#voice "doublages_jp4/scene8/scene8_jp4.ogg"
jp "Bon, virez de bord, on leur échappera sous le vent."

"Malheureusement, la manoeuvre était tentée un peu trop tard pour être un succès."

show abordage
"Dans la plus grande panique, ils subirent un abordage."
"Le combat fit rage mais les marins étaient désorganisés. La défaite était inéluctabe."

show jp_epee_fourreau
"Jean Plank s'était débattu comme un lion pendant plusieurs minutes mais il n'avait malheureusement pas réussi à sortir son épée rouillée du fourreau."
"De toute évidence celle ci n'avais pas apprécié son récent séjour dans l'eau de mer."
"Notre capitaine fut donc forcé de se rendre sans combattre."

show equipage_surrend
"Les pirates rassemblèrent tout l'équipage, y compris Wayne, au centre du navire de Jean Plank."
"Seul demeurait introuvable ce bon vieux Patrick Balkany."

show kata
"Soudain, sublimée par les flammes qu'elle avait dans le dos, apparut sur le pont une femme à la chevelure rougeoyante."

show kata2
#voice "doublages_jp4/scene8/scene8_kata1.ogg"
katarina "Qui commande ici ?"

"Wayne allait se dénoncer quelque peu à contrecoeur lorsqu'elle fût interrompue par un cri."

#voice "doublages_jp4/scene8/scene8_jp5.ogg"
jp "C'est moi le capitrane !"

"Venait de hurler Jean Plank, bien décidé à rendre culte cette nouvelle réplique."
"Saisissant cette occasion inespérée, Wayne décida de garder le silence pour voir comment Jean Plank allait être exécuté."
"Une voix étrangement familière se fit alors entendre."

play music "music/jinx_kata.ogg"
show jinx_kata
#voice "doublages_jp4/scene8/scene8_jinx1.ogg"
jinx "Jean Plank ?"

#voice "doublages_jp4/scene8/scene8_jp6.ogg"
jp "Jinx ?!"

show jinx_kata2
#voice "doublages_jp4/scene8/scene8_jinx2.ogg"
jinx "Comme on se retrouve !"

#voice "doublages_jp4/scene8/scene8_jp7.ogg"
jp "Heu... Ouais, grave !"

"Jean Plank était un peu perdu, qu'est ce que Jinx foutait là ?"

show jinx_kata3
#voice "doublages_jp4/scene8/scene8_kata2.ogg"
katarina "Tu le connais ?"

#voice "doublages_jp4/scene8/scene8_jinx3.ogg"
jinx "Ouais, c'est Jean Plank. Il est totalement con mais il est marrant !"


"Jean Plank était content : Jinx le trouvait marrant et il aimait bien Jinx."
"De plus, rares étaient les individus qui soulignaient cette caractéristique pourtant évidente de la personnalité du capitaine."

#voice "doublages_jp4/scene8/scene8_jp8.ogg"
jp "C'est qui elle ?"

#voice "doublages_jp4/scene8/scene8_jinx4.ogg"
jinx "Oh, on s'est rencontré dans le désert deux jours après que je t'ai perdu à Shurima."

#voice "doublages_jp4/scene8/scene8_jinx5.ogg"
jinx "J'étais totalement déshydratée et je me suis dit que j'allais crever."

#voice "doublages_jp4/scene8/scene8_jinx6.ogg"
jinx "J'ai donc allumé un des tonneaux de poudre que je t'avais piqué, histoire de partir en beauté !"

#voice "doublages_jp4/scene8/scene8_jinx7.ogg"
jinx "Quand je me suis réveillée, Katarina ci-présente était là..."

show jinx_marin
#voice "doublages_jp4/scene8/scene8_pirate1.ogg"
pirate "Capitaine, il y'a quelque chose de suspect dans la cale."

#voice "doublages_jp4/scene8/scene8_jinx8.ogg"
jinx "Tu viens de me couper la parole là ?!"

#voice "doublages_jp4/scene8/scene8_pirate2.ogg"
pirate "Heu..."

show jinx_marin2
"Jinx se saisit alors d'une barre de fer qui traînait là et commença à corriger le malheureux membre d'équipage."

#voice "doublages_jp4/scene8/scene8_jinx9.ogg"
$ renpy.pause(0.5)
show jinx_marin3 #Replique avec des gros bruit de bare de fer
$ renpy.pause(0.5)
show jinx_marin4
$ renpy.pause(0.5)
show jinx_marin5
$ renpy.pause(0.5)
show jinx_marin6
$ renpy.pause(0.5)
show jinx_marin7
$ renpy.pause(0.5)
show jinx_marin8
$ renpy.pause(0.5)
show jinx_marin9
pause

show jp_kata
#voice "doublages_jp4/scene8/scene8_jp9.ogg"
jp "Fougueuse, hein." #Le jp de vayne_nego_1 en zoomé ou un qui ressemble

#voice "doublages_jp4/scene8/scene8_kata3.ogg"
katarina "Calme toi, Jinx !"

show jp_kata2
"Jinx lâcha immédiatement sa barre de fer et sauta sur Katarina pour lui faire un câlin."

#voice "doublages_jp4/scene8/scene8_jinx10.ogg"
jinx "Oui m'dame !"

play music "music/lee_kata.ogg"
#voice "doublages_jp4/scene8/scene8_lee1.ogg"
inconnu "En voilà une bien étrange personnalité !"

show kata_lee
"La voix venait de l'intérieur de la cale."

#voice "doublages_jp4/scene8/scene8_kata4.ogg"
katarina "Qui es-tu ?"

#voice "doublages_jp4/scene8/scene8_lee2.ogg"
inconnu "Un personnage mystérieux..."

#voice "doublages_jp4/scene8/scene8_kata5.ogg"
katarina "Montre toi ! Ton capitaine s'est rendu."

show kata_lee2
"Apparut alors depuis les escaliers menant à la cale un personnage qui, il faut le dire, n'avait en fait pas grand chose de mystérieux."

#voice "doublages_jp4/scene8/scene8_jp10.ogg"
jp "Ce n'est pas un des miens !"

#voice "doublages_jp4/scene8/scene8_kata6.ogg"
katarina "Un passager clandestin ?"

#voice "doublages_jp4/scene8/scene8_lee3.ogg"
inconnu "Je suis certes un passager, mais sache que je n'appartiens à aucun clan."

#voice "doublages_jp4/scene8/scene8_lee4.ogg"
inconnu "En revanche, pour ce qui est du destin..."

#voice "doublages_jp4/scene8/scene8_kata7.ogg"
katarina "Tu es bien louche, manant."

#voice "doublages_jp4/scene8/scene8_lee5.ogg"
inconnu "Louche ?"

show kata_lee3
#voice "doublages_jp4/scene8/scene8_lee6.ogg"
lee  "EH BIEN NON, JE SUIS AVEUGLE !"

#voice "doublages_jp4/scene8/scene8_jp11.ogg"
jp "Encore toi !?"

#voice "doublages_jp4/scene8/scene8_jp12.ogg"
jp "Mais t'es pas mort, espèce de connard ?"

#voice "doublages_jp4/scene8/scene8_lee7.ogg"
lee "Crois-tu en la réincarnation, petit mimosa ?"

#voice "doublages_jp4/scene8/scene8_jp13.ogg"
jp "Heu, non ?"

#voice "doublages_jp4/scene8/scene8_lee8.ogg"
lee "Et bien, tu devrais !"

show kata_lee4
#voice "doublages_jp4/scene8/scene8_kata8.ogg"
katarina "Encore une de tes connaissances ?"

#voice "doublages_jp4/scene8/scene8_jinx11.ogg"
jinx "Une diseuse de bonne aventure, elle est inoffensive."

show lee_revelations
#voice "doublages_jp4/scene8/scene8_lee9.ogg"
lee "Silence, sac à foutre !"

#voice "doublages_jp4/scene8/scene8_lee10.ogg"
lee "J'ai d'importantes révélations à faire !"

"Bien conscients que les prophéties de cet illuminé étaient le seul moyen de faire avancer ce foutu scénario, aucun des personnages présents ne le jeta à la flotte."

show lee_revelations2
#voice "doublages_jp4/scene8/scene8_lee11.ogg"
lee "Ecoutes-moi bien petit scarabée : Tu as fait fausse route !"

#voice "doublages_jp4/scene8/scene8_jp14.ogg"
jp "Ah."

#voice "doublages_jp4/scene8/scene8_lee12.ogg"
lee "Tu n'as pas suivi le destin que le destin t'avait destiné."

#voice "doublages_jp4/scene8/scene8_jp15.ogg"
jp "Ah bon ?"

#voice "doublages_jp4/scene8/scene8_lee13.ogg"
lee "Mais il est encore temps de rectifier !"

#voice "doublages_jp4/scene8/scene8_lee14.ogg"
lee "Tu dois retrouver ton mal intentionné magicien malodorant malotru !"

#voice "doublages_jp4/scene8/scene8_jp16.ogg"
jp "Quoi ?"

#voice "doublages_jp4/scene8/scene8_lee15.ogg"
lee "Le noir qui fait de la magie !"

#voice "doublages_jp4/scene8/scene8_jp17.ogg"
jp "Lucien ?"

#voice "doublages_jp4/scene8/scene8_lee16.ogg"
lee "Bah oui, t'en connais beaucoup des noirs qui font de la magie toi ?"

"Jean Plank prit un instant de reflexion."
"Non en effet, il n'en connaissait pas d'autre."

#voice "doublages_jp4/scene8/scene8_jp18.ogg"
jp "Pourquoi dois-je le retrouver ?"

#voice "doublages_jp4/scene8/scene8_lee17.ogg"
lee "Parce qu'il est ton destin !"

#voice "doublages_jp4/scene8/scene8_jp19.ogg"
jp "Je ne peux pas en changer ?"

#voice "doublages_jp4/scene8/scene8_lee18.ogg"
lee "C'est mort !"

#voice "doublages_jp4/scene8/scene8_jp20.ogg"
jp "Très bien, tu m'as convaincu."

show lee_revelations3
"Lasse d'entendre ces conneries, Wayne sortit du silence dans lequel elle s'était murée."

#voice "doublages_jp4/scene8/scene8_wayne3.ogg"
wayne "Attends, mais c'est totalement con !"

#voice "doublages_jp4/scene8/scene8_lee19.ogg"
lee "Mmmh, ta gueule ! "

#voice "doublages_jp4/scene8/scene8_lee20.ogg"
lee "Tu ne fais pas partie de son destin ! Tu es un personnage secondaire !"

#voice "doublages_jp4/scene8/scene8_wayne4.ogg"
wayne "Mais je vais te péter la gueule !"

#voice "doublages_jp4/scene8/scene8_lee21.ogg"
lee "Très bien mais ça devra attendre !"

#voice "doublages_jp4/scene8/scene8_wayne5.ogg"
wayne "Oh, et en quel honneur ?"

#voice "doublages_jp4/scene8/scene8_lee22.ogg"
lee "Il y a quelques minutes, j'ai rencontré un certain \"Patrick Balkany\" dans la cale."

#voice "doublages_jp4/scene8/scene8_lee23.ogg"
lee "Personnage fascinant au fabuleux destin."

#voice "doublages_jp4/scene8/scene8_lee24.ogg"
lee "Il cherchait un moyen astucieux et efficace pour quitter le navire."

#voice "doublages_jp4/scene8/scene8_lee25.ogg"
lee "Et a voir le niveau de la mer par rapport à la coque, je pense que la hache que je lui ai donné a été la pierre angulaire de son projet de tunnel sous-marin !"

show lee_revelations4
#voice "doublages_jp4/scene8/scene8_kata9.ogg"
katarina "Quoi ?!"

#voice "doublages_jp4/scene8/scene8_lee26.ogg"
lee "C'était le destin !"

show changement_navire
"La panique gagna alors l'équipage. Tous tentèrent de gagner le navire de Katarina."

show jp_naufrage
"Nombreux y parvinrent mais pas Jean Plank."
"Voyant le capitaine à la mer, Lee n'était pas inquiet."

#voice "doublages_jp4/scene8/scene8_lee27.ogg"
lee "Ne t'inquiète pas ! Tu vogues vers ton destin !"
"Dit-il en lançant un tonneau de sauvetage à Jean Plank."

#voice "doublages_jp4/scene8/scene8_lee28.ogg"
lee "Retrouve ce sombre traître et pète lui la gueule !"

#voice "doublages_jp4/scene8/scene8_jp21.ogg"
jp "Oui !"

#voice "doublages_jp4/scene8/scene8_lee29.ogg"
lee "Et une fois ton affaire finie, retrouve Jinx au pub de DeadChien !"

#voice "doublages_jp4/scene8/scene8_lee30.ogg"
lee "Elle est ta destinée, elle aussi !"


show jp_tonneau_mer1
"Ainsi, notre bon capitaine reprit sa dérive dans l'océan."

show jp_tonneau_mer
"Après quelques heures d'essais infructeux il finit par se rendre compte que s'accrocher au tonneau n'était pas vraiment pratique."

show jp_planche
"Il opta à nouveau pour la technique dejà éprouvée de la planche laissant ainsi la structure de bois qui n'aura donc eu aucune utilité dans l'histoire."
"Fatigué il ferma les yeux, bercé par le doux clapotis des vagues, se laissant ainsi porter par l'océan."
"Etrangement, Jean Plank dériva dans la bonne direction, comme si les prédictions de Lee n'étaient pas simplement les paroles d'un illuminé qu'il faudrait sérieusement songer à interner."

scene iles_obscures
play music "music/iles_obscures.ogg"
$renpy.sound.play("sound/sound_iles_obscures.ogg", loop=True) 
"Quelques temps plus tard, notre héros finit donc par arriver sain et sauf là où tout n'avait pas commencé : les Îles Obscures."

#Scene 9

"Il lui fallait maintenant trouver Lucien."
"Seulement à l'heure actuelle, il était seul et perdu dans cet immense et mystérieux archipel. Il lui fallait clairement un guide. Mais voilà, comment en trouver un dans tout ce bordel ?"
"Se fiant à son instinct et remettant son sort au DESTIN, il s'enfonça d'un pas décidé dans le paysage désolé qui s'offrait à lui."

show creature
"Il marcha longtemps et rencontra d'innombrables créatures, certaines totalement informes et sordides et d'autres, ni informes ni sordides."
"Mais aucune d'elles ne put lui indiquer le chemin vers celui qui lui indiquerait le chemin."

show cabane_urgo
"Après des jours d'errance, il finit par tomber sur un cabanon."
"Perdu au font des bois, la devanture lui paraissait fort familière."

play sound "sound/sound_violent_open_door.ogg"
show urgo_jp4
#voice "doublages_jp4/scene9/scene9_jp1.ogg"
jp "Gibier de potence !"

#voice "doublages_jp4/scene9/scene9_urgo1.ogg"
Urgo "Jean Plank ?! Ca alors, je ne t'ai pas revu depuis ce jour où tu voulais éviter de payer ta dette et où, après m'être fait humilier, casser la gueule et trancher un bras, j'ai consenti à te laisser fuir tel un lâche."

#voice "doublages_jp4/scene9/scene9_jp2.ogg"
jp "Haha , inutile de ressasser le passé, de nombreuses années se sont écoulées depuis cette époque."

#voice "doublages_jp4/scene9/scene9_urgo2.ogg"
Urgo "Mmmh, je ne crois pas, non. Mais du coup, j'imagine que tu ne viens pas pour me rendre mon argent ?"

#Crayon

#voice "doublages_jp4/scene9/scene9_jp3.ogg"
jp "Urgo ?"

#voice "doublages_jp4/scene9/scene9_urgo3.ogg"
Urgo "Oui, Jean Plank ?"
#(jp degeu cotérisation)

#voice "doublages_jp4/scene9/scene9_jp4.ogg"
jp "As-tu déjà vu ce chef d'œuvre ?"

"Subjugué par la beauté de l'art, Urgo décida d'annuler la dette de Jean Plank en guise de remerciement."
"Cet épisode passé, il discutèrent pendant un long moment,  se remémorant tous leur bons souvenirs communs." #(tu peux te lacher sur les sprite de jp qui casse la gueule à Urgo)
"Après avoir bien ri, Jean Plank finit par en arriver aux faits :"

#voice "doublages_jp4/scene9/scene9_jp5.ogg"
jp "Saurais-tu ou est caché ce traître de Lucien ?"

#voice "doublages_jp4/scene9/scene9_urgo4.ogg"
Urgo "Cela me paraît assez évident."

#voice "doublages_jp4/scene9/scene9_jp6.ogg"
jp "Ah oui ? Et où donc, mon vieil ami ?"

#voice "doublages_jp4/scene9/scene9_urgo5.ogg"
Urgo "Sur l'Île des Traîtres, comme tous les traîtres."

"En effet, c'était plutot évident."
"Jean Plank se demanda pourquoi il n'y avait pas lui même pensé."
"Urgo expliqua alors à Jean Plank comment il pourrait rejoindre la fameuse Île des Traîtres."
"Cependant, il le mit en garde : le chemin était périlleux."

#voice "doublages_jp4/scene9/scene9_urgo6.ogg"
Urgo "Jean Plank..."

"Afin de rendre ce passage stylé, les auteurs ont provisoirement décidé de changer la voix d'Urgo."
"Merci de votre compréhension."
#play musique dramatique

#voice "doublages_jp4/scene9/scene9_jp7.ogg"
jp "Oui ?"

#voice "doublages_jp4/scene9/scene9_urgo7.ogg"
Urgo "Approche-toi."

#voice "doublages_jp4/scene9/scene9_urgo8.ogg"
Urgo "As-tu déjà entendu parler du fléau de Thresh ?"

#voice "doublages_jp4/scene9/scene9_jp8.ogg"
jp "Le fléau de Thresh ?"

#voice "doublages_jp4/scene9/scene9_urgo9.ogg"
Urgo "Chuuut, pas si fort."

#voice "doublages_jp4/scene9/scene9_urgo10.ogg"
Urgo "Thresh le moissonneur nocturne."

#voice "doublages_jp4/scene9/scene9_urgo11.ogg"
Urgo "A la base, ce n'était qu'un pauvre connard comme tant d'autres ici, vouant sa vie à faire le mal et semant mort, désolation et injustice dans son sillage." 

#voice "doublages_jp4/scene9/scene9_urgo12.ogg"
Urgo "Cependant, il y a quelques années, il est par hasard tombé sur un terrible pouvoir nommé \"Moisson Noire\"."

#voice "doublages_jp4/scene9/scene9_urgo13.ogg"
Urgo "Un pouvoir noir et malfaisant permettant à quiconque en prend possession de collectionner les âmes. Un tel pouvoir..." 

#voice "doublages_jp4/scene9/scene9_urgo14.ogg"
Urgo "Rapidement le scélérat en est devenu fou. Il s'est mis à parcourir les îles pour arracher l'âme de tous les malheureux qui ont la malchance de se trouver sur son passage." 

#voice "doublages_jp4/scene9/scene9_urgo15.ogg"
Urgo "Il est devenu si puissant que même la Sorcière des Eaux Profondes l'évite désormais."

#voice "doublages_jp4/scene9/scene9_jp9.ogg"
jp "La Sorcière des Eaux Profondes ?"
#retour voix normale

#voice "doublages_jp4/scene9/scene9_urgo16.ogg"
Urgo "Ouaip, elle vit dans les eaux profondes. Un conseil Jean Plank, méfie toi de cette salope."

#voice "doublages_jp4/scene9/scene9_jp10.ogg"
jp "J'en prends note."

scene vex

"Cette discussion terminée, Jean Plank prit une bonne nuit de sommeil avant de repartir le lendemain en direction de la tant recherchée Île des Traîtres."
"La route était longue et notre héros s'appliquait à suivre méticuleusement l'itinéraire que lui avait partagé son ami DE CONFIANCE afin de ne pas s'égarer."
"Après plusieurs heures de hors piste, il finit par arriver au cœur d'une forêt aussi dense qu'inquiétante."
"La faible luminosité et les arbres biscornus entravaient toute visibilité, contribuant à créer une ambiance inquiétante, presque lugubre."
"Chaque bruit suspect qui retentissait derrière les fourrés était systématiquement suivi d'un autre bruit encore plus suspect."
"Alerte, notre dévoué capitaine crût alors entendre ce qui ressemblait à des pleurs."
"Curieux, il se dirigea vers ces étranges sanglots."
"Quelques pas plus tard, il put distinguer à travers les feuillages ce qu'il estima être une fillette recroquevillée sur une racine."
"Jean, dans l'optique de mieux distinguer ses traits, se rapprocha un peu plus en prenant soin de rester camouflé."
"Il la voyait désormais distinctement."
"Il s'agissait, en effet, d'une petite fille roulée en boule, des yeux emplis de larmes enfouis dans ses manches trop grandes."
menu:
    "Aller voir": 
        "Poussé par la curiosité et par son instinct de gentilhomme (j'en vois qui rigolent au fond, mais oui, Jean Plank en a un), notre héros se dirigea vers la fillette."

    "Tel n'est pas mon destin":
        
        #voice "doublages_jp4/scene9/scene10_jp1.ogg"
        jp "J'ai autre chose à faire que de la garde d'enfants !" #de chiards ?
        "Il tourna les talons et, d'un pas décidé, se mangea dans la face une branche qu'il n'avait pas vue."

        #voice "doublages_jp4/scene9/scene10_jp2.ogg"
        jp "Aie !"
        "Y voyant là un signe du DESTIN, Jean Plank changea d'avis."
        "En plus, la fillette l'avait repéré et il n'avait pas envie de passer pour un connard."
        "Aussi étrange que cela puisse paraître, Jean Plank prenait soin de son image."

"Arrivé à sa hauteur, notre héros se rendit compte qu'elle avait vraiment une sale gueule pour une fillette."
"Cette dernière, quant à elle, se rendit compte que Jean Plank avait vraiment une sale gueule tout court."

#voice "doublages_jp4/scene9/scene10_vex1.ogg"
fillette "T'es qui toi ?"

#voice "doublages_jp4/scene9/scene10_jp3.ogg"
jp "Plank. Jean Plank."

#voice "doublages_jp4/scene9/scene10_vex2.ogg"
fillette "Fous le camp, Jean Plank. Va-t'en, laisse-moi tranquille !"
menu:
    "Au revoir !":
        
        #voice "doublages_jp4/scene9/scene10_jp4.ogg"
        jp "Eh bien, au revoir !"

        "Il se retourna, prit une brindille dans l'œil, hurla à la mort en insultant les divinités et la destinée, puis se résolut à continuer la conversation à laquelle il n'avait visiblement pas le droit d'échapper."
        jump vex
    "Qu'est-ce qui t'arrive ?":
        "Jean Plank, rempli d'altruisme, et seulement parce que c'est un gars bien, insista une seconde fois."

label vex:

#voice "doublages_jp4/scene9/scene10_jp4.ogg"
jp "Allez, qu'est-ce qui t'arrive ? Je peux t'aider !"
"La fillette plongea alors son regard larmoyant dans celui de Jean Plank."

#voice "doublages_jp4/scene9/scene10_vex3.ogg"
fillette "C'est vrai ?"
"Elle le fixait avec une telle intensité qu'elle réveilla la fibre paternelle de notre bon capitaine."
"Il en fut lui-même surpris. Sans doute était-ce là le résultat de son contact prolongé avec cette crapule de Jinx."
"Songeant que cette dernière lui manquait, il répondit à la fillette qui s'était timidement rapproché de lui."

#voice "doublages_jp4/scene9/scene10_jp5.ogg"
jp "Mais oui petite... Comment tu t'appelles ?"

#voice "doublages_jp4/scene9/scene10_vex4.ogg"
fillette "Désoh."
"Une sueur algide glissa alors le long de la colonne de notre cher capitaine."

#voice "doublages_jp4/scene9/scene10_jp6.ogg"
jp "Nan, quand même pas..."

#voice "doublages_jp4/scene9/scene10_vex5.ogg"
vex "Désoh Profonde."
"Jean Plank regarda le pistolet qui appuyait désormais sur son imposante bedaine, pensa très très fort au destin qui l'avait conduit à cet endroit précis, et s'exclama très stupéfait et très énervé à la fois :"

#voice "doublages_jp4/scene9/scene10_jp7.ogg"
jp "Mais, mais vraiment ?!"
"Eh oui, vraiment... Jean Plank aurait dû se méfier de cette salope."
"Désoh arborait à présent un sourire radieux."

#voice "doublages_jp4/scene9/scene10_vex6.ogg"
vex "Bon \"Jean\", je vais être sympa. Je vais juste tout te prendre."

#voice "doublages_jp4/scene9/scene10_jp8.ogg"
jp "Comment ça ?"

#voice "doublages_jp4/scene9/scene10_vex7.ogg"
vex "Je veux tout. Ta veste, ton épée, ton flingue, ton futal... Tout !"

#voice "doublages_jp4/scene9/scene10_jp9.ogg"
jp "Mais !"

"Elle ajusta le chien de son pistolet pour signifier à Jean Plank qu'elle s'impatientait."
"À contrecœur, il commença à se déshabiller."
"Il se consolait en se disant que, au moins, il n'avait plus d'honneur à perdre."
"Jean Plank était dorénavant en caleçon."

#voice "doublages_jp4/scene9/scene10_jp10.ogg"
jp "Je peux partir maintenant ?"
"Désoh avait maintenant quelque chose de félin dans le regard, en plus du sourire pervers qui était apparu sur son visage."
"Malgré son mètre vingt de haut, elle était vraiment effrayante."

#voice "doublages_jp4/scene9/scene10_vex8.ogg"
vex "J'ai dit \"tout\" !"
"Jean commença à baisser le vêtement qui camouflait son serpent d'argent quand, soudainement, surgit des branchages un visage familier."

#voice "doublages_jp4/scene9/scene10_jinx1.ogg"
jinx "Saluuuuuuuut !!!"
"Vive comme un écureuil sous caféine, Jinx sortit son double canon et le braqua sur le crâne de Désoh avant même que celle-ci n'ait eu le temps de réagir."

#voice "doublages_jp4/scene9/scene10_jinx2.ogg"
jinx "Alors, Jean ?"

#voice "doublages_jp4/scene9/scene10_jinx3.ogg"
jinx "Comment ça va, vieille branche ?" #Je veux un montage de jinx qui a une branche dans les mains juste pour faire sa vanne de merde
"Le capitaine était bouche bée."
"Désoh, au comble de la frustration, n'eut d'autre choix que de remettre son arme à Jinx."
"Notre capitaine ramassa ses effets personnels sur le sol et, tout en se rhabillant, questionnait Jinx qui s'amusait à prendre des poses complexes tout en gardant Désoh en joue."
"Cette dernière commençait à comprendre qu'elle n'avait malheureusement pas vraiment une gueule de protagoniste."  

#voice "doublages_jp4/scene9/scene10_jp11.ogg"
jp "Qu'est ce que tu fais là ?"

#voice "doublages_jp4/scene9/scene10_jinx4.ogg"
jinx "Avec Kata on a eu une grosse dispute et j'ai préféré partir."
menu:
    "Voir ce qui s'est réellement passé":
        "Très bien, voici pour toi petit curieux :"
        #flashback
        
        $renpy.sound.set_volume(0.00, delay=0, channel='music')
        play sound "sound/flashback.ogg"
        play alder "music/melancolie.ogg"
        scene jinx_cacahouete
        #voice "doublages_jp4/scene9/scene10_jinx5.ogg"
        jinx "Kata ?"
        
        #voice "doublages_jp4/scene9/scene10_kata1.ogg"
        katarina "Oui, mon cœur ?"
        
        #voice "doublages_jp4/scene9/scene10_jinx6.ogg"
        jinx "C'est toi qui as fini mes cacahouètes ?"
        
        #voice "doublages_jp4/scene9/scene10_kata2.ogg"
        katarina "Oui, pourquoi ?"
        
        show jinx_colere_kata
        #voice "doublages_jp4/scene9/scene10_jinx7.ogg"
        jinx "Mais je te démolis, grosse pute !"

        "Je pense qu'il est inutile d'avoir toute la dispute."
        "Voici cependant le détail que Jinx a omis sur son dénouement."
        #scene de lee sin qui attache jinx sur son missile
        
        #voice "doublages_jp4/scene9/scene10_jinx8.ogg"
        jinx "Lâchez-moi ! Lâchez-moi !"
        
        #voice "doublages_jp4/scene9/scene10_kata3.ogg"
        katarina "Envoyez ça loin de moi, je ne veux plus la voir."
        
        #voice "doublages_jp4/scene9/scene10_lee1.ogg"
        lee "Je vais surtout l'envoyer vers son destin !"
        
        #voice "doublages_jp4/scene9/scene10_kata4.ogg"
        katarina "Mais t'es encore là, toi ?!"
        
        #voice "doublages_jp4/scene9/scene10_lee2.ogg"
        lee "Destiiiin !"

        $renpy.sound.set_volume(1.00, delay=0, channel='music')
        $renpy.sound.set_volume(1.00, delay=0, channel='sound')
        stop alder

    "On s'en balance":
        jump no_flashback

label no_flashback:
#voice "doublages_jp4/scene9/scene10_jp12.ogg"
jp "Préféré partir ?"

#voice "doublages_jp4/scene9/scene10_jinx9.ogg"
jinx "Ouaip !"

#voice "doublages_jp4/scene9/scene10_jp13.ogg"
jp "Fort bien, puisque tu es là, tu vas pouvoir m'aider à me venger !"

#voice "doublages_jp4/scene9/scene10_jp14.ogg"
jp "En avant !"

#bruit de coup de feu

#voice "doublages_jp4/scene9/scene10_jinx10.ogg"
jinx "Ouais, grave !"
"Très content d'avoir récupéré son acolyte préférée et sachant à quel point celle-ci lui avait sauvé la mise, Jean Plank repris alors son chemin vers l'Île des Traîtres."

#scene 11

scene ile_des_traitres
play music "music/ile_traitres.ogg"
$renpy.sound.play("sound/sound_village.ogg", loop=True)
"Après quelques péripéties qui, bien qu'elles aient renforcé l'amitié entre Jinx et notre bon capitaine, seraient trop longues à raconter, nos deux protagonistes arrivèrent sur l'Île des Traîtres."
"Nos deux compères, qui s'attendaient à tomber sur un trou à rats malfamé, furent fort surpris de constater à quel point ils s'étaient trompés."

show rues_ile_traitres
"Très loin du repaire de pouilleux décérébrés attendu, l'île toute entière respirait la propreté, la richesse, l'opulence et l'opportunisme."
"Visiblement, la roublardise, le crime et le mensonge étaient des activités lucratives."
"Jean Plank se demanda donc naturellement pourquoi lui n'était pas encore riche."
"Il s'agissait désormais de trouver la maison de Lucien."

show simon_traitre
"Tout d'un coup Jean Plank sentit une main sur son épaule."
"Il se retourna brusquement."

show simon_traitre2
play music "music/simon2.ogg"
#voice "doublages_jp4/scene8/scene11_simon1.ogg"
simon2 "Salutations à toi, jeune opportuniste !"
"\"Jeune\"..."
"Le compliment alla droit au coeur de Jean Plank, dont le visage s'illumina d'un sourire accentuant toutes les rides de son faciès."
"Néanmoins, quelque chose l'interpella sur le visage de son interlocuteur."

#voice "doublages_jp4/scene8/scene11_jp1.ogg"
jp "Ta tête me dit quelque chose, t'aurais-je déjà tabassé ?"

#voice "doublages_jp4/scene8/scene11_simon2.ogg"
simon2 "Hmm c'est peu probable. Je pense que je me souviendrais de... de ça."
"Jean Plank n'arrivait pas à se souvenir."

show jinx_simon
#voice "doublages_jp4/scene8/scene11_jinx1.ogg"
jinx "Shurima ! T'es le mec qui vendait des chameaux !"

hide jinx_simon
#voice "doublages_jp4/scene8/scene11_simon3.ogg"
simon2 "Oh, vous avez dû tomber sur mon frère Arthurus de Mile. Il a pas mal traîné sa croupe par là-bas. Il devait faire fortune avec quelque bassesse pyramidale."

"Jean Plank réalisa alors qu'en fait il s'en fichait pas mal, et qu'il était temps d'aller droit au but !"

#voice "doublages_jp4/scene8/scene11_jp2.ogg"
jp "Je cherche la résidence de Lucien !"

#voice "doublages_jp4/scene8/scene11_simon4.ogg"
simon2 "Lucien qui ?"

#voice "doublages_jp4/scene8/scene11_jinx2.ogg"
jinx "Le magicien !"

#voice "doublages_jp4/scene8/scene11_simon5.ogg"
simon2 "Vous avez vraiment de la chance, je dispose de cette information."

#voice "doublages_jp4/scene8/scene11_simon6.ogg"
simon2 "Moyennant bon prix, je peux vous la donner."

#voice "doublages_jp4/scene8/scene11_jp3.ogg"
jp "Moyennant un bon prix, hein..."

show jinx_suspicious
"Jinx murmura alors à l'oreille de Jean Plank."

#voice "doublages_jp4/scene8/scene11_jinx3.ogg"
jinx "On est sur l'Île des Traîtres, tu penses qu'on peut lui faire confiance ?"

hide jinx_suspicious
#voice "doublages_jp4/scene8/scene11_simon7.ogg"
simon2 "Je t'ai entendu fillette. Si cela peut te rassurer, sache que je suis un traître à la traîtrise."

#voice "doublages_jp4/scene8/scene11_jinx4.ogg"
jinx "Donc tu es honnête ?"

#voice "doublages_jp4/scene8/scene11_simon8.ogg"
simon2 "Totalement et universellement !" 

"C'était évident qu'il mentait."
"Enfin pour l'instant..."

#voice "doublages_jp4/scene8/scene11_jp4.ogg"
jp "Très bien, tu m'as convaincu !"

#voice "doublages_jp4/scene8/scene11_simon9.ogg"
simon2 "Que penses-tu d'une pièce d'or ?"

#voice "doublages_jp4/scene8/scene11_simon10.ogg"
simon2 "Enfin le premier mois. Ensuite c'est multiplié par deux toutes les deux semaines, mais il est possible de payer uniquement tous les 3 mois si ça t'arrange."

#voice "doublages_jp4/scene8/scene11_jp5.ogg"
jp "Hmm..."

#voice "doublages_jp4/scene8/scene11_simon11.ogg"
simon2 "Et surtout, je te fais une promotion sur toutes les prochaines informations de ton choix parmi une sélection !"

#voice "doublages_jp4/scene8/scene11_jp6.ogg"
jp "Alléchant, en effet..."

show jinx_suspicious_jp_dodge
"Jinx se rapprocha à nouveau pour murmurer à l'oreille de Jean Plank mais, vif comme une huître, celui-ci esquiva."

#voice "doublages_jp4/scene8/scene11_jp7.ogg"
jp "Haha !"

show jinx_colere
"Enervée, Jinx se saisit de la barbe de Jean Plank et tira dessus afin de ramener l'hideux faciès du capitaine à la hauteur de ses yeux."

jinx "..."

"Elle n'avait pas trouvé d'insulte mais Jean Plank avait tout de même compris."
"Aussi s'excusa-t-il un peu misérablement mais d'une manière qui lui permit de conserver sa dignité."

hide jinx_colere
hide jinx_suspicious_jp_dodge
show jinx_suspicious
"La pression retomba."

#voice "doublages_jp4/scene8/scene11_jinx5.ogg"
jinx "C'est vraiment une super offre mais on a plus une thune !"

#voice "doublages_jp4/scene8/scene11_jp8.ogg"
jp "Comment ça ? Et le coffre qu'on a volé l'autre jour ?"

#voice "doublages_jp4/scene8/scene11_jinx6.ogg"
jinx "Je l'ai troqué contre de l'opium !"

"Jean Plank allait râler mais il se rendit compte qu'il aurait probablement fait la même chose."

#voice "doublages_jp4/scene8/scene11_jp9.ogg"
jp "Comment on fait ?"

#voice "doublages_jp4/scene8/scene11_jinx7.ogg"
jinx "Je sais pas... On le savatte ?"
hide jinx_suspicious

show simon_contrat
#voice "doublages_jp4/scene8/scene11_simon12.ogg"
simon2 "Allons, inutile d'en arriver à de telles extrémités."

#voice "doublages_jp4/scene8/scene11_simon13.ogg"
simon2 "Il se trouve que je suis aussi prêteur sur gage et -quelle coïnçidence folle !- que j'ai sur moi les documents nécessaires."

#voice "doublages_jp4/scene8/scene11_jp10.ogg"
jp "Ah ?"

show simon_contrat1
#voice "doublages_jp4/scene8/scene11_simon14.ogg"
simon2 "Tenez, ceci est le contrat et ça c'est une déclaration sur l'honneur. Vous signez ici, puis ici."

"Empressé de conclure cette bonne affaire, Jean Plank se saisit du contrat et signa à l'aide d'une croix."

show simon_contrat2
"Il donna le document au bonimenteur qui lui tendit alors une superbe déclaration sur l'honneur."

show simon_contrat3
"Mais, alors que le capitaine tentait de prendre le parchemin, sa main s'arrêta net."
"Le ciel s'assombrit, il ne pouvait toucher le tant convoité papier."

show simon_contrat4
"Jean contracta tous les muscles de son corps mais rien ni faisait."

show simon_contrat5
stop sound
play music "music/contrat_illaoi.ogg"
"Subitement, les yeux du futé vendeur devinrent blancs."
"Une forme fantômatique enveloppa alors son corps."
"Un vent de tempête commença à souffler sur notre héros."
"Alors qu'elle grossissait à vue d'oeil, l'aura qui s'accumulait autour du vendeur prit les traits d'un personnage bien connu du capitaine."

show illaoi_contrat
#voice "doublages_jp4/scene8/scene11_illaoi1.ogg"
illaoi_version_esprit "Tu es un idiot, Jean Plank !"


jp "..."

play music "music/desespoir.ogg"
show jp_abattu
"Réalisant qu'il ne pourrait jamais souscrire à cette super offre, notre capitaine totalement déprimé tomba à genoux sur le sol."
"Le spectre disparut et le ciel reprit ses couleur ordinaires."
"Seul demeurait au sol notre triste capitaine."

show jp_abattu1
"Pleine de compassion, jinx lui posa alors une main sur l'épaule."

#voice "doublages_jp4/scene8/scene11_jinx8.ogg"
jinx "Jean..."

#voice "doublages_jp4/scene8/scene11_jinx9.ogg"
jinx "Dis-toi que les fleurs poussent mieux dans la merde."

show jp_espoir
play music "music/espoir.ogg"
"Jean Plank se releva et fixa son regard dans les nuages."
"Il prit une profonde inspiration, réalisant le sens profond des paroles de son acolyte."
"D'un geste du bras, il essuya ses larmes d'homme."

show jp_espoir_jinx
"Reconnaissant, il adressa ensuite un regard à Jinx."

#voice "doublages_jp4/scene8/scene11_jp11.ogg"
jp "Merci petite."

#voice "doublages_jp4/scene8/scene11_jinx10.ogg"
jinx "Seruvisu !"
"Ensuite, uniquement parce qu'ils n'avaient pas d'autre choix, ils torturèrent le marchand afin d'obtenir la position de la demeure de Lucien."
"Jean Plank était quand même un peu triste, il aurait bien voulu être correct avec ce noble vendeur."














































"Deux jour plus tard alors qu'il marchait tranquillement après avoir tabassé deux mendiants"
"Jean Plank fit la connaissance du tant redouter Thresh. Il était tel que l'avait décrit Urgo." 
"Grand, froid, un sourire machiavélique ce decinait sur ce qu'il restait de son visage rongé par les ombres."
"Une aura malsaine ce dessinait autour de lui. Visible à l'oeil nu, elle permettait instinctivement de se rendre compte du nombre de personne qui était tombé au main de ce monstre." 
#(Je veux une icone de dark harvest à avec genre 900 stacks).
menu:
    "Sortir son poignard":
        "N'écoutant pas les sages conseil d'Urgo, Jean Plank sortie son poignard"
        "Prendre la fuite, et puis quoi encore ? Jean Plank n'était pas un lache."
        thresh "Inutile, tu n'est pas de taille."
        menu :
            "faire une roulade trop tot":
                "C'était presque pixel mais Jean Plank rata son esquive."
                "Alors qu'il se relevait peniblement de sa roulade digne d'un hero de dark soul, un grapin alla se planter dans sa poitrine."

            "faire une roulade trop tard":
                "C'était presque piwel mais Jean Plank rata son esquive avant même de la commencer."
                "Alors qu'il se préparait à réaliser une roulade digne d'un hero de dark soul, un grapin alla se planter dans sa poitrine."
                menu:
                    "Manger une orange pour se libérer":
                        "Il n'y avait qu'une solution, manger une orange !"
                        "Sous le regard un peu confu de tresh, Jean Plank sorti une orange de sa veste et la pela avec diffuculté avant de la manger goulument."
                        "Pas de chance, son stratagème n'avait pas fonctionné, mais désormais il avait un peu moins faim"
    "Prendre la fuite":
        "N'écoutant que les sages conseil d'Urgo, Jean Plank prit la fuite"
        "Sortir son poignar, et puis quoi encore ? Jean Plank n'était pas un preux"
        "Il ne parcourut  pas deux mètre avant de voir un grapin lui transpercer le ventre."
        menu :
            "Hurler merde avec nonchalance":
                jp "merde"
            "Paniquer" :
                "Jean Plank paniqua, mais celà ne changea pas grand chose"

"Il  n'y avait pas de sang. Pourtant Jean plnak ne pouvais ce mouvoir"
"Toute à coup une  sensation affreuse parcourut son corp"
"Celle de son ame qui se faisait extraire hors de son envelopppe charnelle"
"Impuissant il assista à la chute de son copr sans vie sur le sol boueux."
"Jean Plank n'était désormais plus qu'une petite boule de lumière dans le main de thresh."
"Celui ci inspectait sa nouvelle prise."
thresh "Mais c'est de la merde !"
"thresh n'avais jamais rien vue d'aussi laid."
"Si tous les déchets du monde avait été personnifié"#Phrase random
"Il ne pouvait décemment pas garder cette horreur sur lui."
"Aussi lacha-t-il la chose immonde qu'il avait entr les main avnat de partir en courrant en quête d'un desinfectant pour ces mimines."
"L'ame de Jean Plank roula paisiblement vers son corp avant d'en reprendre possession."
jp "Haha "
"hurla jp alors qu'il revenait à la vie."
"Un haha qui traduisait toute sa félicité vis à vis de cette nouvelle victoire méritée"
"Fort de cette nouvelle et enrichissante experience, il reprit son chemin"






























#
#jinx "Hé tu trouve pas que mes cheuveux sont super beau en ce moment ?"
#"Elle dépouille les gens" --> elle va piquer les affaires de Jean Plank -> flash back du pistolet du pere --> "Si tu y touche je te jure que je te ..." "Depuis ce jour jp ne pouvais plus ---, mais franchement ça valait le coup" "Enfin sauf s'il ne retrouvait pas ce foutu pitolet !!"
#"Sorcière des eau profonde"
#"Jean Plank aurait du se méfier"
#jp "La salope !"
#"Il  n'y avait pas de sang. Pourtant Jean plnak ne pouvais ce mouvoir"
#"Toute à coup une  sensation affreuse parcourut son corp"
#"Celle de son ame qui se faisait extraire hors de son envelopppe charnelle"
#"Impuissant il assista à la chute de son copr sans vie sur le sol boueux."
#"Jean Plank n'était désormais plus qu'une petite boule de lumière dans le main de thresh."
#"Celui ci inspectait sa nouvelle prise."
#thresh "Mais c'est de la merde !"
#"thresh n'avais jamais rien vue d'aussi laid."
#"C'était comme si un million de soleil avait chier sur cette âme."
#"Il ne pouvait décemment pas garder cette horreur sur lui."
#"Aussi lacha-t-il la chose immonde qu'il avait entr les main avnat de partir en courrant en quête d'un desinfectant pour ces mimines."
#"L'ame de Jean Plank roula paisiblement vers son copr avant d'en reprendre possession."
#jp "Haha "
#"hurla jp alors qu'il revenait à la vie."
#"Un haha qui traduisait toute sa félicité vis à vis de cette nouvelle victoire méritée"

