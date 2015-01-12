import twitter
from secrets import consumerKey, consumerSecret, tokenKey, tokenSecret
from utilities import getNext,setNext
from num_generator import numToWord, numToNepali
#api = twitter.Api(consumer_key=consumerKey,consumer_secret=consumerSecret,
#                  access_token_key=tokenKey, access_token_secret=tokenSecret)

nextNum = getNext()
nepaliNum = numToNepali(nextNum).decode('utf-8')
nepaliWord = numToWord(nextNum).decode('utf-8')
Result = nepaliNum + u" : " + nepaliWord
setNext(nextNum+1)
#api.postUpdate(Result)
