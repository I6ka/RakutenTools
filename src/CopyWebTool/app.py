import os

#1_作成するhtmlファイルを選択（モードを選択）
def Select_Mode():
    Mode = input("作成するファイルを選択してください（1:pc-details 2:pc-overray 3:phone-details 4:phone-items）:")
    #pc-details.html
    if Mode == "1":
        create_pc_details()
    #pc-overray.html
    elif Mode == "2":
        create_pc_overray()
    #phone-details.html
    elif Mode == "3":
        create_phone_details()
    #phone-items.html
    elif Mode == "4":
        create_phone_items()
    else:
        print("1~4で入力してください")
#2_モードに従ってコードを発行
def create_pc_details():
    judge = "Y"
    #ファイルの入力
    htmlfile = ""
    itemtitle = input("内容を入力してください:")
    description_save = input("保存方法を入力してください:")
    htmlfile += """
        <table class="design01"> 
        <tr>
            <th>内容</th>
            <td>{itemtitle}</td>
            <th>保存方法</th>
            <td>{description_save}</td>
        </tr>
        </table>
        """.format(itemtitle=itemtitle,description_save=description_save)
    while judge == "Y":
        th_item_name = input("商品名称を入力してください: ")
        td_item_material = input("原材料を入力してください: ")
        td_item_size = input("商品の内容量を入力してください: ")
        htmlfile += """
        <br>
        <table class="design01">   
            <!-- 行1 -->
            <tr>
                <th>名称</th>
            </tr>
            <!-- 行2 -->
            <tr>
                <td>{th_item_name}</td>
            </tr>
            <tr>
                <th>原材料</th>
            </tr>
            <tr>
                <td>{td_item_material}</td>
            </tr>
            <tr>
                <th>内容量</th>
            </tr>
            <tr>
                <td>{td_item_size}</td>
            </tr>
            <tr>
                <th>賞味期限</th>
            </tr>
            <tr>
                <td>パッケージに記載</td>
            </tr>
            <tr>
                <th>製造者</th>
            </tr>
            <tr>
                <td>有限会社ミートの元気商事 ( 山形県山形市下条町５丁目６－１２ )</td>
            </tr>
        </table>
        """.format(th_item_name=th_item_name,td_item_material=td_item_material,td_item_size=td_item_size)
        judge = input("続けますか？（Y/N）:")

    html_code_head = '''
    <html>
    <head>
        <meta charset='utf-8'>
    </head>
    <style type="text/css">
        .design01 {{
            width: 100%;
            text-align: left;
            padding: 3;
            border-collapse: collapse;
            border-spacing: 0;
        }}
        .design01 th {{
            font-size:16px;
            font-family:"Noto Serif JP",serif;
            font-weight: normal;
            background: #DDD;
            border: solid 1px #000;
        }}
        .design01 td {{
            font-size:16px;
            font-family:"Noto Serif JP",serif;
            border: solid 1px #000;
        }}
    </style>
    <body>
        {pc_overray}
    </body>
    </html>
    '''.format(pc_overray=htmlfile)
    #ファイル名の入力と保存に遷移
    filesave(html_code_head)
def create_pc_overray():
    judge = "Y"
    #ファイルの入力
    htmlfile = ""
    while judge == "Y":
        itemtitle = input("INPUT_item-title:")
        imgurl = input("INPUT_imgurl:")
        itemdetails = input("INPUT_itemdetails:").replace('@@','<br>')
        htmlfile += """
        <p class="item-title">{item_title}</p>
        <img src="{img_url}" width=700></img>
        <p class="item-details">{item_details}</p>
        """.format(item_title=itemtitle,img_url=imgurl,item_details=itemdetails)
        judge = input("続けますか？（Y/N）:")
    html_code_head = '''
    <html>
    <head>
        <meta charset='utf-8'>
    </head>
    <style type="text/css">
    .item-title{{
        border-bottom:1px solid;
        font-size:30px;
        width: 700px;        
        text-align:center;
        font-family:"Noto Serif JP",serif;
    }}
    .item-details{{
        font-size:16px;
        background-color: #EEE;
        width: 700px;   
        font-family:"Noto Serif JP",serif;
    }}
    </style>
    <body>
        {pc_overray}
    </body>
    </html>
    '''.format(pc_overray=htmlfile)
    #ファイル名の入力と保存に遷移
    filesave(html_code_head)
def create_phone_details():
    judge = "Y"
    #ファイルの入力
    htmlfile = ""
    itemtitle = input("内容を入力してください:")
    description_save = input("保存方法を入力してください:")
    htmlfile += """
        <table align="left" frame="void" border="2">
            <th bgcolor="#DDD"><font>内容</font></th>
            <td bgcolor="#fff"><font>{itemtitle}</font></td>
            <th bgcolor="#DDD"><font>保存方法</font></th>
            <td bgcolor="#fff"><font>{description_save}</font></th>
        </table>
        <br><br>
        """.format(itemtitle=itemtitle,description_save=description_save)
    while judge == "Y":
        th_item_name = input("商品名称を入力してください: ")
        td_item_material = input("原材料を入力してください: ")
        td_item_size = input("商品の内容量を入力してください: ")
        htmlfile += """
        <table align="left" frame="void" border="2"> 
            <tr>
                <th bgcolor="#DDD"><font>名称</font></th>
            </tr>   
            <tr>
                <td bgcolor="#fff"><font>{th_item_name}</font></td>
            </tr>
            <tr>
                <th bgcolor="#DDD"><font>原材料</font></th>
            </tr>   
            <tr>
                <td bgcolor="#fff"><font>{td_item_material}</font></td>
            </tr>
            <tr>
                <th bgcolor="#DDD"><font>内容量</font></th>
            </tr>   
            <tr>
                <td bgcolor="#fff"><font>{td_item_size}</font></td>
            </tr>
            <tr>
                <th bgcolor="#DDD"><font>賞味期限</font></th>
            </tr>
            <tr>
                <td bgcolor="#fff"><font>パッケージに記載</font></td>
            </tr>
            <tr>
                <th bgcolor="#DDD"><font>製造者</font></th>
            </tr>
            <tr>
                <td bgcolor="#fff"><font>有限会社ミートの元気商事 ( 山形県山形市下条町５丁目６－１２ )</font></td>
            </tr>
        </table>
        """.format(th_item_name=th_item_name,td_item_material=td_item_material,td_item_size=td_item_size)
        judge = input("続けますか？（Y/N）:")


    html_code_head = '''
    <html>
    <head>
        <meta charset='utf-8'>
    </head>
    <body>
        {pc_overray}
    </body>
    </html>
    '''.format(pc_overray=htmlfile)
    #ファイル名の入力と保存に遷移
    filesave(html_code_head)
def create_phone_items():
    judge = "Y"
    #ファイルの入力
    htmlfile = ""
    while judge == "Y":
        itemtitle = input("INPUT_item-title:")
        imgurl = input("INPUT_imgurl:")
        itemdetails = input("INPUT_itemdetails(改行は@@と入力してください):").replace('@@','<br>')
        htmlfile += """
        <center>
        <p align="center"><font size="4">{itemtitle}</font></p>
        <hr size="2" color="#000"></hr>
        </center>
        <img src="{imgurl}" width=700>
        <br>
        <table>
            <td bgcolor="#EEE" width="700px" >
                <font size="2px">
                    {itemdetails}
                </font>
            </td>
        </table><br>
        """.format(itemtitle=itemtitle,imgurl=imgurl,itemdetails=itemdetails)
        judge = input("続けますか？（Y/N）:")
    html_code_head = '''
    <html>
    <head>
        <meta charset='utf-8'>
    </head>
    <body>
        {pc_overray}
    </body>
    </html>
    '''.format(pc_overray=htmlfile)

    #ファイル名の入力と保存に遷移
    filesave(html_code_head)

#3_ファイル名を入力＆保存
def filesave(html_code):
    filename = input("保存するファイル名を入力してください：")
    path = os.path.dirname(__file__) + "/"
    file = path + filename + ".html"

    with open(file,'w',encoding='utf-8') as f:
        f.write(html_code)
        f.close()
    Continue_Check()

#4_ファイル作成実行の確認
def Continue_Check():
    Continue = input("操作を続けますか？(Y/N):")
    if Continue == "Y":
        Select_Mode()
    elif Continue == "N":
        return 0

if __name__ == '__main__':
    Select_Mode()
