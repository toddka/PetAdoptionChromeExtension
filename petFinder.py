import petfinder

api = petfinder.PetFinderClient(api_key='710fb86300ed19f143a1671a3c171456', api_secret='64e4de99d362e6b4b1b53bda89c65296')
#Getting pet's dictionary id
id = api.pet_getrandom(
    animal="dog", location="02912", output="basic",
    breed="Golden Retriever")
photo = id['photos'][0]['url']
name = id['name']
breed = id['breeds']
contact = id'contact']
print photo + name + breed + shelter

