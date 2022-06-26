from extract import json_extract
import urllib.request
import json


url = "https://dev.shepherd.appoly.io/fruit.json"
response = urllib.request.urlopen(url)
data = response.read()
json_dict = json.loads(data)
# print(json_dict)
items = json_dict['menu_items']
# print(items)

layer_one=[]
layer_two=[]
layer_three=[]
layer_four=[]

def get_layer_label():
   for item in items:
   # print(item['label']) first layer
      item_one = item['label']
      layer_one.append(item_one)
   # print(type(item['children']))
      children_item = item['children']
      for child in children_item:
         # print(child['label']) second layer
         item_two = child['label']
         layer_two.append(item_two)
         # print(type(child))
         child2 = child['children']
         # print(child2)
         for childed in child2:
            # print(childed)third layer
            item_three = childed['label']
            layer_three.append(item_three)
            # print(childed['label'])
            child_bearer = childed['children']
            # print(child_bearer)
            for child_bear in child_bearer:
               item_four = child_bear['label']
               layer_four.append(item_four)
               # print(child_bear['label'])

get_layer_label()
print(layer_one)
print(layer_two)
print(layer_three)
print(layer_four)

