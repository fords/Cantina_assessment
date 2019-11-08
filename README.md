## EXERCISE PROBLEM

https://github.com/jdolan/quetoo/blob/master/src/cgame/default/ui/settings/SystemViewController.json

Your program may assume that the file resides locally on the same filesystem as the program itself, or it may retrieve it via web request if you prefer.

The JSON file represents a view hierarchy in a user interface. You can think of it as a tree of nodes, just like elements in an HTML DOM. Like in HTML, views have certain attributes that are selectable, ala CSS selectors.


Once parsed, your program should wait for user input on stdin. Each line the user enters on stdin should be treated as a selector, and your program should print the matching views, as JSON, to stdout. The exact format of your output is entirely up to you.

The program must support simple selectors for the following view attributes:

class - The view class name, e.g. "StackView"

classNames - CSS class names, e.g. ".container"

identifier - The view identifier, e.g. "#videoMode"


## ASSUMPTION
When identifier is reached, the program finished running

When class has same name, first class is used

When invalid selector is used, the program exits

## EXAMPLES
```
1st input StackView
2nd input StackView
3rd input StackView
4th input videoMode  

should give  the identifier class output
```

```
1st input StackView
2nd input a

should exit the program
```
