import streamlit as st
import pandas as pd

# 設定網頁標題與排版
st.set_page_config(page_title="Loyverse 每日自動對賬系統", layout="wide")

st.title("📊 Loyverse 庫存與紙張手寫數據自動對賬系統")
st.markdown("請在下方上傳您的 Loyverse 銷售報表，並輸入紙張上手寫的數據進行精確比對。")

# 初始化一間店鋪的換算規則
# 根據老闆反饋：1 Set = 3 罐 (Tin)
SET_TO_TIN_RATIO = 3

# 1. 檔案上傳區
st.sidebar.header("📁 數據輸入區")
uploaded_file = st.sidebar.file_uploader("上傳 Loyverse 銷售報表 (CSV 或 Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # 讀取上傳的檔案
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # 為了相容截圖中的欄位名稱，進行標準化處理
        df.columns = [c.strip() for c in df.columns]
        
        # 尋找商品名稱和銷售數量的欄位
        name_col = None
        sold_col = None
        for col in df.columns:
            if 'item' in col.lower() or '商品' in col.lower() or '名稱' in col.lower():
                name_col = col
            if 'sold' in col.lower() or '量' in col.lower() or 'count' in col.lower():
                sold_col = col
                
        if name_col and sold_col:
            st.success("✅ Loyverse 報表解析成功！")
            
            # 整理系統銷售數據
            loyverse_data = {}
            for _, row in df.iterrows():
                item_name = str(row[name_col]).strip()
                try:
                    qty = float(row[sold_col])
                except:
                    qty = 0.0
                if qty > 0:
                    loyverse_data[item_name] = qty
            
            # 2. 顯示抓取到的商品，並讓用戶輸入手寫紙張數據
            st.subheader("📝 請對照紙張，輸入當天手寫的出貨數量 (OUT)")
            st.info("💡 系統已設定規則：1 Set ＝ 3 罐。比對時會自動將 Set 乘以 3 換算為單罐數量與紙張核對。")
            
            comparison_rows = []
            
            # 建立一個表單讓用戶輸入
            with st.form("input_form"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write("**📦 啤酒與散件類**")
                    # 1602 Smooth Lager 1 Ctn
                    l_1602_ctn = loyverse_data.get("1602 Smooth Lager 1 Ctn", 0.0)
                    paper_1602_ctn = st.number_input(f"1602 箱數 (Ctn) [系統賣出: {int(l_1602_ctn)}]", min_value=0, value=0)
                    
                    # 1602 Smooth Lager 1 Set Tin
                    l_1602_set = loyverse_data.get("1602 Smooth Lager 1 Set Tin", 0.0)
                    paper_1602_tin = st.number_input(f"1602 紙張右邊單罐數 (Tin) [系統賣出: {int(l_1602_set)} Set = {int(l_1602_set * SET_TO_TIN_RATIO)} 罐]", min_value=0, value=0)
                    
                    st.write("---")
                    # Anchor Tin 1 Ctn
                    l_anchor_ctn = loyverse_data.get("Anchor Tin 1 Ctn", 0.0)
                    paper_anchor_ctn = st.number_input(f"Anchor 箱數 (Ctn) [系統賣出: {int(l_anchor_ctn)}]", min_value=0, value=0)
                    
                    # Anchor Tin 1 Set
                    l_anchor_set = loyverse_data.get("Anchor Tin 1 Set", 0.0)
                    paper_anchor_tin = st.number_input(f"Anchor 紙張右邊單罐數 (Tin) [系統賣出: {int(l_anchor_set)} Set = {int(l_anchor_set * SET_TO_TIN_RATIO)} 罐]", min_value=0, value=0)
                
                with col2:
                    st.write("**🍷 其他酒類與飲料**")
                    # Anggur 1 Bottle
                    l_anggur = loyverse_data.get("Anggur 1 Bottle", 0.0)
                    paper_anggur = st.number_input(f"Anggur 紅酒瓶數 [系統賣出: {int(l_anggur)}]", min_value=0, value=0)
                
                with col3:
                    st.write("**🚬 香菸類 (Rokok)**")
                    # Rokok 系列 (根據截圖價格)
                    l_r129 = loyverse_data.get("12.9", 0.0)
                    paper_r129 = st.number_input(f"香菸 RM12.90 包數 [系統賣出: {int(l_r129)}]", min_value=0, value=0)
                    
                    l_r167 = loyverse_data.get("16.7", 0.0)
                    paper_r167 = st.number_input(f"香菸 RM16.70 包數 [系統賣出: {int(l_r167)}]", min_value=0, value=0)
                    
                    l_r182 = loyverse_data.get("18.2", 0.0)
                    paper_r182 = st.number_input(f"香菸 RM18.20 包數 [系統賣出: {int(l_r182)}]", min_value=0, value=0)
                
                submit_btn = st.form_submit_button("🔥 開始自動對賬比對")
            
            # 3. 點擊比對後的計算邏輯
            if submit_btn:
                st.subheader("📊 最終對賬分析結果")
                
                # 定義核對清單
                check_items = [
                    {"name": "1602 啤酒 (整箱 Carton)", "system": l_1602_ctn, "paper": paper_1602_ctn, "unit": "箱"},
                    {"name": "1602 啤酒 (單罐 Tin - 由 Set 換算)", "system": l_1602_set * SET_TO_TIN_RATIO, "paper": paper_1602_tin, "unit": "罐"},
                    {"name": "Anchor 啤酒 (整箱 Carton)", "system": l_anchor_ctn, "paper": paper_anchor_ctn, "unit": "箱"},
                    {"name": "Anchor 啤酒 (單罐 Tin - 由 Set 換算)", "system": l_anchor_set * SET_TO_TIN_RATIO, "paper": paper_anchor_tin, "unit": "罐"},
                    {"name": "Anggur 紅酒 (Bottle)", "system": l_anggur, "paper": paper_anggur, "unit": "支"},
                    {"name": "香菸 RM12.90", "system": l_r129, "paper": paper_r129, "unit": "包"},
                    {"name": "香菸 RM16.70", "system": l_r167, "paper": paper_r167, "unit": "包"},
                    {"name": "香菸 RM18.20", "system": l_r182, "paper": paper_r182, "unit": "包"},
                ]
                
                # 建立比對表格
                res_data = []
                has_error = False
                
                for item in check_items:
                    diff = item["paper"] - item["system"]
                    if diff == 0:
                        status = "✅ 完全吻合"
                    else:
                        status = f"⚠️ 數據不符 (紙張差了 {int(diff)} {item['unit']})"
                        has_error = True
                        
                    res_data.append({
                        "商品項目": item["name"],
                        "Loyverse 系統銷量": f"{int(item['system'])} {item['unit']}",
                        "紙張點貨銷量 (OUT)": f"{int(item['paper'])} {item['unit']}",
                        "對賬狀態": status
                    })
                
                res_df = pd.DataFrame(res_data)
                
                # 使用顏色高亮樣式
                def color_status(val):
                    if "完全吻合" in str(val):
                        return 'background-color: #d4edda; color: #155724; font-weight: bold;'
                    elif "數據不符" in str(val):
                        return 'background-color: #f8d7da; color: #721c24; font-weight: bold;'
                    return ''
                
                st.table(res_df.style.applymap(color_status, subset=['對賬狀態']))
                
                # 彈出最終小結論報告
                if has_error:
                    st.error("🚨 警告：發現部分商品的手寫點貨數量與系統銷售不一致！請店長根據上方紅色標記核對倉庫實體庫存。")
                else:
                    st.success("🎉 太棒了！今天所有上報的商品賬目與紙張點貨完全吻合，一分不差！")
        else:
            st.error("❌ 無法識別報表中的商品名稱或銷量欄位，請確認您導出的是 Loyverse 的『商品銷售報告』。")
            
    except Exception as e:
        st.error(f"❌ 讀取檔案時出錯: {str(e)}")
else:
    st.warning("👈 請先在左側邊欄上傳您的 Loyverse 銷售報表（CSV 或 Excel 檔案）。")
