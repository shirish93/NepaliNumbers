All Nepali Numbers Ever
=======================
Inspired by [this Twitter account posting Finnish numbers] (https://twitter.com/everyfinnishno), 
this is a python bot that lists all Nepali numbers.

##ToDo:

* Generalize to all Languages
* Automatic generalization: Pick language data from wiki automatically, and automatically figure out the schemes

##The Start

###Getting all the numbers
I considered writing all unique words by hand, but considering [all Nepali numbers till 100 are unique, with no repeting parts] (http://en.wikipedia.org/wiki/Numbers_in_Nepali_language), decided to use the wiki.

Then I opened up Google sheets, used my favorite function ImportHTML, and BAM, a list of all Nepali Numbers. Entering the formula in sheets will give
the wiki table in spreadsheet.
*
>=importHTML("http://en.wikipedia.org/wiki/Numbers_in_Nepali_language", "table" ,1)

Unfortunately, the list skips most of the numbers after 30. That's no good. Back to the Google.

[Thank gods for the internets!] (http://www.imnepal.com/nepali-numbers/)

From that, we extract the words for numbers.

Now that we have raw data ready, we're ready to get coding!