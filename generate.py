from PIL import Image
import random
import json

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["default_0", "default_1", "default_2", "default_3", "default_4",
              "default_5", "default_6", "default_7", "default_8", "default_9",
              "default_10", "default_11", "default_12", "default_13", "default_14",
              "default_15", "red_gradient", "sky_gradient", "blue_gradient",
              "rainbow", "cloud"] 
background_weights = [6, 6, 6, 6, 5,
                      5, 5, 5, 5, 5,
                      5, 5, 5, 5, 5,
                      5, 5, 4, 5, 1, 1]

skin = ["default", "brown", "gray", "pink", "black", "blue", "purple", "sky", "amethyst", "mint"]
skin_weights = [20, 15, 15, 10, 10, 10, 5, 5, 5, 5]

eyes = ["default", "right", "center"] 
eyes_weights = [55, 40, 5]

mouth = ["default", "tooth"] 
mouth_weights = [80, 20]

nose = ["default", "white_point", "snot"] 
nose_weights = [60, 35, 5]

poo = ["default", "red", "green", "blue", "black", "white", "rainbow", "gold"] 
poo_weights = [40, 10, 10, 10, 5, 5, 3, 2]

TOTAL_IMAGES = 2000 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
  new_image = {} #

  # For each trait category, select a random trait based on the weightings 
  new_image["Background"] = random.choices(background, background_weights)[0]
  new_image["Skin"] = random.choices(skin, skin_weights)[0]
  new_image["Eyes"] = random.choices(eyes, eyes_weights)[0]
  new_image["Mouth"] = random.choices(mouth, mouth_weights)[0]
  new_image["Nose"] = random.choices(nose, nose_weights)[0]
  new_image["Poo"] = random.choices(poo, poo_weights)[0]

  if new_image in all_images:
    return create_new_image()
  else:
    return new_image

# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
  new_trait_image = create_new_image()
  all_images.append(new_trait_image)

def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)

# Get Trait Counts

background_count = {}
for item in background:
    background_count[item] = 0
    
skin_count = {}
for item in skin:
    skin_count[item] = 0

eyes_count = {}
for item in eyes:
    eyes_count[item] = 0

mouth_count = {}
for item in mouth:
    mouth_count[item] = 0

nose_count = {}
for item in nose:
    nose_count[item] = 0

poo_count = {}
for item in poo:
    poo_count[item] = 0

for image in all_images:
    background_count[image["Background"]] += 1
    skin_count[image["Skin"]] += 1
    eyes_count[image["Eyes"]] += 1
    mouth_count[image["Mouth"]] += 1
    nose_count[image["Nose"]] += 1
    poo_count[image["Poo"]] += 1
    
print(background_count)
print(skin_count)
print(eyes_count)
print(mouth_count)
print(nose_count)
print(poo_count)

#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

#### Generate Images    
for item in all_images:

    im1 = Image.open(f'./trait-layers/background/{item["Background"]}.png').convert('RGBA')
    im2 = Image.open(f'./trait-layers/skin/{item["Skin"]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/eyes/{item["Eyes"]}.png').convert('RGBA')
    im4 = Image.open(f'./trait-layers/mouth/{item["Mouth"]}.png').convert('RGBA')
    im5 = Image.open(f'./trait-layers/nose/{item["Nose"]}.png').convert('RGBA')
    im6 = Image.open(f'./trait-layers/poo/{item["Poo"]}.png').convert('RGBA')
    im7 = Image.open(f'./trait-layers/bone.png').convert('RGBA')
    im8 = Image.open(f'./trait-layers/shadow.png').convert('RGBA')


    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)
    com7 = Image.alpha_composite(com6, im8)

    #Convert to RGB
    rgb_im = com7.convert('RGB')
    rgb_im = rgb_im.resize((1024, 1024), Image.NEAREST)
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)

#### Generate Images    
im1 = Image.open(f'./trait-layers/background/cloud.png').convert('RGBA')
im2 = Image.open(f'./trait-layers/skin/mint.png').convert('RGBA')
im3 = Image.open(f'./trait-layers/eyes/center.png').convert('RGBA')
im4 = Image.open(f'./trait-layers/mouth/tooth.png').convert('RGBA')
im5 = Image.open(f'./trait-layers/nose/snot.png').convert('RGBA')
im6 = Image.open(f'./trait-layers/poo/gold.png').convert('RGBA')
im7 = Image.open(f'./trait-layers/bone.png').convert('RGBA')
im8 = Image.open(f'./trait-layers/shadow.png').convert('RGBA')


#Create each composite
com1 = Image.alpha_composite(im1, im2)
com2 = Image.alpha_composite(com1, im3)
com3 = Image.alpha_composite(com2, im4)
com4 = Image.alpha_composite(com3, im5)
com5 = Image.alpha_composite(com4, im6)
com6 = Image.alpha_composite(com5, im7)
com7 = Image.alpha_composite(com6, im8)

#Convert to RGB
rgb_im = com7.convert('RGB')
rgb_im = rgb_im.resize((10000, 10000), Image.NEAREST)
file_name = "best.png"
rgb_im.save(file_name)

f = open('./metadata/all-traits.json',) 
data = json.load(f)


IMAGES_BASE_URI = "http://dogsandpoo.s3-website.ap-northeast-2.amazonaws.com/"
PROJECT_NAME = "Dogs and Poo"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Skin", i["Skin"]))
    token["attributes"].append(getAttribute("Eyes", i["Eyes"]))
    token["attributes"].append(getAttribute("Mouth", i["Mouth"]))
    token["attributes"].append(getAttribute("Nose", i["Nose"]))
    token["attributes"].append(getAttribute("Poo", i["Poo"]))

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()
