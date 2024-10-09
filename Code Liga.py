with open('data/Liga/Widget_ID.txt', 'r', encoding='latin-1') as file:
    Widget_IDs = file.read().splitlines()

with open('data/Liga/liganummer.txt', 'r', encoding='latin-1') as file:
    liganummern = file.read().splitlines()

code_long = []
# Generate the script code for each pair of Widget_ID and Mannschaft_ID
for widget_id, liganummer in zip(Widget_IDs, liganummern):
    script_code_long = f'''
    <div id="widget_{widget_id}"></div>
        <script>
            widget.ligawidget('widget_{widget_id}',
                    {{"iframeWidth":1200,"iframeHeight":600,"showRefreshButton":true,"titleColor":"FFFFFF","titleBgColor":"00CC00","tapColor":"FFFFFF","tapBgColor":"333333","colorMatchGroup":"666666","bgColorMatchGroup":"F0F0F0","colorMatchListItem":"000000","bgColorMatchListItem":"FFFFFF","showKuerzelInSpiele":false,"ligaNr":"{liganummer}","vereinsId":"977","rangeDays":8,"activeTap":"tabelle","tapColorActive":"FFFFFF","tapBgColorActive":"000000","tapBorderColorActive":"00CC00","colorTableHeader":"666666","bgColorTableHeader":"F0F0F0","colorTableListItem":"000000","bgColorTableListItem":"FFFFFF","colorTableListItem2":"000000","bgColorTableListItem2":"FFFFFF","showKuerzelInTabelle":false}});
        </script>
    '''
    code_long.append(script_code_long)

code_short = []
# Generate the script code for each pair of Widget_ID and Mannschaft_ID
for widget_id, liganummer in zip(Widget_IDs, liganummern):
    script_code_short = f'''
    <div id="widget_{widget_id}"></div>
        <script>
                widget.ligawidget('widget_{widget_id}',
                        {{"iframeWidth":600,"iframeHeight":600,"showRefreshButton":true,"titleColor":"FFFFFF","titleBgColor":"00CC00","tapColor":"FFFFFF","tapBgColor":"333333","colorMatchGroup":"666666","bgColorMatchGroup":"F0F0F0","colorMatchListItem":"000000","bgColorMatchListItem":"FFFFFF","showKuerzelInSpiele":false,"ligaNr":"{liganummer}","vereinsId":"977","rangeDays":8,"activeTap":"tabelle","tapColorActive":"FFFFFF","tapBgColorActive":"000000","tapBorderColorActive":"00CC00","colorTableHeader":"666666","bgColorTableHeader":"F0F0F0","colorTableListItem":"000000","bgColorTableListItem":"FFFFFF","colorTableListItem2":"000000","bgColorTableListItem2":"FFFFFF","showKuerzelInTabelle":false}});
        </script>
    '''
    code_short.append(script_code_short)

# Write the properly formatted code to the file
with open('data/Liga/code_snippets_big.txt', 'w', encoding='utf-8') as file:
    for snippet in code_long:
        file.write(snippet + "\n")
with open('data/Liga/code_snippets_small.txt', 'w', encoding='utf-8') as file:
    for snippet in code_short:
        file.write(snippet + "\n")
