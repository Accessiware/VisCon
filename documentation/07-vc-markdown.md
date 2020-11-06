# Overview of VisCon Markdown

VisCon can generally use the common form of markdown, so in the vast majority of cases you will probably not experience problems when checking your work for errors. If you are accustomed to writing Markdown, however, we have compiled a list of small changes that you should be aware of as you write. We've added examples to help you see how you can check your Markdown formatting. For Most examples, you can see how the result of the conversion would look directly in your Web browser.

Note: In some cases, the examples will not be converted because the result of converting two types of writing will be the same. When this appears in this chapter, there will be an explicit explanation in the text of why you only see a pure Markdown formatting and not a converted example.

If you find that a desired formatting isn't working as you'd like, please contact us so we can try to help you. When you contact us with a specific Markdown problem, please send one or more examples, otherwise we are unable to help you.

# # Paragraphs

A paragraph is described in Markdown as continuous text of one or more lines. To create a new paragraph, two hard linebreaks must be made (made by pressing the Enter/Return key twice.
Example:

```
Here's a paragraph.

Here is another paragraph.
```

The example will look like this:

Here's a paragraph.

Here is another paragraph.

As seen in the example above, there are no linebreaks between the two paragraphs when the Markdown is converted. However, it is possible to make linebreaks within the same paragraph.

# # # Paragraph with line break

VisCon makes it simple to insert a manual (also called a forced) line break in a paragraph. All you need to do is make a line break as you would in any other word processing program. This is done by pressing the enter/return key once.

Example:

```
Here's a line of text.
Here's a new line.
```

The example will look like this:

Here's a line of text.
Here's a new line.

Note: In this case VisCon deviates from a general principle in most Markdown variants which describe manual line breaks a little differently. In most Markdown variants, line breaks can be performed by ending the line with two or more spaces. This makes it clear that a line break is desired. The challenge, however, is that you cannot visually see that spaces are inserted because spaces are invisible characters.

# # # Insert blank lines between two paragraphs
Skal undersøges nærmere. Måske backslash efterfulgt af enter gør noget.

## Headings

Headings can be up to six levels. Level 1 is usually a main heading, Level 2 is a sub-heading of level 1 and so on.

The heading level is specified by one or more # characters. See the following examples as well as their results below.

``
# Here is a Level 1 heading

## Here is a Level 2 heading

### Here is a Level 3 heading

#### Here is a level 4 heading

##### Here is a level 5 heading

###### Here is a level 6 heading
```

The example above will look like this:

# Here is a Level 1 heading

## Here is a Level 2 heading

### Here is a Level 3 heading

#### Here is a level 4 heading

##### Here is a level 5 heading

###### Here is a level 6 heading

## Lists

Lists can be unordered or ordered. We will start with unordered lists and work through different cases.

### Bulleted lists - also known as unordered lists

Bulleted list can be written in several ways. There are generally three different ways to set a bullet. Type +, -(hyphen) or * in front of the text that you want to be part of the bulleted list. A simple bulleted list might look like this:

```
* Here is the first item.
* Here is the second item.
* Here is the third item.

Or:

+ Here is the first item.
+ Here's the second item.
+ Here is the third item.

Or:

-This is the first item.
This is the second item.
-This is the third item.
```

The example above will look like this:

* Here is the first point.
* Here is the second point.
* Here is the third point.

Or:

+ Here is the first point.
+ Here's the second point.
+ Here is the third point.

Or:

-This is the first point.
This is the second point.
-This is the third point.
```

The examples above will look like this:
* Here is the first item.
* Here is the second item.
* Here is the third item.

Or:

+ Here is the first item.
+ Here's the second item.
+ Here is the third item.

Or:

-This is the first item.
This is the second item.
-This is the third item.

# # Bulleted lists and general readability 

You can combine the three types of bulleted list markers, but it is recommended for readability that you do not mix them, except in the case of nested lists which we will cover later.
The following example is therefore acceptable, but it is harder to read:

```
* Here is the first item.
+ Here's the second item.
- This is the third item.
```

The example will look like this:

* Here is the first item.
+ Here's the second item.
- This is the third item.

Note: VisCon does not require a mandatory blank line before starting a bulleted list, which is true in many other Markdown variants. However, VisCon supports both types of writing.

See the following two examples that show these two types of writing:

~~~
Example 1 where there is no blank line before the first item:
* Here is a list where the first item does not have a blank line above it.
* Here is the second item in the same list.

Example 2 where a blank line has been inserted before the first item:

+ Here starts the first item. There is a blank line above this item.
+ Here is the second item in this list.
~~~

The example above will look like this:

Example 1 where there is no blank line before the first item:
* Here is a list where the first item does not have a blank line above.
* Here is the second item in the same list.

Example 2 where a blank line has been inserted before the first item:

+ Here starts the first item. There is a blank line above this item.
+ Here is the second item in this list.

###Ordered  list with numbers and/or letters


# # # Smart, continuous bulleted list

# # # unordered lists with nested lists

It is possible to have bulleted lists in several levels. Each time a new level is desired, you must write four spaces or one tab. This applies regardless of the type of bulleted list used.

See the following example with a common bulleted list:

```
* Fruits
	-Apples
	-Bananas,
* Vegetables:
	+ Potatoes
	+ Carrots
	+ Brocoli 
```

The example will look like this:
* Fruits
	-Apples
	-Bananas,
* Vegetables:
	+ Potatoes
	+ Carrots
	+ Brocoli 

# # # Bulleted lists with paragraphs

It is possible to have text paragraphs within a bulleted list. However, this requires a blank line before the paragraph, and an indent is made before the text starts.

# # Code Blocks

# # Links

# # # Unformatted links (clean URL)

# # # Anker links which refers to another place in the same text

# # # Inline Links

# # # Reference Links