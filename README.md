This repository is an interview assignment from Band Protocol for backend developer position.

Problem 1 : The function checkBoy() will take strings input of R and S and give back return of either "Good boy" or "Bad boy". 

The function acheive this by using checking methods where it go into for loops for all char in the string once and each time increment shotCount variable by 1 if the character is S and minus 1 if it is R.
shotCount will never go below 0 in case of multiple revenges, this is done to prevent revenge counting after next shot have been fired.
And next for each time the function loop, it will check if shotCount is more than the rest of remaining char left or not. This is done because I assume in best case scenarios where all remaining character is revenges.
If the shotCount ever exceed remainingLength we will know for sure that revenge is not poissible and thus return "Bad boy".

The rest of if/else statement is to handle edge cases and cases where input is invalid.
The time complexity is O(n) where n is the number of character inside of the string.

Problem 2 : The function findMaxChicken() will take object input that have 3 attributes, 1.chicken being number of chicken 2.roofLength being the size of roof that superman can carry and 3. chickenIndexes being the position on the line where chicken would be located.
This function would then return the maximum number of chicken that superman can protect with the roof of that length that he is carrying.

Using sliding window approach where I use 2 pointers left and right to iterate inside of the chickenIndexes array. The first for loop is to create right iterator and iterate across the line where chicken exist.
Second while loop purpose is to check if the chicken position at the left most iterator and right most iterator distance is more than the roof length or not, and when it is more our window is longer than the roof so we must increment left iterator up.
The left pointer only moves forward and never backward. Across all iterations of the for loop, left progresses at most n times, just like right.
This ensures that the total number of left increments over the entire execution is O(n) even though the while loop appears nested.
Next, for every for loop that happen the function will check for maxChickens which is just the length of our window (right - left + 1) and compare the length to previous maxChicken of last loop until all the indexes have been went through.

The rest of if/else statement is to handle edge cases and cases where input is invalid.
The time complexity is O(n) where n is the number of character inside of the chicken indexes.

Problem 3 : I decide to use django as a module to fufil the requirements. 

I design a main application call "api" that handle all of the GET and POST request. And inside of views.py contain 2 class-based views that fulfil both first and second requirement.
class PostPayloadView(View) handle POST of json information to the specified url. Right now inside of my code I have the json payload being randomly generated but this can easily be change to real data from database if need to be integrate into main application.
class GetTransactionView(View) handle GET hash code from the specified second url and returning the recieved json respond.

Scalability, reliability, and performance will be industry standard. The module that I have create could be easily plugged into existing django project by just configuring settings.py and adding it.
Or if the existing application isn't a django project, this application can run fully standalone and fulfil every requirement by itself also.
Reliability and performance would also be very robust since this is a very simple api that just read and return value.

On my design choices of where I use 2 view instead of one. I was considering using just 1 view that once recieve the data from the url would send GET request immedietly within the same view to get the hash code also. This approach would reduce the view/url path bloat.
But I decided against it since we might not be always needing the hash code depending on the situation.
