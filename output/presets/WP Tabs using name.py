import pyperclip
import base64
import os
import urllib.parse


def encode_url_and_base64(input_string):
    # Step 1: URL encode
    url_encoded = urllib.parse.quote(input_string)

    # Step 2: Encode to Base64
    base64_encoded = base64.b64encode(
        url_encoded.encode('utf-8')).decode('utf-8')

    # Step 3: Remove padding
    base64_encoded = base64_encoded.rstrip('=')

    return (base64_encoded)


# preparation

# Read the content of the code_snippets.txt file
with open('data/Mannschaft/code_snippets_big.txt', 'r', encoding='utf-8') as file:
    code_snippets1 = file.read()

mannschaft_code_snippets = [snippet.replace('\n', ' ')
                            for snippet in code_snippets1.strip().split('\n\n')]
# Read the content of the code_snippets.txt file
with open('data/Liga/code_snippets_big.txt', 'r', encoding='utf-8') as file:
    code_snippets2 = file.read()

liga_code_snippets = [snippet.replace('\n', ' ')
                      for snippet in code_snippets2.strip().split('\n\n')]


def create_output(name):
    with open(f'output/presets/{name}', 'r', encoding='utf-8') as file:
        input = file.read().splitlines()
    len = int(input.pop(0))

    mannschafts_index = []
    liga_index = []
    names = []
    for _ in range(len):
        mannschafts_index.append(int(input.pop(0)))
    for _ in range(len):
        liga_index.append(int(input.pop(0)))
    for _ in range(len):
        names.append(str(input.pop(0)))
    print(mannschafts_index)
    print(liga_index)
    print(names)

    anfang = '''
    [/vc_column_text][divider line_type="Full Width Line" line_thickness="4" divider_color="accent-color" animate="yes" custom_height="50"][tabbed_section style="default" alignment="left" spacing="default" tab_color="Accent-Color"]
    '''
    tab1 = '[tab icon_family="none" title="'
    tab2 = '" id="'
    tab3 = '" tab_id="'
    tab4 = '"][vc_raw_html]'
    tab5 = '[/vc_raw_html][vc_raw_html]'
    tab6 = '[/vc_raw_html][/tab]'

    end = '''
    [/tabbed_section][divider line_type="Full Width Line" line_thickness="4" divider_color="accent-color" animate="yes" custom_height="50"][divider line_type="No Line" custom_height="100"][/vc_column][/vc_row][vc_row type="in_container" full_screen_row_position="middle" column_margin="default" scene_position="center" text_color="dark" text_align="left" overlay_strength="0.3" shape_divider_position="bottom" bg_image_animation="none"][vc_column column_padding="no-extra-padding" column_padding_position="all" background_color_opacity="1" background_hover_color_opacity="1" column_link_target="_self" column_shadow="none" column_border_radius="none" width="1/1" tablet_width_inherit="default" tablet_text_alignment="default" phone_text_alignment="default" overlay_strength="0.3" column_border_width="none" column_border_style="solid" bg_image_animation="none"][/vc_column][/vc_row]
    '''

    middleparte = ""
    for i in range(len):
        middleparte += tab1
        middleparte += names[i]
        middleparte += tab2
        middleparte += str(i)
        middleparte += tab3
        middleparte += str(i)
        middleparte += tab4
        middleparte += encode_url_and_base64(
            mannschaft_code_snippets[mannschafts_index[i]])
        middleparte += tab5
        middleparte += encode_url_and_base64(liga_code_snippets[liga_index[i]])
        middleparte += tab6

    result = ""
    result += anfang
    result += middleparte
    result += end
    pyperclip.copy(result)
    print("Copied to clipboard!")
    with open(f"output/output/{input[-1]}.txt", "w", encoding="utf-8") as file:
        file.write(result)
    print(f"Written to file output/{input[-1]}.txt")


folder_path = 'output/presets'
for file_name in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, file_name)) and file_name.endswith('.txt'):
        print(file_name)
        # Getting data for every file
        create_output(file_name)
