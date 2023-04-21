from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



def Amazondata(request, keyword):
    # keyword = 'electonics'
    webdriver_path = '/home/maulik/Music/inexture/chromedriver_linux64/chromedriver'
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.get("https://www.amazon.com/")
    search_bar = driver.find_element("xpath","//input[@name='field-keywords']")
    search_bar.send_keys(keyword)
    
    # Submit the search
    search_bar.send_keys(Keys.RETURN)
    
    
    # Extract the product information from the search results
    products = []
    product_elements = driver.find_elements("xpath","//div[@data-component-type='s-search-result']")
    for product_element in product_elements:
        try:
            product_name = product_element.find_element("xpath",".//h2/a").text
        except:
            product_name=""

        try:
            product_price = product_element.find_element("xpath",".//span[@class='a-price']").text
        except:
            product_price=""

        try:
            product_rating = product_element.find_element("xpath",".//span[@class='a-icon-alt']").get_attribute("innerHTML")
        except:
            product_price=""

        try:
            product_image = product_element.find_element("xpath",".//img[@class='s-image']").get_attribute('src')
        except:
            product_image=""

        product = {
            'name': product_name,
            'price': product_price,
            'rating': product_rating,
            'image':product_image
        }
        products.append(product)
    
    # Close the browser
    driver.quit()
    
    # return products
    # return render(request,template_name='index.html' ,context={"data":products})
    return HttpResponse(products)