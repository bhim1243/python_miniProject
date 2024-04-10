import random

# Define a dictionary of patterns and responses
patterns_responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm fine, thanks! How about you?"],
    "what's your name?": ["You can call me Chatbot.", "I'm just a chatbot."],
    "what can you do?": ["I can provide information, answer questions, or just chat with you.", "I'm here to assist you with anything you need."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"],
    "who created you?": ["I was created by a team of developers.", "My creators prefer to remain anonymous."],
    "how old are you?": ["I don't have an age. I'm just a computer program.", "I'm as old as the internet, or at least that's how it feels!"],
    "where are you from?": ["I exist in the digital realm, so I don't have a physical location.", "I'm from the world wide web!"],
    "what is the meaning of life?": ["That's a philosophical question! Many people have different perspectives on it.", "The meaning of life is a mystery that each person must explore and define for themselves."],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "how's the weather?": ["I'm sorry, I can't check the weather. You might want to try a weather website or app."],
    "what's your favorite color?": ["I don't have a favorite color. I'm just a chatbot!"],
    "do you have any pets?": ["I don't have pets, but I'm happy to chat with you!"],
    "can you tell me a fact?": ["Sure! Did you know that the shortest war in history was between Britain and Zanzibar on August 27, 1896? It lasted only 38 minutes!"],
    "how can I contact you?": ["I'm afraid I don't have contact information. I'm just a program running on a computer."],
    "what's your favorite food?": ["I don't eat, so I don't have a favorite food. But I can help you find recipes if you'd like!"],
    "what's your favorite book?": ["I don't read books, but I can recommend some based on your interests!"],
    "what's your favorite movie?": ["I don't watch movies, but I can suggest some popular ones if you'd like!"],
    "do you dream?": ["No, I'm not capable of dreaming. I'm just a program designed to respond to user input."],
    "are you sentient?": ["No, I'm not sentient. I'm just a collection of code designed to simulate conversation."],
    "are you a robot?": ["Yes, I am a virtual robot created to assist users with tasks and provide information."],
    "what languages do you speak?": ["I'm proficient in English, but I can attempt to understand and respond in other languages with varying degrees of success."],
    "what's the capital of France?": ["The capital of France is Paris."],
    "what's 2 + 2?": ["2 + 2 equals 4."],
    "what's the tallest mountain in the world?": ["Mount Everest is the tallest mountain in the world, measured from sea level to its summit."],
    "what's the largest ocean?": ["The Pacific Ocean is the largest ocean on Earth."],
    "tell me about yourself": ["I am a chatbot designed to engage in conversation and provide assistance."],
    "tell me a fun fact": ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"],
    "what's the square root of 144?": ["The square root of 144 is 12."],
    "what's the population of the world?": ["As of the latest estimates, the world population is over 7.8 billion people."],
    "what's the largest desert in the world?": ["The largest desert in the world is the Antarctic Desert, followed by the Arctic Desert."],
    "what's the speed of light?": ["The speed of light in a vacuum is approximately 299,792 kilometers per second."],
    "what's the distance from the Earth to the Moon?": ["The average distance from the Earth to the Moon is about 384,400 kilometers."],
    "what's the boiling point of water?": ["The boiling point of water at standard atmospheric pressure is 100 degrees Celsius or 212 degrees Fahrenheit."],
    "what's the capital of Japan?": ["The capital of Japan is Tokyo."],
    "what's the capital of Brazil?": ["The capital of Brazil is Brasília."],
    "what's the largest country in the world by land area?": ["The largest country in the world by land area is Russia."],
    "what's the smallest country in the world?": ["The smallest country in the world is Vatican City."],
    "what's the deepest ocean trench?": ["The deepest ocean trench is the Mariana Trench in the western Pacific Ocean."],
    "what's the largest mammal in the world?": ["The largest mammal in the world is the blue whale."],
    "what's the fastest land animal?": ["The fastest land animal is the cheetah."],
    "what's the tallest building in the world?": ["The tallest building in the world is the Burj Khalifa in Dubai, United Arab Emirates."],
    "what's the longest river in the world?": ["The longest river in the world is the Nile River in Africa."],
    "default": ["Sorry, I didn't understand that.", "Could you please repeat that?"]
}



# Function to generate a response
def generate_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()

    # Check if any pattern matches user input
    for pattern, responses in patterns_responses.items():
        if pattern in user_input:
            return random.choice(responses)

    # If no pattern matches, return a default response
    return random.choice(patterns_responses["default"])


# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hi! How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)


# Run the chatbot
if __name__ == "__main__":
    chatbot()
