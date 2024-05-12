import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

urls = [
    "https://www.raymond-weil.us/collections/for-her/",
    "https://www.raymond-weil.us/collections/for-him/"
]

product_details = []

for url in urls:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        product_items = soup.find_all('li', class_='product')

        for item in product_items:
            product_title = item.find('h2', class_='woocommerce-loop-product__title').text.strip()
            product_link = item.find('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')['href']

            product_details.append({
                'title': product_title,
                'link': product_link
            })

    else:
        print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
data=[]
for product in product_details:
    response1 = requests.get(product['link'], headers=headers)
    if response1.status_code == 200:
        soup1 = BeautifulSoup(response1.text, 'html.parser')

        reference_number_element = soup1.find(class_='rwproduct__main__infos__sku')
        reference_number = reference_number_element.text.strip() if reference_number_element else ""
        watch_URL=product_link
        type_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Size') + td")
        type_value = type_element.get_text(strip=True).capitalize() if type_element else ""
        brand = "Raymond Weil"
        year_introduced_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Introduced') + td")
        year_introduced = year_introduced_element.get_text(strip=True) if year_introduced_element else ""

        parent_model_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Collection') + td")
        parent_model = parent_model_element.get_text(strip=True) if parent_model_element else ""

        specific_model_element = soup1.find(class_='rwproduct__main__infos__name')
        specific_model = specific_model_element.find("div").text.strip() if specific_model_element else ""

        nickname_element = soup1.find(class_='rwproduct__main__infos__name')
        nickname = nickname_element.find("div").text.strip() if nickname_element else ""

        marketing_name_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Model') + td")
        marketing_name = marketing_name_element.get_text(strip=True) if marketing_name_element else ""

        style_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Style') + td")
        style = style_element.get_text(strip=True) if style_element else ""

        currency = 'USD'

        price_element = soup1.find('span', class_='woocommerce-Price-amount').text.strip()
        price_text_cleaned = price_element.replace("$", "").replace(",", "")
        price_float = float(price_text_cleaned)
        # Convert the price to an integer (removing decimal places)
        price_int= int(price_float)

        image_elements = soup1.find_all("div", {"class": "woocommerce-product-gallery__wrapper"})
        image_url = image_elements[0].find("img").attrs["data-src"] if image_elements else ""

        made_in = "Switzerland"

        case_shape_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Shape') + td")
        case_shape = case_shape_element.get_text(strip=True) if case_shape_element else ""

        case_material_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('material') + td")
        case_material = case_material_element.get_text(strip=True) if case_material_element else ""

        case_finish_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Finish') + td")
        case_finish = case_finish_element.get_text(strip=True) if case_finish_element else ""

        caseback_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Case back') + td")
        caseback = caseback_element.get_text(strip=True) if caseback_element else ""

        diameter_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Case size') + td")
        diameter = diameter_element.get_text(strip=True) if diameter_element else ""

        between_lugs=" "
        lug_to_lug=" "

        case_thickness_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('thickness') + td")
        case_thickness = case_thickness_element.get_text(strip=True) if case_thickness_element else ""

        bezel_material_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Bezel') + td")
        bezel_material = bezel_material_element.get_text(strip=True) if bezel_material_element else ""

        bezel_color_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Bezel') + td")
        bezel_color = bezel_color_element.get_text(strip=True) if bezel_color_element else ""

        crystal_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Crystal') + td")
        crystal = crystal_element.get_text(strip=True) if crystal_element else ""

        water_resistance_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Water') + td")
        water_resistance = water_resistance_element.get_text(strip=True) if water_resistance_element else ""

        weight_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Weight') + td")
        weight = weight_element.get_text(strip=True) if weight_element else ""

        dial_color_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Dial') + td")
        dial_color = dial_color_element.get_text(strip=True) if dial_color_element else ""

        numerals_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Dial') + td")
        numerals = numerals_element.get_text(strip=True) if numerals_element else ""

        bracelet_material_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Bracelet/Strap') + td")
        bracelet_material = bracelet_material_element.get_text(strip=True) if bracelet_material_element else ""

        bracelet_color_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Bracelet/Strap') + td")
        bracelet_color = bracelet_color_element.get_text(strip=True) if bracelet_color_element else ""

        clasp_type_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Clasp') + td")
        clasp_type = clasp_type_element.get_text(strip=True) if clasp_type_element else ""

        movement_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Movement') + td")
        movement = movement_element.get_text(strip=True) if movement_element else ""

        caliber_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Movement') + td")
        caliber = caliber_element.get_text(strip=True) if caliber_element else ""

        power_reserve_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Power reserve') + td")
        power_reserve = power_reserve_element.get_text(strip=True) if power_reserve_element else ""

        frequency_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Frequency') + td")
        frequency = frequency_element.get_text(strip=True) if frequency_element else ""

        jewels_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Jewels') + td")
        jewels = jewels_element.get_text(strip=True) if jewels_element else ""

        features_element = soup1.select_one("table.rwproduct__datas__tech__table tr th:contains('Features') + td")
        features = features_element.get_text(strip=True) if features_element else ""

        description_element = soup1.select_one("div.rwproduct__datas__description__inner")
        description_text = description_element.text.strip() if description_element else ""

        start_index = description_text.index("Description") + len("Description")
        description = description_text[start_index:].strip()

        short_description_element = soup1.find('span', {'data-sheets-value': True})
        short_description = short_description_element.text.strip() if short_description_element else ""


        data.append([reference_number,watch_URL,type_value, brand, year_introduced, parent_model, specific_model, nickname,
                     marketing_name, style, currency, price_int, image_url, made_in, case_shape, case_material,
                     case_finish, caseback, diameter, between_lugs, lug_to_lug, case_thickness, bezel_material,
                     bezel_color, crystal, water_resistance, weight, dial_color, numerals, bracelet_material,
                     bracelet_color, clasp_type, movement, caliber, power_reserve, frequency, jewels, features,
                     description, short_description])

    else:
        print(f"Failed to retrieve product details for {product['title']}. Status Code: {response1.status_code}")

with open('scriping-result.csv', mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Reference_Number','watch_URL','type', 'brand', 'year_introduced', 'parent_model', 'specific_model',
                     'nickname', 'marketing_name', 'style', 'currency', 'price', 'image_url', 'made_in',
                     'case_shape', 'Case_material', 'case_finish', 'caseback', 'diameter', 'between_lugs',
                     'lug_to_lug', 'Case_thickness', 'bezel_material', 'bezel_color', 'crystal', 'water_resistance',
                     'weight', 'dial_color', 'numerals', 'bracelet_material', 'bracelet_color', 'clasp_type',
                     'movement', 'caliber', 'power_reserve', 'frequency', 'jewels', 'features', 'description',
                     'short_description'])
    writer.writerows(data)