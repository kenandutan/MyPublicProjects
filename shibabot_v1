# importing regex and random libraries
import re
import random

class ShibaBot:

  # keywords for exiting the interaction
  exit_commands = ("quit", "exit", "goodbye", "bye", "later", "see ya")
  # random shiba actions
  shiba_actions = (
        "*The Shiba scratches their ear* ",
        "*The Shiba yawns* ",
        "*The Shiba starts sniffing the ground* ",
        "*The Shiba starts licking their paw* ",
        "*The Shiba stares at you* ",
        "*The Shiba looks away from you* ",
        "*The Shiba stretches in a downward dog position* "
    )

  def __init__(self):
    self.commands = {'speak_intent': r'.*\s*speak.*', 'sit_intent': r'.*\s*sit.*', 'high_five_intent': r'.*\s*high*.*five*', 'down_intent': r'.*\s*down.*'}

  # when you encounter the Shiba
  def meet(self):
    print("*You see a dog. You quickly realize it's a Shiba Inu and walk up to it.* ")

    self.shiba_interaction()

  # if the user says an exit command
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("*You walk past the Shiba and go along with your day* ")
        return True

  # continuously interacting with Shiba
  def shiba_interaction(self):
    reply = input(random.choice(self.shiba_actions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))


  # matching user's response to an item
  def match_reply(self, reply):
    for intent, regex_pattern in self.commands.items():
      found_match = re.match(regex_pattern, reply)
      if found_match and intent == 'speak_intent':
        return self.speak_intent()
      elif found_match and intent == 'sit_intent':
        return self.sit_intent()
      elif found_match and intent == 'high_five_intent':
        return self.high_five_intent()
      elif found_match and intent == 'down_intent':
        return self.down_intent()
      else:
        return self.no_match_intent()


  # speak command
  def speak_intent(self):
    responses = ("BARK! ", "*The Shiba stares at you* ", "WOOF! ")
    return random.choice(responses)

  # sit command
  def sit_intent(self):
    responses = ("*The Shiba sits down* ", "*The Shiba lays down* ", "*The Shiba does nothing* ", "*The Shiba stares at you* ")
    return random.choice(responses)

  # high five command
  def high_five_intent(self):
    responses = ("*The Shiba gives you a high* ", "*The Shiba does nothing* ", "*The Shiba stares at you* ")
    return random.choice(responses)

  # down command
  def down_intent(self):
    responses = ("*The Shiba lays down* ", "*The Shiba sits down* ", "*The Shiba does nothing* ", "*The Shiba stares at you* ")
    return random.choice(responses)

  # when the reply doesn't match any intent
  def no_match_intent(self):
    responses = ("*The Shiba does nothing* ", "*The Shiba stares at you* ", "BARK! ", "*The Shiba tilts its head, confused* ", "*The Shiba whines* ", "*The Shiba starts panting* ", "*The Shiba looks away from you* ", "*The Shiba yawns* ")
    return random.choice(responses)

# calling the ShibaBot
my_bot = ShibaBot()
my_bot.meet()
