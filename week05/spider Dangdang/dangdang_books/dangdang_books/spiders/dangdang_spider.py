import scrapy

class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    start_urls = [
        'http://search.dangdang.com/?key=计算机&category_path=01.00.00.00.00.00',
    ]

    def parse(self, response):
        for book in response.css('.bigimg li'):
            yield {
                'title': book.css('.name a::text').get(),
                'author': book.css('.search_book_author span::text').get(),
                'price': book.css('.search_now_price span::text').get(),
            }

        next_page = response.css('.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
