import tweepy
power="AIzaSyDkw4qkSMPli1e_GO_l9FkvgngqreYM1SQ" #Google
lies="caa905e0f8b4acf6e690ad1876cbb8f7d98a94f9" #Census
future="544242d01c1bead586e510ac748fc6ca" #Openweathermap

#twitter
#consumer api key EdyWCQNqsi6DDuK0Y1wNVo33P
#consumer secret AcCJin1QVDsqlFN3PkR4eDoHunefZHaU5OZFSCo1vxQNSIxNnf
#access token 	773260063-eur6RZrpPdxnaazFOUEbdacKaWbY1Hq1whJUX80m
#access token secret Y5AuEVz2cI0HUwaH08q0aPJe1tHSwJkH7S9Gf4Cb2xkMh
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
chirp = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) #chirp is the var I want for twittering