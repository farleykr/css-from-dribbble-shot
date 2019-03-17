from bs4 import BeautifulSoup
import requests
import fire

template = """ 
.text-color-{num} {{
    color: {color};
}}

.bg-color-{num} {{
    background-color: {color};
}}

"""

def get_shot_colors(shot_url):
    source = requests.get(shot_url).text
    soup = BeautifulSoup(source, 'lxml')
    colors = soup.find_all('li', class_='color')

    with open('styles.css', 'w+') as f:
        num = 1
        
        for color in colors:
            color_hex = color.text.strip()

            context = {
                'num' : num,
                'color' : color_hex,
            }

            f.write(template.format(**context))
            num += 1


if __name__ == '__main__':
    fire.Fire(get_shot_colors)