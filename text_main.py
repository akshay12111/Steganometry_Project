from src.TxtSteg import HideData as Hide
from src.TxtSteg import ExtractData as Extract
from src.TxtSteg import ExtractDataTo

message = '''Cicada 3301 is a nickname given to an alleged enigmatic organization that posted three sets of puzzles online between 2012 and 2014.
The first Internet puzzle started on January 4, 2012, on 4chan and ran for nearly a month. A second round began one year later on 
January 4, 2013, and then a third round following the confirmation of a fresh clue posted on Twitter on January 4, 2014. The third 
puzzle has yet to be solved. The stated intent was to recruit "intelligent individuals" by presenting a series of puzzles which were
to be solved. No new puzzles were published on January 4, 2015. However, a new clue was posted on Twitter on January 5, 2016.

    Cicada 3301 posted their last verified PGP-signed message in April 2017, denying the validity of any unsigned puzzle.
Unfortunately, the actually important message was harder to get.
As with the previous two years, the image included text hidden with steganography, a technique which lets users bury information in seemingly innocuous files. To get the information out required me to use a program called OutGuess. To install OutGuess, I need to compile the program from source. To do that, I need to install Xcode, the Mac OS X developer tools, create a new command line project based on the source code I downloaded, reconfigure the program for Mac, deal with any dependency issues, build it, and then run it from the terminal.
What I actually do is spend the better part of an hour clicking around in Xcode, desperately trying to find a magic button to click which will make everything work without requiring me to learn how to code in an afternoon. There is no such button. This may be harder than I thought.
Out of desperation, I turn to the community. Apparently I'm a few days behind the curve; they've already extracted the text and solved the puzzle. As I look at the solution, my hope begins to melt. It really is mind-bogglingly obtuse.

Solution
The text which can be extracted from the image is split into three parts. The third is just a signature, proof that the image really does come from Cicada and that it hasn't been tampered with. But above it is the next step of the puzzle.
The first part reads like a poem: "The work of a private man/ who wished to transcend,/ He trusted himself, / to produce from within." That's followed by a series of numbers, separated by colons: "1:2:3:1/3:3:13:5/45:5:2:3," and so on, capped by the word ".onion". That last bit means that the solution, when found, will be the url to another website on Tor following the pattern of the previous years.
So how is it solved? The numbers give a clue: the code probably involves a book. That format is a relatively well-known way of using a book as a key to a code. The first digit is the paragraph, the second is the sentence, the third is the word, and the fourth is the letter. But which book?
The answer is contained in the poem. Sort of. It's like the most frustrating cryptic crossword ever, with no conventions, no help as to length, and no way of checking whether you've got the right answer beyond seeing whether the url works.'''

Hide('media/mac.jpg',message)
ExtractDataTo('media/test.png','cicada.txt')