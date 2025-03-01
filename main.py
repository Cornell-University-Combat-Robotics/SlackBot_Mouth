import slackbot
import compute
import time

bot = slackbot.SlackBot()
bot.send_message()
time.sleep(5)
# Take the last message send by a user, then parse the value into a and b
result = bot.retrieve_last_message()
print(result)
#compute step
#computation = compute.Compute(a, b)

#  post computation
bot.send_message(result)
