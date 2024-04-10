import tkinter as tk

# Define the dictionary with word definitions and translations
word_dict = {
    "python": {
        "english": "a large heavy-bodied nonvenomous constrictor snake occurring throughout the Old World tropics.",
        "nepali": "पुरानो विश्व गर्मकटिबाट होइनट्रामा हुने एक ठूलो भारी-शारी विषहीन संकुचित साँप।"
    },
    "program": {
        "english": "a planned series of future events, items, or performances.",
        "nepali": "भविष्यको घटनाहरू, वस्त्रहरू, वा प्रदर्शनीहरूको योजना गरिएको।"
    },
    "computer": {
        "english": "an electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program.",
        "nepali": "डेटा संचयन र प्रसंस्करणको लागि एक इलेक्ट्रोनिक यन्त्र, बिनारी रूपमा सामान्यत: कम्प्युटर प्रोग्राममा दिइएका निर्देशिकाहरूअनुसार।"
    },
    "dictionary": {
        "english": "a reference book or electronic resource listing words typically in alphabetical order along with their meanings.",
        "nepali": "शब्दकोष: शब्दहरूलाई सामान्यत: वर्णानुक्रममा राखेर उनको अर्थसहितको संदर्भ पुस्तक वा इलेक्ट्रोनिक स्रोत।"
    },
    "example": {
        "english": "a thing characteristic of its kind or illustrating a general rule.",
        "nepali": "उदाहरण: आफ्नै प्रकारको कुरा वा एक सामान्य नियमको प्रदर्शन गर्ने कुरा।"
    },
    "knowledge": {
        "english": "facts, information, and skills acquired through experience or education; the theoretical or practical understanding of a subject.",
        "nepali": "ज्ञान: अनुभव वा शिक्षाद्वारा प्राप्त तथ्य, जानकारी, र कौशल; विषयको सिद्धान्तिक वा व्यावहारिक समझ।"
    },
    "effort": {
        "english": "a vigorous or determined attempt.",
        "nepali": "प्रयास: एक प्रकारको शक्तिशाली वा निर्धारित प्रयास।"
    },
    "passion": {
        "english": "strong and barely controllable emotion.",
        "nepali": "उत्कृष्टता: ठूलो र थोरै संयमहीन भावना।"
    },
    "journey": {
        "english": "an act of traveling from one place to another.",
        "nepali": "यात्रा: एउटा स्थानबाट अर्का स्थानमा यात्रा गर्ने कार्य।"
    },
    "success": {
        "english": "the accomplishment of an aim or purpose.",
        "nepali": "सफलता: लक्ष्य वा उद्देश्यको पूरा गर्नु।"
    },
    "challenge": {
        "english": "a call to take part in a contest or competition, especially a duel.",
        "nepali": "चुनौती: प्रतियोगिता वा प्रतिस्पर्धामा भाग लिनका लागि एक आह्वान, विशेषतः एक युद्ध।"
    },
    "victory": {
        "english": "an act of defeating an enemy or opponent in a battle, game, or other competition.",
        "nepali": "जय: एक शत्रु वा प्रतियोगीलाई युद्ध, खेल, वा अन्य प्रतिस्पर्धामा पराजित गर्ने कार्य।"
    },
    "education": {
        "english": "the process of receiving or giving systematic instruction, especially at a school or university.",
        "nepali": "शिक्षा: विशेषत: एक विद्यालय वा विश्वविद्यालयमा, यस्तै यात्रा वा प्रदान गर्ने वा प्राप्त गर्ने विधि।"
    },
    "friendship": {
        "english": "the emotions or conduct of friends; the state of being friends.",
        "nepali": "मित्रता: मित्रहरूको भावनाहरू वा आचरण; मित्रहरू हुनुको स्थिति।"
    },
    "happiness": {
        "english": "the state of being happy.",
        "nepali": "खुशी: खुशी हुनुको अवस्था।"
    },
    "sadness": {
        "english": "feeling or showing sorrow; unhappy.",
        "nepali": "दु: खुशी: दु: खुसी भोग्ने वा देखाउने; अखुसी।"
    },
    "love": {
        "english": "an intense feeling of deep affection.",
        "nepali": "प्रेम: गहिरो अफेक्सनको तीव्र अनुभूति।"
    },
    "family": {
        "english": "a group of one or more parents and their children living together as a unit.",
        "nepali": "परिवार: एक वा अधिक बालकहरूसहितको एक वा बढी अभिभावकहरूको एक समूह रूपमा एक साथ बस्ने।"
    },
    # Add more words here
    "beauty": {
        "english": "a combination of qualities, such as shape, color, or form, that pleases the aesthetic senses, especially the sight.",
        "nepali": "सुन्दरता: आकर्षक अनुभूति, खासकर दृष्टिमा।"
    },
    "nature": {
        "english": "the phenomena of the physical world collectively, including plants, animals, the landscape, and other features and products of the earth.",
        "nepali": "प्रकृति: भौतिक विश्वका घटनाहरूको समूह, जसमा पौधा, प्राणी, भूभाग, र पृथ्वीका अन्य विशेषताहरू र उत्पादहरू समाहित हुन्छन्।"
    },
    "health": {
        "english": "the state of being free from illness or injury.",
        "nepali": "स्वास्थ्य: बिमारी वा चोटबाट बिमुक्त अवस्था।"
    },
    "friend": {
        "english": "a person whom one knows and with whom one has a bond of mutual affection, typically exclusive of sexual or family relations.",
        "nepali": "साथी: जसले जान्छन् र जससँग मिल्दैछन् जसले एक अपेक्षित स्नेहको बंध छ, खासकर सेक्सुअल वा परिवार संबन्धहरूबाहेक।"
    },
    "dream": {
        "english": "a series of thoughts, images, or emotions occurring during sleep.",
        "nepali": "सपना: निद्रामा हुने विचार, चित्र, वा भावनाहरूको एक सिरिज।"
    },
    # Add more words here

}


# Function to look up a word in the dictionary
def lookup_word():
    word = entry.get().lower()
    translation_language = language_choice.get().lower()
    definition = word_dict.get(word, {}).get(translation_language, "Word not found in dictionary.")
    output_label.config(text=definition)

# Create the main application window
root = tk.Tk()
root.title("Word Dictionary")

# Create input elements
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Language selection
language_choice = tk.StringVar()
language_choice.set("English")
language_menu = tk.OptionMenu(root, language_choice, "English", "Nepali")
language_menu.pack(pady=5)

# Create a button
button = tk.Button(root, text="Lookup", command=lookup_word)
button.pack(pady=5)

# Create a label for displaying the definition
output_label = tk.Label(root, text="")
output_label.pack(pady=5)

# Run the application
root.mainloop()
