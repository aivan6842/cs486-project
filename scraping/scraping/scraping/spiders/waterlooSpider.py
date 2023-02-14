import scrapy
from scraping.enums.subjects import Subject

class WaterlooSpider(scrapy.Spider):
    name = "waterlooSpider"
    allowed_domains = ["ucalendar.uwaterloo.ca"]
    start_urls = ["https://ucalendar.uwaterloo.ca/2223/COURSE/course-" + course.name + ".html" for course in Subject]

    def parse(self, response):
        courseCodesRaw = response.xpath("//div[@class='divTableCell']/strong/text()").getall()
        courseCodes = [" ".join(x.split()[:2]) for x in courseCodesRaw]

        courseNames = response.xpath("//div[@class='divTableCell colspan-2']/strong/text()").getall()

        courseDescriptions = response.xpath("//div[@class='divTableCell colspan-2']/text()").getall()

        for i in range(len(courseCodesRaw)):
            yield {
                'courseCode': courseCodes[i], 
                'courseName': courseNames[i],
                'courseDescription': courseDescriptions[i]
            }
