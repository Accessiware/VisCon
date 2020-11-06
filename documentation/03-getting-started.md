# Getting Started with VisCon

This chapter will teach you about various basic features and capabilities of VisCon.

To find detailed information on how to work with Markdown in VisCon it is highly recommended that you read the chapter ["Overview over VisCon Markdown"](insert link here) But do not try to master it all at once. Instead, try to do some specific tasks with VisCon. For instance. Try to make a document with a few headings, paragraphs and even a bulleted list. Use the chapter as a reference guide and just keep practicing. All of a sudden you will understand the basics, and it will be easier for you to get your documents done.

In the following paragraphs, we will explore the menus. In the next chapter ["Working with documents"](#working-with-documents) you will find detailed information about some of the concepts VisCon uses to import, export and preview documents.

VisCon is visually very simple. At the top of the screen is a menu bar from which all functions can be accessed. The menus and their functions are explained in the following sections.

Note: When you examine the menus in VisCon, you will see that there are hotkeys for the vast majority of functions. For example, you can press CONTROL + N (on Windows) or command-N (on Mac OS) to create a new document rather than clicking the File menu and then clicking "New " with the mouse. Using the keyboard as you type can be a good way to increase the pacing of your work.

## The VisCon menu: Mac OS only

The menu structure on Windows and Mac OS differ due to the way the operating systems work. On Mac OS you will therefore have a VisCon menu that will not be visible in the Windows version. The menu items in this menu are located in other menus in the Windows version.

* About: Shows relevant information about VisCon such as which version you are running - and where to find VisCon on the web.
* Preferences: Shows VisCon preferences. In here you can change the interface language and other settings. For more information see ([VisCon preferences](#VisCon-preferences))
* Quit VisCon: Exits VisCon. If you have one or more open documents that are not already saved, VisCon will prompt you for each document before exiting. This is done so that you do not inadvertently lose any of your open documents.


## The File Menu

The File menu contains the following menu items:

* New: Creates a new document.
* Open: Allows you to open a document from anywhere on your computer.

	Note: If you select a document that is not a plain text document (with the txt extension) or a Markdown document (with the md extension), VisCon will automatically attempt to convert the document you open to Markdown.
Thus, if you open a Word document with VisCon you will see a converted document showing how the document looks in Markdown. You can freely change the text and layout of the document accordingly. For more information see: [Importing documents into VisCon](#importing-documents-into-VisCon)
* Save: Saves your current document. If the document does not already have a name, the "Save as " dialog box will open automatically.
* Save As: presents you with a dialog box where you can give your document a name and choose its format. If you select Markdown or plain text, your document will remain unchanged. The only exception to this rule, is if you change the settings for text encoding under the [Advanced category](#advanced-prefences) in Preferences. If you save in any other supported format, VisCon will automatically convert your document to the format you have selected. For more information read [Exporting your document](#exporting-documents-from-VisCon)
* Exit: Exits VisCon. If you have one or more open documents that are not already saved, VisCon will prompt you for each document before exiting. This is done so that you do not inadvertently lose any of your open documents.

	Note: This menu item is only shown in the Windows version of VisCon.

## The Edit Menu

The Edit menu contains the following menu items:

* Undo: Will undo the last edit you have done. This includes last keypress etc.
* Redo: Will redo the last edit you have done. This includes last keypress etc.
* Cut: Cuts the selected text to the clipboard.
* Copy: Copies the selected text to the clipboard.
* Paste: Paste the contents of the clipboard to the cursor position.

	Tip: If you are pasting contents which was copied from another application all formating will be ignored, so only the plain text is kept. Linebreaks will be preserved.
* Select All: Selects all contents in the current document.
* Search: Opens a screen with the following options:
	* Find what: Here you can enter text to search for. Press enter to activate the "Find next" button.
	* Match whole word only  checkbox: If you check this checkbox only entire words will be matched. This checkbox is unchecked by default.
	* Match case checkbox: If this checkbox is checked the search will try to match upper and lowercase results. This is useful if you for example search for a word that begins with a capital character. This checkbox is unchecked by default.
	* Find next: Searches the document and places the cursor at the next match. This button can be triggered directly from the search field by pressing the enter key.
	* Cancel: Closes the screen. Press escape on the keyboard to activate this button.
* Find and replace: Search for some text and type something else to replace any matches. The window contains the following options:
	* Case sensitive checkbox: Allows you to choose if you want the search and replace matches to be case sensitive or not. This is unchecked by default.
	* Find what: Here you can type in the text you want to search for.
	* Replace with: Type the text you want to be replacing the search matches.
	* Replace: Will search and replace.
	* Cancel: Will cancel and close the window and return you to the VisCon main window.

## The Insert Menu

This menu is useful when you are learning the Markdown markup language. However, to get the most out of the markup formating VisCon provides, use the appendix 1 "Introduction to Markdown"](#appendix 1-an-introduction-to-markdown) as a reference guide.

The insert menu has the following items:

* Headings: This is a submenu where you can choose among six heading levels. Level 1 is the biggest type of headings. When you choose a heading level the Markup syntax will be inserted at the cursor position, and you can then start typing the content for the heading.
* Lists: This submenu allows you to select different types of lists. These are the following:
	* Ordered list: Inserts a list with four empty items starting from 1. to 4. You can add as manny items as you wish to this list.
	* Unordered list 1: Creates a bulleted list with the - as a list marker.
	* Unordered list 2: Creates a bulleted list with the * as a list marker.
* Links: This submenu allows you to insert links. You have the following options:
	 * Raw link: This will insert <http://url.com> you will need to change the link accordingly. The link will be converted to a clickable link as long as the\< and \> characters are placed around the url.
	* Inline link: Will insert a more friendly URL where you can add a text to the link. Simply change the text between the two brackets to whatever you like. Then change the URL which is put between two regular square brackets.
* Blockquote: Lets you insert a quote in a classic blockquote.
* Image: 

## The Tools menu

The tools menu contains the following items:

* Preview: Previews the current document in your default web browser. This is a good way to watch your formating and structure before sharing or converting your document to an alternative format. For more information see: [Previewing a document from VisCon](#previewing-a-document-from-ison)
* Document statistics: This is very useful if you are working on a document which has specific needs, such as a maximum of words, characters or number of pages. The document statistic window will show you the following details about your document:
	- Lines: Shows the number of lines your document contains.
	- Pages: Shows the number of pages.
	- Characters: Displays the amount of characters including linebreaks, spaces etc.
	- Characters without spaces: Displays the number of characters excluding linebreaks and spaces.
	- Words: The number of words in your document.

## The Help Menu

* About: Shows relevant information about VisCon such as which version you are running - and credits.
* Preferences: Shows VisCon preferences. In here you can change the interface language and other settings. For more information see ([VisCon preferences](#VisCon-preferences))
* What's new: Opens a webpage displaying all information about each released version of VisCon. This is very useful if you want to know what has changed since the last update. After an update this website will be launched automatically.
* Check for updates: Allows you to check for updates manually. Note however that VisCon by default will check for updates every time you start the application.

	When an update is found VisCon will tell you that an update is ready for you to install. Simply answer yes to download and install the update. First you will see a dialog which shows you the status of the download. When the update is downloaded, VisCon will exit, and you will be asked to allow the update to be continued. On Windows this is done by allowing VisCon via the User Account Control dialog. On Mac OS, you will need to enter your user account password. When VisCon is updated, you will see a dialog box where a change log is displayed. Just press enter, and you are back to VisCon.

	Note: If there are any open documents, VisCon will ask you to save, before the update can take place. This is done, so you wan't loose your work.
* Go to our homepage: Will open your web browser of choice on the VisCon website at: <https://visconapp.com>
