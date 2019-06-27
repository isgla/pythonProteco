#pip3 install tweepy --user
import tweepy
import os
import wget

#Keys and tokens
consumer_key = "#####"
consumer_secret = "#######"

#Create Token
access_token = "######"
access_secret = "#########"

#tweepy tiene una clase OAuthHandler con un metodo OAuthHandler que regresa un objeto de ese tipo
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#Pasarle las otras dos token y darle permiso de escritura y lectura
auth.set_access_token(access_token, access_secret)

twitter = tweepy.API(auth)
#Te regresa una lista de los ultimos 20 tweets de tu timeline
tweets = twitter.home_timeline()

"""
#Imprimir los ultimos tweets de tu timeline
for tweet in tweets:
	print(tweet.text)
"""
user = twitter.get_user("ariana211200")
print(user)
print(user.screen_name)
print(user.followers_count)

print("-"*100)
user = twitter.get_user("hannah_hgl")
print(user)

"""
print("-"*100)
for i in range(3000, 3006):
	twitter.update_status("I love you " + str(i) + " @ariana211200; saludos desde mi bot")
"""

"""
print("-"*100)
twitter.update_with_media("husky.jpg", "Bot: Guau dijo el ... ")
"""

"""
for tweet in tweets:
	print(tweet.id, tweet.text)

twitter.retweet(1144250044507480064)
twitter.create_favorite(1144250044507480064)
"""

#Descargar fotos de perfiles 
#pip3 install wget --user
os.mkdir("profilePics")
os.chdir("profilePics")
followers = tweepy.Cursor(twitter.followers, id = "hannah_hgl").items()

for follower in followers:
	wget.download(follower.profile_image_url)


