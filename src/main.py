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

    item_content = f"<description>\
            <![CDATA[\
            <p>Weather forecast for {conf.date} in {conf.city_name}({conf.country_name}, {conf.region_name})</p>\
            <p>General info:</p>\
            <p>Date: {conf.date}</p>\
            <img src='{conf.weather_avg_icon}'>\
            <p>{conf.weather_avg}</p>\
            <p>Max tempreture: {conf.maxtemp_c}</p>\
            <p>Min tempreture: {conf.mintemp_c}</p>\
            <p>Avarege tempreture {conf.avgtemp_c}</p>\
            <p>Average wind speed: {conf.maxwind_kph}kph</p></p>\
            <br>\
           <p>Astrological data:</p>\
           <p>Sunrise: {conf.sunrise}</p>\
           <p>Sunset: {conf.sunset}</p>\
           <p>Moonrise: {conf.moonrise}</p>\
           <p>Moonset: {conf.moonset}</p>\
           <p>Moon phase: {conf.moon_phase}</p>\
           <br>\
           <table>\
           <tr>\
           <td>&nbsp;</td>\
           <td>{conf.hour_data['0']['time']}</td>\
           <td>{conf.hour_data['1']['time']}</td>\
           </tr>\
           <tr>\
           <td>Tempreture</td>\
           <td>{conf.hour_data['0']['temp_c']}</td>\
           <td>{conf.hour_data['1']['temp_c']}</td>\
           </tr>\
           </table>\
           ]]>\
            </description>"
    print(item_content)

def main(response):
    data = response.json()
    conf.define_data(data)

    # print(list(conf.hour_data.values())[0])
    gen_item()
    print(conf.hour_data)
    # print(file_content)

response = requests.get(conf.url)

if response.status_code == 200:
    main(response)
else:
    print("FAILED")
