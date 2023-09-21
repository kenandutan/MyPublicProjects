# importing regex and random libraries
import re
import random

class ShibaBot:

  # keywords for exiting the interaction
  exit_commands = ("goodbye", "bye", "later", "see ya", "see you")
  # random shiba actions
  shiba_actions = (
        "*The Shiba scratches their ear* ",
        "*The Shiba yawns* ",
        "*The Shiba starts sniffing the ground* ",
        "*The Shiba starts licking their paw* ",
        "*The Shiba stares at you* ",
        "*The Shiba stretches in a downward dog position* ",
        "*The Shiba wags his tail* ",
        "*The Shiba jumps up on you* ",
        "AH-WOOOOOO!!"
    )
 
  def __init__(self):
    self.commands = {'speak_intent': r'.*\s*speak.*', 'sit_intent': r'.*\s*sit.*', 'high_five_intent': r'.*\s*high*.*five*', 'down_intent': r'.*\s*down.*', 'paw_intent': r'.*\s*paw.*', 'spin_intent': r'.*\s*snap.*finger*', 'bang_intent': r'.*\s*bang.*', 'follow_intent': r'.*let.*go*', 'yip_intent': r'.*yip*.*yip*', 'pet_intent': r'.*pet*.*', 'scratch_intent': '.*scratch*.*'}

  # when you encounter the Shiba
  def meet(self):
    print("*You see a dog. You notice it's a Shiba Inu and walk up to it.* ")

    self.shiba_interaction()

  # if the user says an exit command
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("*You walk away from the Shiba* ")
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
      elif found_match and intent == 'paw_intent':
        return self.paw_intent()
      elif found_match and intent == 'spin_intent':
        return self.spin_intent()
      elif found_match and intent == 'bang_intent':
        return self.bang_intent()
      elif found_match and intent == 'follow_intent':
        return self.follow_intent()
      elif found_match and intent == 'pet_intent':
        return self.pet_intent()
      elif found_match and intent == 'yip_intent':
        return self.yip_intent()
      elif found_match and intent == 'scratch_intent':
        return self.scratch_intent()

    return self.no_match_intent()

  # speak command
  def speak_intent(self):
    responses = ("BARK! ", "*The Shiba does nothing* ", "WOOF! ")
    return random.choice(responses)

  # sit command
  def sit_intent(self):
    responses = ("*The Shiba sits down* ", "*The Shiba does nothing* ")
    return random.choice(responses)

  # high five command
  def high_five_intent(self):
    responses = ("*The Shiba gives you a high five* ", "*The Shiba does nothing* ")
    return random.choice(responses)

  # down command
  def down_intent(self):
    responses = ("*The Shiba lays down* ", "*The Shiba does nothing* ")
    return random.choice(responses)

  # paw command
  def paw_intent(self):
    responses = ("*The Shiba touches your hand with their paw* ", "*The Shiba does nothing* ")
    return random.choice(responses)

  # spin command
  def spin_intent(self):
    responses = ("*The Shiba does a spin* ")
    return responses

  # play dead command
  def bang_intent(self):
    responses = ("*The Shiba falls down with their feet in the air* ")
    return responses

  # follow command
  def follow_intent(self):
    responses = ("*You start walking and the Shiba follows you* ")
    return responses

    # yip command
  def yip_intent(self):
    responses = ("*You start walking and the Shiba quickly follows you* ")
    return responses

  # pet command
  def pet_intent(self):
    responses = ("*The Shiba wags their tail* ", "*The Shiba grins* ")
    return random.choice(responses)

    # scratch command
  def scratch_intent(self):
    responses = ("*The Shiba smiles with their toungue sticking out* ")
    return responses

  # when the reply doesn't match any intent
  def no_match_intent(self):
    responses = ("*The Shiba stares at you* ", "*The Shiba tilts its head, confused* ", "*The Shiba whines* ", "*The Shiba starts panting* ", "*The Shiba looks away from you* ", "*The Shiba yawns* ", "*The Shiba lays down and starts sleeping* ")
    return random.choice(responses)

# calling the ShibaBot
my_bot = ShibaBot()
my_bot.meet()
