<<<<<<< HEAD
# shelfradar-gateway-notify
Notification Librarian
=======
# the_library

Thin query service for test that can be deployed as a Lambda function. 

Search code can be found in flaskRouter file. All searches starts with :

fuzzy_match.fuzzy_spine_search(searchstring)

Submission to flask endpoint requires the payload as json in the body. 

i.e. { "searchterm": "one fish two fish seuss" }

Searchstring expects : "{book title} {author name}"

Subtitle searching is included, so feel free to include subtitles. 

Has debug config for VSCode (f5 to run + debug).

Can be run as service : 
docker-compose up 


>>>>>>> Initial Commit
