# Apache Nutch

[Apache Nutch](http://nutch.apache.org) is an open source, web crawler written in Java. It boasts scalable performance on distributed computing environments, while still being quite feature-rich. In the following essay, I will briefly define a web crawler, then highlight some of the features of Apache Nutch, and conclude by describing how you can start using Apache Nutch.

### Web Crawling

A [web crawler](https://en.wikipedia.org/wiki/Web_crawler) is a program which systematically navigates the internet indexing webpages. The most famous application of web crawling is [Google's Search Engine](https://www.google.com/search/howsearchworks/crawling-indexing/). Below is a diagram of the internal workings of a typical web crawler:

![web_crawler](https://user-images.githubusercontent.com/6633242/36811402-e6aa7554-1c8a-11e8-95b6-1f066fbbb5f6.png)
_Diagram for the workflow of a typical web crawler. Dashed lines denote optional actions._

The queue listed above is often called the "frontier", and in the case of "focused" or "topical" web crawlers the URLs in this list might be scored and ranked in a priority queue. In addition, URLs might be filtered from the queue based on their domain or filetype. Often web crawling is used in conjunction with [web scraping](https://en.wikipedia.org/wiki/Web_scraping). In this process, pages are fetched and then parsed for content relevant to the developer's reserach interests.

From the presepctive a website developer, web crawlers can be seen as a nuisance. These internet bots masquerade as real website visitors and can request many pages from your site in rapid succession, thereby increasing server loads. The upside is crawlers like Google and Yahoo! index your content and serve it to interested users, drawing more actual visitors to your site. In order to control the number of, and types of requests made, many domains include a [`robots.txt`](https://en.wikipedia.org/wiki/Robots_exclusion_standard) file which tells developers how they would like internet bots to interact with their site (e.g. University of Colorado's [`robots.txt`](https://www.colorado.edu/robots.txt) file).

### Features of Apache Nutch

Nutch requires a list of initial URLs to start from (see [Nutch Tutorial](https://wiki.apache.org/nutch/NutchTutorial#Introduction)), as is shown above and typical for a web crawler. Additionally, built-in to Nutch is capability to filter particular URLs from being added to the the queue (see [`URL Filter Plugins`](http://nutch.apache.org/apidocs/apidocs-1.14/index.html)). Also, Nutch internally handles URL normalization (see [`URL Normalizer Plugins`](http://nutch.apache.org/apidocs/apidocs-1.14/index.html)). By that I mean, `google.com`, `www.google.com`, and `www.google.com/` refer to the same page, so URL normalization reduces two to the other, since requesting both would be redundant. These two particular features can help reduce the overall size of a crawler's URL queue.

Nutch also allows items to be prioritized withing a crawler's URL queue (see [`Scoring Plugins`](http://nutch.apache.org/apidocs/apidocs-1.14/index.html)). These scoring mechanisms can be rather simple - ["limiting the number of hops from the initial seed urls"](http://nutch.apache.org/apidocs/apidocs-1.14/org/apache/nutch/scoring/depth/package-summary.html), and more complex and context driven - [looking for the existance of particular "meta" tags on a page](http://nutch.apache.org/apidocs/apidocs-1.14/org/apache/nutch/scoring/urlmeta/package-summary.html). Web scraping can also be carried out via Nutch (see [`Parse Plugins` and `Parse Filter Plugins`](http://nutch.apache.org/apidocs/apidocs-1.14/index.html))

Though probably the highlights of Nutch are its integrations with distributed databases like [ElasticSearch](https://github.com/kenbod/5828_S18/wiki/Elasticsearch:-Overview) and Apache Solr, and the fact that the process of fetching new URLs is handled efficiently via Hadoop (see [Prashil's essay](https://github.com/kenbod/5828_S18/wiki/Hadoop:-Overview) or [Shayon's essay](https://github.com/kenbod/5828_S18/wiki/Scheduling-Algorithms-in-Hadoop)). 

### Getting Started

Nutch has a [nice tutorial](https://wiki.apache.org/nutch/NutchTutorial) for how to get started running the software locally. The code can be downloaded from [Github](https://github.com/apache/nutch) or from [one of the following mirrors](http://www.apache.org/dyn/closer.cgi/nutch/).

### References
- **Web Crawling**:
	- "Focused" web crawling: ["Crawling the Web"](http://www.divms.uiowa.edu/~psriniva/Papers/crawlingFinal.pdf) by Pant, Srinivasan & Menczer, ["ARCCHNID: Adaptive Retrieval Agents Choosing Heuristic Neighborhoods"](https://dl.acm.org/citation.cfm?id=657140) by Menczer
	- Python packages for requestion webpages, [Selenium](http://selenium-python.readthedocs.io) (see Shemal's [essay](https://github.com/kenbod/5828_S18/wiki/Selenium-Framework:Overview)), and for parsing webpages, [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

- **Apache Nutch**:
	- [Tutorial](https://wiki.apache.org/nutch/NutchTutorial)
	- [Wikipedia](https://en.wikipedia.org/wiki/Apache_Nutch)
	- ["About" section](https://wiki.apache.org/nutch/FrontPage#What_is_Apache_Nutch.3F) of Apache Nutch's documentation.
	- Detailed [Documentation](http://nutch.apache.org/apidocs/apidocs-1.14/index.html)