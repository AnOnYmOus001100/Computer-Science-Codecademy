"""
	Author: AnOnYmOus001100
	Date: 31/08/2020

Censor Dispenser
Overview
This project is slightly different than others you have encountered thus far on Codecademy. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you’ll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

Project Goals
You’ve recently gotten a job working in the IT department at one of Silicon Valley’s hottest new startups, AirWeb. The company is developing a state-of-the-art artificial intelligence engine designed to help provide a new perspective on the world’s problems. Interestingly, very few people know the details of AirWeb ‘s work and the company is very secretive about its technology, even to its own investors.

You report directly to the Head of Product, a person named Mr. Cloudy, and he has a very important task for you. You see, every month, the head researchers down in the lab send an email to the board of investors to tell them about the status of the project. Cloudy wants you to intercept these emails and censor any “proprietary information” included in them.

Setup Instructions
If you choose to do this project on your computer instead of Codecademy, you can download what you’ll need by clicking the “Download” button below. If you need help setting up your computer, be sure to check out our setup guides.

Tasks:

Prerequisites
1.
In order to complete this project, you should have completed the first 4 milestones of the Codecademy Pro Computer Science Path and the Learn Python: Strings lesson, or completed the first 6 sections of the Learn Python 3 course.

Project Requirements
2.
Write a function that can censor a specific word or phrase from a body of text, and then return the text.

Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning algorithms from the first email, email_one. Mr. Cloudy doesn’t care how you censor it, he just wants it done.

3.
Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.

Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
4.
The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’”

Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three.

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

5.
This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”

Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.

6.
Great job! The Board of Investors is none the wiser to what is going on in the lab and Mr. Cloudy is very happy.

Take a moment to look over your functions, are they the best they can be? As a challenge, make sure they:

Handle upper and lowercase letters.
Handle punctuation.
Censor words while preserving their length.

7.
Great work! Visit our forums to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.
"""

#Code:
# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

all_censored_terms = proprietary_terms + negative_words

# function for censoring work
def censor_word(text,word):
  text = text.replace(word.upper(),"")
  text = text.replace(word.lower(),"")
  text = text.replace(word,"")
  return text

#print (email_one)
#print(censor_word(email_one,"the"))

#function to censor list of words
def censor_wordlist(text,wordlist):
  text_in_lower = text.lower()
  # make it a list since strings are immutable
  text = list(text)
  for term in wordlist:
    index = 0
    while index < len(text):
      index = text_in_lower.find(term, index)
      # if nothing more is found, -1 is returned
      if index == -1:
        break
      if text[index-1] == ' ' or text[index-1] == '\n':
        for i in range(index, index + len(term)):
          text[i] = 'X'
      index += len(term)
  text = ''.join(text)
  return text

#print (email_two)
#print (censor_wordlist(email_two,proprietary_terms))

# function to censor negative words
def censor_negativewords(text, negative_wordlist):
  text = censor_wordlist(email_three, proprietary_terms)
  text_in_lower = text.lower()
  text = list(text)
  indexes = []
  for word in negative_wordlist:
    index = text_in_lower.find(word)
    if index != -1:
      indexes.append(index)
  indexes.sort()
  for term in negative_wordlist:
    index = indexes[0] + 1
    while index < len(text):
      index = text_in_lower.find(term, index)
      if index == -1:
        break
      if text[index-1] == ' ' or text[index-1] == '\n':
        for i in range(index, index + len(term)):
          text[i] = 'X'
      index += len(term)
  text = ''.join(text)
  return text

#print (email_three)
#print (censor_negativewords(email_three,negative_words))

# function to censor all
def censor_all(text, wordlist):
  text_split = text.split()
  censor_words_indexes = []
  new_indexes = []
  for i in range(len(text_split)):
    for j in range(len(wordlist)):
      if text_split[i].lower() == wordlist[j] or text_split[i][:-1].lower() == wordlist[j]:
        censor_words_indexes.append(i)
  for i in censor_words_indexes:
    new_indexes.append(i - 1)
    new_indexes.append(i)
    new_indexes.append(i + 1)
  
  for i in new_indexes:
    text_split[i] = len(text_split[i]) * 'X'
  
  text_split = ' '.join(text_split)
  return text_split

#print (email_four)
#print (censor_all(email_four, all_censored_terms))
