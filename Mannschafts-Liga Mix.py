with open('data/Mannschaft/Widget_ID.txt', 'r', encoding='latin-1') as file:
    Widget_IDsM = file.read().splitlines()
with open('data/Liga/Widget_ID.txt', 'r', encoding='latin-1') as file:
    Widget_IDsL = file.read().splitlines()

with open('data/Mannschaft/Mannschaft_ID.txt', 'r', encoding='latin-1') as file:
    Mannschaft_IDs = file.read().splitlines()

with open('data/Liga/Liganummer.txt', 'r', encoding='latin-1') as file:
    liganummer = file.read().splitlines()


while True:
    print("Index der Mannschaft:")
    M = input()
    print("Index der Liga:")
    L = input()

    try:
        M = int(M)
        L = int(L)
        break
    except:
        print("Not valid numbers")
        continue

widget1 = Widget_IDsM[M]
mannschaft = Mannschaft_IDs[M]
widget2 = Widget_IDsL[L]
liga = liganummer[L]

code = f'''
<div style="display: flex; justify-content: space-between;">
    <div id="widget_{widget1}"></div>
    <div id="widget_{widget2}"></div>
</div>
    <script>
        widget.mannschaftswidget('widget_{widget1}',
                {{"iframeWidth": 600, "iframeHeight": 600, "showRefreshButton": false, "titleColor": "FFFFFF", "titleBgColor": "00CC00", "tapColor": "FFFFFF", "tapBgColor": "333333", "colorMatchGroup": "666666", "bgColorMatchGroup": "F0F0F0", "colorMatchListItem": "000000", "bgColorMatchListItem": "FFFFFF", "showKuerzelInSpiele": false, "mannschaftsId": "{mannschaft}"
                }});
        widget.ligawidget('widget_{widget2}',
                {{"iframeWidth": 600,"iframeHeight":600,"showRefreshButton":true,"titleColor":"FFFFFF","titleBgColor":"00CC00","tapColor":"FFFFFF","tapBgColor":"333333","colorMatchGroup":"666666","bgColorMatchGroup":"F0F0F0","colorMatchListItem":"000000","bgColorMatchListItem":"FFFFFF","showKuerzelInSpiele":false,"ligaNr":"{liga}","vereinsId":"977","rangeDays":8,"activeTap":"tabelle","tapColorActive":"FFFFFF","tapBgColorActive":"000000","tapBorderColorActive":"00CC00","colorTableHeader":"666666","bgColorTableHeader":"F0F0F0","colorTableListItem":"000000","bgColorTableListItem":"FFFFFF","colorTableListItem2":"000000","bgColorTableListItem2":"FFFFFF","showKuerzelInTabelle":false
                }});
    </script>
'''

with open(f'data/code_mix_{M},{L}.txt', 'w', encoding='utf-8') as file:
    file.write(code + "\n")
