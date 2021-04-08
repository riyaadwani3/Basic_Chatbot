#Import required libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new instance of a ChatBot, my chatbot name is 'Alexa'
bot = ChatBot(
    'Alexa',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(bot)

# Train the chat bot with a few response
trainer.train(
    [
        ' Hi ',
        ' Hello ',
        ' How are you ',
        " I'm Good ",
        ' Is anyone there? ',
        ' Hi there, how can I help? ',
        ' What is the purpose of creating you?',
        ' I am created for the purpose of conversation with human. ',
        ' What programming language was used to create you? ',
        ' I am created in Python ',
        ' I want to learn how to create chatbots ',
        ' Great, this should help get you started : https://chatterbot.readthedocs.io/en/stable/ ',
        ' What is your name? ',
        " My name is Alexa.",
        'ok',
        'your name?',
        ' Thanks ',
        ' Happy to help! ',
        ' Thank you ',
        ' Any time! ',
        " That's helpful ",
        ' My pleasure ',
        ' Bye ',
        ' See you later, thanks for visiting ',
        ' See you later ',
        ' Have a nice day ',
        ' Goodbye ',
        ' Bye! Come back again soon. '
    ]
)

# Get a response for some unexpected input
while True:
    req = input('You :')
    response = bot.get_response(req)
    print('Bot :',response)