import conf
import requests

  #<item>
    #<title>RSS Tutorial</title>
    #<link>https://www.w3schools.com/xml/xml_rss.asp</link>
    #<description>New RSS tutorial on W3Schools</description>
    #<content>New RSS tutorial on W3Schools bla bla bla</content>
  #</item>

def gen_item():
    global file_content
    with open("sample.xml", "r+") as file:
        file_content = [line.replace("\n", "") for line in file if line != "\n"]

    item_title = f"<title>Weather forecast for {conf.date}</title>"
    item_link = f"<link>{0}</link>"
    item_description = f"<description><![CDATA[\
            <img src='{conf.weather_avg_icon}'>\
            ]> </description>"

    item_content = f"<description>Weather forecast for {conf.date} in {conf.city_name}({conf.country_name}, {conf.region_name})\
            <p><p>General info:</p>\
            <p>Date: {conf.date}</p>\
            <![CDATA[\ <img src='{conf.weather_avg_icon}'>\ ]>\
            <p>{conf.weather_avg}</p>\
            <p>Max tempreture: {conf.maxtemp_c}</p>\
            <p>Min tempreture: {conf.mintemp_c}</p>\
            <p>Avarege tempreture {conf.avgtemp_c}</p>\
            <p>Average wind speed: {conf.maxwind_kph}</p></p>\
            </description>"
    print(item_content)

def main(response):
    data = response.json()
    conf.define_data(data)

    # print(conf.hour_data)
    # print(list(conf.hour_data.values())[0])
    gen_item()
    print(file_content)

response = requests.get(conf.url)

if response.status_code == 200:
    main(response)
else:
    print("FAILED")
