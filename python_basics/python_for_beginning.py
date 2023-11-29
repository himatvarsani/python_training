import random

print("Hello World")

# Variables - holds a piece of information

# int
wallet = 41
print(wallet)
print("£" + str(wallet))

wallet = 32
print(wallet)

# Challenge - Make a variable called day and set it equal to the date if the month
day = 30
month = "December"
print(str(day) + "th " + month)

# Float
weight = 190.4
print(weight)

# String
store = "Himat's Pizza Shop"
print(store)

store = "Himat's Pizza Shop, the \"best\" there is"
print(store)


# Challenge - Put the name of a movie you like into a variable called movie
movie = "The Avengers"
print(movie)

# Using  variable in strings
# Challenge - Make a variable called day_name and set it to day of the week
# like Tuesday a nd add it to the string we print
day = 15
month = "November"
day_name = "Tuesday"
temp = 65
print (f"Today is {day_name} {month} {day} and it's {temp} degrees outside")

# Booleans - True or False - good with an if statement
# if statement
light_is_on = True

if light_is_on:
    print("Light is On, We're in the light")
else:
    print("Light is Off, We're in the dark")
    
# Challenge - Make a variable age, and if someone is 18 years or older, print
# that they are an adult. Otherwise print that they are a child.
age = 40
if age >= 18:
    print("They are an adult")
else:
    print("They are a child")
    

# you need to 'import random' package when using Random function
# Random int between 1 to 10
print(random.randint(1,10))

# Random float
print(random.random())

# Challenge - Make your own version of a magic 8 ball that prints yes, no, or maybe
# each time you ask it

answer = random.randint(1,3)

if answer == 1:
    print("Yes")
elif answer == 2:
    print("No")
elif answer == 3:
    print("Maybe")
    

# Challenge - print("You will have a great day! Your Lucky Number is: 44")
lucky_number = random.randint(1,100)
print(f"You will have a great day! Your Lucky Number is: {lucky_number}")

# Project 1: Fortune Cookie exercise
fortune_number = random.randint(1,3)
#fortune_text = ''

if fortune_number == 1:
    fortune_text = 'You will have a great day!'
elif fortune_number == 2:
    fortune_text = 'Today will be tough, but it will be worth it!'
elif fortune_number == 3:
    fortune_text = 'This will be you\'re luckiest year'
print(f"{fortune_text} Your Lucky Number is: {lucky_number}")


# Lists - List is with a square brackets []
fav_movies = ["The Matrix", "The Avengers", "Spider-Man", "Superman", "The Lion King"]
print(fav_movies[0], fav_movies[1], fav_movies[2], fav_movies[3], fav_movies[4])

# The number of items in the list
print(len(fav_movies))

# Add another movie to the list
fav_movies.append("Iron Man")
print(fav_movies)

# Insert another movie - the list start from 0
# The number below as 1, will put the movie after the "The Matrix"
fav_movies.insert(1, "Batman")
print(fav_movies)

# Delete a movie
# del(fav_movies[2])
# print(fav_movies)

# For Loop
for movies in fav_movies:
    print(movies) 
    
# Challenge - Loop 40 times and print the number of the loop times 2. eg. 2, 4, 6, 8....

# for number in range(40):
    # print((number + 1) * 2)
    
# Dictionaries - with dictionaries curly brackets {}
# First is the Key 
# followed by a :
# Second is the Value
cats = {"Jane":6,
        "Tom":14,
        "Sara":8}
print(cats)
print(cats["Tom"])

# Add a name to the dictionary
cats["Wilson"] = 1
print(cats)

# Delete a cat from the dictionary
del(cats["Tom"])
print(cats)
print(len(cats))

text = """
Hanuman Chalisa In English And With Description In English

Shri Guru Charan Saroj Raj 
Nij mane mukure sudhar
Varnao Raghuvar Vimal Jasu
Jo dayaku phal char

After cleansing the mirror of my mind with the pollen dust of holy Guru's Lotus feet. 
I Profess the pure, untainted glory of Shri Raghuvar which bestows the four fold fruits 
of life.(Dharma, Artha, Kama and Moksha).

Budhi Hin Tanu Janike
Sumirau Pavan Kumar
Bal budhi Vidya dehu mohe
Harahu Kalesa Vikar

Fully aware of the deficiency of my intelligence, I concentrate my attention on Pavan Kumar 
and humbly ask for strength, intelligence and true knowledge to relieve me of all blemishes, 
causing pain.

Jai Hanuman gyan gun sagar 
Jai Kapis tihun lok ujagar

Victory to thee, O'Hanuman! Ocean of Wisdom-All hail to you O'Kapisa! (fountain-head of 
power,wisdom and Shiva-Shakti) You illuminate all the three worlds (Entire cosmos) with 
your glory.

Ram doot atulit bal dhama 
Anjani-putra Pavan sut nama

You are the divine messenger of Shri Ram. The repository of immeasurable strength, 
though known only as Son of Pavan (Wind), born of Anjani.

Mahavir Vikram Bajrangi 
Kumati nivar sumati Ke sangi

With Limbs as sturdy as Vajra (The mace of God Indra) you are valiant and brave. 
On you attends good Sense and Wisdom. You dispel the darkness of evil thoughts.

Kanchan varan viraj subesa 
Kanan Kundal Kunchit Kesa

Your physique is beautiful golden coloured and your dress is pretty. 
You wear ear rings and have long curly hair.

Hath Vajra Aur Dhuvaje Viraje 
Kandhe moonj janehu sajai 

You carry in your hand a lightening bolt along with a victory
(kesari) flag and wear the sacred thread on your shoulder.

Sankar suvan kesri Nandan As a descendant of Lord Sankar, you are a comfort and pride
Tej pratap maha jag vandan of Shri Kesari. With the lustre of your Vast Sway, you are
propitiated all over the universe.

Vidyavan guni ati chatur 
Ram kaj karibe ko aatur 

You are the repository of learning, virtuous and fully accomplished, always keen to 
carry out the behest's of Shri Ram.

Prabu charitra sunibe ko rasiya 
Ram Lakhan Sita man Basiya

You are an ardent listener, always so keen to listen to the narration of Shri Ram's 
Life Stories. Your heart is filled with what Shri Ram stood for. You therefore always 
dwell in the hearts of Shri Ram, Lakshman and Sita.

Sukshma roop dhari Siyahi dikhava
Vikat roop dhari lanka jarava

You appeared before Sita in a Diminutive form and spoke to her in humility. 
You assumed an awesome form and struck terror by setting Lanka on fire.

Bhima roop dhari asur sanghare
Ramachandra ke kaj sanvare

With over-whelming might you destroyed the Asuras (demons) and performed all tasks 
assigned to you by Shri Ram with great skill.

Laye Sanjivan Lakhan Jiyaye 
Shri Raghuvir Harashi ur laye

You brought Sanjivan (A herb that revives life) and restored Lakshman back to life, 
Shri Raghuvir (Shri Ram) cheerfully embraced you with his heart full of joy.

Raghupati Kinhi bahut badai 
Tum mam priye Bharat-hi sam bhai

Shri Raghupati (Shri Ram) lustily extolled your excellence and said: 
"You are as dear to me as my own brother Bharat."

Sahas badan tumharo yash gaave 
Us kahi Shripati kanth lagaave

Thousands of living beings are chanting hymns of your glories; saying thus, Shri 
Ram warmly hugged him (Shri Hanuman).

Sankadik Brahmadi Muneesa 
Narad Sarad sahit Aheesa

When prophets like Sanka, even the Sage like Lord Brahma, the great hermit Narad 
himself, Goddess Saraswati and Ahisha (one of immeasurable dimensions).

Yam Kuber Digpal Jahan te 
Kavi kovid kahi sake kahan te 

Even Yamraj (God of Death) Kuber (God of Wealth) and the Digpals (deputies guarding 
the four corners of the Universe) have been vying with one another in offering 
homage to your glories. How then, can a mere poet give adequate expression
of your super excellence.

Tum upkar Sugreevahin keenha 
Ram milaye rajpad deenha
Tumharo mantra Vibheeshan mana
Lankeshwar Bhaye Sub jag jana

You rendered a great service to Sugriv. You united him with Shri Ram and he installed 
him on the Royal Throne. By heeding your advice, Vibhishan became Lord of Lanka. 
This is known all over the Universe.

Yug sahastra jojan par Bhanu 
Leelyo tahi madhur phal janu

On your own you dashed upon the Sun, which is at a fabulous distance of thousands of miles, 
thinking it to be a sweet luscious fruit.

Prabhu mudrika meli mukh mahee 
Jaladhi langhi gaye achraj nahee

Carrying the Lord's Signet Ring in your mouth, there is hardly any wonder that you 
easily leapt across the ocean.

Durgaam kaj jagat ke jete
Sugam anugraha tumhre tete

The burden of all difficult tasks of the world become light with your kind grace.

Ram dware tum rakhvare, 
Hoat na agya binu paisare

You are the sentry at the door of Shri Ram's Divine Abode. No one can enter it 
without your permission,

Sub sukh lahai tumhari sarna 
Tum rakshak kahu ko dar na

All comforts of the world lie at your feet. The devotees enjoy all divine pleasures 
and feel fearless under your benign Protection.

Aapan tej samharo aapai 
Teenhon lok hank te kanpai 

You alone are befitted to carry your own splendid valour. All the three worlds 
(entire universe) tremor at your thunderous call.

Bhoot pisach Nikat nahin aavai 
Mahavir jab naam sunavai

All the ghosts, demons and evil forces keep away, with the sheer mention of your 
great name, O'Mahaveer!!

Nase rog harai sab peera 
Japat nirantar Hanumant beera

All diseases, pain and suffering disappear on reciting regularly Shri Hanuman's holy name.

Sankat se Hanuman chudavai 
Man Karam Vachan dyan jo lavai

Those who remember Shri Hanuman in thought, words and deeds with Sincerity and Faith, 
are rescued from all crises in life.

Sub par Ram tapasvee raja 
Tin ke kaj sakal Tum saja

All who hail, worship and have faith in Shri Ram as the Supreme Lord and the king of penance. 
You make all their difficult tasks very easy.

Aur manorath jo koi lavai 
Sohi amit jeevan phal pavai

Whosoever comes to you for fulfillment of any desire with faith and sincerity, Will he alone 
secure the imperishable fruit of human life.

Charon Yug partap tumhara 
Hai persidh jagat ujiyara

All through the four ages your magnificent glory is acclaimed far and wide. 
Your fame is Radiantly acclaimed all over the Cosmos.

Sadhu Sant ke tum Rakhware 
Asur nikandan Ram dulhare

You are Saviour and the guardian angel of Saints and Sages and destroy all Demons. Y
ou are the angelic darling of Shri Ram.

Ashta sidhi nav nidhi ke dhata 
Us var deen Janki mata 

You can grant to any one, any yogic power of Eight Siddhis (power to become light and heavy at will) 
and Nine Nidhis (Riches,comfort,power,prestige,fame,sweet relationship etc.)
This boon has been conferred upon you by Mother Janki.

Ram rasayan tumhare pasa 
Sada raho Raghupati ke dasa

You possess the power of devotion to Shri Ram. In all rebirths you will always remain 
Shri Raghupati's most dedicated disciple.

Tumhare bhajan Ram ko pavai 
Janam janam ke dukh bisravai

Through hymns sung in devotion to you, one can find Shri Ram and become free from 
sufferings of several births.

Anth kaal Raghuvir pur jayee 
Jahan janam Hari-Bakht Kahayee

If at the time of death one enters the Divine Abode of Shri Ram, thereafter in all future 
births he is born as the Lord's devotee.

Aur Devta Chit na dharehi 
Hanumanth se hi sarve sukh karehi

One need not entertain any other deity for Propitiation, as devotion of Shri Hanuman 
alone can give all happiness.

Sankat kate mite sab peera 
Jo sumirai Hanumat Balbeera

One is freed from all the sufferings and ill fated contingencies of rebirths in the world. 
One who adores and remembers Shri Hanuman.

Jai Jai Jai Hanuman Gosahin 
Kripa Karahu Gurudev ki nyahin

Hail, Hail, Hail, Shri Hanuman, Lord of senses. Let your victory over the evil be firm and 
final. Bless me in the capacity as my supreme guru (teacher).

Jo sat bar path kare kohi 
Chutehi bandhi maha sukh hohi 

One who recites Chalisa one hundred times, becomes free from the bondage of life and death 
and enjoys the highest bliss at last.

Jo yah padhe Hanuman Chalisa 
Hoye siddhi sakhi Gaureesa

All those who recite Hanuman Chalisa (The forty Chaupais) regularly are sure to be benedicted. 
Such is the evidence of no less a witness as Bhagwan Sankar.

Tulsidas sada hari chera 
Keejai Das Hrdaye mein dera

Tulsidas as a bonded slave of the Divine Master, stays perpetually at his feet, he prays 
"Oh Lord! You enshrine within my heart & soul."

Pavantnai sankat haran, 
Mangal murti roop.
Ram Lakhan Sita sahit,
Hrdaye basahu sur bhoop.

Oh! conqueror of the Wind, Destroyer of all miseries, you are a symbol of Auspiciousness.
Along with Shri Ram, Lakshman and Sita, reside in my heart.
Oh! King of Gods.

"""
print(text)
print(len(text.split()))

text = """
a b c A a b
"""
#print(text.split())

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


# Functions - To give a name to a chunk of code
# def - define a function
def bark():
    print("Woof woof!")
    print("I am a dog!")
# Calling a function
bark()

# Challenge - Create a function called hello that prints "Hello Himat!"
def hello():
    print("Hello Himat!")
hello()

# Parameters - Pass information into a function
# name is a parameters
def hello(name):
    print(f"Hello {name}!")
hello("Himat")

def add_numbers(num1, num2):
    print(num1 + num2)
add_numbers(4, 8)
add_numbers(3, 7)

# Challenge - Create a function called dog_info that takes in a dog's age and name 
# prints a sentence about the dog
def dog_info(age, name):
    print(f"The dog name is {name} and it's age is {age}")
dog_info(3, "Chantelle")

# Return - Pass out of information
def double(number):
    return number * 2

new_number = double(5)
print(new_number)

# Challenge - Create a function that returns a string in all caps
def uppercase(upper_text):
    return upper_text.upper()
print(uppercase("This is a text in capital letters"))

names = ['Nick', 'Jane', 'Sara']

for name in names:
    print(uppercase(name))
    
    
# Input
user_text = input('Enter some text: ')
print(user_text)
# print(user_text.upper())

user_number = input('What do you want to double? ')
print(int(user_number) * 2)

# Challenge - First ask for some text, and then prompt 
# "Enter 1 to Uppercase ans 2 to lowercase: " and then 
# either upper or lowercase it

enter_text = input('Enter some text: ')

prompt = input('Enter 1 for uppercase or 2 for lowercase: ')

# The prompt is a string hence the 1 or 2 is in ""
if prompt == "1":
    print(enter_text.upper())
if prompt == "2":
    print(enter_text.lower())

    
