from bs4 import BeautifulSoup
import requests

# this is a function (also called method, and also called an object). this is how you are supposed to code.
def parseTomBrady(msg, webpage):
    # this weird string contains terminal codes for text coloring
    print('\033[31m' + '=== Parsing ' + msg + ' ===\033[30m')
    # make the web request to get content
    response = requests.get(webpage, headers = {'User-agent': 'nfl-bot-1.0'})
    # idk what this does
    soup = BeautifulSoup(response.text, "html.parser")
    # find the table element on the webpage
    table = soup.findAll(class_="table")

    # loop through rows in table until you find tom brady - then print each item in the row
    for table_row in table:
        # 'td' is the HTML identifier for a row in a table. press F12 on webpage and select the element to see
        cells = table_row.findAll('td')
        # at this point, cells is now an array of the rows in the table. lets loop through each row to see if it contains tom brady
        for i in range(len(cells)):
            if (cells[i].get_text() == 'Tom Brady'):
                print('Player = ' + cells[i+0].get_text())
                print('Pos = ' + cells[i+1].get_text())
                print('Team = ' + cells[i+2].get_text())
                print('Gms = ' + cells[i+3].get_text())
                print('Pass Yds = ' + cells[i+4].get_text())
                print('TD = ' + cells[i+5].get_text())
                print('Int = ' + cells[i+6].get_text())
                print('Rush Yds = ' + cells[i+7].get_text())
                print('TD = ' + cells[i+8].get_text())
                print('Rec = ' + cells[i+9].get_text())
                print('Yds = ' + cells[i+10].get_text())
                print('TD = ' + cells[i+11].get_text())
                print('Sck = ' + cells[i+12].get_text())
                print('Int = ' + cells[i+13].get_text())
                print('FF = ' + cells[i+14].get_text())
                print('FR = ' + cells[i+15].get_text())
                print('PPG = ' + cells[i+16].get_text())
                print('Fantasy Points = ' + cells[i+17].get_text())
                break # break the for loop because we are done searching
        print() # prints whitespace line for easy reading


# this is your main function. whatever is written in this guy will be run
def main():
    # I saw that the data on the page can be given via url (this is a RESTful API)
    # this gives stats for 2017 through 2002 regular season
    for i in range(15):
        # formatting int with string is a common problem when coding.
        parseTomBrady('{} regular season'.format((2017 - i)), 'https://fantasydata.com/nfl-stats/nfl-fantasy-football-stats.aspx?fs=0&stype=' + str(0) + '&sn=' + str(i) + '&scope=0&w=0&ew=0&s=&t=0&p=0&st=FantasyPoints&d=1&ls=FantasyPoints&live=false&pid=false&minsnaps=4')

    # 2017-2002 preseason stats
    for i in range(15):
        parseTomBrady('{} pre season'.format((2017 - i)), 'https://fantasydata.com/nfl-stats/nfl-fantasy-football-stats.aspx?fs=0&stype=' + str(1) + '&sn=' + str(i) + '&scope=0&w=0&ew=0&s=&t=0&p=0&st=FantasyPoints&d=1&ls=FantasyPoints&live=false&pid=false&minsnaps=4')

    # 2017-2002 postseason stats
    for i in range(15):
        parseTomBrady('{} post season'.format((2017 - i)), 'https://fantasydata.com/nfl-stats/nfl-fantasy-football-stats.aspx?fs=0&stype=' + str(2) + '&sn=' + str(i) + '&scope=0&w=0&ew=0&s=&t=0&p=0&st=FantasyPoints&d=1&ls=FantasyPoints&live=false&pid=false&minsnaps=4')


# this is python. because python is a script and not a compiled language (AKA it is interpreted on runtime), when you run it,
# it is looking for what it should do first. Since we define a bunch of functions in the file, it is not just going to run
# everything yolo style, it wants a clear instruction on what to do first.
# Python will run this oddly named if __name__== "__main__": function if you write python like it is supposed to be written
# (like using methods/functions and having structured code)
if __name__== "__main__":
    main()