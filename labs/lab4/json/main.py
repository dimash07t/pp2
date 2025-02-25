import json

data = json.load(open('sample-data.json', 'r', encoding='utf-8'))

print("Interface Status")
print("="*80)
print(f'{"DN":<50} {"Description":<21} Speed   MTU   ')
print(f'{"-"*50} {"-"*20}  ------  ------')
#print('-------------------------------------------------- --------------------  ------  ------')

arr = data['imdata']

for i in arr:
    print(f"{i['l1PhysIf']['attributes']['dn']:<50} {i['l1PhysIf']['attributes']['descr']:<21} {i['l1PhysIf']['attributes']['speed']:<7} {i['l1PhysIf']['attributes']['mtu']:<6}")

#Made by Nurassyl