import streamlit as st
import pandas as pd

st.set_page_config(page_title="Loyverse 店鋪全品項自動對賬系統", layout="wide")

st.title("📱 Loyverse 截圖 ⇄ 實體全品項點貨紙張 —— 自動對賬系統")
st.markdown("💡 **終極無卡死版啟用成功**：本系統已完全配置您店鋪專屬的規格換算規則。請在左側上傳今日的兩張照片（留存備查），並在下方確認或微調今日的實體數據，系統將實時為您呈現百分之百精準的對賬結果。")

SET_TO_TIN_RATIO = 3

st.sidebar.header("📁 雙照片上傳與存檔區")
loyverse_img_file = st.sidebar.file_uploader("1. 上傳今日 Loyverse 銷售畫面【截圖照片】", type=["jpg", "jpeg", "png"])
paper_img_file = st.sidebar.file_uploader("2. 上傳當天手寫點貨【紙張照片】", type=["jpg", "jpeg", "png"])

if loyverse_img_file and paper_img_file:
    st.success("✅ 雙照片上傳成功！請對照您拍的照片，在下方確認或微調今日的數據，對賬表格會即時在下方更新：")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("### 📦 1. 左邊欄位 - 整箱進出 (Ctn)")
        st.write("**【大樽/瓶裝酒與紅酒 - 每箱12瓶】**")
        
        st.write("*Tiger Botol (大樽)*")
        p_tiger_botol_in = st.number_input("Tiger Botol 左邊今日進貨 (IN) *扣回請填負數*", value=-1, key="tb_in")
        p_tiger_botol_out = st.number_input("Tiger Botol 左邊今日出貨 (OUT)", value=5, key="tb_out")
        l_tiger_botol_ctn = st.number_input("Loyverse 顯示：Tiger Botol 銷售箱數", value=6)
        
        st.write("*Anggur (紅酒)*")
        p_anggur_in = st.number_input("Anggur 左邊今日進貨 (IN) *扣回請填負數*", value=-1, key="ag_in")
        p_anggur_out = st.number_input("Anggur 左邊今日出貨 (OUT)", value=1, key="ag_out")
        l_anggur_ctn = st.number_input("Loyverse 顯示：Anggur 銷售箱數", value=2)
        
        st.write("*Heineken & Anchor Botol*")
        p_heineken_botol_in = st.number_input("Heineken Botol 左邊今日進貨 (IN)", value=-1)
        p_heineken_botol_out = st.number_input("Heineken Botol 左邊今日出貨 (OUT)", value=0)
        p_anchor_botol_in = st.number_input("Anchor Botol 左邊今日進貨 (IN)", value=0)
        p_anchor_botol_out = st.number_input("Anchor Botol 左邊今日出貨 (OUT)", value=0)

        st.write("**【罐裝啤酒 - 每箱24罐】**")
        st.write("*1602 Lager Tin*")
        p_1602_in = st.number_input("1602 左邊今日進貨 (IN)", value=0)
        p_1602_out = st.number_input("1602 左邊今日出貨 (OUT)", value=3)
        l_1602_ctn = st.number_input("Loyverse 顯示：1602 銷售箱數", value=3)
        
        st.write("*Anchor Tin*")
        p_anchor_in = st.number_input("Anchor Tin 左邊今日進貨 (IN)", value=0)
        p_anchor_out = st.number_input("Anchor Tin 左邊今日出貨 (OUT)", value=5)
        l_anchor_ctn = st.number_input("Loyverse 顯示：Anchor Tin 銷售箱數", value=5)
        
        st.write("*Tiger Tin*")
        p_tiger_in = st.number_input("Tiger Tin 左邊今日進貨 (IN)", value=0)
        p_tiger_out = st.number_input("Tiger Tin 左邊今日出貨 (OUT)", value=0)

        st.write("**【能量飲/調酒 - 每箱12件】**")
        st.write("*Labour's*")
        p_labours_in = st.number_input("Labour's 左邊今日進貨 (IN)", value=-4)
        p_labours_out = st.number_input("Labour's 左邊今日出貨 (OUT)", value=0)
        l_labours_ctn = st.number_input("Loyverse 顯示：Labour's 銷售箱數", value=4)

    with col2:
        st.write("### 2. 右邊欄位 - 啤酒散件賣出 (OUT)")
        
        st.write("*Tiger Botol (散瓶出貨)*")
        p_tiger_botol_single_out = st.number_input("紙張右邊：TIGER BOTOL (OUT)", value=16)
        l_tiger_botol_single = st.number_input("Loyverse 顯示：Tiger Botol 散瓶賣出數", value=16)
        
        st.write("---")
        p_1602_tin = st.number_input("紙張右邊：1602 LAGER TIN (OUT)", value=12)
        l_1602_set = st.number_input("Loyverse 顯示：1602 賣出組數 (Set)", value=4)
        
        p_anchor_tin = st.number_input("紙張右邊：ANCHOR TIN (OUT)", value=3)
        l_anchor_set = st.number_input("Loyverse 顯示：Anchor 賣出組數 (Set)", value=1)
        
        p_tiger_tin = st.number_input("紙張右邊：TIGER TIN (OUT)", value=12)
        l_tiger_set = st.number_input("Loyverse 顯示：Tiger 賣出組數 (Set)", value=4)
        
        p_carlsberg_tin = st.number_input("紙張右邊：CARLSBERG GREEN (OUT)", value=3)
        l_carlsberg_tin = st.number_input("Loyverse 顯示：Carlsberg Green 賣出罐數", value=3)
        
        p_guinness_tin = st.number_input("紙張右邊：GUINNESS TIN (OUT)", value=3)
        l_guinness_tin = st.number_input("Loyverse 顯示：Guinness Tin 賣出罐數", value=3)

        st.write("**【散裝洋酒/紅酒類 OUT】**")
        p_anggur = st.number_input("紙張右邊：ANGGUR 紅酒散瓶 (OUT)", value=11)
        l_anggur_single = st.number_input("Loyverse 顯示：Anggur 紅酒散瓶數", value=11)
        
        p_soju = st.number_input("紙張右邊：SOJU 燒酒散瓶 (OUT)", value=1)
        l_soju = st.number_input("Loyverse 顯示：Soju 賣出瓶數", value=1)

    with col3:
        st.write("### 3. 右邊欄位 - 飲料與香菸賣出 (OUT)")
        st.write("**【能量飲/調酒類散件 OUT】**")
        p_redbull = st.number_input("紙張右邊：RED BULL (OUT)", value=2)
        l_redbull = st.number_input("Loyverse 顯示：Red Bull 賣出罐數", value=2)
        
        p_blackjack = st.number_input("紙張右邊：BLACK JACK'S (OUT)", value=2)
        l_blackjack = st.number_input("Loyverse 顯示：Black Jack's 賣出罐數", value=2)
        
        p_labours_tin = st.number_input("紙張右邊：LABOUR'S 單罐 (OUT)", value=30)
        l_labours_tin = st.number_input("Loyverse 顯示：Labour's 銷售單罐數", value=30)

        st.write("**【香菸類 - Rokok OUT】**")
        p_r129 = st.number_input("紙張右邊：香菸 RM12.90 (OUT)", value=1)
        l_r129 = st.number_input("Loyverse 顯示：香菸 RM12.90 銷售包數", value=1)
        
        p_r167 = st.number_input("紙張右邊：香菸 RM16.70 (OUT)", value=2)
        l_r167 = st.number_input("Loyverse 顯示：香菸 RM16.70 銷售包數", value=2)
        
        p_r182 = st.number_input("紙張右邊：香菸 RM18.20 (OUT)", value=4)
        l_r182 = st.number_input("Loyverse 顯示：香菸 RM18.20 銷售包數", value=4)

    # 4. 全品項自動對賬計算核心
    st.subheader("📊 最終全品項雙照片自動對賬分析結果")
    
    def format_p(out_v, in_v):
        return f"OUT: {int(out_v)} 箱 / IN: {int(in_v)} 箱" if in_v != 0 else f"{int(out_v)} 箱"
        
    def get_status(p_calc, sys_v, unit_name):
        diff = p_calc - sys_v
        return "✅ 完全吻合" if diff == 0 else f"⚠️ 數據不符 (差了 {int(diff)} {unit_name})"

    # 平鋪直述結構，100% 保證順暢渲染
    data_list = []
    data_list.append({"商品項目": "1602 啤酒 (整箱 Carton)", "Loyverse 系統銷量": f"{int(l_1602_ctn)} 箱", "紙張手寫記錄": format_p(p_1602_out, p_1602_in), "對賬狀態": get_status(p_1602_out - p_1602_in, l_1602_ctn, "箱")})
    data_list.append({"商品項目": "1602 啤酒 (單罐 Tin)", "Loyverse 系統銷量": f"{int(l_1602_set * SET_TO_TIN_RATIO)} 罐", "紙張手寫記錄": f"{int(p_1602_tin)} 罐", "對賬狀態": get_status(p_1602_tin, l_1602_set * SET_TO_TIN_RATIO, "罐")})
    data_list.append({"商品項目": "Anchor 啤酒 (整箱 Carton)", "Loyverse 系統銷量": f"{int(l_anchor_ctn)} 箱", "紙張手寫記錄": format_p(p_anchor_out, p_anchor_in), "對賬狀態": get_status(p_anchor_out - p_anchor_in, l_anchor_ctn, "箱")})
    data_list.append({"商品項目": "Anchor 啤酒 (單罐 Tin)", "Loyverse 系統銷量": f"{int(l_anchor_set * SET_TO_TIN_RATIO)} 罐", "紙張手寫記錄": f"{int(p_anchor_tin)} 罐", "對賬狀態": get_status(p_anchor_tin, l_anchor_set * SET_TO_TIN_RATIO, "罐")})
    data_list.append({"商品項目": "Tiger 罐裝啤酒 (單罐 Tin)", "Loyverse 系統銷量": f"{int(l_tiger_set * SET_TO_TIN_RATIO)} 罐", "紙張手寫記錄": f"{int(p_tiger_tin)} 罐", "對賬狀態": get_status(p_tiger_tin, l_tiger_set * SET_TO_TIN_RATIO, "罐")})
    data_list.append({"商品項目": "Tiger 瓶裝啤酒 (整箱 Carton)", "Loyverse 系統銷量": f"{int(l_tiger_botol_ctn)} 箱", "紙張手寫記錄": format_p(p_tiger_botol_out, p_tiger_botol_in), "對賬狀態": get_status(p_tiger_botol_out - p_tiger_botol_in, l_tiger_botol_ctn, "箱")})
    data_list.append({"商品項目": "Tiger 瓶裝啤酒 (Bottle 散瓶)", "Loyverse 系統銷量": f"{int(l_tiger_botol_single)} 支", "紙張手寫記錄": f"{int(p_tiger_botol_single_out)} 支", "對賬狀態": get_status(p_tiger_botol_single_out, l_tiger_botol_single, "支")})
    data_list.append({"商品項目": "Carlsberg Green (單罐 Tin)", "Loyverse 系統銷量": f"{int(l_carlsberg_tin)} 罐", "紙張手寫記錄": f"{int(p_carlsberg_tin)} 罐", "對賬狀態": get_status(p_carlsberg_tin, l_carlsberg_tin, "罐")})
    data_list.append({"商品項目": "Guinness 啤酒 (單罐 Tin)", "Loyverse 系統銷量": f"{int(l_guinness_tin)} 罐", "紙張手寫記錄": f"{int(p_guinness_tin)} 罐", "對賬狀態": get_status(p_guinness_tin, l_guinness_tin, "罐")})
    data_list.append({"商品項目": "Anggur 紅酒 (整箱 Carton)", "Loyverse 系統銷量": f"{int(l_anggur_ctn)} 箱", "紙張手寫記錄": format_p(p_anggur_out, p_anggur_in), "對賬狀態": get_status(p_anggur_out - p_anggur_in, l_anggur_ctn, "箱")})
    data_list.append({"商品項目": "Anggur 紅酒 (Bottle 散瓶)", "Loyverse 系統銷量": f"{int(l_anggur_single)} 支", "紙張手寫記錄": f"{int(p_anggur)} 支", "對賬狀態": get_status(p_anggur, l_anggur_single, "支")})
    data_list.append({"商品項目": "Soju 燒酒 (Bottle)", "Loyverse 系統銷量": f"{int(l_soju)} 支", "紙張手寫記錄": f"{int(p_soju)} 支", "對賬狀態": get_status(p_soju, l_soju, "支")})
    data_list.append({"商品項目": "Red Bull 紅牛 (單罐)", "Loyverse 系統銷量": f"{int(l_redbull)} 罐", "紙張記錄": f"{int(p_redbull)} 罐", "對賬狀態": get_status(p_redbull, l_redbull, "罐")})
    data_list.append({"商品項目": "Black Jack's (單罐)", "Loyverse 系統銷量": f"{int(l_blackjack)} 罐", "紙張記錄": f"{int(p_blackjack)} 罐", "對賬狀態": get_status(p_blackjack, l_blackjack, "罐")})
    data_list.append({"商品項目": "Labour's 啤酒 (整箱 Carton)", "Loyverse 系統銷量": f"{int(l_labours_ctn)} 箱", "紙張手寫記錄": format_p(p_labours_out, p_labours_in), "對賬狀態": get_status(p_labours_out - p_labours_in, l_labours_ctn, "箱")})
    data_list.append({"商品項目": "Labour's 啤酒 (單罐 Tin)", "Loyverse 系統銷量": f"{int(l_labours_tin)} 罐", "紙張手寫記錄": f"{int(p_labours_tin)} 罐", "對賬狀態": get_status(p_labours_tin, l_labours_tin, "罐")})
    data_list.append({"商品項目": "香菸 RM12.90", "Loyverse 系統銷量": f"{int(l_r129)} 包", "紙張手寫記錄": f"{int(p_r129)} 包", "對賬狀態": get_status(p_r129, l_r129, "包")})
    data_list.append({"商品項目": "香菸 RM16.70", "Loyverse 系統銷量": f"{int(l_r167)} 包", "紙張手寫記錄": f"{int(p_r167)} 包", "對賬狀態": get_status(p_r167, l_r167, "包")})
    data_list.append({"商品項目": "香菸 RM18.20", "Loyverse 系統銷量": f"{int(l_r182)} 包", "紙張手寫記錄": f"{int(p_r182)} 包", "對賬狀態": get_status(p_r182, l_r182, "包")})
    
    res_df = pd.DataFrame(data_list)
    
    def color_status(val):
        if "完全吻合" in str(val): return 'background-color: #d4edda; color: #155724; font-weight: bold;'
        if "數據不符" in str(val): return 'background-color: #f8d7da; color: #721c24; font-weight: bold;'
        return ''
        
    st.table(res_df.style.map(color_status, subset=['對賬狀態']))
    
    if any("數據不符" in str(row["對賬狀態"]) for row in data_list):
        st.error("🚨 警告：系統發現有商品數據對不上，請立刻前往實物倉庫複核！")
    else:
