# Twitter-js-to-csv


## Backgorund 
Twitter allows its users to [downlaod](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive) data in different formats including .json, .html, and .js file formats. However, these formats provide less manuverability options. Due to this limitation, the scope of things that you can do with your Twitter archive also gets limited. For instance, you will have a hard time preprocessing your data for a machine learning project.

With a view to make Twitter archive more useful for developers, this repository will help convert the .js (JavaScript) files you get in your Twitter dump to csvs. Csvs are more manuverable and will increase the efficiency of your workflow in case you are aiming to use Twitter Archive in one of your projects.


## Method
The `script.py` file uses a recursive technique to parse the Twitter dump. Before that,
1. The script reads through all the .js files
2. It uses string manipulation techniques to make the file structure similar to a JSON

After using recursion, the script saves the output (i.e. single csv per .js) into the desired directory.

## Input
Once you download your Twitter archive in .js format, unzip the dowload file. Within the unzipped directory, you will have a `data` folder. This fodler will contain all the .js files that would be the part of your dump. 

Give the path of `data ` folder to the variable named path in `script.py`.

## Output
Output of `script.py` is a .csv per .js file. It will create csvs and store them in a separate directory called `csvs` that would be in the same path as the input `data`directory. 
