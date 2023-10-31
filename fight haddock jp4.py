"Dit Haddock en se levant brusquement de sa chaise."
label fight_pass1:
menu:
    "Courir vers Haddock et le frapper":
        "Jean Plank courut vers Haddock pour lui mettre une de ses fameuses baffes secrètes."
        "Cependant il avait oublié qu'Haddock était à l'autre bout de la pièce."
        menu : 
        	"courrir plus vite":
        		"Cependant j'en Plank était malin, si Hadock était plus loin, il n'avait qu'a courrir plus vite."
        		"Ce qu'il fit avec brio."
        		"Tel le bison qui traverse la savane, il traversa la pièce et se jetta sur Haddock."
        		label run_down_haddock:
        		scene chaise
        		"Ce dernier qui venait tout juste de se saisir d'une chaise, et se préparait à en foutre un coup à Jean Plank."
        		menu: 
        			"Reculer de peur de se prendre la chaise":
        				 "Aïe aïe aïe, mauvais choix."
        				 "Jean Plank recula si vite qu'il se congna contre un truc."
        				 "Vous ne saurez jamais quoi, mais il en mourru."
        				 jump end_tomb

        			"La chaise n'existe que si tu as peur d'elle.":
        				"Jean Plank navait pas peur des chaises"
        				"Hadock, lui non plus n'avait encore jamais eu peur d'une chaise."
        				"Cependant celle que Jean Plank venanit de lui arracher des mains semblait vraiment menaçante."
        				"Pas autant que de courrir avec des ciseaux, mais vraiment pas loin."
        				"Tétanisé par la peur, il ne pu que regarder le destin dans les yeux."
        				"En l'occurance ,le destin avait quand meme vachement la forme d'un tabouret."
        				menu:
        					"Faire attention à Milou, le chien de Tintin":
		                        "Jean Plank était méfiant. Il n'attaqua pas et chercha du regard ce fichu clébard."
		                        "Il y avait en effet un chien !"
		                        "Mais celui ci semblait empaillé depuis un moment."
		                        "Pas un danger pour notre héro en somme."
		                        "Par contre la femme d'haddock, qui avait profité de ce moment d'inattention se saisir d'un vase, en était un."
		                        menu:
		                        	"Eviter le coup de vase in-extremis":
		                        		"Malheureusement, il était trop tard pour éviter le vase."
		                        		"Jean Plank distrait par sa tentative d'esquive, se prit le vase de plein fouet et perdi connaissance."
		                        		jump fin_prison

		                        	"Prendre le coup de vase comme un brave":
		                        		"De toute façon il était trop tard pour l'éviter."
		                        		"Cependant la bravoure de Jean Plank fit en sorte qu'il s'en sorti sans perdre connaissance."
		                        		"Il lanca rapidement son tabouret sur la tronche de Haddock qui tomba lourdement au sol."
		                        		"Puis, suspectant la fille de preparer elle aussi un coup en traitre, il se saisi de cette dernière pour la lancer sur la mère."
		                        		"Les deux etre humains de sexe feminin volèrent dans la pièce"
		                        		"Jean plank hallllaaa verifier qu'elles ne lui causerait plus d'ennuit"
		                        		"Il prit une pause pour penser un peu à l'ocean" #Un jean pank stylé avec la musique d'ultra vomit discretement en son sonnore 
		                        		"Puis il retourna cogner sur hadock."
		                        		menu : 
		                        			"Revérifier que la femme ne causera pas d'ennui":
		                        				"Jean Plank décida de suivre son instinct."
		                        				"Delaissant Haddock il HALLA se saisir de la femme. Il raprocha son visage du sien en soulevant son corp inerte par le col."
		                        				jp "TU FAIS SEMBLANT UN C'EST CA ?! TU CROIS QUE CA M'AMUSE ?!"
		                        				"Voyant qu'elle ne repondait pas, il lui mit une baffe titanesque qui l'envoya quelque mettre plus loin."
		                        				"Desormais serein, il retourna cogner sur haddock."

		                        			"Cogner sur Haddock mais avec le doute que la femme puisse quand meme se relever et attaquer dans le dos en traitre comme le font toutes les femmes":
		                        				"Jean Plank cogna Haddock, cependant, il le fit avec une lègère anxiété."
		                        				"Cela gachait un peu son plaisir."
		                        				"Il continua de congner de bon coeur malgrès tout."
		                        				"Le stress vous fait gagner \"Cheuveux blanc\""
		                        		jump fin_fight_haddock


		                        
		                    "Abbatre la chaise sur ce gredin !":
		                    	"Jean plank abattu violamment ça chaise sur le crane de son enemie"
		                    	"Sa fureux n'ayant d'egale que sa stupidité, la cervelle du capitaine des doc se répendie sur le sol sous les yeux horifiés de sa femme et sa fille."
		                    	"Stylé dans la vengence, Jean plank frappa chacune d'entre elle avant de les violer."
		                    	"Ceci fait, il les frappa encore hisoire de marquer le coup."
		                    	"Jean plank était victorieux."
		                    	"Cependant il regrettait un peu cette victoire trop facile."
		                    	"Le scénariste aussi d'ailleur."
		                    	"C'est pour cela que malgrès votre victoire, totale et incontestabe, vous n'aurez tout de meme que l'ecran de défaite en récompense."
		                    	jump end_false_vitory

        	"Courrir moin vite":
        		"Jean Plank ralenti le rythme afin d'avoir plus de teps pour anticiper la reaction d'Hadock"
        		"Mais plus il ralentissait, plus haddock avait le temps de preparer une contre offensive."
        		"Il se vait donc de ralentir encore."
        		"Mais haddock avait toujours plus de temps"
        		"Et Jean plank devait toujours plus ralentir."
        		"et ..."
        		"Totalement ahuri par le fait que jean plank ne bougeait maintenant plus du tout, haddock fini par se lever pour aller à sa rencontre."
        		#scene crayon
        		haddock "Jean Plank tu es un attardé mental c'est ça ?"
        		jp "Bah n..."
        		#Scene flash back musique triste (peut-etre la faire en vidéo)
        		#ryse "mais vous etes totallement attardé"
        		#lucien "Attend tu sais pas compter ?"
        		#Jp et pas lire non plus
        		"Le triste vérité atteignait enfin Jean Plank."
        		jp "Haddock,"
        		jp "PERSONNE NE ME TRAITE D'ATTARDE MENTAL."
        		"Jean Plank vennait de tirer au pistolet dans le crane de son ennemi, causant ainsi son décès précipité."
        		"La cervelle de son ennemi sur les murs, sa compagne tumefiée au sol et sa fille qui allait très bientot comprendre ce que celà impliquait d'etre une femme."
        		"(Car Jean Plank allait lui faire un exposé)"
        		"Jean Plank était indéniablement victorieux"
        		"Cependant il regratta longtemps cette victoire trop facile."
		        "Le scénariste aussi d'ailleur."
		        "C'est pour cela que malgrès votre victoire, totale et incontestabe, vous n'aurez tout de meme que l'ecran de défaite en récompense"
		        jump end_false_vitory

    "Les femmes et les enfants d'abord":
        "D'accord mais la femme ou la fille ?"
        menu:
        	"La femme !":
        	"La fille !":
        	"Les deux ?":
            	"Il n'y avait qu'une seulement manière de neutraliser ces deux puissants adversaires en un coup."
            	"Jean Plank se saisit de son pistolet d'une main et de son épé de l'autre."
            	"Puis, d'un agile mouvement il lança puissanment ses deux armes à travers la pièce."
            	"Mais Jean Plank n'était pas très bon lanceur et ne toucha absolument personne."
            	"L'égo de Jean Plank fut tout bonement anéhenti en réalisant cette effroyable vérité."
            	"Ayant perdu toute volonté de se battre et désomais dépressif, il alla lui meme se rendre à la police."
            	"Seul et déprimé au fond de ça cellule il prit la resolution de ne plus jamais rien lancer."
            	jump fin_prison
        jp "GIBIER DE POTENCE ! C'EST HADDOCK QUE JE VEUX FRAPPER !"
        "Hurla Jean Plank, en se précipitant sur Haddock."
        jump run_down_haddock


label end_tomb:
label end_false_victory:
label fin_prison:
label fin_fight_haddock:

de pression à cause sa faiblesse
qui veut du grog
"jean plank était vraiment, un connard."
"jean plank était vraiment, un sale con."
JP MAIS JE SUIS QUELQU4UN DE BON? BAS MOI
