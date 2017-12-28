'''
Name: Karl Honse
Date created: 10-16-2017
Purpose: Read from a large file, being able to break each line up into individual lists. Then search through each list in order to answer specific questions, much like a database. 




Sample run(s):
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
> 1
Enter beginning year: 1980
Enter ending year: 1981
The books reaching #1 between 1980 and 1981 are: 

An Indecent Obsession, by Colleen McCullough (11/15/1981)
Cujo, by Stephen King (8/23/1981)
Firestarter, by Stephen King (9/28/1980)
Gorky Park, by Martin Cruz Smith (4/26/1981)
Key to Rebecca, by Ken Follett (10/19/1980)
Noble House, by James Clavell (5/10/1981)
Princess Daisy, by Judith Krantz (2/17/1980)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
> 1
Enter beginning year: 1992
Enter ending year: 1990
Make sure the beginning year is smaller than the ending year.
...

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
> 2
Enter month (as a number between 1 and 12): 1
Enter year: 1980
Smiley's People, by John le Carre (1/20/1980)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
> 2
Enter month (as a number between 1 and 12): 14
Enter year: 1980
Please enter a month between 1 and 12.

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
> 3
Enter an author's name (or part of a name): Martin
A Dance With Dragons, by George R. R. Martin (7/31/2011)
A Feast For Crows, by George R. R. Martin (11/27/2005)
Gorky Park, by Martin Cruz Smith (4/26/1981)
Polar Star, by Martin Cruz Smith (8/6/1989)
Jennie, by Ralph Martin (5/11/1969)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
> 3
Enter an author's name (or part of a name): Tom Cruise
The author tom cruise was not found

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
> 4
Enter a title (or part of a title): Machine
The Love Machine, by Jacqueline Susann (6/22/1969)
The Omen Machine, by Terry Goodkind (9/4/2011)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
> 4
Enter a title (or part of a title): pumpkin
A book with the title containing pumpkin was not found.

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
> q

Program Execution Complete
'''


def find_books_by_title(thistitle, booklist): ### Function that gets 'thistitle' from the main and searches the booklist for matching titles

    foundTitle = False   ### Set a variable to false
    for book in booklist:
        title = book[0].lower()         ### Makes and input from the user to lowercase and compares it to a lowercase version of the book title in the list
        thistitle = thistitle.lower() 
        if thistitle in title:
            foundTitle = True  ### Makes variable true if expression is true
            print("%s, by %s (%s)" %(book[0], book[1], book[3]) )
    if not foundTitle:   ### if variable is still false print this message informing user of what went wrong
        print("A book with the title containing %s was not found." %thistitle)
    print("\n")


def find_books_by_author(thisauthor, booklist):
    
    foundAuthor = False
    for book in booklist:
        author = book[1].lower()
        thisauthor = thisauthor.lower()
        if author == thisauthor or thisauthor in author:
            foundAuthor = True
            print("%s, by %s (%s)" %(book[0], book[1], book[3]))
    if not foundAuthor:
        print("The author %s was not found" %thisauthor)  ### Displays this error message if an author was not found from what the user typed
    print("\n")
            

def find_books_between(beginyear, endyear, booklist):
    
    if beginyear > endyear:
        print("Make sure the beginning year is smaller than the ending year.")
        print("\n")
    else:
        foundDates = False
        print("The books reaching #1 between %i and %i are: \n" %(beginyear, endyear))
        for book in booklist:
            date = book[3].split('/')   ### finds only the date which is at index 0 of each list then splist the year up on the '/' symbol 
            year = int(date[2])   ### Now the date is broken up into month/day/year [index 0, index 1, index 2]
            if year >= beginyear and year <= endyear:
                foundDates = True
                print("%s, by %s (%s)" %(book[0], book[1], book[3]))  
        if not foundDates:
            print("There are no books found between %s and %s." %(beginyear, endyear))
        print("\n")
        
        
def find_books_in_month(pubmonth, pubyear, booklist):
    
    if pubmonth > 12 or pubmonth < 1:  ### if the user types a non existant month display this error message, ELSE actually complete the function
        print("Please enter a month between 1 and 12.")
        print("\n")
    else:
        foundMonth = False
        for book in booklist:
            date = book[3].split('/')
            month = int(date[0])
            year = (date[2])
            if month == pubmonth and year == pubyear:
                foundMonth = True
                print("%s, by %s (%s)" %(book[0], book[1], book[3]))
        if not foundMonth:
            print("No books reached #1 on month %s and year %s." %(pubmonth, pubyear))
        print("\n")
            
            
def read_best_sellers(filename):   ### function to read the information within the text file
    
    fileIn = open(filename, 'r')  ### opens file and reads it
    
    book = []
    for line in fileIn:
        line = line.rstrip('\n')  ### strip away on every new line statement
        book.append(line.split('\t'))    ### append on every tab
        
    fileIn.close()   
    return book

    
def display_menu():  ### builds a formatted menu and return the user input to the main function to knw what option was chosen
    
    menu = input("What would you like to do?\n1: Look up year range\n2: Look up month/year\n3: Search for author\n4: Search for title\nQ: Quit\n> ")
    
    if menu != ("1") and menu != ("2") and menu != ("3") and menu != ("4") and menu != ("q") and menu != ("Q"):
        print("Please Enter a Choice listed above.\n")
        menu
    return menu
        

def main():
    book_data = read_best_sellers('bestsellers.txt')  ###tells the read function what file to read
    
    #print(book_data) ### Test to see if list was created correctly
    
    choice = display_menu()
    while choice != 'q' and choice != 'Q':
        if choice == "1":                       ### if 1 is entered begin the year range option
            beginyear = int(input("Enter beginning year: "))
            endyear = int(input("Enter ending year: "))
            find_books_between(beginyear, endyear, book_data)
            
        if choice == "2":                       ### if 2 is entered begin the look up month/year option
            pubmonth = int(input("Enter month (as a number between 1 and 12): "))
            pubyear = input("Enter year: ")
            find_books_in_month(pubmonth, pubyear, book_data)
            
        if choice == "3":                       ### if 3 is entered begin the search for author option
            thisauthor = input("Enter an author's name (or part of a name): ")
            find_books_by_author(thisauthor, book_data)
            
        if choice == "4":                       ### if 4 is entered begin the search for title option
            thistitle = input("Enter a title (or part of a title): ")
            find_books_by_title(thistitle, book_data)
                    
        choice = display_menu()
        
    print("\nProgram Execution Complete")     
        
        
main()