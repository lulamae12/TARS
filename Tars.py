from chatterbot import ChatBot
trainingIterations = 1
tars = ChatBot(
    'Tars',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
# Train based on the english corpus
while trainingIterations != 0:
    tars.train("chatterbot.corpus.english")

    trainingIterations = trainingIterations - 1
while True:
    question = input(str('Question:'))
    # Get a response to an input statement
    answer = tars.get_response(question)
    print('Tars:',answer)
