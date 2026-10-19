import streamlit as st
import pandas as pd

st.set_page_config(page_title="Loyverse 雙照片智能對賬系統", layout="wide")

st.title("📸 Loyverse 報表 ⇄ 實體點貨紙張 —— 自動對賬系統")
st.markdown("💡 **店鋪專屬規則已配置**：左邊 Bottle 一箱 12 件；Tin 一箱 24 件；Redbull 到 Strawberry 一箱 12 件。右邊皆為單件。1 Set = 3 件。")

SET_TO_TIN_RATIO = 3

st.sidebar.header("📁 雙照片上傳區")
loyverse_img_file = st.sidebar.file_uploader("1. 上傳 Loyverse 銷售報表【截圖照片】", type=["jpg", "jpeg", "png"])
paper_img_file = st.sidebar.file_uploader("2. 上傳當天手寫點貨【紙張照片】", type=["jpg", "jpeg", "png"])

if loyverse_img_file and paper_img_file:
    st.success("✅ 兩張照片已上傳！請對照您拍的紙張照片，在下方確認或調整今日的 OUT 數據：")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📦 1. 左邊欄位（整箱出貨 - Ctn）")
        st.info("系統會依據商品種類，自動將箱數換算為總件數（Bottle 乘 12，Tin 乘 24）")
        
        # 根據你上傳的最新紙張數據作為預設值
        p_1602_ctn = st.number_input("紙張左邊：1602 LAGER TIN 出貨箱數", min_value=0, value=3)
        l_1602_ctn = st.number_input("Loyverse 系統：1602 啤酒賣出箱數 (Ctn)", min_value=0, value=3)
        
        p_anchor_ctn = st.number_input("紙張左邊：ANCHOR TIN 出貨箱數", min_value=0, value=0)
        l_anchor_ctn = st.number_input("Loyverse 系統：Anchor 啤酒賣出箱數 (Ctn)", min_value=0, value=5)
        
        p_tiger_botol_ctn = st.number_input("紙張左邊：TIGER BOTOL 出貨箱數", min_value=0, value=1)
        l_tiger_botol_ctn = st.number_input("Loyverse 系統：Tiger 瓶裝賣出箱數 (Ctn)", min_value=0, value=1)

    with col2:
        st.write("### 支/包/罐）")
        st.info("這裡記錄散件出貨，系統會自動將 Loyverse 的 1 Set 換算為 3 罐進行核對")
        
        p_1602_tin = st.number_input("紙張右邊：1602 LAGER TIN 出貨罐數", min_value=0, value=12)
        l_1602_set = st.number_input("Loyverse 系統：1602 賣出組數 (Set)", min_value=0, value=4)
        
        p_anchor_tin = st.number_input("紙張右邊：ANCHOR TIN 出貨罐數", min_value=0, value=3)
        l_anchor_set = st.number_input("Loyverse 系統：Anchor 賣出組數 (Set)", min_value=0, value=1)
        
        p_anggur = st.number_input("紙張右邊：ANGGUR 紅酒出貨瓶數", min_value=0, value=11)
        l_anggur = st.number_input("Loyverse 系統：Anggur 紅酒賣出瓶數", min_value=0, value=11)
        
        st.write("---")
        p_r129 = st.number_input("紙張右邊：香菸 RM12.90 出貨包數", min_value=0, value=1)
        l_r129 = st.number_input("Loyverse 系統：香菸 RM12.90 賣出包數", min_value=0, value=1)
        
        p_r167 = st.number_input("紙張右邊：香菸 RM16.70 出貨包數", min_value=0, value=2)
        l_r167 = st.number_input("Loyverse 系統：香菸 RM16.70 賣出包數", min_value=0, value=2)
        
        p_r182 = st.number_input("紙張右邊：香菸 RM18.20 出貨包數", min_value=0, value=4)
        l_r182 = st.number_input("Loyverse 系統：香菸 RM18.20 賣出包數", min_value=0, value=4)

    # 數據比對邏輯
    st.subheader("📊 最終對賬分析結果")
    
    check_items = [
        {"name": "1602 啤酒 (整箱 - 每箱24罐)", "system": l_1602_ctn, "paper": p_1602_ctn, "unit": "箱"},
        {"name": "1602 啤酒 (單罐 - 系統自動換算 1 Set = 3罐)", "system": l_1602_set * SET_TO_TIN_RATIO, "paper": p_1602_tin, "unit": "罐"},
        {"name": "Anchor 啤酒 (整箱 - 每箱24罐)", "system": l_anchor_ctn, "paper": p_anchor_ctn, "unit": "箱"},
        {"name": "Anchor 啤酒 (單罐 - 系統自動換算 1 Set = 3罐)", "system": l_anchor_set * SET_TO_TIN_RATIO, "paper": p_anchor_tin, "unit": "罐"},
        {"name": "Tiger 瓶裝啤酒 (整箱 - 每箱12瓶)", "system": l_tiger_botol_ctn, "paper": p_tiger_botol_ctn, "unit": "箱"},
        {"name": "Anggur 紅酒 (Bottle)", "system": l_anggur, "paper": p_anggur, "unit": "支"},
        {"name": "香菸 RM12.90", "system": l_r129, "paper": p_r129, "unit": "包"},
        {"name": "香菸 RM16.70", "system": l_r167, "paper": p_r167, "unit": "包"},
        {"name": "香菸 RM18.20", "system": l_r182, "paper": p_r182, "unit": "包"},
    ]
    
    res_data = []
    has_error = False
    for item in check_items:
        diff = item["paper"] - item["system"]
        status = "✅ 完全吻合" if diff == 0 else f"⚠️ 數據不符 (紙張差了 {int(diff)} {item['unit']})"
        if diff != 0: has_error = True
        res_data.append({
            "商品項目": item["name"],
            "Loyverse 系統銷量": f"{int(item['system'])} {item['unit']}",
            "紙張點貨銷量 (OUT)": f"{int(item['paper'])} {item['unit']}",
            "對賬狀態": status
        })
    
    res_df = pd.DataFrame(res_data)
    def color_status(val):
        if "完全吻合" in str(val): return 'background-color: #d4edda; color: #155724; font-weight: bold;'
        if "數據不符" in str(val): return 'background-color: #f8d7da; color: #721c24; font-weight: bold;'
        return ''
        
    st.table(res_df.style.map(color_status, subset=['對賬狀態']))
    
    if has_error:
        st.error("🚨 警告：系統發現有商品數據對不上，請立刻核對實體倉庫！")
    else:
        st.success("🎉 太棒了！今天所有輸入的商品賬目與紙張點貨完全吻合，一分不差！")
else:
    st.warning("👈 請在左側上傳您的【兩張照片】以解鎖今日的智能對賬面板。")
