# numonster

## Problem statement

I want to create a game based on guessing number to make guess number game more
 interesting. In our game, monsters (small creatures and bosses) launch random
 numbers of varying lengths as “attacks.” And players have to guess number to
 avoid taking damage. Our game has different types of characters and damage.
 The game challenges players to use both luck and strategy to survive each round.

## Background


This project combines elements of classic turn-based strategy games with
guessing number feature.If players can guess the right number, player can avoid
damage. The project including

1. random function: Monsters would generate numbers of different length
2. different difficulty: players can choose different difficulty
3. different characters: players can choose their origin role which has
different life, defensive power, physical/magical power/real power
4. reward: After clearing a level player can earn new weapon or buffs to improve
their power

## Target users

Who are the intended users of the application for which you are making a
prototype? What are their needs? This section does not need to be long, but
avoid being too broad in your description of the users. "Anyone who wants it"
is not a specific enough set of people to target an application.

1.students who like role playing games
2.gamers who enjoy turn_based strategy
3.people who like playing games based on luck

## Minimum Viable Product/Prototype

Consider what the simplest solution to the problem above would be. For this
project, you are not required to produce a completely polished product fit for
general use, but you should still take into account usability when deciding
viability. In this section, describe a version of your application with the
fewest possible features, but which would still be useful to the target users.

For the purpose of the proposal stage of the project, MVPs do not require data
to persist from one execution of the program to another. Having an MVP which is
useful as long as the user does not close the application and re-open it, is
sufficient. If persistent data is desirable, it should be included as the first
NTH (nice-to-have) feature.

* Feature 1: Basic Turn _based system: a single battle round (monster launch random number)
* Feature 2: guessing feature: if guess correct then gamer can avoid damage
* Feature 3: character selection: choose different character with different HP,
defensive power and damage power
* Feature 4: have random reward after clearing every level

## User Interface Design



Home page: choose character and level
play page:Shows the monster’s “attack” (the random number).
Includes an input field for the guess and a submit button.
A message area that informs the player whether their guess was correct or shows
damage taken.
Shows a summary of the battle.
Displays the reward earned (new weapon or buff).


## Implement First Stage of MVPThe drawings may be done:

*

Your code must be able to run a Flask server and serve an HTML webpage in order
to get these marks.

Using your user interface and the code provided in `src/server.py` as a
starting point, write a flask server for your application. The server should
have all the required routes for your MVP, each one returning the required HTML
to the browser. Your first stage should be able to display each of the web
pages and allow users to enter information, but does not need to store or
process any information.

For web pages which involve displaying information in a certain layout, for
this stage you may hard-code some sample data within the route which needs to
display the data. When you later go to implement your back end, the hard-coded
sample data would be replaced with accessing the information entered by the
user.

## "Nice to have" features

Describe any additional features that would improve the experience of using
your prototype for the target users. These features should not be strictly
necessary for the prototype to be useful, but may include things most users
would expect as standard. This could include things like: being able to
register an account, saving user preferences, or social media integration.

* Feature 1: Multiple Levels: Increasing difficulty with more challenging monsters.
* Feature 2: Player Progression: Save progress between levels and allow upgrades over time.
* Feature 3: monster have different stage and have different attribute.
* ...

## Stretch goals

Include here any features that would make your prototype really shine, but
which you are not confident you can implement in the time available for this
project. Don't be afraid to be ambitious in selecting stretch goals. See the
marking scheme for the final prototype for information on what marks are
available for completing stretch goals.

* Goal 1: Monster can based player's behaviors to adjust attack or defend
* Goal 2: Motion screen
* Goal 3: more detailed characters and their specific weapon
* ...

## Marking Criteria

The table below contains the marking criteria for this proposal. Don't delete
it as your tutor will fill it in during marking.

| Criteria | Mark | Notes |
| -------------------------------------------------------- | ---- | --- |
| Clearly defined problem to be solved (1 mark)                                     |      | |
| Background includes information necessary for building a prototype (2 mark)       |      | |
| Appropriate set of target users (1 marks)                                         |      | |
| MVP is both minimal and viable (1 marks)                                          |      | |
| The user interface design clearly conveys what will be visible upon completion of the MVP implementation (1 mark) | | |
| Code in first stage of project produces an appropriate result (2 marks)           |      | |
| Comprehensive list of "nice to have" features (1 mark)                            |      | |
| Appropriate ambitious stretch goals (1 mark)                                      |      | |
