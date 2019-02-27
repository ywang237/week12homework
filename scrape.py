
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_facts_data = {}

    url = "https://mars.nasa.gov/news/
    browser.visit(url)
    html = browser.html
    soup = bs(html,"html.parser")

    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    print(f"Title: {news_title}")
    print(f"Paragraph: {news_paragraph}")

    featured_url_image = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19808_ip.jpg"
    browser.visit(featured_url_image)

    url_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_weather)

    html_weather = browser.html
    soup = bs(html_weather, "html.parser")
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(f"mars_weather: {mars_weather}")

    url_facts = "https://space-facts.com/mars/"
    table = pd.read_html(url_facts)
    table[0]

    df_mars_facts = table[0]
    df_mars_facts.columns = ["Parameter", "Values"]
    df_mars_facts.set_index(["Parameter"])

    html_table = df_mars_facts.to_html()
    html_table = html_table.replace("\n", "")
    html_table

    url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemisphere)
    hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_hemisphere))
    print(hemisphere_base_url)

    hemisphere_img_urls = []
    results = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    cerberus_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    cerberus_image = browser.html
    soup = bs(cerberus_image, "html.parser")
    cerberus_url = soup.find("img", class_="wide-image")["src"]
    cerberus_img_url = hemisphere_base_url + cerberus_url
    print(cerberus_img_url)
    cerberus_title = soup.find("h2",class_="title").text
    print(cerberus_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
    hemisphere_img_urls.append(cerberus)

    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    schiaparelli_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    schiaparelli_image = browser.html
    soup = bs(schiaparelli_image, "html.parser")
    schiaparelli_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
    print(schiaparelli_img_url)
    schiaparelli_title = soup.find("h2",class_="title").text
    print(schiaparelli_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
    hemisphere_img_urls.append(schiaparelli)

    results2 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    syrtis_major_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    syrtis_major_image = browser.html
    soup = bs(syrtis_major_image, "html.parser")
    syrtis_major_url = soup.find("img", class_="wide-image")["src"]
    syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
    print(syrtis_major_img_url)
    syrtis_major_title = soup.find("h2",class_="title").text
    print(syrtis_major_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
    hemisphere_img_urls.append(syrtis_major)

    results3 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    valles_marineris_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    valles_marineris_image = browser.html
    soup = bs(valles_marineris_image, "html.parser")
    valles_marineris_url = soup.find("img", class_="wide-image")["src"]
    valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
    print(valles_marineris_img_url)
    valles_marineris_title = soup.find("h2",class_="title").text
    print(valles_marineris_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
    hemisphere_img_urls.append(valles_marineris)

    mars_facts_data["hemisphere_img_url"] = hemisphere_img_urls

    return mars_facts_data