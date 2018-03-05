# BeautifulSoup

In my essay last week about Apache Nutch, I briefly described web crawling. This week I'd like to describe a method often used in conjunction with web crawling, that is, [web scraping](https://en.wikipedia.org/wiki/Web_scraping). Then I would like to highlight a Python package which can be used for this purpose called BeautifulSoup.

### Web Scraping

Web scraping involves requesting pages and extracting data from those pages. There are many [techniques](https://en.wikipedia.org/wiki/Web_scraping#Techniques) which can be used for web scraping - ranging from requiring human involvement ("human copy-paste") to fully automated systems (using computer vision). Somewhere in the middle is the web scraping I am most familiar with, and which BeautifulSoup can be used for, which is HTMl parsing.

When you visit a webpage, your web browser renders an [HTML document](https://en.wikipedia.org/wiki/HTML) with [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) and [Javascript](https://en.wikipedia.org/wiki/JavaScript) to produce a visually appealing page. For example, the HTML below:

```html
<html>
  <body>
    <p>Hello world!</p>
  </body>
</html>
```

renders a page saying: "Hello world!"

Web scraping using HTML parsing is often used on webpages which share similar HTML structure. For example, you might want to scrape the ingredients from [chocolate chip cookie recipes](https://www.allrecipes.com/search/results/?wt=chocolate%20chip%20cookies&sort=re) to identify correlations between ingredients and five-star worthy cookies, or you might want to predict who will win March Madness by looking at [game play-by-plays](http://www.espn.com/mens-college-basketball/playbyplay?gameId=401020698). (As an aside, you should check a site's terms of service before embarking on either of those tasks - ESPN and AllRecipes ask you not to do so. In some cases, these services have public APIs, which you can access for the same data in a legal fashion.)

### BeautifulSoup

BeautifulSoup is a Python library for parsing HTML and allowing for easy traversal of HTML trees (more on this below). Its name comes from [a song in Alice in Wonderland](https://www.quora.com/Does-the-phrase-beautiful-soup-come-from-Alice-in-Wonderland). 

#### Example

Say I wanted to know all of the names, ages, and breeds of the [dogs](https://www.boulderhumane.org/animals/adoption/dogs), [cats](https://www.boulderhumane.org/animals/adoption/cats) and [small animals](https://www.boulderhumane.org/animals/adoption/adopt_other) currently up for adoption at the Boulder Humane Society. I could write a Python script to request these pages and parse them using BeautifulSoup!

Note, that the feature of these pages which we are exploiting is the repeated similar HTML structure. Every animal listed has the following HTML variant:

```html
<div class="views-row views-row-1 views-row-odd views-row-first Adopt Me">
    ... 
    <div class="views-field views-field-field-pp-animalname">
        <div class="field-content">
            <a href="/animals/adoption/37933070" title="Adopt Me!">Romeo</a>
        </div>  
    </div>  
    <div class="views-field views-field-field-pp-primarybreed">
        <div class="field-content">New Zealand</div>
    </div>  
    <div class="views-field views-field-field-pp-secondarybreed">        
        <div class="field-content">Rabbit</div>  
    </div>  
    <div class="views-field views-field-field-pp-age">    
        <span class="views-label views-label-field-pp-age">Age: </span>    
        <span class="field-content">0 years 2 months</span>  
    </div>  
    <div class="views-field views-field-field-pp-gender">    
        <span class="views-label views-label-field-pp-gender">Sex: </span>    
        <span class="field-content">Male</span>  
    </div>  
    ...
</div>
```


### Getting Started


### References
- [BeautifulSoup Homepage](https://www.crummy.com/software/BeautifulSoup/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)