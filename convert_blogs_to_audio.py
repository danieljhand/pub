import os
import feedparser
import httplib2
import html2text
from bs4 import BeautifulSoup,SoupStrainer
from subprocess import call


# Create a dictionary of feeds
rss_feeds = {'Seths Blog': 'http://feeds.feedblitz.com/SethsBlog/',
             'Red Hat': 'https://www.redhat.com/en/rss/blog',
             'AWS': 'https://aws.amazon.com/new/feed/',
             'Battery Ventures': 'https://www.battery.com/powered/feed/'}

search_filter = {'Seths Blog': {'class': 'entry-body'},
             'AWS': {'class': 'aws-text-box'},
             'Battery Ventures': {'class':'post-content-container'},
             'Red Hat': 'article'}

base_dir = os.path.expanduser('~') + "/Desktop/blogs/"

file = open(base_dir+'/'+"last_run"+".txt",'w')
file.write(".")  
file.close()


for feed_name in rss_feeds.keys():
  if os.path.exists(base_dir + feed_name):
    print "\nDirectory for blog " + feed_name + " already exists"
  else:
    print "about to create " + base_dir + feed_name
    call(["mkdir","-p",base_dir+feed_name])

  feed = feedparser.parse(rss_feeds[feed_name])
  http = httplib2.Http()

  for entry in feed.entries:
    output_dir = base_dir + feed_name
    status, response = http.request(entry.link)

    if feed_name == "Red Hat":
       data_boxen = SoupStrainer(search_filter[feed_name])
    else:
       data_boxen = SoupStrainer('div', search_filter[feed_name])

    soup = BeautifulSoup(response.decode('utf8','ignore'), "html.parser", parse_only=data_boxen)

    # create a new file with a name matching the blog post title
    blog_title = entry.title

    if os.path.isfile(output_dir+'/'+feed_name+'-'+blog_title+".txt"):
      #print "already exists do nothing."
      print '.', 
    else:
      print "\nNew blog post."
      file = open(output_dir+'/'+feed_name+'-'+blog_title+".txt",'w')

      # add title and blog content to file
      file.write(entry.title.encode('utf-8'))
      parsed_text = soup.get_text()
      file.write(parsed_text.encode('utf-8'))  

      # close the file
      file.close()

      call(["say","-o",output_dir+"/"+feed_name+'-'+blog_title+".m4a","-f",output_dir+"/"+feed_name+'-'+blog_title+".txt"])
