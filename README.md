# tradr-helpr
Entry to FrostHack 2021.

## Links
Link to the web server hosted on Windows server machine on Google Cloud - [tradr-helpr]("http://34.123.154.196")

## What is tradr-helpr?
If you are a day trader, you would know how difficult it is to be up-to-date with the news in realtime, with a lot of news sources being available. And you would also know how important it is to know about some specific news at the right time. So we made a bot which will be **watching** all the business news channels available through live stream, and output the recommendation/suggestion or even a news related to stock markets on a website from disctinct news channels.

## Tech Stack used
We hosted an Apache web server on Windows Server 2019 DataCenter for Containers on Google Cloud Platform. Then, we have python scripts to fetch the live stream from respective channel's YouTube livestream. We save the data in a JSON file on the server to be used by the website(for now, we are also planning to make apps).

## Workflow of the project
We execute two python scripts stored on the apache web server, one python script downloads the live stream from the respective channel's YouTube live stream and keeps saving 30 seconds length of videos. Then the other python script is called when each 30 seconds of video is downloaded. The second python script first converts the video into a .WAV file to be converted to text using the Google's SpeechRecognition python model. Then the converted text from the speech is added to a transcipt file which will have the whole transcript of the live stream from the beginning. We then pass this transcript file to a python model which selects the keywords and understands the words and outputs the following things: 
1. Time at which the recommendation was given
2. Person who is giving the recommendation
3. Name of the asset of which the recommendation is given of
4. Levels given, if any such as buy above/below, sell above/below , or just hold/wait to buy/sell
5. Stoplosses and target, if any

Then the output is converted to a JSON file and saved in the same web server. Then the website fetches data from the JSON file saved in the server.

We also thought of merging all the 30 seconds video together to keep saving the livestream from the beginning and while producing the output, we trim out the recommendation from the main big file of video that we have been merging and display both, the text output and the trimmed video with the suggestion.

## Tesing
We were able to fetch the live stream, convert it to transcript within a minute on the Windows server machine on the Google Cloud, but we can also reduce this time by making the code more efficient and using a powerful machine with great internet connection.

## Problems Faced
The transcipter part of the python script was running fine on our pc, but when we upload the files to the server hosted on Google CLoud, it was giving out rubbish values. We tried a lot and a lot of things that wasted our 10 hours because of the google cloud itself. As the python script was running properly on our pc we thought of hosting it on our pc but again that was not successful and wasted a lot of time. At last we were able to make it working with the help of VPN on the google cloud server.
