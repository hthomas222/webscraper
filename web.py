import requests
import re
from rich.console import Console
from rich.table import Table
from rich import print
import sys


def scraped_to_file(site, filename):
    response = requests.get(site)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)


def findings(filename, reg_exp):
    with open(filename, "r") as file:
        content = file.read()
        pattern = re.compile(reg_exp)
        print(pattern)
        matches = re.findall(pattern, content)
        for match in matches:
            print("The elements found are:", match)


def check(test):
    if test == "2":
        return test
    if test == "1":
        sys.exit()
    sel = ["1", "2"]
    while test not in sel:
            console.log("Please enter either 1 or 2")
            test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    return test


test = ""
while test != "1":
    print()
    table = Table(title="Scrapy Commands")
    table.add_column("NUM", style="green")
    table.add_column("TASK", style="red")
    table.add_column("Description", style="blue")

    table.add_row("1", "Scrape_and_Save", "This will perform the webscraper and save it to the file of your choice. ")
    table.add_row("2", "Stock_Viewer", "This will find all of the matches from the website you scraped.")
    console = Console()
    console.print(table)
    print()
    selection = input("enter a number to execute the command: ")
    if selection == "1":
        site = input("Please enter the link of the website you want to scrape: ")
        filename = input("Please enter the filename you want to save the site you scraped: ")
        scraped_to_file(site, filename)
    elif selection == "2":
        print()
        reg_exp = input("Please enter the regular expression to search through: ")
        filename = input("Please enter a filename that you want to pull the data out of: ")
        findings(filename, reg_exp)
        print()
    else:
        console.log("[bold red]Please enter a valid choice!")
    print()
    test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    if test != "1":
        x = check(test)
        if x == "1":
            sys.exit()
