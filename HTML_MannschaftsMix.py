import pyperclip

with open('data/Mannschaft/Widget_ID.txt', 'r', encoding='latin-1') as file:
    Widget_IDs = file.read().splitlines()

with open('data/Mannschaft/Mannschaft_ID.txt', 'r', encoding='latin-1') as file:
    Mannschaft_IDs = file.read().splitlines()


while True:
    print("Index Mannschaft 1:")
    M1 = input()
    print("Index Mannschaft 2:")
    M2 = input()

    try:
        M1 = int(M1)
        M2 = int(M2)
        break
    except:
        print("Not valid numbers")
        continue

mannschaft1 = Mannschaft_IDs[M1]
widget1 = Widget_IDs[M1]
mannschaft2 = Mannschaft_IDs[M2]
widget2 = Widget_IDs[M2]

code = f'''
<div style="display: flex; justify-content: space-between;">
    <div id="widget_{widget1}"></div>
    <div id="widget_{widget2}"></div>
</div>
    <script>
        widget.mannschaftswidget('widget_{widget1}',
                {{"iframeWidth": 600, "iframeHeight": 600, "showRefreshButton": false, "titleColor": "FFFFFF", "titleBgColor": "00CC00", "tapColor": "FFFFFF", "tapBgColor": "333333", "colorMatchGroup": "666666", "bgColorMatchGroup": "F0F0F0", "colorMatchListItem": "000000", "bgColorMatchListItem": "FFFFFF", "showKuerzelInSpiele": false, "mannschaftsId": "{mannschaft1}"
                }});
        widget.mannschaftswidget('widget_{widget2}',
                {{"iframeWidth": 600, "iframeHeight": 600, "showRefreshButton": false, "titleColor": "FFFFFF", "titleBgColor": "00CC00", "tapColor": "FFFFFF", "tapBgColor": "333333", "colorMatchGroup": "666666", "bgColorMatchGroup": "F0F0F0", "colorMatchListItem": "000000", "bgColorMatchListItem": "FFFFFF", "showKuerzelInSpiele": false, "mannschaftsId": "{mannschaft2}"
                }});
    </script>

'''


pyperclip.copy(code)
with open(f'data/code_mix_{M1},{M2}.txt', 'w', encoding='utf-8') as file:
    file.write(code + "\n")
