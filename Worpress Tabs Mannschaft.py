import pyperclip
import base64
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


# Read the content of the code_snippets.txt file
with open('data/Mannschaft/code_snippets_big.txt', 'r', encoding='utf-8') as file:
    code_snippets_big = file.read()

code_snippets_big2 = [snippet.replace('\n', ' ')
                      for snippet in code_snippets_big.strip().split('\n\n')]


with open('input.txt', 'r', encoding='utf-8') as file:
    input = file.read().splitlines()
indeces = []
names = []
len = int(input[0])
for i in range(len):
    indeces.append(int(input[i+1]))
    names.append(input[i+1+len])


anfang = f'''
[/vc_column_text][divider line_type="Full Width Line" line_thickness="4" divider_color="accent-color" animate="yes" custom_height="50"][tabbed_section style="default" alignment="left" spacing="default" tab_color="Accent-Color"]
'''
tab1 = f'[tab icon_family="none" title="'
tab2 = f'" id="'
tab3 = f'" tab_id="'
tab4 = f'"][vc_raw_html]'
tab5 = f'[/vc_raw_html][/tab]'

end = f'''
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
    middleparte += encode_url_and_base64(code_snippets_big2[indeces[i]])
    middleparte += tab5


result = ""
result += anfang
result += middleparte
result += end
pyperclip.copy(result)
print("Copied to clipboard!")
