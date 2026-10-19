import streamlit as st
import pandas as pd

st.set_page_config(page_title="Loyverse 店鋪全品項自動對賬系統", layout="wide")

st.title("📸 Loyverse 報表 ⇄ 實體全品項點貨紙張 —— 自動對賬系統")
st.markdown("💡 **店鋪專屬換算規則**：左邊一箱箱進(IN)出(OUT)都要算。右邊散件只算賣出(OUT)。1 Set = 3 件。")

SET_TO_TIN_RATIO = 3

st.sidebar.header("📁 雙照片上傳區")
loyverse_img_file = st.sidebar.file_uploader("1. 上傳 Loyverse 銷售報表【截圖照片】", type=["jpg", "jpeg", "png"])
paper_img_file = st.sidebar.file_uploader("2. 上傳當天手寫點貨【紙張照片】", type=["jpg", "jpeg", "png"])

if loyverse_img_file and paper_img_file:
    st.success("✅ 雙照片已上傳成功！請根據您的實體紙張，在下方確認或微調今日數據：")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("### 📦 1. 左邊欄位 - 整箱進出 (Ctn)")
        st.write("**【大樽/瓶裝酒與紅酒 - 每箱12瓶】**")
        
        st.write("*Tiger Botol (大樽)*")
        p_tiger_botol_in = st.number_input("Tiger Botol 左邊 IN", value=-1)
        p_tiger_botol_out = st.number_input("Tiger Botol 左邊 OUT", value=5)
        l_tiger_botol_ctn = st.number_input("Loyverse：Tiger Botol 銷售箱數", value=6)
        
        st.write("*Anggur (紅酒)*")
        p_anggur_in = st.number_input("Anggur 左邊 IN", value=-1)
        p_anggur_out = st.number_input("Anggur 左邊 OUT", value=1)
        l_anggur_ctn = st.number_input("Loyverse：Anggur 銷售箱數", value=2)
        
        st.write("*Heineken & Anchor Botol*")
        p_heineken_botol_in = st.number_input("Heineken Botol 左邊 IN", value=-1)
        p_heineken_botol_out = st.number_input("Heineken Botol 左邊 OUT", value=0)
        p_anchor_botol_in = st.number_input("Anchor Botol 左邊 IN", value=0)
        p_anchor_botol_out = st.number_input("Anchor Botol 左邊 OUT", value=0)

        st.write("**【罐裝啤酒 - 每箱24罐】**")
        st.write("*1602 Lager Tin*")
        p_1602_in = st.number_input("1602 左邊 IN", value=0)
        p_1602_out = st.number_input("1602 左邊 OUT", value=3)
        l_1602_ctn = st.number_input("Loyverse：1602 銷售箱數", value=3)
        
        st.write("*Anchor Tin*")
        p_anchor_in = st.number_input("Anchor Tin 左邊 IN", value=0)
        p_anchor_out = st.number_input("Anchor Tin 左邊 OUT", value=5)
        l_anchor_ctn = st.number_input("Loyverse：Anchor Tin 銷售箱數", value=5)
        
        st.write("*Tiger Tin*")
        p_tiger_in = st.number_input("Tiger Tin 左邊 IN", value=0)
        p_tiger_out = st.number_input("Tiger Tin 左邊 OUT", value=0)

        st.write("**【能量飲/調酒 - 每箱12件】**")
        st.write("*Labour's*")
        p_labours_in = st.number_input("Labour's 左邊 IN", value=-4)
        p_labours_out = st.number_input("Labour's 左邊 OUT", value=0)
        l_labours_ctn = st.number_input("Loyverse：Labour's 銷售箱數", value=4)

    with col2:
        st.write("### 2. 右邊欄位 - 啤酒散件賣出 (OUT)")
        p_1602_tin = st.number_input("紙張右邊：1602 LAGER TIN (OUT)", value=12)
        l_1602_set = st.number_input("Loyverse：1602 賣出組數 (1Set=3罐)", value=4)
        
        p_anchor_tin = st.number_input("紙張右邊：ANCHOR TIN (OUT)", value=3)
        l_anchor_set = st.number_input("Loyverse：Anchor 賣出組數 (1Set=3罐)", value=1)
        
        p_tiger_tin = st.number_input("紙張右邊：TIGER TIN (OUT)", value=12)
        l_tiger_set = st.number_input("Loyverse：Tiger 賣出組數 (1Set=3罐)", value=4)
        
        p_carlsberg_tin = st.number_input("紙張右邊：CARLSBERG GREEN (OUT)", value=3)
        l_carlsberg_tin = st.number_input("Loyverse：Carlsberg Green 賣罐數", value=3)
        
        p_guinness_tin = st.number_input("紙張右邊：GUINNESS TIN (OUT)", value=3)
        l_guinness_tin = st.number_input("Loyverse：Guinness Tin 賣罐數", value=3)

        st.write("**【散裝洋酒/紅酒類 OUT】**")
        p_anggur = st.number_input("紙張右邊：ANGGUR 紅酒散瓶 (OUT)", value=11)
        l_anggur = st.number_input("Loyverse：Anggur 紅酒散瓶數", value=11)
        
        p_soju = st.number_input("紙張右邊：SOJU 燒酒散瓶 (OUT)", value=1)
        l_soju = st.number_input("Loyverse：Soju 賣出瓶數", value=1)

    with col3:
        st.write("### 3. 右邊欄位 - 飲料與香菸賣出 (OUT)")
        st.write("**【能量飲/調酒類散件 OUT】**")
        p_redbull = st.number_input("紙張右邊：RED BULL (OUT)", value=2)
        l_redbull = st.number_input("Loyverse：Red Bull 賣罐數", value=2)
        
        p_blackjack = st.number_input("紙張右邊：BLACK JACK'S (OUT)", value=2)
        l_blackjack = st.number_input("Loyverse：Black Jack's 賣罐數", value=2)
        
        p_labours_tin = st.number_input("紙張右邊：LABOUR'S 單罐 (OUT)", value=30)
        l_labours_tin = st.number_input("Loyverse：Labour's 單罐數", value=30)

        st.write("**【香菸類 - Rokok OUT】**")
        p_r129 = st.number_input("紙張右邊：香菸 RM12.90 (OUT)", value=1)
        l_r129 = st.number_input("Loyverse：香菸 RM12.90 包數", value=1)
        
        p_r167 = st.number_input("紙張右邊：香菸 RM16.70 (OUT)", value=2)
        l_r167 = st.number_input("Loyverse：香菸 RM16.70 包數", value=2)
        
        p_r182 = st.number_input("紙張右邊：香菸 RM18.20 (OUT)", value=4)
        l_r182 = st.number_input("Loyverse：香菸 RM18.20 包數", value=4)

    # 4. 全品項自動對賬邏輯中心
    st.subheader("📊 最終全品項雙流向對賬分析結果")
    
    # 建立一個方便格式化左邊箱數顯示的函式，原汁原味呈現 - 號和原始數字
    def format_paper_box(out_val, in_val):
        if in_val != 0:
            return f"OUT: {int(out_val)} 箱 / IN: {int(in_val)} 箱"
        return f"{int(out_val)} 箱"

    check_items = [
        {"name": "1602 啤酒 (整箱 Carton)", "system": f"{int(l_1602_ctn)} 箱", "paper": format_paper_box(p_1602_out, p_1602_in), "is_match": (p_1602_out - p_1602_in) == l_1602_ctn, "diff": (p_1602_out - p_1602_in) - l_1602_ctn, "unit": "箱"},
        {"name": "1602 啤酒 (單罐 Tin - 1 Set = 3罐)", "system": f"{int(l_1602_set * SET_TO_TIN_RATIO)} 罐", "paper": f"{int(p_1602_tin)} 罐", "is_match": (l_1602_set * SET_TO_TIN_RATIO) == p_1602_tin, "diff": p_1602_tin - (l_1602_set * SET_TO_TIN_RATIO), "unit": "罐"},
        {"name": "Anchor 啤酒 (整箱 Carton)", "system": f"{int(l_anchor_ctn)} 箱", "paper": format_paper_box(p_anchor_out, p_anchor_in), "is_match": (p_anchor_out - p_anchor_in) == l_anchor_ctn, "diff": (p_anchor_out - p_anchor_in) - l_anchor_ctn, "unit": "箱"},
        {"name": "Anchor 啤酒 (單罐 Tin - 1 Set = 3罐)", "system": f"{int(l_anchor_set * SET_TO_TIN_RATIO)} 罐", "paper": f"{int(p_anchor_tin)} 罐", "is_match": (l_anchor_set * SET_TO_TIN_RATIO) == p_anchor_tin, "diff": p_anchor_tin - (l_anchor_set * SET_TO_TIN_RATIO), "unit": "罐"},
        {"name": "Tiger 罐裝啤酒 (單罐 Tin - 1 Set = 3罐)", "system": f"{int(l_tiger_set * SET_TO_TIN_RATIO)} 罐", "paper": f"{int(p_tiger_tin)} 罐", "is_match": (l_tiger_set * SET_TO_TIN_RATIO) == p_tiger_tin, "diff": p_tiger_tin - (l_tiger_set * SET_TO_TIN_RATIO), "unit": "罐"},
        {"name": "Tiger 瓶裝啤酒 (整箱 Carton)", "system": f"{int(l_tiger_botol_ctn)} 箱", "paper": format_paper_box(p_tiger_botol_out, p_tiger_botol_in), "is_match": (p_tiger_botol_out - p_tiger_botol_in) == l_tiger_botol_ctn, "diff": (p_tiger_botol_out - p_tiger_botol_in) - l_tiger_botol_ctn, "unit": "箱"},
        {"name": "Carlsberg Green (單罐 Tin)", "system": f"{int(l_carlsberg_tin)} 罐", "paper": f"{int(p_carlsberg_tin)} 罐", "is_match": l_carlsberg_tin == p_carlsberg_tin, "diff": p_carlsberg_tin - l_carlsberg_tin, "unit": "罐"},
        {"name": "Guinness 啤酒 (單罐 Tin)", "system": f"{int(l_guinness_tin)} 罐", "paper": f"{int(p_guinness_tin)} 罐", "is_match": l_guinness_tin == p_guinness_tin, "diff": p_guinness_tin - l_guinness_tin, "unit": "罐"},
        {"name": "Anggur 紅酒 (整箱 Carton)", "system": f"{int(l_anggur_ctn)} 箱", "paper": format_paper_box(p_anggur_out, p_anggur_in), "is_match": (p_anggur_out - p_anggur_in) == l_anggur_ctn, "diff": (p_anggur_out - p_anggur_in) - l_anggur_ctn, "unit": "箱"},
        {"name": "Anggur 紅酒 (Bottle 散瓶)", "system": f"{int(l_anggur)} 支", "paper": f"{int(p_anggur)} 支", "is_match": l_anggur == p_anggur, "diff": p_anggur - l_anggur, "unit": "支"},
        {"name": "Soju 燒酒 (Bottle)", "system": f"{int(l_soju)} 支", "paper": f"{int(p_soju)} 支", "is_match": l_soju == p_soju, "diff": p_soju - l_soju, "unit": "支"},
        {"name": "Red Bull 紅牛 (單罐)", "system": f"{int(l_redbull)} 罐", "paper": f"{int(p_redbull)} 罐", "is_match": l_redbull == p_redbull, "diff": p_redbull - l_redbull, "unit": "罐"},
        {"name": "Black Jack's (單罐)", "system": f"{int(l_blackjack)} 罐", "paper": f"{int(p_blackjack)} 罐", "is_match": l_blackjack == p_blackjack, "diff": p_blackjack - l_blackjack, "unit": "罐"},
        {"name": "Labour's 啤酒 (整箱 Carton)", "system": f"{int(l_labours_ctn)} 箱", "paper": format_paper_box(p_labours_out, p_labours_in), "is_match": (p_labours_out - p_labours_in) == l_labours_ctn, "diff": (p_labours_out - p_labours_in) - l_labours_ctn, "unit": "箱"},
        {"name": "Labour's 啤酒 (單罐 Tin)", "system": f"{int(l_labours_tin)} 罐", "paper": f"{int(p_labours_tin)} 罐", "is_match": l_labours_tin == p_labours_tin, "diff": p_labours_tin - l_labours_tin, "unit": "罐"},
        {"name": "香菸 RM12.90", "system": f"{int(l_r129)} 包", "paper": f"{int(p_r129)} 包", "is_match": l_r129 == p_r129, "diff": p_r129 - l_r129, "unit": "包"},
        {"name": "香菸 RM16.70", "system": f"{int(l_r167)} 包", "paper": f"{int(p_r167)} 包", "is_match": l_r167 == p_r167, "diff": p_r167 - l_r167, "unit": "包"},
        {"name": "香菸 RM18.20", "system": f"{int(l_r182)} 包", "paper": f"{int(p_r182)} 包", "is_match": l_r182 == p_r182, "diff": p_r182 - l_r182, "unit": "包"},
    ]
    
    res_data = []
    has_error = False
    for item in check_items:
        if item["is_match"]:
            status = "✅ 完全吻合"
        else:
            status = f"⚠️ 數據不符 (差了 {int(item['diff'])} {item['unit']})"
            has_error = True
        res_data.append({
            "商品項目": item["name"],
            "Loyverse 系統銷量（換算後）": item["system"],
            "紙張手寫記錄（原始呈现）": item["paper"],
            "對賬狀態": status
        })
    
    res_df = pd.DataFrame(res_data)
    def color_status(val):
        if "完全吻合" in str(val): return 'background-color: #d4edda; color: #155724; font-weight: bold;'
        if "數據不符" in str(val): return 'background-color: #f8d7da; color: #721c24; font-weight: bold;'
        return ''
        
    st.table(res_df.style.map(color_status, subset=['對賬狀態']))
    
    if has_error:
