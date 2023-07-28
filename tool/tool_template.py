if True: # 固定引用開發環境 或 發佈環境 的 路徑
    import os, sys, custom_path
    config_path = os.getcwd() if os.getenv('COMPUTERNAME')=='VM-TESTER' else custom_path.custom_path['pdm_202209'] # 目前路徑
    sys.path.append(config_path); sys.path.append(os.path.join(config_path, 'tool'))


class PDM_Template():
    def __init__(self):
        pass
    def head(self):
        return {
            'product_name': '產品名稱',
            'product_attr': '工程屬性',
        }

    def body(self):
        return {
            'part_number':    '件號', # 文字
            'serial_number': '序號', #
            'bom_level':     '階數',
            'make_type':     '製造類別',
            'main_type':     '主品號',
            'drawing_book':  '圖冊',
            'drawing_no':    '圖號',
            'drawing_version': '版次',
            'part_no':       '品號',
            'part_name':     '工程品名',
            'part_spec':     '規格',
            'part_material': '材質',
            'make_htr':      '熱處理',
            'make_step':     '製程',
            'check_pd_type': '品號檢查',
            'check_pd_no':   '品號類別',
            'check_pd_box':  '庫別',
            'part_quantity': '用量',
            'salse_type':    '供貨狀態',
            'bom_type':      'BOM狀態',
            'bom_assemble':  '組件',
            'part_attr':     '工程屬性',
            'part_attr_remove': '移除屬性',
            'part_attr_backup': '屬性備選',
            'part_attr_low': '用料規則',
            'part_child':    '子零件',
        }

def test1():
    temp = PDM_Template()
    print(temp.head())
    for k, v in temp.head().items():
        print(k, v )

def test2():
    temp = PDM_Template()
    # print(temp.body())
    for k, v in temp.body().items():
        print(k, v )
if __name__ == '__main__':
    test2()