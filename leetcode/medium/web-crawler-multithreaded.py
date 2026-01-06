# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import threading

class ThreadCrawl():
    def __init__(self,hostname,htmlParser):
        self.visited_urls = set()
        self.lock_1 = threading.Lock()
        self.lock_2 = threading.Lock()
        self.hostname = hostname
        self.htmlParser = htmlParser
        self.n_threads = 1

    def url_already_visited(self,url):
        self.lock_1.acquire()
        has_been_visited = url in self.visited_urls
        self.lock_1.release()
        return has_been_visited

    def store_url(self,url):
        self.lock_2.acquire()
        self.visited_urls.add(url)
        self.lock_2.release()

    def traverse_tree(self,url):
        self.n_threads+=1
        print(self.n_threads)
        if self.url_already_visited(url):
            self.n_threads-=1
            return
        self.store_url(url)
        threads = []
        for child_url in self.htmlParser.getUrls(url):
            if child_url.strip("http://").split("/")[0] == self.hostname:
                if not self.url_already_visited(child_url):
                    thread = threading.Thread(target = self.traverse_tree,args = (child_url,))
                    threads.append(thread)
                    while self.n_threads>200:
                        pass 
                    thread.start()
        for thread in threads:
            thread.join()
        self.n_threads-=1

class Solution:
        
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        thread_crawl = ThreadCrawl(startUrl.strip("http://").split("/")[0],htmlParser)
        thread_crawl.traverse_tree(startUrl)
        return list(thread_crawl.visited_urls)
