import discord
import os
import server
import random
from replit import db
from discord.utils import get
client = discord.Client()

my_secret = os.environ['TOKEN']
msg_motivation = [
  'Qui veut faire quelque chose trouve un moyen, qui ne veut rien faire trouve une excuse.',
  'Celui qui ne progresse pas chaque jour, recule chaque jour. - Confucius',
  'L\'obstination est le chemin de la réussite. - Charlie Chaplin',
  'Celui qui n\'a pas d\'objectifs ne risque pas de les atteindre. - Sun Tzu',
  'Le succès n\'est pas final l\'echec n\'est pas fatal C\'est le courage de continuer qui compte. - Winston Churchill',
  'Il est dur d\'échouer ; mais il est pire de n\'avoir jamais tenté de réussir. - Franklin Delano Roosevelt',
  'Gardez toujours à l\'esprit que votre propre décision de réussir est plus importante que n\'importe quoi d\'autre. -Abraham Lincoln',
  'Celui qui avance avec confiance dans la direction de ses rêves connaîtra un succès inattendu dans la vie ordinaire. - N.H. Kleinbaum',
  'Il ne faut pas toujours tourner la page, il faut parfois la déchirer. -Achille Chavée'
]
def update_key(key,text):
  if key in db.keys():
    db[key] = text
  



@client.event
async def on_ready():
  print('Botjour')
  await client.get_channel(924002669151027211).send("Bot is online")
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  channel = message.channel
# Reset/Init
  if  msg =='!Init' and channel.name == '❗𝐖𝐚𝐫-𝐌𝐚𝐜𝐡𝐢𝐧𝐞❗' and channel.category.name == '🏆RUSH ROYAL BBF TOURNOI🏆' and get(message.author.roles, name = 'InitBot'):

    db.clear()
    db["GDCTTF"] = "GDC TTF"
    db["GDCBBF"] = "GDC BBF"
    db["GDCMNF"] = "GDC MNF"
    db["CONSIGNESTTF"] = "CONSIGNES TTF"
    db["CONSIGNESBBF"] = "CONSIGNES BBF"
    db["CONSIGNESMNF"] = "CONSIGNES MNF"
    db["SANDALESTTF"] = "SANDALES TTF"
    db["SANDALESBBF"] = "SANDALES BBF"
    db["SANDALESMNF"] = "SANDALES MNF"
    db["BONUSTTF"] = "BONUS TTF"
    db["BONUSBBF"] = "BONUS BBF"
    db["BONUSMNF"] = "BONUS MNF"
    db["SOINSTTF"] = "SOINS TTF"
    db["SOINSBBF"] = "SOINS BBF"
    db["SOINSMNF"] = "SOINS MNF"
    db["AVERTOTTF"] = "AVERTO TTF"
    db["AVERTOBBF"] = "AVERTO BBF"
    db["AVERTOMNF"] = "AVERTO MNF"
    db["COMMANDESBBF"] = "Iron Man : \n\n!GDC : Blablabla\n!Sandales : Blablabla\n!Bonus : Blablabla\n!Soins : Blablabla\n!Averto : Blablabla\n!Consignes : Blablabla\n!Commandes : Envoie un MP avec la liste des commandes du bot.\n\nMembres (Tous les clans):\n\n!Malediction\n!Meteores\n!Journee typique\n!Extremum\n!Coins\n!Mouvement brownien\n!Secheresse\n!Surprise\n!Vent du changement\n!Evolution\n!Bonus : Blablabla"
    # BONUS GDC
    db["COINSBBF"] = "https://urlz.fr/gXWY"
    db["EVOLUTIONBBF"] = "https://urlz.fr/gXX0"
    db["EXTREMUMBBF"] = "https://urlz.fr/gXX1"
    db["JOURNEE TYPIQUEBBF"] = "https://urlz.fr/gXX4"
    db["MALEDICTIONBBF"] = "https://urlz.fr/gXX5"
    db["METEORESBBF"] = "https://urlz.fr/gXX6"
    db["MOUVEMENT BROWNIENBBF"] = "https://urlz.fr/gXX7"
    db["SECHERESSEBBF"] = "https://urlz.fr/gXX8"
    db["SURPRISEBBF"] = "https://urlz.fr/gXXa"
    db["VENT DU CHANGEMENTBBF"] = "https://urlz.fr/gXXb"
#Fin reset/Init
# !MODIFYTEXT
  if  msg.startswith('!MODIFYTEXT') and channel.name == '❗𝐖𝐚𝐫-𝐌𝐚𝐜𝐡𝐢𝐧𝐞❗' and channel.category.name == '🏆RUSH ROYAL BBF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    tampon = msg.split('!',2)[2]
    key = tampon.split(' : ')[0] + 'BBF'
    text = tampon.split(" : ",1)[1]
    if key in db.keys() :
      update_key(key,text)
      await message.channel.send('Message modifié')

  if  msg.startswith('!MODIFYTEXT') and channel.name == '❗𝐖𝐚𝐫-𝐌𝐚𝐜𝐡𝐢𝐧𝐞❗' and channel.category.name == '🏆RUSH ROYAL MNF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    tampon = msg.split('!',2)[2]
    key = tampon.split(' : ')[0] + 'MNF'
    text = tampon.split(" : ")[1]
    if key in db.keys() :
      update_key(key,text)
      await message.channel.send('Message modifié')


  if  msg.startswith('!MODIFYTEXT') and channel.name == '❗𝐖𝐚𝐫-𝐌𝐚𝐜𝐡𝐢𝐧𝐞❗' and channel.category.name == '🏆Rush Royal TTF Tournoi🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    tampon = msg.split('!',2)[2]
    key = tampon.split(' : ')[0] + 'TTF'
    text = tampon.split(" : ")[1]
    if key in db.keys() :
      update_key(key,text)
      await message.channel.send('Message modifié')
# !MODIFYTEXT fin    

#!GDC

  if  msg =='!GDC' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL BBF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["GDCBBF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["GDCBBF"] + '\n' + message.author.nick)

  if  msg =='!GDC' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL MNF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["GDCMNF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["GDCMNF"] + '\n' + message.author.nick)


  if  msg =='!GDC' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆Rush Royal TTF Tournoi🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    if not message.author.nick : 
      await channel.send(db["GDCTTF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["GDCTTF"] + '\n' + message.author.nick)
# !GDC fin  
# !BONUS GDC
  if  msg =='!Coins' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["COINSBBF"])
  
  if  msg =='!Evolution' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["EVOLUTIONBBF"])

  if  msg =='!Extremum' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["EXTREMUMBBF"])

  if  msg =='!Journee typique' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["JOURNEE TYPIQUEBBF"])

  if  msg =='!Malediction' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["MALEDICTIONBBF"])

  if  msg =='!Meteores' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["METEORESBBF"])

  if  msg =='!Mouvement brownien' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["MOUVEMENT BROWNIENBBF"])

  if  msg =='!Secheresse' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["SECHERESSEBBF"])

  if  msg =='!Surprise' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["SURPRISEBBF"])

  if  msg =='!Vent du changement' and channel.name == '♦tournoi-en-cours♦' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["VENT DU CHANGEMENTBBF"])
# !BONUS GDC FIN

#!Consignes
  if  msg =='!Consignes' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL TTF TOURNOI🏆' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["CONSIGNESTTF"])

  if  msg =='!Consignes' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL BBF TOURNOI🏆' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["CONSIGNESBBF"])


  if  msg =='!Consignes' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL MNF TOURNOI🏆' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["CONSIGNESMNF"])

#!ConsignesFin

#!Sandales
  if  msg =='!Sandales' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL TTF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["SANDALESTTF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["SANDALESTTF"] + '\n' + message.author.nick)

  if  msg =='!Sandales' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL BBF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["SANDALESBBF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["SANDALESBBF"] + '\n' + message.author.nick)


  if  msg =='!Sandales' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL MNF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["SANDALESMNF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["SANDALESMNF"] + '\n' + message.author.nick)
#!Sandales Fin

#!Bonus
  if  msg =='!Bonus' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆Rush Royal TTF Tournoi🏆' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["BONUSTTF"])

  if  msg.startswith('!Bonus') and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL BBF TOURNOI🏆' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["BONUSBBF"])


  if  msg == '!Bonus' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL MNF TOURNOI🏆' and not get(message.author.roles, name="Gamin"):
    await message.delete()
    await message.author.send(db["BONUSMNF"])
#!Bonus Fin

#!Soins
  if  msg == '!Soins' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL TTF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["SOINSTTF"] + '\n' + message.author.nick)

  if  msg == '!Soins' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL BBF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["SOINSBBF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["SOINSBBF"] + '\n' + message.author.nick)


  if  msg == '!Soins' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL MNF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["SOINSMNF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["SOINSMNF"] + '\n' + message.author.nick)
#!Soins Fin
#!Commandes
  if  msg =='!Commandes' and channel.name == '♦tournoi-en-cours♦' :
    await message.delete()
    await message.author.send(db["COMMANDESBBF"])
    #!Commandes Fin
# !Averto
  if  msg =='!Averto' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL TTF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["AVERTOTTF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["AVERTOTTF"] + '\n' + message.author.nick)

  if  msg =='!Averto' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL BBF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["AVERTOBBF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["AVERTOBBF"] + '\n' + message.author.nick)


  if  msg =='!Averto' and channel.name == '♦tournoi-en-cours♦' and channel.category.name == '🏆RUSH ROYAL MNF TOURNOI🏆' and get(message.author.roles, name="Iron Man") and not get(message.author.roles, name="Gamin"):
    await message.delete()
    if not message.author.nick : 
      await channel.send(db["AVERTOMNF"] + '\n' + message.author.name)
    else : 
      await channel.send(db["AVERTOMNF"] + '\n' + message.author.nick)
#!Averto Fin

#Score
  if  channel.name == '🔸score-joueurs🔸' and not get(message.author.roles, name="Gamin"):
    if msg.find("/") > 0 :
      splitMsg = msg.split("/", 1)
      resultat = splitMsg[0][len(splitMsg[0])-1]
      total = splitMsg[1][0]

      if resultat.isnumeric() and total.isnumeric() :
        diff = int(total) - int(resultat)
        if diff == 0 :
          await channel.send('Felicitations ! Si ton deck utilisé ne fait pas parti des decks proposés n\'hesite pas a le proposer au staff !')
        if diff == 1 or diff == 2:
          await channel.send(msg_motivation[random.randrange(0,8)])
        if diff >= 3 :
          await channel.send('Tu as eu des difficultés lors de cette journée, n\'hesite pas a voir avec le staff si ils peuvent t\'aider')

#Score fin
    
#Easter Eggs    
  if msg =='!Elijah':
    await channel.send('Il est notre héros, Gadget n\'a qu\'a bien aller se faire foutre')
  if msg =='!Jeje':
    await channel.send('Il est mon créateur, mon dieu !')
  if msg =='!Valerie':
    await channel.send('La plus belle d\'entre toutes !')
  if msg =='!Merenoel':
    await channel.send('https://tenor.com/view/merry-christmas-model-posing-sexy-fierce-gif-15882492')
  if msg =='!Perenoel':
    await channel.send('https://tenor.com/view/luke-paine-sexy-message-merry-christmas-sexy-boyfriend-gif-19434283')    
#Easter Eggs  Fin

client.run(my_secret)
server.server()
