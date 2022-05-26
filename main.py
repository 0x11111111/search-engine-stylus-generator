import json
import PySimpleGUI as sg
import base64
import os
import time


class FileTypeNotSupportedError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class DependencyFileError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def img2base64(img_path) -> str:
    """An image-to-base64 convertor.

    Convert input image file into base64 form.

    Args:
        img_path (str): currently supports local image files only. URL form will be implemented in the next version.

    Returns:
        str: image content displayed in html url().
    """
    mime_dict = {
        'apng': 'apng',
        'avif': 'avif',
        'bmp': 'bmp',
        'gif': 'gif',
        'ico': 'x-icon',
        'cur': 'x-icon',
        'jpeg': 'jpeg',
        'jpg': 'jpeg',
        'jfif': 'jpeg',
        'pjpeg': 'jpeg',
        'pjp': 'jpeg',
        'png': 'png',
        'webp': 'webp'
    }

    if os.path.exists(img_path):
        extension = img_path.split('.')[-1]
        mime_type = None
        if extension in mime_dict:
            mime_type = mime_dict[extension]
        else:
            raise FileTypeNotSupportedError('File type \"{}\" not supported.'.format(extension))

        with open(img_path, 'rb') as img:
            img_base64 = base64.b64encode(img.read())
            return 'data:image/{};base64,{}'.format(mime_type, img_base64.decode('utf-8'))
    else:
        raise FileNotFoundError('Image file {} not found.'.format(img_path))


def get_option() -> dict:
    """GUI of the generator.

    Fetch file path and destination name from user.

    Returns:
        dict: contains file_name, bg_image_text_path, logo_image_text_path.
    """
    layout = [
        [
            sg.Text(text='文件名 File Name', size=(30, 1), font='Any 15'),
            sg.InputText(key='file_name', font='Any 15')
        ],
        [
            sg.Text(text='背景图 Background Image', size=(30, 1), font='Any 15'),
            sg.InputText(key='bg_image_text_path', font='Any 15'),
            sg.FileBrowse(key='bg_image_path', button_text='浏览 Browse', font='Any 15')
        ],
        [
            sg.Text(text='图标 Logo Image', size=(30, 1), font='Any 15'),
            sg.InputText(key='logo_image_text_path', font='Any 15'),
            sg.FileBrowse(key='logo_image_path', button_text='浏览 Browse', font='Any 15')
        ],
        [
            sg.Submit(key='submit', button_text='提交 Submit', font='Any 15'),
            sg.Text(text='', size=(60, 1), font='Any 15'),
            sg.Cancel(key='exit', button_text='退出 Exit', font='Any 15')
        ]
    ]

    window = sg.Window('Stylus Generator', layout)

    # Event loop
    while True:
        event, values = window.read(timeout=100)
        if event == 'exit' or event == sg.WIN_CLOSED:
            break
        elif event == 'submit':
            if values['bg_image_text_path'] == '':
                sg.popup('请选择背景图 Please choose a Background Image', font='Any 15')
                event = ''
            elif values['logo_image_text_path'] == '':
                sg.popup('请选择图标 Please choose a Logo Image', font='Any 15')
                event = ''
            else:
                break

    window.close()
    return values


if __name__ == '__main__':

    option = get_option()
    dst_path = None
    timestamp = int(time.time() * 1000)
    # print(option)

    if option:
        try:
            content_path = './content.json'
            dst_path = option['file_name'] + '.json' if option['file_name'] else 'SESG_style.json'
            if not os.path.exists(content_path):
                raise DependencyFileError('File content.json not found.')

            with open(content_path, 'r') as f:
                content = json.load(f)
                f.close()

            if not content:
                raise DependencyFileError('File content.json damaged or empty')

        except:
            print('File not found or conversion failed')

        bg_path = option['bg_image_text_path']
        logo_path = option['logo_image_text_path']
        bg_base64 = img2base64(bg_path)
        logo_base64 = img2base64(logo_path)

        main_body = content['main_body']
        regexps = content['regexps']
        code = content['code']
        code = code.replace('{bg_img}', bg_base64)
        code = code.replace('{logo_img}', logo_base64)
        code = code.replace('\u00A0', ' ')

        file_name = 'SESG Generated Shigure\'s Google Arknights Theme ' + (option['file_name'] if option['file_name'] \
            else str(timestamp))
        source_code_header = content['sourceCode_header']
        source_code = source_code_header.replace('{file_name}', file_name)
        source_code = source_code.replace('{code}', code)
        source_code = source_code.replace('\u00A0', ' ')
        # default_resource = content['default_resource']

        main_body[1]['installDate'] = timestamp
        main_body[1]['sections'][0]['code'] = code
        main_body[1]['sections'][0]['regexps'] = regexps
        main_body[1]['sourceCode'] = source_code
        main_body[1]['usercssData']['name'] = main_body[1]['name'] = file_name

        # print(main_body)

        with open(dst_path, 'w') as f:
            json.dump(main_body, f)
            f.close()
