from selenium import webdriver


def calculateAverage(list):
    """Calcuate the average

    Arguments:
        list {int} -- unit sold of a certain product

    Returns:
        [int] -- [the averagge units sold by product]
    """
    sum_num = 0
    for number in list:
        sum_num = sum_num + int(number)
        avg = sum_num / len(list)
    return avg


def startBrowser():
    """Start Chrome Browser
    """
    sourceURL = "https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week05/WI20-Assignment/sales_data.html"
    my_browser = webdriver.Chrome(executable_path="downloads\chromedriver.exe")
    my_browser.get(sourceURL)
    return my_browser
