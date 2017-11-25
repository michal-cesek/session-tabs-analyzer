import json

# buddy ukazoval cca 300 duplikatov
export_buddy = 'data/session_buddy_export_2017_11_25_17_23_24(all_user_saved).json'

data = json.load(open(export_buddy, encoding="utf-8-sig"))
tabs = data['tabs']

print('Tabs count: {}'.format(len(tabs)))


# tabs = tabs[0]['url']
# tabs = tabs[0]['title']

# TODO
def group_by_domain():
    pass

def remove_duplicates(tabs):
    to_remove_indicies = []
    dict_filter = {}

    for i, tab in enumerate(tabs):
        if tab['url'] in dict_filter:
            print('There is already tab {}'.format(tab['url']))
            to_remove_indicies.append(i)
        else:
            dict_filter[tab['url']] = i

    print(len(to_remove_indicies))


remove_duplicates(tabs)
