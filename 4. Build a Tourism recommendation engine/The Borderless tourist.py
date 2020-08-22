"""
	Author: AnOnYmOus001100
	Date: 22/08/2020
	Description:
	The Boredless Tourist
Welcome to The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the pace of your life. We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by. Let’s get started!

Setting Up Your Project:
1.
We here at The Boredless Tourist believe that mistakes should be easily corrected, so we keep all of our code version controlled using git.

Start by running git init in the terminal.

2.
We’ll be doing most of our coding in script.py so we want to make sure that we are tracking that in git.

Add script.py to git’s staging area.


3.
Let’s create the first commit for this project.

Perform a git commit with the message "initial commit"


4.
Now let’s create some data that we’re going to use to test the functionality that we create for The Boredless Tourist.

The first is our list of destinations that we’re going to be using.

Create a list with the following destinations and save it into a variable called destinations.

“Paris, France”
“Shanghai, China”
“Los Angeles, USA”
“São Paulo, Brazil”
“Cairo, Egypt”

5.
And let’s define a test traveler to see how our functionality is working so far.

Create a test_traveler variable. Assign to it the following list:

['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes historical buildings and art. Erin is in China right now, hopefully we can find some good places to show her.

6.
Looks like we’ve got some good sample data to get started with. Let’s commit these changes.

First, save the file, then add script.py to the git index using git add.

7.
Next, perform a git commit with the message "Added test objects".

Travelling To Faraway Lands
8.
Now that we have test data for a traveler and a list of destinations that we can use, we can start building some of the Boredless Tourist‘s functionality.

When a traveler arrives at a destination, we want to know where they are! Since we use lists for all of our data — we are going to identify each location based on its index in our destinations list. But we need to retrieve that index first.

Define a function called get_destination_index(). It should take a single parameter, destination, the destination as a string.


9.
In the body of get_destination_index(), find the index of destination and save the results into a variable called destination_index.


10.
In the body of get_destination_index(), after you’ve defined destination_index, return it.


11.
Test out your function. Try to call get_destination_index() with the argument "Los Angeles, USA".

Print out the results.

Save your code and then run it by typing python3 script.py in the terminal. Is the destination index for “Los Angeles, USA” equal to 2?

12.
Try to call get_destination_index() with the argument “Paris, France” instead. Since that is the first element on our destinations list, it should return the index 0.

13.
What happens if we call get_destination_index() with a destination not in our destinations list?

Try it now: call get_destination_index() with the argument “Hyderabad, India”. What happens?

14.
If you used the .index() method to get the index of a destination from the list, you’ll notice that calling get_destination_index() with data that is missing from our destinations list will raise a ValueError.

Don’t add any logic to avoid triggering this ValueError, it’s going to be useful for us in the future.

15.
Now let’s define a function called get_traveler_location().

get_traveler_location() is going to take a single parameter, traveler.

16.
In the body of get_traveler_location(), access the traveler’s destination string and save it into traveler_destination.


17.
Use traveler_destination along with get_destination_index() to retrieve the index of the destination where the traveler is. Save the index of the traveler’s destination into the variable traveler_destination_index.


18.
Make get_traveler_location() return the destination index of the traveler by returning traveler_destination_index.

19.
Create a variable called test_destination_index. Save the results of calling get_traveler_location() with our test_traveler.

20.
Print out test_destination_index.

21.
Save your code and run it by calling python3 script.py in the terminal.

Is the test_destination_index you created equal to 1?

22.
Let’s save our work to the git tracker. Add script.py to the git index with git add.

23.
And commit your changes with the message

"Added logic to find traveler destinations and convert to internal data"

Visiting Interesting Places
24.
Now we want to create and maintain a list of attractions. Let’s start by defining a list called attractions.


25.
Actually, we want attractions to be an empty list for every destination in destinations. You can do this with this code:

attractions = [[], [], [], [], []]
But there are other ways to accomplish the same thing: by looping through destinations or with a list comprehension.

Define attractions to be a list of 5 (one for each test destination) empty lists using a loop or list comprehension.


26.
Print out your attractions. Save, and then run your code by typing python3 script.py in the terminal.

Does attractions look like:

[[], [], [], [], []]
27.
Now let’s create a function called add_attraction(). This function should take two parameters: destination, the name of the location and attraction, the attraction.

28.
First we should attempt to find the index of the destination. Use get_destination_index() with the passed in destination in order to retrieve the index of the destination. Save the results into destination_index.

29.
What happens if the destination passed in to add_attraction() doesn’t exist? Right now we want to ignore it.

Add a try block to the body of add_attraction() and catch the possible ValueError that could happen when you define destination_index.


30.
In your except block, we don’t want to add an attraction to a destination we don’t have, so simply return.

31.
If the destination does exist, then we already have a list for it in attractions. Use the destination_index to find the appropriate list in attractions and save that list to attractions_for_destination.


32.
Append the attraction passed into add_attraction to the list attractions_for_destination.

That’s all we want this function to do, so we can return after adding the attraction to the list.

33.
Try adding the following attraction:

['Venice Beach', ['beach']]
To the “Los Angeles, USA” destination by calling add_attraction() with the two as arguments.

34.
Print out attractions. Then save and run your code with python3 script.py. Your print statement should render the following:

[[], [], [['Venice Beach', ['beach']]], [], []]
If it doesn’t something went wrong with add_attraction().


35.
Let’s add a few more interesting places to go, paste the following code to add a few more attractions:

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
36.
Let’s add this change to our git repo. First add script.py to your git index.

37.
Then commit the changes with the message

"Created attractions and functionality for adding new attractions"
Finding the Best Places to Go
38.
We want to be able to help our traveler’s find the most interesting places in a new city for them. In order to do that we need to match their interests with the possible locations in a city.

Write a function called find_attractions() that takes two parameters: destination, the name of the destination and interests, a list of interests.

39.
We’ll need the city’s destination_index to look up its attractions in our attractions table.

Create a variable called destination_index and save the destination’s index to it using get_destination_index()

40.
Look up that destination’s attractions by indexing into attractions with destination_index. Save this into the variable attractions_in_city.


41.
Create a new list called attractions_with_interest. Make it empty when declaring it, we’ll save attractions into this list if they match one of our interests.

42.
Create a loop over attractions_in_city saving each item in the list into the temporary variable possible_attraction.


43.
For each attraction, retrieve the tagged information about it. The tags are all saved in the second place (index 1) in the attraction. In the body of the for loop, save the attraction’s tags into the variable attraction_tags.


44.
After retrieving the attraction tags, we want to see if any of the given interests are in attraction_tags. In order to do this, we’re going to loop through the interests and check if any of them are in attraction_tags.

Create a for loop in the body of the current for loop to loop through each interest in interests.


45.
For every interest in interests, check if that interest is in attraction_tags.

If the interest is in the attraction_tags, append possible_attraction to attractions_with_interest.

46.
At the end of your function, return attractions_with_interest. Remember to unindent so you don’t accidentally return before both the for loops finish running!

47.
Let’s test out our function! Call find_attractions() with "Los Angeles, USA" and ['art'] as the two arguments and save the results to la_arts.

48.
Print out la_arts.

Save, and run your code by typing python3 script.py in the terminal. It should have returned the following:

['LACMA', ['art', 'museum']]

49.
We don’t want to show the tags to our users when we recommend things to them, so let’s just append the name of each attraction.

In the body of find_attractions(), find where you append possible_attraction to attractions_with_interest. Change this so you only append possible_attraction[0] which will only append the name.

50.
Save and try rerunning your la_arts test codewWith python3 script.py Printing it now should just print the following:

['LACMA']
51.
Looks like we’ve got an interest finder! Let’s save these changes to our git repo! First let’s add script.py to the git index using git add.

52.
Now let’s commit the changes with the message "Added interest finder logic"

See The Parts of a City You want to See
53.
Now let’s get to the main event, connecting people with the attractions that they are interested in.

Define a function called get_attractions_for_traveler() that takes a single parameter, traveler.

54.
Let’s separate out the traveler’s data. Save the following data:

Save traveler[1] into a variable called traveler_destination.
Save traveler[2] into a variable called traveler_interests.
55.
Call find_attractions() with the two arguments traveler_destination and traveler_interests. Save the results into traveler_attractions.

56.
Create a new string, this is what we’ll want to show our traveler when they open our application:

"Hi Dorothy Bortman, we think you'll like these places around Seattle, USA: the SAM, the Pike Place Market."
Start with the beginning, just "Hi " (with a space afterwards).

Save "Hi " into a variable called interests_string.

57.
Update interests_string to include the name of the traveler. The traveler’s name can be found at traveler[0]. “Add” this to interests_string so that it includes the name of the traveler.


58.
We’ll want to add a little more to the interests_string before we list the interests. Add the following:

This string:
", we think you'll like these places around "
The place
59.
Lastly, we want to add the names of the places to go! Loop through traveler_attractions and for every attraction in the list concatenate that attraction to interests_string. You can add commas and spaces to interests_string to make it more legible as well.

60.
After you’re finished adding all the names of the interests, return interests_string

61.
Let’s give it a test drive! Try calling get_attractions_for_traveler() with the following argument:

['Dereck Smill', 'Paris, France', ['monument']]
Save the results of get_attractions_for_traveler() into the variable smills_france.

62.
Print out smills_france. Save your work and run it by typing python3 script.py in the terminal. You should get a string that looks like the following:

"Hi Dereck Smill, we think you'll like these places around Paris, France: the Arc de Triomphe"

63.
Looks great! Let’s add it to our git repository! First git add script.py.

64.
Now let’s commit it! Use this message:

"Added function to generate message for traveler and present attractions they might be interested in."
"""

#Code:
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  #for i in range(len(destinations)):
    #if destination == destinations[i]:
      #destination_index = i
  destination_index = destinations.index(destination)
  return destination_index

print (get_destination_index("Los Angeles, USA"))
print (get_destination_index("Paris, France"))
#print (get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print (test_destination_index)

#attractions = [[], [], [], [], []]
"""
attractions = []
for l in destinations:
  attractions.append([])
"""
attractions = [[] for l in destinations]
print (attractions)

def add_attraction(destination,attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destinaition = attractions[destination_index].append(attraction)
  except SyntaxError:
    return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print (attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  
  for ac in attractions_in_city:
    possible_attraction = ac
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA",['art'])
print (la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)

  interests_string = "Hi "+ str(traveler[0]) + ", we think you'll like these places around " + str(traveler[1]) + ": the "
  for attraction in traveler_attractions:
    interests_string += str(attraction)
  
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print (smills_france)
