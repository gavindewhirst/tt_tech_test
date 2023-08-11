# TrackTitan Technical Test

## Exercises

* Boilerplate has been provided for you. You should only need to change src/routes/config.ts and create new files in src/routes/routeHandlers.
* Ideally you should not spent more than 3 hours on the below.
* Do not create explicit unit tests, but you should be able to demonstrate you have tested your solutions.
* Code comments as you feel is most appropriate. I am not expecting comments everywhere, or that they are even required.
* All responses should be in JSON.
* If you are less experienced with Typescript, feel free to replace the boilerplate with what you are comfortable with. If for example you want to do this in Javascript, ideally enable JS in the tsconfig and create the new files in JS, integrating them to the existing boilerplate; otherwise create however you wish. We will discuss the code in the next technical round.
* If you have any problems, please contact nic@titanacademy.io

### Exercise 1

Create a new route "/lap_times" with GET method that returns the data provided by functions 'scanAllTable' and 'getUserSession' in src/data.

When given query string param 'userId' return all the lap time data for this user (array). When given query string param 'userId' AND 'sessionId' return only the lap time data for this user's session (single session item).

* 'userId' query string parameter is optional.
* 'sessionId' query string parameter is optional and can only be provided if 'userId' query string parameter is also present.

Note: Try to think from the perspective of a frontend engineer on what this API should look like.

### Exercise 2

Add new optional query string param 'sort'.

* When this 'sort' query string param is equal to 'lapTime', sort the response by the lap time DESCENDING for the sessions returned.
* When this 'sort' query string param is equal to 'userId', sort the response by the user id, DESCENDING for the sessions returned.
* When this 'sort' query string param is equal to 'userId,lapTime', sort the response by the user id and THEN the lap time, both DESCENDING. I.E if the userIds are equal then the items should be sorted by lap time descending. Equally if 'sort' query string param is equal to 'lapTime,userId' sort by lap time and then userId.

Note: Try and think about what future potential business asks may be when writing your code, and how you could therefore make it more future proof. Not required to implement this, be wary of time, but I'd like you to at least think about this.

### Excercise 3

Create a new route 'ratings'.

Rate the users based on their session data lap times and return a list of userIds from best to worst from this new 'ratings' route. You can assume all these sessions are for the same track/car.

In this rating system:
* The LOWER the lap time the BETTER the user, therefore the HIGHER the rating.

Note: A "rating" is a numerical value that summarises the user's ability. This is different to a "ranking" which is closer to a leaderboard. Implement whatever you wish, feel free to email me if you want to validate any assumptions, but if you'd like inspiration for a more complete solution you can get some inspiration from: https://en.wikipedia.org/wiki/Sports_rating_system

## Boilerplate 
* ```npm run start``` will run the server in production mode.
* ```npm run dev``` will run the server in developer mode, with hot reloading enabled.