import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
from dash import html, Output, Input, callback
import pandas as pd
from dash_iconify import DashIconify
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

data = [["1", "工單查詢"], ["2", "工廠工站查詢"], ["3", "員工編號查詢"]]

df = pd.read_csv('整合後檔案.csv')
df2 = pd.read_csv('Factoryworkstation.csv')
df3 = pd.read_csv('virtual_data_with_permissions.csv')
selected_data_1 = [{'value':value,'label':value} for value in df.Date.unique()]
selected_data_2 = [{'value': value, 'label': value} for value in df2.Plant.unique()]
selected_data_3 = [{'value': value, 'label': value} for value in df3.ID.unique()]

app.layout = dmc.MantineProvider(

 dmc.AppShell(
    [
        dmc.AppShellHeader(
                dmc.NavLink(
                    label="職能發展學院",
                    leftSection=DashIconify(icon="tabler:gauge"),
                    active=True,
                    variant="filled",
                    color="blue",
                    id="school_icon",
                    h=70,
                    href='/',
                    refresh=True                                    
                ),
                h=70         
        
            ),
        dmc.AppShellMain(
            children=[ dmc.Container(        
                    dmc.Title(f"風扇良率判定及相關資料查詢系統", order=2),
                    fluid=True,
                    ta='center',
                    my=30  
                ),
                dmc.Flex(
                         [
            html.Div(
                        [#選單欄位
                            dmc.RadioGroup(
                                children=dmc.Group([dmc.Radio(l, value=k) for k, l in data], my=10),
                                id="radiogroup-simple",
                                value="1",
                                label="請選擇模式",
                                size="md",
                                mb=10,
                                style={
                                                "width": 500,
                                                "margin": "0 auto",  # 居中對齊
                                }

                            ),        
                                dmc.Select(
                                    label="請選擇",
                                    placeholder="請選擇1個",
                                    id="dropdown-selection",
                                    value="",
                                    data=selected_data_1,
                                    w=200,
                                    mb=10,
                                ),
                                
                            
                        ]
                    ),
                        dmc.Box([
                                        dmc.Text(
                                            id="radio-output",
                                            style={
                                                "width": 700,
                                                "maxWidth": "1000px",
                                                "margin": "0 auto",  # 居中對齊
                                            },
                                        )
                                    ],
                                    style={"padding": "20px"},  # 外框填充
                                ),

                          ],
                                                        

                                            )
        ]),
    ],
    header={"height": 70},
    padding="xl",    

)
)


@callback(
    Output("dropdown-selection", "data"),
    Input("radiogroup-simple", "value"),
)
def update_dropdown(radio_value):
    # **紅色修改部分：根據 Radio 值返回不同選單內容**
    if radio_value == "1":
        return [{'value': value, 'label': value} for value in df.Date.unique()]
    elif radio_value == "2":
        return [{'value': value, 'label': value} for value in df2.Plant.unique()]
    elif radio_value == "3":
        return [{'value': value, 'label': value} for value in df3.ID.unique()]





@callback(

        Output("radio-output", "children"), 
        Input("radiogroup-simple", "value"),
        Input("dropdown-selection", "value"))
def choose_framework(R_value,D_Value):
    if R_value == "1":
        dff = df[df.Date == D_Value]
        diff = dff[['Date','OrderID','Product','Prediction','Confidence']]
        diff['Confidence'] = diff['Confidence'].apply(lambda x: f"{x:.3f}")
        elements = diff.to_dict('records')
        rows = [
        dmc.TableTr(
            [   dmc.TableTd(element["Date"]),
                dmc.TableTd(element["OrderID"]),
                dmc.TableTd(element["Product"]),
                dmc.TableTd(element["Prediction"]),
                dmc.TableTd(element["Confidence"]),
            ]
        )
        for element in elements
        ]

        head = dmc.TableThead(
            dmc.TableTr(
                [   dmc.TableTh("日期"),
                    dmc.TableTh("工單號碼"),
                    dmc.TableTh("產品料號"),
                    dmc.TableTh("判定結果"),
                    dmc.TableTh("評估指數"),
                ]
            )
        )
        body = dmc.TableTbody(rows)
        caption = dmc.TableCaption("工單詳細清單")


        return dmc.LineChart(
    h=300,
    dataKey="date",
    data=elements,
    series = [
        {"name": "Confidence", "color": "blue.6"},
    ],
    curveType="linear",
    tickLine="xy",
    withXAxis=False,
    withDots=False,
),dmc.Table([head, body, caption])
    

    elif R_value == "2":
        dff2 = df2[df2.Plant == D_Value]
        diff2 = dff2[['Plant','Workstation Code',"Code",'Step Name (English)','Step Name (Chinese)']]
        elements = diff2.to_dict(orient='records')
        rows = [
        dmc.TableTr(
            [
                dmc.TableTd(element["Plant"]),
                dmc.TableTd(element["Workstation Code"]),
                dmc.TableTd(element["Code"]),
                dmc.TableTd(element["Step Name (English)"]),
                dmc.TableTd(element["Step Name (Chinese)"]),
            ]
        )
        for element in elements
        ]

        head = dmc.TableThead(
            dmc.TableTr(
                [
                    dmc.TableTh("廠區"),
                    dmc.TableTh("車間"),
                    dmc.TableTh("工站名稱"),
                    dmc.TableTh("工站完整名稱(英文)"),
                    dmc.TableTh("工站完整名稱(中文)"),
                ]
            )
        )
        body = dmc.TableTbody(rows)
        caption = dmc.TableCaption("廠區工站查詢")
        return dmc.Table([head, body, caption])
    elif R_value == "3":
        dff3 = df3[df3.ID == D_Value]
        diff3 = dff3[['ID','姓名','權限代號']]
        elements = diff3.to_dict(orient='records')
        rows = [
        dmc.TableTr(
            [
                dmc.TableTd(element["ID"]),
                dmc.TableTd(element["姓名"]),
                dmc.TableTd(element["權限代號"]),
            ]
        )
        for element in elements
        ]

        head = dmc.TableThead(
            dmc.TableTr(
                [
                    dmc.TableTh("ID"),
                    dmc.TableTh("姓名"),
                    dmc.TableTh("權限代號"),
                ]
            )
        )
        body = dmc.TableTbody(rows)
        caption = dmc.TableCaption("員工查詢")
        return dmc.Table([head, body, caption])


if __name__ == "__main__":
    app.run(debug=True)