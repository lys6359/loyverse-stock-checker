import streamlit as st
import pandas as pd

st.set_page_config(page_title="Loyverse 店鋪電子點貨對賬系統", layout="wide")

st.title("📱 Loyverse 截圖 ⇄ 網頁電子點貨 —— 智能對賬系統")
st.markdown("💡 **方案 ① 運作中**：請店員下班點貨時，直接在下方網頁表格填入當日的進出貨數量（免用手寫紙），並對照 Loyverse 畫面輸入數據即可自動對賬！")

SET_TO_TIN_RATIO = 3

# 建立電子點貨單輸入界面
st.subheader("📝 今日店鋪實體點貨電子輸入單（請店員下班點貨時直接填寫）")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### 📦 1. 左邊欄位 - 整箱進出清點 (Ctn)")
    st.write("**【大樽/瓶裝酒與紅酒 - 每箱12瓶】**")
    
    st.write("*Tiger Botol (大樽)*")
    p_tiger_botol_out = st.number_input("Tiger Botol 左邊今日出貨 (OUT)", min_value=0, value=0, key="tb_out")
    p_tiger_botol_in = st.number_input("Tiger Botol 左邊今日進貨 (IN) *如有扣回請輸入負數*", min_value=-50, max_value=50, value=0, key="tb_in")
    
    st.write("*Anggur (紅酒)*")
    p_anggur_out = st.number_input("Anggur 左邊今日出貨 (OUT)", min_value=0, value=0, key="ag_out")
    p_anggur_in = st.number_input("Anggur 左邊今日進貨 (IN) *如有扣回請輸入負數*", min_value=-50, max_value=50, value=0, key="ag_in")
    
    st.write("*Heineken & Anchor Botol*")
    p_heineken_botol_out = st.number_input("Heineken Botol 左邊今日出貨 (OUT)", min_value=0, value=0)
    p_heineken_botol_in = st.number_input("Heineken Botol 左邊今日進貨 (IN)", min_value=-50, max_value=50, value=0)
    p_anchor_botol_out = st.number_input("Anchor Botol 左邊今日出貨 (OUT)", min_value=0, value=0)
    p_anchor_botol_in = st.number_input("Anchor Botol 左邊今日進貨 (IN)", min_value=-50, max_value=50, value=0)

    st.write("**【罐裝啤酒 - 每箱24罐】**")
    st.write("*1602 Lager Tin*")
    p_1602_out = st.number_input("1602 左邊今日出貨 (OUT)", min_value=0, value=0)
    p_1602_in = st.number_input("1602 左邊今日進貨 (IN)", min_value=-50, max_value=50, value=0)
    
    st.write("*Anchor Tin*")
    p_anchor_out = st.number_input("Anchor Tin 左邊今日出貨 (OUT)", min_value=0, value=0)
    p_anchor_in = st.number_input("Anchor Tin 左邊今日進貨 (IN)", min_value=-50, max_value=50, value=0)
    
    st.write("*Tiger Tin*")
    p_tiger_out = st.number_input("Tiger Tin 左邊今日出貨 (OUT)", min_value=0, value=0)
    p_tiger_in = st.number_input("Tiger Tin 左邊今日進貨 (IN)", min_value=-50, max_value=50, value=0)

    st.write("**【能量飲/調酒 - 每箱12件】**")
    st.write("*Labour's*")
    p_labours_out = st.number_input("Labour's 左邊今日出貨 (OUT)", min_value=0, value=0)
    p_labours_in = st.number_input("Labour's 左邊今日進貨 (IN)", min_value=-50, max_value=50, value=0)

with col2:
    st.write("### 2. 右邊欄位 - 啤酒與其餘散件今日賣出 (OUT)")
    st.write("**【大樽酒與紅酒散瓶】**")
    p_tiger_botol_single_out = st.number_input("網頁右邊：TIGER BOTOL 單支賣出 (OUT)", min_value=0, value=0)
    p_anggur = st.number_input("網頁右邊：ANGGUR 紅酒散瓶 (OUT)", min_value=0, value=0)
    p_soju = st.number_input("網頁右邊：SOJU 燒酒散瓶 (OUT)", min_value=0, value=0)
    
    st.write("**【罐裝啤酒散件】**")
    p_1602_tin = st.number_input("網頁右邊：1602 LAGER TIN 罐數 (OUT)", min_value=0, value=0)
    p_anchor_tin = st.number_input("網頁右邊：ANCHOR TIN 罐數 (OUT)", min_value=0, value=0)
    p_tiger_tin = st.number_input("網頁右邊：TIGER TIN 罐數 (OUT)", min_value=0, value=0)
    p_carlsberg_tin = st.number_input("網頁右邊：CARLSBERG GREEN 罐數 (OUT)", min_value=0, value=0)
    p_guinness_tin = st.number_input("網頁右邊：GUINNESS TIN 罐數 (OUT)", min_value=0, value=0)

    st.write("**【能量飲與香菸】**")
    p_redbull = st.number_input("網頁右邊：RED BULL 罐數 (OUT)", min_value=0, value=0)
    p_blackjack = st.number_input("網頁右邊：BLACK JACK'S 罐數 (OUT)", min_value=0, value=0)
    p_labours_tin = st.number_input("網頁右邊：LABOUR'S 單罐 (OUT)", min_value=0, value=0)
    p_r129 = st.number_input("網頁右邊：香菸 RM12.90 包數 (OUT)", min_value=0, value=0)
    p_r167 = st.number_input("網頁右邊：香菸 RM16.70 包數 (OUT)", min_value=0, value=0)
    p_r182 = st.number_input("網頁右邊：香菸 RM18.20 包數 (OUT)", min_value=0, value=0)

with col3:
    st.write("### 3. 右邊欄位 - Loyverse 系統銷量對照（請看今日截圖輸入）")
    st.info("💡 請對照 Loyverse 今日的銷售畫面，把系統顯示的賣出數量打在下面：")
    
    l_tiger_botol_ctn = st.number_input("Loyverse 顯示：Tiger Botol 銷售【箱數】", min_value=0, value=0)
    l_tiger_botol_single = st.number_input("Loyverse 顯示：Tiger Botol 銷售【單支數】", min_value=0, value=0)
    
    l_anggur_ctn = st.number_input("Loyverse 顯示：Anggur 紅酒銷售【箱數】", min_value=0, value=0)
    l_anggur_single = st.number_input("Loyverse 顯示：Anggur 紅酒銷售【散瓶數】", min_value=0, value=0)
    
    l_1602_ctn = st.number_input("Loyverse 顯示：1602 銷售【箱數】", min_value=0, value=0)
    l_1602_set = st.number_input("Loyverse 顯示：1602 銷售【組數 Set】", min_value=0, value=0)
    
    l_anchor_ctn = st.number_input("Loyverse 顯示：Anchor 銷售【箱數】", min_value=0, value=0)
    l_anchor_set = st.number_input("Loyverse 顯示：Anchor 銷售【組數 Set】", min_value=0, value=0)
    
    l_tiger_set = st.number_input("Loyverse 顯示：Tiger 罐裝銷售【組數 Set】", min_value=0, value=0)
    l_carlsberg_tin = st.number_input("Loyverse 顯示：Carlsberg Green 銷售【罐數】", min_value=0, value=0)
    l_guinness_tin = st.number_input("Loyverse 顯示：Guinness Tin 銷售【罐數】", min_value=0, value=0)
    l_soju = st.number_input("Loyverse 顯示：Soju 銷售【瓶數】", min_value=0, value=0)
    l_redbull = st.number_input("Loyverse 顯示：Red Bull 銷售【罐數】", min_value=0, value=0)
    l_blackjack = st.number_input("Loyverse 顯示：Black Jack's 銷售【罐數】", min_value=0, value=0)
    l_labours_ctn = st.number_input("Loyverse 顯示：Labour's 銷售【箱數】", min_value=0, value=0)
    l_labours_tin = st.number_input("Loyverse 顯示：Labour's 銷售【單罐數】", min_value=0, value=0)
    l_r129 = st.number_input("Loyverse 顯示：香菸 RM12.90 銷售【包數】", min_value=0, value=0)
    l_r167 = st.number_input("Loyverse 顯示：香菸 RM16.70 銷售【包數】", min_value=0, value=0)
    l_r182 = st.number_input("Loyverse 顯示：香菸 RM18.20 銷售【包數】", min_value=0, value=0)

# 4. 自動對賬核心計算區
st.subheader("📊 今日即時自動對賬分析結果")

def format_paper_box(out_val, in_val):
    if in_val != 0:
        return f"OUT: {int(out_val)} 箱 / IN: {int(in_val)} 箱"
    return f"{int(out_val)} 箱"

check_items = [
    {"name": "1602 啤酒 (整箱 Carton)", "system": f"{int(l_1602_ctn)} 箱", "paper": format_paper_box(p_1602_out, p_1602_in), "diff": (p_1602_out - p_1602_in) - l_1602_ctn, "unit": "箱"},
    {"name": "1602 啤酒 (單罐 Tin - 1 Set = 3罐)", "system": f"{int(l_1602_set * SET_TO_TIN_RATIO)} 罐", "paper": f"{int(p_1602_tin)} 罐", "diff": p_1602_tin - (l_1602_set * SET_TO_TIN_RATIO), "unit": "罐"},
    {"name": "Anchor 啤酒 (整箱 Carton)", "system": f"{int(l_anchor_ctn)} 箱", "paper": format_paper_box(p_anchor_out, p_anchor_in), "diff": (p_anchor_out - p_anchor_in) - l_anchor_ctn, "unit": "箱"},
    {"name": "Anchor 啤酒 (單罐 Tin - 1 Set = 3罐)", "system": f"{int(l_anchor_set * SET_TO_TIN_RATIO)} 罐", "paper": f"{int(p_anchor_tin)} 罐", "diff": p_anchor_tin - (l_anchor_set * SET_TO_TIN_RATIO), "unit": "罐"},
    {"name": "Tiger 罐裝啤酒 (單罐 Tin - 1 Set = 3罐)", "system": f"{int(l_tiger_set * SET_TO_TIN_RATIO)} 罐", "paper": f"{int(p_tiger_tin)} 罐", "diff": p_tiger_tin - (l_tiger_set * SET_TO_TIN_RATIO), "unit": "罐"},
    {"name": "Tiger 瓶裝啤酒 (整箱 Carton)", "system": f"{int(l_tiger_botol_ctn)} 箱", "paper": format_paper_box(p_tiger_botol_out, p_tiger_botol_in), "diff": (p_tiger_botol_out - p_tiger_botol_in) - l_tiger_botol_ctn, "unit": "箱"},
    {"name": "Tiger 瓶裝啤酒 (Bottle 散瓶)", "system": f"{int(l_tiger_botol_single)} 支", "paper": f"{int(p_tiger_botol_single_out)} 支", "diff": p_tiger_botol_single_out - l_tiger_botol_single, "unit": "支"},
    {"name": "Carlsberg Green (單罐 Tin)", "system": f"{int(l_carlsberg_tin)} 罐", "paper": f"{int(p_carlsberg_tin)} 罐", "diff": p_carlsberg_tin - l_carlsberg_tin, "unit": "罐"},
    {"name": "Guinness 啤酒 (單罐 Tin)", "system": f"{int(l_guinness_tin)} 罐", "paper": f"{int(p_guinness_tin)} 罐", "diff": p_guinness_tin - l_guinness_tin, "unit": "罐"},
    {"name": "Anggur 紅酒 (整箱 Carton)", "system": f"{int(l_anggur_ctn)} 箱", "paper": format_paper_box(p_anggur_out, p_anggur_in), "diff": (p_anggur_out - p_anggur_in) - l_anggur_ctn, "unit": "箱"},
    {"name": "Anggur 紅酒 (Bottle 散瓶)", "system": f"{int(l_anggur_single)} 支", "paper": f"{int(p_anggur)} 支", "diff": p_anggur - l_anggur_single, "unit": "支"},
    {"name": "Soju 燒酒 (Bottle)", "system": f"{int(l_soju)} 支", "paper": f"{int(p_soju)} 支", "diff": p_soju - l_soju, "unit": "支"},
    {"name": "Red Bull 紅牛 (單罐)", "system": f"{int(l_redbull)} 罐", "paper": f"{int(p_redbull)} 罐", "diff": p_redbull - l_redbull, "unit": "罐"},
    {"name": "Black Jack's (單罐)", "system": f"{int(l_blackjack)} 罐", "paper": f"{int(p_blackjack)} 罐", "diff": p_blackjack - l_blackjack, "unit": "罐"},
    {"name": "Labour's 啤酒 (整箱 Carton)", "system": f"{int(l_labours_ctn)} 箱", "paper": format_paper_box(p_labours_out, p_labours_in), "diff": (p_labours_out - p_labours_in) - l_labours_ctn, "unit": "箱"},
    {"name": "Labour's 啤酒 (單罐 Tin)", "system": f"{int(l_labours_tin)} 罐", "paper": f"{int(p_labours_tin)} 罐", "diff": p_labours_tin - l_labours_tin, "unit": "罐"},
    {"name": "香菸 RM12.90", "system": f"{int(l_r129)} 包", "paper": f"{int(p_r129)} 包", "diff": p_r129 - l_r129, "unit": "包"},
    {"name": "香菸 RM16.70", "system": f"{int(l_r167)} 包", "paper": f"{int(p_r167)} 包", "diff": p_r167 - l_r167, "unit": "包"},
    {"name": "香菸 RM18.20", "system": f"{int(l_r182)} 包", "paper": f"{int(p_r182)} 包", "diff": p_r182 - l_r182, "unit": "包"},
]

res_data = []
has_error = False
for item in check_items:
    if item["diff"] == 0:
        status = "✅ 完全吻合"
    else:
        status = f"⚠️ 數據不符 (差了 {int(item['diff'])} {item['unit']})"
        has_error = True
    res_data.append({
        "商品項目": item["name"],
        "Loyverse 系統銷量（自動換算）": item["system"],
        "網頁電子點貨記錄（原始呈現）": item["paper"],
        "對賬狀態": status
    })

res_df = pd.DataFrame(res_data)
def color_status(val):
    if "完全吻合" in str(val): return 'background-color: #d4edda; color: #155724; font-weight: bold;'
    if "數據不符" in str(val): return 'background-color: #f8d7da; color: #721c24; font-weight: bold;'
    return ''
    
st.table(res_df.style.map(color_status, subset=['對賬狀態']))

if has_error:
    st.error("🚨 警告：網頁清點與系統數據不符，請立刻核對倉庫貨物！")
else:
    st.success("🎉 太棒了！今日網頁電子清點與系統截圖數據 100% 完全吻合！")
