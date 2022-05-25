import json
import PySimpleGUI as sg
import base64
import os
import time


def img2base64(img_path):
    if os.path.exists(img_path):
        with open(img_path, 'rb') as img:
            img_base64 = base64.b64encode(img.read())
            return 'data:image/png;base64,' + img_base64.decode('utf-8')
    else:
        raise Exception


def get_option() -> dict:

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
    # json_dict = [{'settings': {'openEditInWindow': False, 'openEditInWindow.popup': False, 'windowPosition': {}, 'show-badge': True, 'disableAll': False, 'exposeIframes': False, 'newStyleAsUsercss': False, 'styleViaXhr': False, 'patchCsp': False, 'config.autosave': True, 'popup.breadcrumbs': True, 'popup.breadcrumbs.usePath': False, 'popup.enabledFirst': True, 'popup.stylesFirst': True, 'popup.autoResort': False, 'popup.borders': False, 'popup.findStylesInline': True, 'popup.findSort': 'u', 'manage.onlyEnabled': False, 'manage.onlyLocal': False, 'manage.onlyUsercss': False, 'manage.onlyEnabled.invert': False, 'manage.onlyLocal.invert': False, 'manage.onlyUsercss.invert': False, 'manage.actions.expanded': True, 'manage.backup.expanded': True, 'manage.filters.expanded': False, 'manage.newUI': True, 'manage.newUI.favicons': False, 'manage.newUI.faviconsGray': True, 'manage.newUI.targets': 3, 'manage.newUI.sort': 'title,asc', 'editor.options': {}, 'editor.toc.expanded': True, 'editor.options.expanded': True, 'editor.lint.expanded': True, 'editor.publish.expanded': True, 'editor.lineWrapping': False, 'editor.smartIndent': True, 'editor.indentWithTabs': False, 'editor.tabSize': 4, 'editor.keyMap': 'sublime', 'editor.theme': 'default', 'editor.beautify': {'selector_separator_newline': True, 'newline_before_open_brace': False, 'newline_after_open_brace': True, 'newline_between_properties': True, 'newline_before_close_brace': True, 'newline_between_rules': False, 'preserve_newlines': True, 'end_with_newline': False, 'indent_conditional': True}, 'editor.beautify.hotkey': '', 'editor.lintDelay': 300, 'editor.linter': 'csslint', 'editor.lintReportDelay': 500, 'editor.matchHighlight': 'token', 'editor.autoCloseBrackets': True, 'editor.autocompleteOnTyping': False, 'editor.contextDelete': True, 'editor.selectByTokens': True, 'editor.appliesToLineWidget': True, 'editor.livePreview': True, 'editor.colorpicker': True, 'editor.colorpicker.hexUppercase': False, 'editor.colorpicker.hotkey': '', 'editor.colorpicker.color': '', 'editor.colorpicker.maxHeight': 300, 'hotkey._execute_browser_action': '', 'hotkey.openManage': '', 'hotkey.styleDisableAll': '', 'sync.enabled': 'none', 'iconset': 0, 'badgeDisabled': '#8B0000', 'badgeNormal': '#006666', 'popupWidth': 246, 'updateInterval': 24}}, {'enabled': True, 'updateUrl': 'https://cdn.jsdelivr.net/gh/33kk/uso-archive@flomaster/data/usercss/186139.user.css', 'url': 'https://uso.kkx.one/style/186139', 'installDate': 1652628609141, 'sections': [{'code': '.L3eUgb {\n        background: url("{}") center center !important;\n        background-size: cover !important;\n    }\n    .o3j99 {\n        background: transparent !important;\n    }\n\n\n    /* change color of bottom texts "About Adertising Bussiness ..." */\n    a.pHiOh {\n        color: gainsboro !important;\n    }\n\n    /*location text "United States" */\n    .uU7dJb {\n        color: gainsboro !important/* text color */;\n        border-bottom: 1px solid #cccbcb5e\n    }\n\n\n    a.EzVRq {\n        color: #fff !important\n    }\n\n    a.gb_g {\n        color: gainsboro\n    }\n\n    div#SIvCob {\n        display: none!important;\n    }\n\n    .o3j99.ikrT4e.om7nvf {\n        opacity: 0.75!important;\n    }\n\n    .gb_pa {\n        background-color: rgba(32, 33, 36, 0) !important;\n    }\n\n\n    .b0KoTc {\n        display: none !important;\n    }\n    \n    .lnXdpd{\n        content:url("https://bakaimg.oss-cn-hangzhou.aliyuncs.com/img/logo.png") !important;\n    }\n\n    /*[[icons]]*/\n\n    \n    #logo {\n        background: url("{}") 50% 80% no-repeat !important;\n        /*TOP LEFT ARKNIGHTS LOGO*/\n        background-size: contain !important;\n        padding-bottom: 80px !important;\n        bottom: 70px !important;\n    }', 'start': 531, 'regexps': ['(.*)\\.google\\.(.*)']}], 'sourceCode': '/* ==UserStyle==\n@name           Shigure`s Google Arknights Theme\n@namespace      USO Archive\n@author         bakashigure\n@description    `google.com  Arknights Theme</br>theme by <a href="https://twitter.com/bakashigure ">@bakashigure</a> </br>illustrator <a href="https://twitter.com/lococo31955424 ">@lococo31955424</a> </br>thanks <a href="https://twitter.com/DYProMIKE">@DYProMIKE</a>`\n@version        20211117.12.26\n@license        CC0-1.0\n@preprocessor   uso\n==/UserStyle== */\n@-moz-document regexp("(.*)\\\\.google\\\\.(.*)") {\n    .L3eUgb {\n        background: url(https://bakaimg.oss-cn-hangzhou.aliyuncs.com/img/mrfz.jpg) center center !important;\n        background-size: cover !important;\n    }\n    .o3j99 {\n        background: transparent !important;\n    }\n\n\n    /* change color of bottom texts "About Adertising Bussiness ..." */\n    a.pHiOh {\n        color: gainsboro !important;\n    }\n\n    /*location text "United States" */\n    .uU7dJb {\n        color: gainsboro !important/* text color */;\n        border-bottom: 1px solid #cccbcb5e\n    }\n\n\n    a.EzVRq {\n        color: #fff !important\n    }\n\n    a.gb_g {\n        color: gainsboro\n    }\n\n    div#SIvCob {\n        display: none!important;\n    }\n\n    .o3j99.ikrT4e.om7nvf {\n        opacity: 0.75!important;\n    }\n\n    .gb_pa {\n        background-color: rgba(32, 33, 36, 0) !important;\n    }\n\n\n    .b0KoTc {\n        display: none !important;\n    }\n    \n    .lnXdpd{\n        content:url("https://bakaimg.oss-cn-hangzhou.aliyuncs.com/img/logo.png") !important;\n    }\n\n    /*[[icons]]*/\n\n    \n    #logo {\n        background: url("https://bakaimg.oss-cn-hangzhou.aliyuncs.com/img/logo.png") 50% 80% no-repeat !important;\n        /*TOP LEFT ARKNIGHTS LOGO*/\n        background-size: contain !important;\n        padding-bottom: 80px !important;\n        bottom: 70px !important;\n    }\n}', 'usercssData': {'name': 'Shigure`s Google Arknights Theme', 'namespace': 'USO Archive', 'author': 'bakashigure', 'description': 'google.com  Arknights Theme</br>theme by <a href="https://twitter.com/bakashigure ">@bakashigure</a> </br>illustrator <a href="https://twitter.com/lococo31955424 ">@lococo31955424</a> </br>thanks <a href="https://twitter.com/DYProMIKE">@DYProMIKE</a>', 'version': '20211117.12.26', 'license': 'CC0-1.0', 'preprocessor': 'uso'}, 'author': 'bakashigure', 'description': 'google.com  Arknights Theme</br>theme by <a href="https://twitter.com/bakashigure ">@bakashigure</a> </br>illustrator <a href="https://twitter.com/lococo31955424 ">@lococo31955424</a> </br>thanks <a href="https://twitter.com/DYProMIKE">@DYProMIKE</a>', 'name': 'Shigure`s Google Arknights Theme', 'installationUrl': 'https://uso.kkx.one/style/186139', 'originalDigest': 'ee3c470e3a71ed8a0db90a744aba43d6740440ec', '_id': '50c220b0-f2b2-46a2-9994-7f8086955c42', '_rev': 1652628609142, 'id': 3}]

    option = get_option()
    print(option)

    if option:
        content_path = './content.json'
        dst_path = option['file_name'] + '.json'
        content = None
        if not os.path.exists(content_path):
            print("content.json not found.")
            exit(1)


        with open(content_path, 'r') as f:
            content = json.load(f)

        if not content:
            print('content.json damaged or empty')
            exit(2)

        bg_path = option['bg_image_text_path']
        logo_path = option['logo_image_text_path']

        try:
            bg_base64 = img2base64(bg_path)
            logo_base64 = img2base64(logo_path)

            # print(bg_base64)
            # print(logo_base64)
            #
            # with open('./bg_base64.txt', 'w') as bg_f:
            #     bg_f.write(bg_base64)
            #
            # with open('./logo_base64.txt', 'w') as logo_f:
            #     logo_f.write(logo_base64)

        except:
            print('File not found or conversion failed')

        timestamp = int(time.time() * 1000)
        main_body = content['main_body']
        regexps = content['regexps']
        code = content['code']
        code = code.replace('{bg_img}', bg_base64)
        code = code.replace('{logo_img}', logo_base64)
        code = code.replace('\u00A0', ' ')

        source_code_header = content['sourceCode_header']
        source_code = source_code_header.replace('{code}', code)
        source_code = source_code.replace('\u00A0', ' ')
        # default_resource = content['default_resource']

        main_body[1]['installDate'] = timestamp
        main_body[1]['sections'][0]['code'] = code
        main_body[1]['sections'][0]['regexps'] = regexps
        main_body[1]['sourceCode'] = source_code

        # print(main_body)

        with open(dst_path, 'w') as f:
            json.dump(main_body, f)
