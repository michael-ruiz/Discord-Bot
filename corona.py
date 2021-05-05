from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def corona():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get('https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html')
    cad_case_num = browser.find_element_by_xpath('//*[@id="newCases"]/tbody/tr[1]/td[2]').text
    ont_case_num = browser.find_element_by_xpath('//*[@id="newCases"]/tbody/tr[6]/td[2]').text

    browser.get('https://app.powerbi.com/view?r=eyJrIjoiMzE5MzJlOTItOWE2ZS00MDNlLTlkNDEtMTcyYTg5OGFhMTFiIiwidCI6ImRjNTYxMjk1LTdjYTktNDFhOS04M2JmLTUwODM0ZDZhOWQwZiJ9')
    lon_case_num = browser.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[25]/transform/div/div[3]/div/visual-modern/div/div/div/p/span').text

    browser.quit()

    print_title = 'COVID-19 Cases\n'
    print_cad = 'New cases in Canada: ' + str(cad_case_num)
    print_ont = '\nNew cases in Ontario: ' + str(ont_case_num)
    print_lon = '\nNew cases in London: ' + str(lon_case_num)
    print_info = print_title + print_cad + print_ont + print_lon
    return print_info