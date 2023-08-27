import data
import config
import requests

  #<item>
    #<title>RSS Tutorial</title>
    #<link>https://www.w3schools.com/xml/xml_rss.asp</link>
    #<description>New RSS tutorial on W3Schools</description>
    #<content>New RSS tutorial on W3Schools bla bla bla</content>
  #</item>

def gen_table():
    table = f"""<table>
            <style>
            table {{
                color: white;
                background-color: black;
                width: 100%;
                border-collapse: collapse;
                border: 1px solid;
            }}
            td {{
                border: 1px solid;
                text-align: center;
            }}
            </style>
            <tr>
            <td>&nbsp;</td>
            <td>{data.hour_data['0']['time']}</td>
            <td>{data.hour_data['1']['time']}</td>
            <td>{data.hour_data['2']['time']}</td>
            <td>{data.hour_data['3']['time']}</td>
            <td>{data.hour_data['4']['time']}</td>
            <td>{data.hour_data['5']['time']}</td>
            <td>{data.hour_data['6']['time']}</td>
            <td>{data.hour_data['7']['time']}</td>
            <td>{data.hour_data['8']['time']}</td>
            </tr>
            <tr>
            <td>Tempreture</td>
            <td>{data.hour_data['0']['temp_c']}C</td>
            <td>{data.hour_data['1']['temp_c']}C</td>
            <td>{data.hour_data['2']['temp_c']}C</td>
            <td>{data.hour_data['3']['temp_c']}C</td>
            <td>{data.hour_data['4']['temp_c']}C</td>
            <td>{data.hour_data['5']['temp_c']}C</td>
            <td>{data.hour_data['6']['temp_c']}C</td>
            <td>{data.hour_data['7']['temp_c']}C</td>
            <td>{data.hour_data['8']['temp_c']}C</td>
            </tr>
            <tr>
            <td>Feels like</td>
            <td>{data.hour_data['0']['feels_like']}C</td>
            <td>{data.hour_data['1']['feels_like']}C</td>
            <td>{data.hour_data['2']['feels_like']}C</td>
            <td>{data.hour_data['3']['feels_like']}C</td>
            <td>{data.hour_data['4']['feels_like']}C</td>
            <td>{data.hour_data['5']['feels_like']}C</td>
            <td>{data.hour_data['6']['feels_like']}C</td>
            <td>{data.hour_data['7']['feels_like']}C</td>
            <td>{data.hour_data['8']['feels_like']}C</td>
            </tr>
            <td>Description</td>
            <td>{data.hour_data['0']['desc']}</td>
            <td>{data.hour_data['1']['desc']}</td>
            <td>{data.hour_data['2']['desc']}</td>
            <td>{data.hour_data['3']['desc']}</td>
            <td>{data.hour_data['4']['desc']}</td>
            <td>{data.hour_data['5']['desc']}</td>
            <td>{data.hour_data['6']['desc']}</td>
            <td>{data.hour_data['7']['desc']}</td>
            <td>{data.hour_data['8']['desc']}</td>
            </tr>
            <td>Icon</td>
            <td><img src='{data.hour_data['0']['desc_icon']}'></td>
            <td><img src='{data.hour_data['1']['desc_icon']}'></td>
            <td><img src='{data.hour_data['2']['desc_icon']}'></td>
            <td><img src='{data.hour_data['3']['desc_icon']}'></td>
            <td><img src='{data.hour_data['4']['desc_icon']}'></td>
            <td><img src='{data.hour_data['5']['desc_icon']}'></td>
            <td><img src='{data.hour_data['6']['desc_icon']}'></td>
            <td><img src='{data.hour_data['7']['desc_icon']}'></td>
            <td><img src='{data.hour_data['8']['desc_icon']}'></td>
            </tr>
            <tr>
            <td>Chance of rain</td>
            <td>{data.hour_data['0']['chance_of_rain']}%</td>
            <td>{data.hour_data['1']['chance_of_rain']}%</td>
            <td>{data.hour_data['2']['chance_of_rain']}%</td>
            <td>{data.hour_data['3']['chance_of_rain']}%</td>
            <td>{data.hour_data['4']['chance_of_rain']}%</td>
            <td>{data.hour_data['5']['chance_of_rain']}%</td>
            <td>{data.hour_data['6']['chance_of_rain']}%</td>
            <td>{data.hour_data['7']['chance_of_rain']}%</td>
            <td>{data.hour_data['8']['chance_of_rain']}%</td>
            </tr>
            <tr>
            <td>Chance of snow</td>
            <td>{data.hour_data['0']['chance_of_snow']}%</td>
            <td>{data.hour_data['1']['chance_of_snow']}%</td>
            <td>{data.hour_data['2']['chance_of_snow']}%</td>
            <td>{data.hour_data['3']['chance_of_snow']}%</td>
            <td>{data.hour_data['4']['chance_of_snow']}%</td>
            <td>{data.hour_data['5']['chance_of_snow']}%</td>
            <td>{data.hour_data['6']['chance_of_snow']}%</td>
            <td>{data.hour_data['7']['chance_of_snow']}%</td>
            <td>{data.hour_data['8']['chance_of_snow']}%</td>
            </tr>
            <tr>
            <td>Wind speed</td>
            <td>{data.hour_data['0']['wind_kph']}kph </td>
            <td>{data.hour_data['1']['wind_kph']}kph </td>
            <td>{data.hour_data['2']['wind_kph']}kph </td>
            <td>{data.hour_data['3']['wind_kph']}kph </td>
            <td>{data.hour_data['4']['wind_kph']}kph </td>
            <td>{data.hour_data['5']['wind_kph']}kph </td>
            <td>{data.hour_data['6']['wind_kph']}kph </td>
            <td>{data.hour_data['7']['wind_kph']}kph </td>
            <td>{data.hour_data['8']['wind_kph']}kph </td>
            </tr>
            <tr>
            <td>Wind direction</td>
            <td>{data.hour_data['0']['wind_dir']}</td>
            <td>{data.hour_data['1']['wind_dir']}</td>
            <td>{data.hour_data['2']['wind_dir']}</td>
            <td>{data.hour_data['3']['wind_dir']}</td>
            <td>{data.hour_data['4']['wind_dir']}</td>
            <td>{data.hour_data['5']['wind_dir']}</td>
            <td>{data.hour_data['6']['wind_dir']}</td>
            <td>{data.hour_data['7']['wind_dir']}</td>
            <td>{data.hour_data['8']['wind_dir']}</td>
            </tr>
            </table>"""
    # print(table)

    table_data = {"html": table}
    
    image_req = requests.post(url = config.HCTI_API_ENDPOINT, data = table_data, auth=(config.HCTI_API_USER_ID, config.HCTI_API_KEY))
    global image
    image = "asdf"
    image = image_req.json()["url"]


def gen_item():
    gen_table()

    item_title = f"<title>Weather forecast for {data.date}</title>"

    item_content = f"""
            <item>
            {item_title}
            <description>
            <![CDATA[
            <p>Weather forecast for {data.date} in {data.city_name}({data.country_name}, {data.region_name})</p>
            <p>General info:</p>
            <p>Date: {data.date}</p>
            <img src='{data.weather_avg_icon}'>
            <p>{data.weather_avg}</p>
            <p>Max tempreture: {data.maxtemp_c}C</p>
            <p>Min tempreture: {data.mintemp_c}C</p>
            <p>Avarege tempreture {data.avgtemp_c}C</p>
            <p>Average wind speed: {data.maxwind_kph}kph</p></p>
            <br>
           <p>Astrological data:</p>
           <p>Sunrise: {data.sunrise}</p>
           <p>Sunset: {data.sunset}</p>
           <p>Moonrise: {data.moonrise}</p>
           <p>Moonset: {data.moonset}</p>
           <p>Moon phase: {data.moon_phase}</p>
           <br>
           <p>Forecast for day</p>
           <img src='{image}'>
           ]]>
            </description>
            </item>"""
    return item_content

def gen_feed():
    rhs = "<rss version='2.0'> <channel> <title>Weather Forecast</title>"
    lhs = "</channel> </rss>"

    mid = gen_item()

    with open("feed.xml", "+w") as file:
        file.write(f"{rhs}{mid}{lhs}")

def main(response):
    response = response.json()
    data.define_data(response)

    gen_feed()

response = requests.get(config.url)

if response.status_code == 200:
    main(response)
else:
    print("FAILED")
