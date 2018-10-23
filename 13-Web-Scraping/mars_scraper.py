from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd

def browse_html(url):
    executable_path = {"executable_path": "./chromedriver"}
    browse = Browser("chrome", **executable_path, headless=False)
    browse.visit(url)
    html = browse.html
    return html

def scrape():
    mars_data = {}

    # Latest news
    url = 'https://mars.nasa.gov/news/'
    html = browse_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    latest_news = soup.find("div", class_="list_text")
    print (latest_news)
    latest_news_date = latest_news.find("div", class_="list_date").text
    latest_news_title = latest_news.find("div", class_="content_title").text
    latest_news_paragraph = latest_news.find("div", class_="article_teaser_body").text

    mars_data["Latest_News_Date"] = latest_news_date
    mars_data["Latest_News_Title"] = latest_news_title
    mars_data["Latest_News_Article"] = latest_news_paragraph

    # Featured image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    html = browse_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    featured_image = soup.find("ul", class_="articles")
    featured_image_hires = featured_image.find("a", class_="fancybox")["data-fancybox-href"]
    featured_image_url = "https://www.jpl.nasa.gov"+featured_image_hires
    mars_data["Featured_Image_URL"] = featured_image_url

    # Mars weather
    url = "https://twitter.com/marswxreport?lang=en"
    html = browse_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    latest_tweet = soup.find("div", class_="js-tweet-text-container")
    mars_weather = latest_tweet.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_data["Mars_Weather"] = mars_weather

    # Mars profile
    url = "https://space-facts.com/mars"
    table_html = pd.read_html(url)[0]
    table_html.columns = ['Object','Mars']
    mars_data["Mars_Profile"] = table_html.to_json(orient='records')

    # Mars hemisphere
    executable_path = {"executable_path": "./chromedriver"}

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    html = browse_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    MarsHemis = []
    Hemis = soup.findAll("div", class_="item")
    browser = Browser("chrome", **executable_path, headless=False)
    for hemi in Hemis:
        downloadpage = hemi.find("a")["href"]
        browser.visit("https://astrogeology.usgs.gov"+downloadpage)
        html = browser.html
        soup2 = BeautifulSoup(html,'html.parser')
        image = soup2.find("div", class_="downloads")
        image_full = image.find("a")["href"]
        MarsHemis.append({'title': hemi.find("h3").text,
                        'img_url':image_full})
    mars_data["Mars_Hemisphere"] = MarsHemis

    return mars_data
