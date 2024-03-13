website_url = 'https://sss-corp.com'
website_url.removeprefix('https://')
cleanURL = website_url.removeprefix('https://')
print(cleanURL)

# # EXERCISE 1
name = "Carl Johnson"
print(f"hello {name}, would you like to bomb Idlewood or chase Ballas fools?")
print(name.upper())
print(name.lower())

# # EXERCISE 2
person = "Albert Einstein"
person_quote = "Gravity is bullshit, make coffee and chase wild boars."
output_message = (f'{person} once said, "{person_quote}"')
print(output_message)

# EXERCISE 3
packageName = ">>GTA-SanAndreas.rar"
packageName_clean = packageName.removeprefix('>>').removesuffix('.rar')  #well done self-learned
print(packageName_clean)