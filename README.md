# PowerPlant Production - Sebastian Olivera  

The challenge asks for a REST API (in docker) to solve the unit commitment problem, using an algorithm handmade and calculating how much power each plant produces to reach a given load (in payload) and this should be optimized on merit order.
The api I build is made with a simple Flask and dockerfile
To build the docker all we need to do is (in the working directory "solutionNG")

docker build -t ng_solution .

This will print in terminal the progress and once its complete we can run the docker:

docker run -p 8888:8888 ng_solution

Api is exposed on the port 8888 as requested in instructions.

The requirements, is just the flask library. I didnt have enough time to add some loggings unfortunetly. 

To test the results, I used postman and gave it the payload_3 and it returns exactly response_3

Sadly, this doesnt necessarily mean this code is bulletproof.

# Notes:

Things I would change if I had more time would be:
- I dont really check / validate data. WHich for this small test is not a problem but for a robust code it should validate the data im receiving in the request. And validate the type of the fields, to avoid "None" "null" or else values that might break this code.
- Add a proper validation for the sum of the power = load. Because of the way I calculate p, with some specific numbers / decimals, it could run into issues because of the way i round the float to 1 decima (as requested) this should have a "observer" or better named, a calculation error function, to ensure the sum of units is the same as the load.









