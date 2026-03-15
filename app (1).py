import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="UniPay — Campus Payment App",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background: linear-gradient(135deg, #0a0a1a 0%, #0d1229 60%, #0a1520 100%);
    min-height: 100vh;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1rem 2rem 2rem !important; max-width: 100% !important; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(15,13,30,0.95) !important;
    border-right: 1px solid rgba(0,82,204,0.2);
}

/* Title */
.app-title {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(90deg, #fff 30%, #0052CC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
    margin: 0;
}
.app-subtitle {
    color: #6b7db3;
    font-size: 0.9rem;
    margin-top: 0.2rem;
    font-weight: 300;
}

.section-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,82,204,0.3), transparent);
    margin: 1.5rem 0;
}

/* Info cards */
.info-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(0,82,204,0.2);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
}
.info-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #a0b4e0;
    margin-bottom: 0.4rem;
}
.info-card-body {
    font-size: 0.82rem;
    color: #5a6d99;
    line-height: 1.6;
}

/* Screen button pills */
.screen-btn-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 1rem 0;
}
.screen-pill {
    background: rgba(0,82,204,0.12);
    border: 1px solid rgba(0,82,204,0.3);
    color: #7ba0e0;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
}

/* Streamlit button overrides */
.stButton>button {
    background: rgba(0,82,204,0.15) !important;
    border: 1px solid rgba(0,82,204,0.4) !important;
    color: #a0b4e0 !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    transition: all 0.2s !important;
}
.stButton>button:hover {
    background: rgba(0,82,204,0.3) !important;
    color: #fff !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
col_logo, col_title = st.columns([1, 11])
with col_logo:
    st.markdown("<div style='font-size:2.5rem;margin-top:0.3rem;'>🎓</div>", unsafe_allow_html=True)
with col_title:
    st.markdown("""
    <div class='app-title'>UniPay</div>
    <div class='app-subtitle'>Campus Payment & Utility App · Design Thinking & Innovation Project</div>
    """, unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ── Layout: Phone left, Info right ────────────────────────────────────────────
col_phone, col_info = st.columns([5, 4], gap="large")

# ── RIGHT SIDE: Info panel ─────────────────────────────────────────────────────
with col_info:
    st.markdown("""
    <div style='font-family:Syne,sans-serif;font-size:1.05rem;font-weight:700;color:#e0e6f5;margin-bottom:1rem;'>
        Navigate All 12 Screens
    </div>
    <div class='screen-btn-row'>
        <span class='screen-pill'>🏠 Home</span>
        <span class='screen-pill'>🔐 Login</span>
        <span class='screen-pill'>📊 Dashboard</span>
        <span class='screen-pill'>🏪 Vendors</span>
        <span class='screen-pill'>🔥 Hot Deals</span>
        <span class='screen-pill'>🎪 Events</span>
        <span class='screen-pill'>💳 Credit</span>
        <span class='screen-pill'>👥 P2P Pay</span>
        <span class='screen-pill'>📈 Vendor Dash</span>
        <span class='screen-pill'>👤 Profile</span>
        <span class='screen-pill'>📷 QR Scanner</span>
        <span class='screen-pill'>📋 Transactions</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='info-card'>
        <div class='info-card-title'>🎯 Core Concept</div>
        <div class='info-card-body'>
            UniPay is a closed digital payment ecosystem for universities. One campus wallet replaces cash, multiple UPIs, and registration forms — for students, vendors, clubs, and university admins.
        </div>
    </div>
    <div class='info-card'>
        <div class='info-card-title'>👩‍🎓 Student Features</div>
        <div class='info-card-body'>
            Campus wallet top-up · QR scan-to-pay · Event registration · Peer payments · Spending insights · AI budget alerts · Loyalty credit score
        </div>
    </div>
    <div class='info-card'>
        <div class='info-card-title'>🏪 Vendor Features</div>
        <div class='info-card-body'>
            Daily sales graph · Top items tracker · Traffic heatmap · Deal creation · Instant digital settlement · No cash handling
        </div>
    </div>
    <div class='info-card'>
        <div class='info-card-title'>💰 Revenue Model</div>
        <div class='info-card-body'>
            1–3% vendor commission · ₹3–10L/yr university SaaS · ₹10/ticket event fees · Fest vendor listing fees · Brand partnerships
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='font-family:Syne,sans-serif;font-size:0.95rem;font-weight:700;color:#e0e6f5;margin-bottom:0.8rem;'>
        📱 How to Use the Prototype
    </div>
    <div style='font-size:0.82rem;color:#5a6d99;line-height:1.8;'>
        → Use the <b style='color:#a0b4e0;'>tab buttons</b> above the phone to jump to any screen<br>
        → Tap <b style='color:#a0b4e0;'>interactive elements</b> inside the app to navigate naturally<br>
        → Try the <b style='color:#a0b4e0;'>numpad</b> on the P2P screen to enter amounts<br>
        → The <b style='color:#a0b4e0;'>QR scanner</b> has an animated sweep line<br>
        → <b style='color:#a0b4e0;'>Android nav buttons</b> (back/home/recents) are at the bottom
    </div>
    """, unsafe_allow_html=True)

# ── LEFT SIDE: Phone prototype ─────────────────────────────────────────────────
with col_phone:
    phone_html = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, 'SF Pro Display', sans-serif; background: transparent; display: flex; flex-direction: column; align-items: center; padding: 16px 0 24px; }

.tab-row { display: flex; gap: 5px; flex-wrap: wrap; justify-content: center; margin-bottom: 14px; max-width: 420px; }
.tab-btn { padding: 5px 11px; border-radius: 18px; font-size: 10.5px; font-weight: 600; border: none; cursor: pointer; white-space: nowrap; background: #1e2a4a; color: #7a96cc; transition: all 0.18s; }
.tab-btn.active { background: #0052CC; color: #fff; }
.tab-btn:hover { background: #2a3d6e; color: #aac4ff; }

.device { width: 375px; background: #fff; border-radius: 44px; border: 8px solid #111; position: relative; overflow: hidden; box-shadow: 0 0 0 2px #222, 0 24px 50px rgba(0,0,0,0.55); display: flex; flex-direction: column; min-height: 812px; }

.status-bar { background: #0052CC; height: 28px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; flex-shrink: 0; }
.status-bar .time { color: #fff; font-size: 12px; font-weight: 600; }
.status-icons { display: flex; gap: 5px; align-items: center; }
.status-icons span { color: #fff; font-size: 10px; }

.screen { flex: 1; overflow: hidden; display: flex; flex-direction: column; background: #f4f6fb; }
.screen-page { display: none; flex-direction: column; flex: 1; overflow: hidden; }
.screen-page.active { display: flex; }
.scroll-content { flex: 1; overflow-y: auto; scrollbar-width: none; }
.scroll-content::-webkit-scrollbar { display: none; }

.android-nav { background: #0d0d0d; height: 42px; display: flex; align-items: center; justify-content: space-around; flex-shrink: 0; }
.nav-btn { width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; cursor: pointer; opacity: 0.8; }
.nav-btn svg { width: 18px; height: 18px; fill: #bbb; }

.bottom-nav { background: #fff; border-top: 0.5px solid #e0e0e0; display: flex; flex-shrink: 0; }
.bnav-item { flex: 1; display: flex; flex-direction: column; align-items: center; padding: 8px 0 6px; cursor: pointer; gap: 3px; }
.bnav-item svg { width: 20px; height: 20px; fill: #bbb; }
.bnav-item span { font-size: 10px; color: #888; }
.bnav-item.active svg { fill: #0052CC; }
.bnav-item.active span { color: #0052CC; font-weight: 600; }

/* HOME */
.home-header { background: linear-gradient(160deg, #0052CC 0%, #0747A6 100%); padding: 16px 18px 24px; color: #fff; }
.home-header .greeting { font-size: 13px; opacity: 0.85; }
.home-header .name { font-size: 18px; font-weight: 700; margin-top: 2px; }
.balance-row { display: flex; justify-content: space-between; align-items: flex-end; margin-top: 14px; }
.balance-label { font-size: 11px; opacity: 0.7; }
.balance-amount { font-size: 28px; font-weight: 700; }
.add-btn { background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.4); color: #fff; font-size: 11px; font-weight: 600; padding: 6px 14px; border-radius: 20px; cursor: pointer; }

.qr-card { margin: -14px 18px 0; background: #fff; border-radius: 16px; padding: 14px; box-shadow: 0 4px 16px rgba(0,82,204,0.12); }
.qr-btn { width: 100%; background: #0052CC; color: #fff; border: none; border-radius: 12px; padding: 14px; font-size: 15px; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; }
.qr-btn svg { width: 20px; height: 20px; fill: #fff; }

.section-label { font-size: 13px; font-weight: 700; color: #1a1a2e; margin-bottom: 12px; }
.actions-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
.action-item { display: flex; flex-direction: column; align-items: center; gap: 6px; cursor: pointer; }
.action-icon { width: 52px; height: 52px; border-radius: 16px; display: flex; align-items: center; justify-content: center; }
.action-icon svg { width: 22px; height: 22px; }
.action-label { font-size: 10px; font-weight: 600; color: #444; text-align: center; line-height: 1.3; }

.spend-widget { background: #fff; border-radius: 14px; padding: 14px 16px; border: 0.5px solid #eee; }
.spend-bar-row { display: flex; gap: 6px; align-items: flex-end; height: 48px; }
.spend-bar { flex: 1; background: #e8efff; border-radius: 4px 4px 0 0; }
.spend-bar.today { background: #0052CC; }
.bc-labels { display: flex; gap: 6px; margin-top: 4px; }
.bc-label { flex: 1; text-align: center; font-size: 8px; color: #888; }

.ann-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; padding: 14px 16px; color: #fff; margin-bottom: 8px; cursor: pointer; }
.ann-tag { font-size: 9px; background: rgba(255,255,255,0.2); padding: 3px 8px; border-radius: 10px; display: inline-block; margin-bottom: 6px; font-weight: 600; }
.ann-title { font-size: 13px; font-weight: 700; }
.ann-sub { font-size: 11px; opacity: 0.8; margin-top: 3px; }

/* LOGIN */
.login-hero { background: linear-gradient(160deg, #0052CC 0%, #0747A6 100%); padding: 40px 24px 36px; text-align: center; }
.login-logo { width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 20px; margin: 0 auto 16px; display: flex; align-items: center; justify-content: center; }
.login-logo svg { width: 32px; height: 32px; fill: #fff; }
.login-form { padding: 24px 24px; background: #fff; flex: 1; }
.login-step { font-size: 11px; color: #0052CC; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 18px; }
.login-field { margin-bottom: 14px; }
.login-field label { font-size: 12px; font-weight: 600; color: #444; display: block; margin-bottom: 6px; }
.login-field input { width: 100%; padding: 11px 14px; border: 1.5px solid #e0e0e0; border-radius: 10px; font-size: 14px; outline: none; background: #fafafa; }
.login-btn { width: 100%; background: #0052CC; color: #fff; border: none; border-radius: 12px; padding: 14px; font-size: 15px; font-weight: 700; cursor: pointer; margin-top: 6px; }
.divider-or { text-align: center; font-size: 12px; color: #aaa; margin: 12px 0; }
.linkedin-btn { width: 100%; background: #0077B5; color: #fff; border: none; border-radius: 12px; padding: 12px; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; }
.verified-badge { background: #e6f9f0; border: 1px solid #52c41a; border-radius: 10px; padding: 10px 14px; display: flex; align-items: center; gap: 10px; margin-top: 12px; }
.verified-badge svg { width: 20px; height: 20px; fill: #52c41a; }
.verified-badge span { font-size: 12px; color: #2d7a2d; font-weight: 600; }

/* DASHBOARD */
.dash-header { background: #0052CC; padding: 14px 18px 20px; color: #fff; }
.ai-insight { background: #fff; border-radius: 14px; padding: 12px 14px; box-shadow: 0 4px 14px rgba(0,82,204,0.1); border-left: 3px solid #FFB800; }
.ai-label { font-size: 9px; color: #FFB800; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; }
.ai-text { font-size: 12px; color: #333; margin-top: 4px; line-height: 1.5; }
.chart-card { background: #fff; border-radius: 14px; padding: 14px 16px; border: 0.5px solid #eee; }
.chart-title { font-size: 12px; font-weight: 700; color: #333; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }
.bar-chart { display: flex; align-items: flex-end; gap: 5px; height: 72px; }
.bc-bar { flex: 1; border-radius: 4px 4px 0 0; background: #d0e4ff; }
.bc-bar.hl { background: #0052CC; }
.cat-row { display: flex; gap: 8px; margin-bottom: 8px; }
.cat-card { flex: 1; background: #fff; border-radius: 12px; padding: 10px 8px; border: 0.5px solid #eee; text-align: center; }
.cat-icon { font-size: 18px; margin-bottom: 4px; }
.cat-name { font-size: 9px; color: #888; }
.cat-amount { font-size: 13px; font-weight: 700; color: #1a1a2e; }
.budget-card { background: #fff; border-radius: 14px; padding: 14px 16px; border: 0.5px solid #eee; }
.progress-bar { height: 8px; background: #e8efff; border-radius: 4px; overflow: hidden; }
.progress-fill { height: 100%; background: #0052CC; border-radius: 4px; }
.credit-meter { background: #fff; border-radius: 14px; padding: 14px 16px; border: 0.5px solid #eee; display: flex; align-items: center; gap: 14px; }
.score-circle { width: 58px; height: 58px; border-radius: 50%; background: conic-gradient(#0052CC 0% 78%, #e8efff 78% 100%); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.score-inner { width: 44px; height: 44px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; }

/* VENDORS */
.vendor-header { background: #0052CC; padding: 14px 18px; }
.search-bar { background: #fff; border-radius: 10px; padding: 9px 14px; display: flex; align-items: center; gap: 8px; }
.search-bar svg { width: 15px; height: 15px; fill: #888; flex-shrink: 0; }
.search-bar span { font-size: 12px; color: #aaa; }
.filter-row { display: flex; gap: 7px; padding: 10px 18px; background: #fff; border-bottom: 0.5px solid #eee; overflow-x: auto; scrollbar-width: none; }
.filter-row::-webkit-scrollbar { display: none; }
.filter-chip { padding: 5px 12px; border-radius: 16px; font-size: 11px; font-weight: 600; border: 1px solid #ddd; background: #fff; cursor: pointer; white-space: nowrap; color: #555; }
.filter-chip.active { background: #0052CC; color: #fff; border-color: #0052CC; }
.vendor-grid { padding: 12px 18px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.vendor-card { background: #fff; border-radius: 14px; overflow: hidden; border: 0.5px solid #eee; }
.vendor-img { height: 68px; display: flex; align-items: center; justify-content: center; font-size: 28px; }
.vendor-info { padding: 9px 10px 12px; }
.vendor-name { font-size: 12px; font-weight: 700; color: #1a1a2e; }
.vendor-meta { display: flex; justify-content: space-between; margin-top: 3px; }
.vendor-dist { font-size: 10px; color: #888; }
.vendor-deal { font-size: 10px; color: #00875A; font-weight: 600; }
.stars { font-size: 9px; color: #FFB800; }
.rating-num { font-size: 10px; color: #666; }

/* DEALS */
.deals-header { background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%); padding: 16px 18px; color: #fff; }
.deal-card { background: #fff; border-radius: 14px; overflow: hidden; border: 0.5px solid #eee; display: flex; }
.deal-img { width: 78px; display: flex; align-items: center; justify-content: center; font-size: 32px; flex-shrink: 0; }
.deal-info { flex: 1; padding: 12px 12px 12px 0; }
.deal-badge { background: #FFF0F0; color: #FF416C; font-size: 9px; font-weight: 700; padding: 2px 8px; border-radius: 8px; display: inline-block; }
.deal-name { font-size: 13px; font-weight: 700; color: #1a1a2e; margin-top: 4px; }
.deal-vendor { font-size: 11px; color: #888; margin-top: 2px; }
.deal-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 7px; }
.deal-price { font-size: 13px; font-weight: 700; color: #0052CC; }
.deal-timer { font-size: 10px; color: #FF416C; font-weight: 600; background: #FFF0F0; padding: 3px 8px; border-radius: 8px; }

/* EVENTS */
.event-card-big { border-radius: 16px; overflow: hidden; border: 0.5px solid #eee; background: #fff; }
.event-img { height: 90px; display: flex; align-items: center; justify-content: center; font-size: 40px; }
.event-body { padding: 12px 14px 14px; }
.event-tag { font-size: 9px; background: #E6F0FF; color: #0052CC; padding: 3px 8px; border-radius: 8px; font-weight: 700; display: inline-block; }
.event-name { font-size: 14px; font-weight: 700; color: #1a1a2e; margin-top: 5px; }
.event-meta { font-size: 11px; color: #888; margin-top: 3px; }
.event-register { width: 100%; background: #0052CC; color: #fff; border: none; border-radius: 10px; padding: 10px; font-size: 13px; font-weight: 700; cursor: pointer; margin-top: 10px; }
.event-row { background: #fff; border-radius: 12px; padding: 12px 14px; display: flex; gap: 12px; align-items: center; border: 0.5px solid #eee; }
.event-date-box { width: 40px; height: 44px; background: #0052CC; border-radius: 10px; display: flex; flex-direction: column; align-items: center; justify-content: center; flex-shrink: 0; }
.ed-day { font-size: 14px; font-weight: 700; color: #fff; }
.ed-mon { font-size: 8px; color: rgba(255,255,255,0.8); font-weight: 600; }

/* CREDIT */
.credit-header { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 20px 18px; color: #fff; }
.credit-balance { font-size: 30px; font-weight: 700; }
.credit-btns { display: flex; gap: 8px; margin-top: 12px; }
.cred-btn { flex: 1; background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.4); color: #fff; border-radius: 10px; padding: 8px; font-size: 11px; font-weight: 700; text-align: center; cursor: pointer; }
.loan-card { background: #fff; border-radius: 14px; padding: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.07); border-left: 3px solid #FFB800; }
.loan-title { font-size: 12px; font-weight: 700; color: #FFB800; }
.loan-text { font-size: 12px; color: #444; margin-top: 4px; line-height: 1.5; }
.loan-btn { background: #FFB800; color: #fff; border: none; border-radius: 8px; padding: 7px 16px; font-size: 12px; font-weight: 700; cursor: pointer; margin-top: 10px; }
.lb-row { display: flex; align-items: center; gap: 12px; padding: 9px 0; border-bottom: 0.5px solid #eee; }
.lb-rank { width: 20px; font-size: 13px; font-weight: 700; color: #0052CC; }
.lb-avatar { width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; color: #fff; }
.lb-name { flex: 1; font-size: 13px; font-weight: 600; color: #333; }
.lb-pts { font-size: 12px; color: #0052CC; font-weight: 700; }

/* P2P */
.p2p-header { background: #0052CC; padding: 14px 18px; color: #fff; }
.p2p-tabs { display: flex; background: rgba(255,255,255,0.15); border-radius: 10px; overflow: hidden; margin-top: 10px; }
.p2p-tab { flex: 1; padding: 8px; text-align: center; font-size: 12px; font-weight: 600; color: rgba(255,255,255,0.7); cursor: pointer; }
.p2p-tab.active { background: #fff; color: #0052CC; border-radius: 10px; }
.contact-row { display: flex; align-items: center; gap: 12px; padding: 10px 0; border-bottom: 0.5px solid #eee; cursor: pointer; }
.contact-avatar { width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 700; color: #fff; flex-shrink: 0; }
.contact-name { font-size: 13px; font-weight: 600; color: #333; }
.contact-email { font-size: 10px; color: #888; }
.contact-action { margin-left: auto; font-size: 11px; color: #0052CC; font-weight: 700; background: #e6f0ff; padding: 5px 12px; border-radius: 8px; }
.amt-display { font-size: 36px; font-weight: 700; color: #1a1a2e; text-align: center; padding: 18px; }
.numpad { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: #eee; border-radius: 12px; overflow: hidden; }
.numpad-key { padding: 14px; text-align: center; font-size: 18px; font-weight: 500; background: #fff; cursor: pointer; color: #333; }
.numpad-key.act { background: #f5f5f5; font-size: 12px; font-weight: 600; color: #0052CC; }
.pay-btn { width: 100%; background: #0052CC; color: #fff; border: none; border-radius: 12px; padding: 13px; font-size: 14px; font-weight: 700; cursor: pointer; margin-top: 12px; }

/* VENDOR DASH */
.vdash-header { background: #1a1a2e; padding: 14px 18px; color: #fff; }
.vdash-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 14px 18px; }
.vstat-card { background: #fff; border-radius: 14px; padding: 12px 14px; border: 0.5px solid #eee; }
.vstat-label { font-size: 10px; color: #888; margin-bottom: 4px; }
.vstat-value { font-size: 18px; font-weight: 700; color: #1a1a2e; }
.vstat-delta { font-size: 10px; color: #00875A; font-weight: 600; margin-top: 2px; }
.hm-grid { display: grid; grid-template-columns: repeat(8, 1fr); gap: 4px; }
.hm-cell { height: 26px; border-radius: 4px; }
.hm-labels { display: grid; grid-template-columns: repeat(8, 1fr); gap: 4px; margin-top: 4px; }
.hm-label { font-size: 8px; text-align: center; color: #888; }
.item-row { display: flex; align-items: center; gap: 10px; padding: 7px 0; border-bottom: 0.5px solid #f0f0f0; }
.item-rank { width: 18px; font-size: 11px; color: #888; }
.item-name { flex: 1; font-size: 12px; font-weight: 600; color: #333; }
.item-bar { height: 6px; background: #e8efff; border-radius: 3px; overflow: hidden; width: 55px; }
.item-bar-fill { height: 100%; background: #0052CC; border-radius: 3px; }
.item-amount { font-size: 12px; font-weight: 700; color: #0052CC; }
.settle-card { background: #fff; border-radius: 14px; padding: 14px 16px; border: 0.5px solid #eee; }
.settle-row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 0.5px solid #f5f5f5; }
.settle-label { font-size: 12px; color: #666; }
.settle-value { font-size: 12px; font-weight: 600; color: #333; }
.settle-btn { width: 100%; background: #1a1a2e; color: #fff; border: none; border-radius: 10px; padding: 11px; font-size: 13px; font-weight: 700; cursor: pointer; margin-top: 12px; }

/* PROFILE */
.profile-header { background: #0052CC; padding: 22px 18px 28px; color: #fff; text-align: center; }
.profile-avatar { width: 68px; height: 68px; border-radius: 50%; background: rgba(255,255,255,0.2); margin: 0 auto 10px; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 700; color: #fff; border: 3px solid rgba(255,255,255,0.4); }
.settings-group { padding: 14px 18px 0; }
.settings-label { font-size: 11px; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px; }
.setting-row { display: flex; align-items: center; gap: 12px; padding: 11px 0; border-bottom: 0.5px solid #f0f0f0; cursor: pointer; }
.setting-icon { width: 34px; height: 34px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.setting-icon svg { width: 17px; height: 17px; }
.setting-label { flex: 1; font-size: 13px; font-weight: 500; color: #333; }
.toggle { width: 36px; height: 21px; background: #0052CC; border-radius: 11px; position: relative; cursor: pointer; }
.toggle-dot { position: absolute; right: 3px; top: 3px; width: 15px; height: 15px; background: #fff; border-radius: 50%; }

/* SCANNER */
.scanner-bg { background: #000; flex: 1; display: flex; flex-direction: column; align-items: center; }
.scanner-area { width: 210px; height: 210px; border: 2px solid rgba(255,255,255,0.25); border-radius: 20px; position: relative; margin: 16px auto; }
.scanner-corner { position: absolute; width: 22px; height: 22px; }
.scanner-corner.tl { top: -2px; left: -2px; border-top: 3px solid #0052CC; border-left: 3px solid #0052CC; border-radius: 8px 0 0 0; }
.scanner-corner.tr { top: -2px; right: -2px; border-top: 3px solid #0052CC; border-right: 3px solid #0052CC; border-radius: 0 8px 0 0; }
.scanner-corner.bl { bottom: -2px; left: -2px; border-bottom: 3px solid #0052CC; border-left: 3px solid #0052CC; border-radius: 0 0 0 8px; }
.scanner-corner.br { bottom: -2px; right: -2px; border-bottom: 3px solid #0052CC; border-right: 3px solid #0052CC; border-radius: 0 0 8px 0; }
.scanner-line { position: absolute; left: 10px; right: 10px; height: 2px; background: linear-gradient(90deg, transparent, #0052CC, transparent); top: 50%; }
.scanner-options { display: flex; gap: 20px; margin-top: 24px; }
.scan-option { display: flex; flex-direction: column; align-items: center; gap: 6px; cursor: pointer; }
.scan-option-icon { width: 50px; height: 50px; background: rgba(255,255,255,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.scan-option-icon svg { width: 22px; height: 22px; fill: #fff; }
.scan-option span { color: rgba(255,255,255,0.8); font-size: 10px; font-weight: 600; }

/* TRANSACTIONS */
.txn-header { background: #0052CC; padding: 14px 18px; color: #fff; }
.txn-row { display: flex; align-items: center; gap: 12px; padding: 10px 0; border-bottom: 0.5px solid #f0f0f0; }
.txn-icon { width: 38px; height: 38px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 17px; flex-shrink: 0; }
.txn-name { font-size: 13px; font-weight: 600; color: #333; }
.txn-sub { font-size: 10px; color: #888; margin-top: 2px; }
.txn-amount { font-size: 13px; font-weight: 700; }
.txn-amount.debit { color: #FF416C; }
.txn-amount.credit { color: #00875A; }
.txn-date { font-size: 11px; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: 0.6px; margin: 10px 0 6px; }
</style>

<div class="tab-row">
  <button class="tab-btn active" onclick="show('home')" id="t-home">🏠 Home</button>
  <button class="tab-btn" onclick="show('login')" id="t-login">🔐 Login</button>
  <button class="tab-btn" onclick="show('dashboard')" id="t-dashboard">📊 Dashboard</button>
  <button class="tab-btn" onclick="show('vendors')" id="t-vendors">🏪 Vendors</button>
  <button class="tab-btn" onclick="show('deals')" id="t-deals">🔥 Deals</button>
  <button class="tab-btn" onclick="show('events')" id="t-events">🎪 Events</button>
  <button class="tab-btn" onclick="show('credit')" id="t-credit">💳 Credit</button>
  <button class="tab-btn" onclick="show('p2p')" id="t-p2p">👥 P2P</button>
  <button class="tab-btn" onclick="show('vdash')" id="t-vdash">📈 Vendor</button>
  <button class="tab-btn" onclick="show('profile')" id="t-profile">👤 Profile</button>
  <button class="tab-btn" onclick="show('scanner')" id="t-scanner">📷 Scanner</button>
  <button class="tab-btn" onclick="show('txns')" id="t-txns">📋 Txns</button>
</div>

<div class="device">
  <div class="status-bar">
    <span class="time">9:41</span>
    <div class="status-icons"><span>▲▲▲</span><span>WiFi</span><span>■■■</span></div>
  </div>

  <div class="screen">

  <!-- HOME -->
  <div class="screen-page active" id="sc-home">
    <div class="scroll-content">
      <div class="home-header">
        <div class="greeting">Good morning,</div>
        <div class="name">Priya Sharma 👋</div>
        <div class="balance-row">
          <div><div class="balance-label">Campus Wallet</div><div class="balance-amount">₹1,840</div></div>
          <button class="add-btn" onclick="show('credit')">+ Add Money</button>
        </div>
      </div>
      <div style="padding:14px 18px 0;">
        <div class="qr-card">
          <button class="qr-btn" onclick="show('scanner')">
            <svg viewBox="0 0 24 24"><path d="M3 11V3h8v8H3zm2-6v4h4V5H5zM3 21v-8h8v8H3zm2-6v4h4v-4H5zM13 3h8v8h-8V3zm2 2v4h4V5h-4zm4 8h2v2h-2zm0 4h2v2h-2zm-4 0h2v2h-2zm-2-4h2v2h-2zm2 4h2v2h-2zm-2 4h2v2h-2zm4 0h2v2h-2z"/></svg>
            Scan QR to Pay
          </button>
        </div>
      </div>
      <div style="padding:16px 18px 0;">
        <div class="section-label">Quick Actions</div>
        <div class="actions-grid">
          <div class="action-item" onclick="show('vendors')"><div class="action-icon" style="background:#E6F0FF;"><svg viewBox="0 0 24 24" style="fill:#0052CC;"><path d="M20 4H4v2l8 5 8-5V4zM4 13v7h16v-7l-8 5-8-5z"/></svg></div><span class="action-label">Pay Vendor</span></div>
          <div class="action-item" onclick="show('p2p')"><div class="action-icon" style="background:#F0FFF4;"><svg viewBox="0 0 24 24" style="fill:#00875A;"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg></div><span class="action-label">Pay Friend</span></div>
          <div class="action-item" onclick="show('credit')"><div class="action-icon" style="background:#FFFBF0;"><svg viewBox="0 0 24 24" style="fill:#FFB800;"><path d="M20 4H4c-1.11 0-2 .89-2 2v12c0 1.1.89 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.11-.9-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/></svg></div><span class="action-label">Add Credit</span></div>
          <div class="action-item" onclick="show('txns')"><div class="action-icon" style="background:#FFF0F0;"><svg viewBox="0 0 24 24" style="fill:#FF416C;"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg></div><span class="action-label">Transactions</span></div>
        </div>
      </div>
      <div style="padding:14px 18px 0;">
        <div class="spend-widget">
          <div style="font-size:12px;font-weight:700;color:#333;margin-bottom:10px;">Today's Spending — ₹340</div>
          <div class="spend-bar-row">
            <div class="spend-bar" style="height:40%;"></div><div class="spend-bar" style="height:65%;"></div><div class="spend-bar" style="height:30%;"></div><div class="spend-bar" style="height:80%;"></div><div class="spend-bar today" style="height:55%;"></div><div class="spend-bar" style="height:20%;background:#f0f0f0;"></div><div class="spend-bar" style="height:20%;background:#f0f0f0;"></div>
          </div>
          <div class="bc-labels"><span class="bc-label">M</span><span class="bc-label">T</span><span class="bc-label">W</span><span class="bc-label">T</span><span class="bc-label" style="color:#0052CC;font-weight:700;">F</span><span class="bc-label">S</span><span class="bc-label">S</span></div>
        </div>
      </div>
      <div style="padding:14px 18px 0;">
        <div class="section-label">Campus Updates</div>
        <div class="ann-card" onclick="show('events')"><div class="ann-tag">LIVE EVENT</div><div class="ann-title">Techfest 2025 — Registrations Open!</div><div class="ann-sub">BITS Pilani · March 15–17 · 40+ events</div></div>
        <div class="ann-card" style="background:linear-gradient(135deg,#0052CC,#003d99);" onclick="show('deals')"><div class="ann-tag">DEAL ALERT</div><div class="ann-title">20% off at Canteen Block A till 3PM</div><div class="ann-sub">Use UniPay wallet to avail</div></div>
      </div>
      <div style="height:70px;"></div>
    </div>
    <div class="bottom-nav">
      <div class="bnav-item active" onclick="show('home')"><svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg><span>Home</span></div>
      <div class="bnav-item" onclick="show('vendors')"><svg viewBox="0 0 24 24"><path d="M20 4H4v2l8 5 8-5V4zm-8 9L4 8v12h16V8l-8 5z"/></svg><span>Vendors</span></div>
      <div class="bnav-item" onclick="show('scanner')"><svg viewBox="0 0 24 24"><path d="M3 11V3h8v8H3zm2-6v4h4V5H5zM3 21v-8h8v8H3zm2-6v4h4v-4H5zM13 3h8v8h-8V3zm2 2v4h4V5h-4zm4 8h2v2h-2zm0 4h2v2h-2zm-4 0h2v2h-2zm-2-4h2v2h-2zm2 4h2v2h-2zm-2 4h2v2h-2zm4 0h2v2h-2z"/></svg><span>Pay</span></div>
      <div class="bnav-item" onclick="show('dashboard')"><svg viewBox="0 0 24 24"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"/></svg><span>Dashboard</span></div>
      <div class="bnav-item" onclick="show('profile')"><svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg><span>Profile</span></div>
    </div>
  </div>

  <!-- LOGIN -->
  <div class="screen-page" id="sc-login" style="background:#fff;">
    <div class="scroll-content">
      <div class="login-hero">
        <div class="login-logo"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg></div>
        <div style="font-size:22px;font-weight:700;color:#fff;">UniPay</div>
        <div style="font-size:13px;color:rgba(255,255,255,0.75);margin-top:6px;">Campus Payment & Utility Platform</div>
      </div>
      <div class="login-form">
        <div class="login-step">Step 1 of 2 — Student Verification</div>
        <div class="login-field"><label>College Email ID</label><input type="email" placeholder="yourname@bits-pilani.ac.in" /></div>
        <div class="login-field"><label>Student ID</label><input type="text" placeholder="2022ABCD0001" /></div>
        <button class="login-btn">Continue</button>
        <div class="divider-or">— or verify with —</div>
        <button class="linkedin-btn">
          <svg viewBox="0 0 24 24" style="width:17px;height:17px;fill:#fff;"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>
          Continue with LinkedIn OAuth
        </button>
        <div class="verified-badge">
          <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
          <span>LinkedIn verified · Student status confirmed</span>
        </div>
      </div>
    </div>
  </div>

  <!-- DASHBOARD -->
  <div class="screen-page" id="sc-dashboard">
    <div class="scroll-content">
      <div class="dash-header"><div style="font-size:15px;font-weight:700;">Spending Dashboard</div><div style="font-size:12px;opacity:0.75;margin-top:2px;">March 2025 · BITS Pilani</div></div>
      <div style="padding:14px 18px 0;"><div class="ai-insight"><div class="ai-label">AI Insight</div><div class="ai-text">You spent 27% more on food this week. Consider using the ₹50 canteen credit offer.</div></div></div>
      <div style="padding:14px 18px 0;"><div class="chart-card"><div class="chart-title">Weekly Spend<div style="display:flex;gap:4px;"><button style="background:#0052CC;color:#fff;border:none;border-radius:8px;padding:3px 8px;font-size:9px;font-weight:600;cursor:pointer;">Week</button><button style="background:#f0f4ff;color:#555;border:none;border-radius:8px;padding:3px 8px;font-size:9px;font-weight:600;cursor:pointer;">Month</button></div></div><div class="bar-chart"><div class="bc-bar" style="height:40%;"></div><div class="bc-bar" style="height:70%;"></div><div class="bc-bar hl" style="height:90%;"></div><div class="bc-bar" style="height:55%;"></div><div class="bc-bar" style="height:75%;"></div><div class="bc-bar" style="height:30%;"></div><div class="bc-bar" style="height:50%;"></div></div><div class="bc-labels"><span class="bc-label">M</span><span class="bc-label">T</span><span class="bc-label" style="color:#0052CC;font-weight:700;">W</span><span class="bc-label">T</span><span class="bc-label">F</span><span class="bc-label">S</span><span class="bc-label">S</span></div></div></div>
      <div style="padding:14px 18px 0;"><div class="cat-row"><div class="cat-card"><div class="cat-icon">🍕</div><div class="cat-name">Food</div><div class="cat-amount">₹820</div></div><div class="cat-card"><div class="cat-icon">🖨</div><div class="cat-name">Printing</div><div class="cat-amount">₹140</div></div><div class="cat-card"><div class="cat-icon">🎟</div><div class="cat-name">Events</div><div class="cat-amount">₹500</div></div></div><div class="cat-row"><div class="cat-card"><div class="cat-icon">👕</div><div class="cat-name">Merch</div><div class="cat-amount">₹300</div></div><div class="cat-card"><div class="cat-icon">🧺</div><div class="cat-name">Laundry</div><div class="cat-amount">₹80</div></div><div class="cat-card"><div class="cat-icon">☕</div><div class="cat-name">Cafe</div><div class="cat-amount">₹220</div></div></div></div>
      <div style="padding:12px 18px 0;"><div class="budget-card"><div style="display:flex;justify-content:space-between;margin-bottom:8px;"><span style="font-size:12px;color:#666;">Monthly Budget</span><span style="font-size:12px;font-weight:700;color:#333;">₹3,200 / ₹5,000</span></div><div class="progress-bar"><div class="progress-fill" style="width:64%;"></div></div><div style="font-size:10px;color:#0052CC;font-weight:600;margin-top:6px;">64% used — ₹1,800 remaining</div></div></div>
      <div style="padding:12px 18px 14px;"><div class="credit-meter"><div class="score-circle"><div class="score-inner"><span style="font-size:12px;font-weight:700;color:#0052CC;">780</span></div></div><div><div style="font-size:12px;font-weight:700;color:#333;">UniPay Credit Score</div><div style="font-size:10px;color:#888;margin-top:2px;">Excellent · Tier Gold</div><div style="font-size:10px;color:#0052CC;font-weight:600;margin-top:4px;">+12 pts this month</div></div></div></div>
      <div style="height:70px;"></div>
    </div>
    <div class="bottom-nav">
      <div class="bnav-item" onclick="show('home')"><svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg><span>Home</span></div>
      <div class="bnav-item" onclick="show('vendors')"><svg viewBox="0 0 24 24"><path d="M20 4H4v2l8 5 8-5V4zm-8 9L4 8v12h16V8l-8 5z"/></svg><span>Vendors</span></div>
      <div class="bnav-item" onclick="show('scanner')"><svg viewBox="0 0 24 24"><path d="M3 11V3h8v8H3zm2-6v4h4V5H5zM3 21v-8h8v8H3zm2-6v4h4v-4H5zM13 3h8v8h-8V3zm2 2v4h4V5h-4zm4 8h2v2h-2zm0 4h2v2h-2zm-4 0h2v2h-2zm-2-4h2v2h-2zm2 4h2v2h-2zm-2 4h2v2h-2zm4 0h2v2h-2z"/></svg><span>Pay</span></div>
      <div class="bnav-item active" onclick="show('dashboard')"><svg viewBox="0 0 24 24"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"/></svg><span>Dashboard</span></div>
      <div class="bnav-item" onclick="show('profile')"><svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg><span>Profile</span></div>
    </div>
  </div>

  <!-- VENDORS -->
  <div class="screen-page" id="sc-vendors">
    <div class="vendor-header"><div style="color:#fff;font-size:15px;font-weight:700;margin-bottom:10px;">Campus Vendors</div><div class="search-bar"><svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg><span>Search vendors...</span></div></div>
    <div class="filter-row"><div class="filter-chip active">All</div><div class="filter-chip">Food</div><div class="filter-chip">Beverages</div><div class="filter-chip">Printing</div><div class="filter-chip">Services</div><div class="filter-chip">Offers</div></div>
    <div class="scroll-content">
      <div class="vendor-grid">
        <div class="vendor-card"><div class="vendor-img" style="background:#FFF8E1;">🍛</div><div class="vendor-info"><div class="vendor-name">Canteen Block A</div><div class="vendor-meta"><span class="vendor-dist">50m away</span><span class="vendor-deal">20% off</span></div><div style="display:flex;align-items:center;gap:3px;margin-top:4px;"><span class="stars">★★★★</span><span class="rating-num">4.2 · ₹80 avg</span></div></div></div>
        <div class="vendor-card"><div class="vendor-img" style="background:#E8F5E9;">🖨</div><div class="vendor-info"><div class="vendor-name">PrintZone</div><div class="vendor-meta"><span class="vendor-dist">120m away</span><span class="vendor-deal">Deal</span></div><div style="display:flex;align-items:center;gap:3px;margin-top:4px;"><span class="stars">★★★★★</span><span class="rating-num">4.8 · ₹15 avg</span></div></div></div>
        <div class="vendor-card"><div class="vendor-img" style="background:#E3F2FD;">☕</div><div class="vendor-info"><div class="vendor-name">Brew & Co.</div><div class="vendor-meta"><span class="vendor-dist">200m away</span><span class="vendor-deal">—</span></div><div style="display:flex;align-items:center;gap:3px;margin-top:4px;"><span class="stars">★★★★</span><span class="rating-num">4.5 · ₹60 avg</span></div></div></div>
        <div class="vendor-card"><div class="vendor-img" style="background:#FCE4EC;">🥗</div><div class="vendor-info"><div class="vendor-name">Green Bowl</div><div class="vendor-meta"><span class="vendor-dist">80m away</span><span class="vendor-deal">New</span></div><div style="display:flex;align-items:center;gap:3px;margin-top:4px;"><span class="stars">★★★</span><span class="rating-num">3.9 · ₹120 avg</span></div></div></div>
        <div class="vendor-card"><div class="vendor-img" style="background:#F3E5F5;">📚</div><div class="vendor-info"><div class="vendor-name">BookNook</div><div class="vendor-meta"><span class="vendor-dist">300m away</span><span class="vendor-deal">—</span></div><div style="display:flex;align-items:center;gap:3px;margin-top:4px;"><span class="stars">★★★★</span><span class="rating-num">4.1 · ₹200 avg</span></div></div></div>
        <div class="vendor-card"><div class="vendor-img" style="background:#E0F7FA;">🧺</div><div class="vendor-info"><div class="vendor-name">CleanPro</div><div class="vendor-meta"><span class="vendor-dist">150m away</span><span class="vendor-deal">—</span></div><div style="display:flex;align-items:center;gap:3px;margin-top:4px;"><span class="stars">★★★★</span><span class="rating-num">4.3 · ₹40 avg</span></div></div></div>
      </div>
      <div style="height:70px;"></div>
    </div>
    <div class="bottom-nav">
      <div class="bnav-item" onclick="show('home')"><svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg><span>Home</span></div>
      <div class="bnav-item active" onclick="show('vendors')"><svg viewBox="0 0 24 24"><path d="M20 4H4v2l8 5 8-5V4zm-8 9L4 8v12h16V8l-8 5z"/></svg><span>Vendors</span></div>
      <div class="bnav-item" onclick="show('scanner')"><svg viewBox="0 0 24 24"><path d="M3 11V3h8v8H3zm2-6v4h4V5H5zM3 21v-8h8v8H3zm2-6v4h4v-4H5zM13 3h8v8h-8V3zm2 2v4h4V5h-4zm4 8h2v2h-2zm0 4h2v2h-2zm-4 0h2v2h-2zm-2-4h2v2h-2zm2 4h2v2h-2zm-2 4h2v2h-2zm4 0h2v2h-2z"/></svg><span>Pay</span></div>
      <div class="bnav-item" onclick="show('dashboard')"><svg viewBox="0 0 24 24"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"/></svg><span>Dashboard</span></div>
      <div class="bnav-item" onclick="show('profile')"><svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg><span>Profile</span></div>
    </div>
  </div>

  <!-- DEALS -->
  <div class="screen-page" id="sc-deals">
    <div class="deals-header"><div style="font-size:15px;font-weight:700;">Hot Deals</div><div style="font-size:12px;opacity:0.8;margin-top:2px;">Flash offers ending soon</div></div>
    <div class="scroll-content">
      <div style="padding:12px 18px;display:flex;flex-direction:column;gap:10px;">
        <div class="deal-card"><div class="deal-img" style="background:#FFF8E1;">🍛</div><div class="deal-info"><div class="deal-badge">20% OFF</div><div class="deal-name">Thali Special</div><div class="deal-vendor">Canteen Block A</div><div class="deal-footer"><span class="deal-price">₹64 <s style="color:#aaa;font-size:10px;">₹80</s></span><span class="deal-timer">Ends 3:00 PM</span></div></div></div>
        <div class="deal-card"><div class="deal-img" style="background:#E3F2FD;">☕</div><div class="deal-info"><div class="deal-badge">BUY 1 GET 1</div><div class="deal-name">Cold Coffee</div><div class="deal-vendor">Brew & Co.</div><div class="deal-footer"><span class="deal-price">₹60</span><span class="deal-timer">Ends 5:00 PM</span></div></div></div>
        <div class="deal-card"><div class="deal-img" style="background:#E8F5E9;">🖨</div><div class="deal-info"><div class="deal-badge">FLAT ₹5 OFF</div><div class="deal-name">A4 Colour Print</div><div class="deal-vendor">PrintZone</div><div class="deal-footer"><span class="deal-price">₹7 <s style="color:#aaa;font-size:10px;">₹12</s></span><span class="deal-timer">Today only</span></div></div></div>
        <div class="deal-card"><div class="deal-img" style="background:#FCE4EC;">🥗</div><div class="deal-info"><div class="deal-badge">15% OFF</div><div class="deal-name">Protein Bowl</div><div class="deal-vendor">Green Bowl</div><div class="deal-footer"><span class="deal-price">₹102 <s style="color:#aaa;font-size:10px;">₹120</s></span><span class="deal-timer">Ends 7:00 PM</span></div></div></div>
        <div class="deal-card"><div class="deal-img" style="background:#F3E5F5;">🎽</div><div class="deal-info"><div class="deal-badge">FEST MERCH</div><div class="deal-name">Techfest Hoodie</div><div class="deal-vendor">Campus Store</div><div class="deal-footer"><span class="deal-price">₹699 <s style="color:#aaa;font-size:10px;">₹899</s></span><span class="deal-timer">48 hrs left</span></div></div></div>
      </div>
      <div style="height:20px;"></div>
    </div>
  </div>

  <!-- EVENTS -->
  <div class="screen-page" id="sc-events">
    <div style="background:#0052CC;padding:14px 18px;color:#fff;"><div style="font-size:15px;font-weight:700;">Events & Announcements</div><div style="font-size:12px;opacity:0.75;margin-top:2px;">BITS Pilani · March 2025</div></div>
    <div class="scroll-content">
      <div style="padding:12px 18px 4px;font-size:12px;font-weight:700;color:#333;">Featured Event</div>
      <div style="margin:0 18px 10px;" class="event-card-big"><div class="event-img" style="background:linear-gradient(135deg,#0052CC,#003d99);">🎪</div><div class="event-body"><div class="event-tag">TECHFEST 2025</div><div class="event-name">Annual Technical Festival</div><div class="event-meta">March 15–17 · BITS Pilani · 40+ events · ₹500 pass</div><button class="event-register" onclick="show('p2p')">Register & Pay — ₹500</button></div></div>
      <div style="padding:4px 18px 4px;font-size:12px;font-weight:700;color:#333;">Upcoming Events</div>
      <div style="padding:0 18px 14px;display:flex;flex-direction:column;gap:8px;">
        <div class="event-row"><div class="event-date-box"><div class="ed-day">18</div><div class="ed-mon">MAR</div></div><div><div style="font-size:12px;font-weight:700;color:#1a1a2e;">Hackathon 2025</div><div style="font-size:10px;color:#888;margin-top:2px;">₹300 · LT 1 · 24hrs sprint</div></div></div>
        <div class="event-row"><div class="event-date-box"><div class="ed-day">22</div><div class="ed-mon">MAR</div></div><div><div style="font-size:12px;font-weight:700;color:#1a1a2e;">Comedy Night</div><div style="font-size:10px;color:#888;margin-top:2px;">₹200 · Auditorium · Zakir Khan</div></div></div>
        <div class="event-row"><div class="event-date-box" style="background:#FF416C;"><div class="ed-day">25</div><div class="ed-mon">MAR</div></div><div><div style="font-size:12px;font-weight:700;color:#1a1a2e;">Battle of Bands</div><div style="font-size:10px;color:#888;margin-top:2px;">₹500 · Open Air Theatre</div></div></div>
        <div class="event-row"><div class="event-date-box" style="background:#11998e;"><div class="ed-day">01</div><div class="ed-mon">APR</div></div><div><div style="font-size:12px;font-weight:700;color:#1a1a2e;">Career Fair 2025</div><div style="font-size:10px;color:#888;margin-top:2px;">Free · SAC Ground · 80+ companies</div></div></div>
      </div>
    </div>
  </div>

  <!-- CREDIT -->
  <div class="screen-page" id="sc-credit">
    <div class="scroll-content">
      <div class="credit-header"><div style="font-size:12px;opacity:0.8;">UniPay Balance</div><div class="credit-balance">₹1,840</div><div class="credit-btns"><div class="cred-btn">+ Add Credit</div><div class="cred-btn">Withdraw</div><div class="cred-btn">History</div></div></div>
      <div style="padding:14px 18px 0;">
        <div class="loan-card"><div class="loan-title">Micro-Loan Offer</div><div class="loan-text">Borrow ₹300 for 7 days at 0% interest. Available for Gold+ users only.</div><button class="loan-btn">Borrow ₹300</button></div>
        <div style="margin-top:14px;background:#fff;border-radius:14px;padding:14px;border:0.5px solid #eee;"><div style="font-size:12px;font-weight:700;color:#333;margin-bottom:10px;">Repayment Schedule</div><div class="settle-row"><span class="settle-label">Borrowed</span><span class="settle-value">₹300</span></div><div class="settle-row"><span class="settle-label">Due Date</span><span class="settle-value" style="color:#FF416C;">Mar 22, 2025</span></div><div class="settle-row"><span class="settle-label">Interest</span><span class="settle-value" style="color:#00875A;">₹0 (0%)</span></div></div>
      </div>
      <div style="padding:14px 18px;">
        <div style="font-size:12px;font-weight:700;color:#333;margin-bottom:10px;">Credit Leaderboard</div>
        <div class="lb-row"><div class="lb-rank">1</div><div class="lb-avatar" style="background:#FFB800;">PS</div><div class="lb-name">Priya Sharma</div><div class="lb-pts">780 pts</div></div>
        <div class="lb-row"><div class="lb-rank">2</div><div class="lb-avatar" style="background:#0052CC;">RK</div><div class="lb-name">Rahul Kumar</div><div class="lb-pts">750 pts</div></div>
        <div class="lb-row"><div class="lb-rank">3</div><div class="lb-avatar" style="background:#11998e;">AS</div><div class="lb-name">Ananya Singh</div><div class="lb-pts">720 pts</div></div>
        <div class="lb-row"><div class="lb-rank">4</div><div class="lb-avatar" style="background:#FF416C;">MV</div><div class="lb-name">Mihir Verma</div><div class="lb-pts">695 pts</div></div>
      </div>
      <div style="height:20px;"></div>
    </div>
  </div>

  <!-- P2P -->
  <div class="screen-page" id="sc-p2p">
    <div class="p2p-header"><div style="font-size:15px;font-weight:700;">Peer Payments</div><div class="p2p-tabs"><div class="p2p-tab active">Pay Friend</div><div class="p2p-tab">Request Money</div></div></div>
    <div class="scroll-content">
      <div style="padding:14px 18px;">
        <div style="font-size:11px;font-weight:700;color:#888;text-transform:uppercase;letter-spacing:0.6px;margin-bottom:8px;">Recent</div>
        <div class="contact-row"><div class="contact-avatar" style="background:#0052CC;">RK</div><div><div class="contact-name">Rahul Kumar</div><div class="contact-email">rahul@bits-pilani.ac.in</div></div><div class="contact-action">Pay</div></div>
        <div class="contact-row"><div class="contact-avatar" style="background:#11998e;">AS</div><div><div class="contact-name">Ananya Singh</div><div class="contact-email">ananya@bits-pilani.ac.in</div></div><div class="contact-action">Pay</div></div>
        <div class="contact-row"><div class="contact-avatar" style="background:#FF416C;">MV</div><div><div class="contact-name">Mihir Verma</div><div class="contact-email">mihir@bits-pilani.ac.in</div></div><div class="contact-action">Pay</div></div>
        <div style="font-size:11px;font-weight:700;color:#888;text-transform:uppercase;letter-spacing:0.6px;margin:12px 0 8px;">All Contacts</div>
        <div class="contact-row"><div class="contact-avatar" style="background:#764ba2;">NK</div><div><div class="contact-name">Neha Khanna</div><div class="contact-email">neha@bits-pilani.ac.in</div></div><div class="contact-action">Pay</div></div>
        <div class="contact-row"><div class="contact-avatar" style="background:#FFB800;">SP</div><div><div class="contact-name">Siddharth Patel</div><div class="contact-email">sid@bits-pilani.ac.in</div></div><div class="contact-action">Pay</div></div>
      </div>
      <div style="padding:0 18px 14px;">
        <div style="font-size:12px;font-weight:600;color:#666;margin-bottom:6px;">Enter Amount</div>
        <div class="amt-display" id="amtDisplay">₹0</div>
        <div class="numpad">
          <div class="numpad-key" onclick="addD('1')">1</div><div class="numpad-key" onclick="addD('2')">2</div><div class="numpad-key" onclick="addD('3')">3</div>
          <div class="numpad-key" onclick="addD('4')">4</div><div class="numpad-key" onclick="addD('5')">5</div><div class="numpad-key" onclick="addD('6')">6</div>
          <div class="numpad-key" onclick="addD('7')">7</div><div class="numpad-key" onclick="addD('8')">8</div><div class="numpad-key" onclick="addD('9')">9</div>
          <div class="numpad-key act">•</div><div class="numpad-key" onclick="addD('0')">0</div><div class="numpad-key act" onclick="delD()">⌫</div>
        </div>
        <button class="pay-btn">Pay Now</button>
      </div>
    </div>
  </div>

  <!-- VENDOR DASH -->
  <div class="screen-page" id="sc-vdash">
    <div class="vdash-header"><div style="font-size:14px;font-weight:700;">Vendor Dashboard — Canteen Block A</div><div style="font-size:11px;opacity:0.7;margin-top:2px;">Today · March 15, 2025</div></div>
    <div class="scroll-content">
      <div class="vdash-stats">
        <div class="vstat-card"><div class="vstat-label">Today's Revenue</div><div class="vstat-value">₹12,480</div><div class="vstat-delta">+18% vs yesterday</div></div>
        <div class="vstat-card"><div class="vstat-label">Transactions</div><div class="vstat-value">156</div><div class="vstat-delta">+22 txns</div></div>
        <div class="vstat-card"><div class="vstat-label">Avg. Order Value</div><div class="vstat-value">₹80</div><div class="vstat-delta">+₹5 avg</div></div>
        <div class="vstat-card"><div class="vstat-label">Net Settlement</div><div class="vstat-value">₹11,856</div><div class="vstat-delta">After 5% fee</div></div>
      </div>
      <div style="padding:0 18px 14px;"><div class="chart-card"><div class="chart-title">Hourly Sales</div><div class="bar-chart"><div class="bc-bar" style="height:20%;"></div><div class="bc-bar" style="height:55%;"></div><div class="bc-bar hl" style="height:95%;"></div><div class="bc-bar" style="height:40%;"></div><div class="bc-bar" style="height:70%;"></div><div class="bc-bar hl" style="height:85%;"></div><div class="bc-bar" style="height:30%;"></div><div class="bc-bar" style="height:15%;"></div></div><div class="bc-labels"><span class="bc-label">8A</span><span class="bc-label">9A</span><span class="bc-label" style="color:#0052CC;">12P</span><span class="bc-label">1P</span><span class="bc-label">4P</span><span class="bc-label" style="color:#0052CC;">6P</span><span class="bc-label">8P</span><span class="bc-label">10P</span></div></div></div>
      <div style="padding:0 18px 12px;"><div style="font-size:12px;font-weight:700;color:#333;margin-bottom:8px;">Traffic Heatmap by Hour</div><div class="hm-grid"><div class="hm-cell" style="background:#E6F0FF;"></div><div class="hm-cell" style="background:#85B7EB;"></div><div class="hm-cell" style="background:#0052CC;"></div><div class="hm-cell" style="background:#85B7EB;"></div><div class="hm-cell" style="background:#B5D4F4;"></div><div class="hm-cell" style="background:#0747A6;"></div><div class="hm-cell" style="background:#85B7EB;"></div><div class="hm-cell" style="background:#E6F0FF;"></div></div><div class="hm-labels"><span class="hm-label">8A</span><span class="hm-label">10A</span><span class="hm-label">12P</span><span class="hm-label">2P</span><span class="hm-label">4P</span><span class="hm-label">6P</span><span class="hm-label">8P</span><span class="hm-label">10P</span></div></div>
      <div style="padding:0 18px 12px;"><div style="font-size:12px;font-weight:700;color:#333;margin-bottom:8px;">Top Selling Items</div><div class="item-row"><div class="item-rank">1</div><div class="item-name">Masala Thali</div><div class="item-bar"><div class="item-bar-fill" style="width:95%;"></div></div><div class="item-amount">₹3,200</div></div><div class="item-row"><div class="item-rank">2</div><div class="item-name">Veg Biryani</div><div class="item-bar"><div class="item-bar-fill" style="width:75%;"></div></div><div class="item-amount">₹2,400</div></div><div class="item-row"><div class="item-rank">3</div><div class="item-name">Paneer Roll</div><div class="item-bar"><div class="item-bar-fill" style="width:55%;"></div></div><div class="item-amount">₹1,760</div></div><div class="item-row"><div class="item-rank">4</div><div class="item-name">Cold Coffee</div><div class="item-bar"><div class="item-bar-fill" style="width:40%;"></div></div><div class="item-amount">₹1,280</div></div></div>
      <div style="padding:0 18px 14px;"><div class="settle-card"><div style="font-size:12px;font-weight:700;color:#333;margin-bottom:8px;">Settlement Details</div><div class="settle-row"><span class="settle-label">Gross Revenue</span><span class="settle-value">₹12,480</span></div><div class="settle-row"><span class="settle-label">Platform Fee (5%)</span><span class="settle-value" style="color:#FF416C;">- ₹624</span></div><div class="settle-row"><span class="settle-label">Net Payable</span><span class="settle-value" style="color:#00875A;font-size:14px;">₹11,856</span></div><button class="settle-btn">Create Deal + Settle</button></div></div>
      <div style="height:20px;"></div>
    </div>
  </div>

  <!-- PROFILE -->
  <div class="screen-page" id="sc-profile">
    <div class="scroll-content">
      <div class="profile-header"><div class="profile-avatar">PS</div><div style="font-size:17px;font-weight:700;">Priya Sharma</div><div style="font-size:12px;opacity:0.75;margin-top:4px;">priya@bits-pilani.ac.in</div><div style="background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);color:#fff;font-size:10px;font-weight:700;padding:4px 12px;border-radius:10px;display:inline-block;margin-top:10px;">Verified Student · BITS Pilani · 2022A3PS001</div></div>
      <div class="settings-group"><div class="settings-label">Payment</div>
        <div class="setting-row"><div class="setting-icon" style="background:#E6F0FF;"><svg viewBox="0 0 24 24" style="fill:#0052CC;"><path d="M20 4H4c-1.11 0-2 .89-2 2v12c0 1.1.89 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.11-.9-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/></svg></div><span class="setting-label">Payment Methods</span><span style="color:#bbb;font-size:14px;">›</span></div>
        <div class="setting-row"><div class="setting-icon" style="background:#FFF8E1;"><svg viewBox="0 0 24 24" style="fill:#FFB800;"><path d="M20 4H4c-1.11 0-2 .89-2 2v12c0 1.1.89 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.11-.9-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/></svg></div><span class="setting-label">Transaction Limits</span><span style="color:#bbb;font-size:14px;">›</span></div>
        <div class="setting-row"><div class="setting-icon" style="background:#E8F5E9;"><svg viewBox="0 0 24 24" style="fill:#00875A;"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg></div><span class="setting-label">Security & PIN</span><span style="color:#bbb;font-size:14px;">›</span></div>
      </div>
      <div class="settings-group"><div class="settings-label">Preferences</div>
        <div class="setting-row"><div class="setting-icon" style="background:#E3F2FD;"><svg viewBox="0 0 24 24" style="fill:#1976D2;"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2z"/></svg></div><span class="setting-label">Notifications</span><div class="toggle"><div class="toggle-dot"></div></div></div>
        <div class="setting-row"><div class="setting-icon" style="background:#F3E5F5;"><svg viewBox="0 0 24 24" style="fill:#7B1FA2;"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm4.24 16L12 15.45 7.77 18l1.12-4.81-3.73-3.23 4.92-.42L12 5l1.92 4.53 4.92.42-3.73 3.23L16.23 18z"/></svg></div><span class="setting-label">Language & Region</span><span style="color:#bbb;font-size:14px;">›</span></div>
      </div>
      <div class="settings-group" style="padding-bottom:80px;"><div class="settings-label">Support</div>
        <div class="setting-row"><div class="setting-icon" style="background:#FCE4EC;"><svg viewBox="0 0 24 24" style="fill:#C62828;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg></div><span class="setting-label">Help & FAQ</span><span style="color:#bbb;font-size:14px;">›</span></div>
        <div class="setting-row"><div class="setting-icon" style="background:#FFF3E0;"><svg viewBox="0 0 24 24" style="fill:#E65100;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></div><span class="setting-label">About UniPay</span><span style="color:#bbb;font-size:14px;">›</span></div>
      </div>
    </div>
    <div class="bottom-nav">
      <div class="bnav-item" onclick="show('home')"><svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg><span>Home</span></div>
      <div class="bnav-item" onclick="show('vendors')"><svg viewBox="0 0 24 24"><path d="M20 4H4v2l8 5 8-5V4zm-8 9L4 8v12h16V8l-8 5z"/></svg><span>Vendors</span></div>
      <div class="bnav-item" onclick="show('scanner')"><svg viewBox="0 0 24 24"><path d="M3 11V3h8v8H3zm2-6v4h4V5H5zM3 21v-8h8v8H3zm2-6v4h4v-4H5zM13 3h8v8h-8V3zm2 2v4h4V5h-4zm4 8h2v2h-2zm0 4h2v2h-2zm-4 0h2v2h-2zm-2-4h2v2h-2zm2 4h2v2h-2zm-2 4h2v2h-2zm4 0h2v2h-2z"/></svg><span>Pay</span></div>
      <div class="bnav-item" onclick="show('dashboard')"><svg viewBox="0 0 24 24"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"/></svg><span>Dashboard</span></div>
      <div class="bnav-item active" onclick="show('profile')"><svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg><span>Profile</span></div>
    </div>
  </div>

  <!-- SCANNER -->
  <div class="screen-page" id="sc-scanner" style="background:#000;">
    <div class="scanner-bg">
      <div style="padding:14px 18px;width:100%;display:flex;align-items:center;gap:12px;">
        <div style="width:30px;height:30px;background:rgba(255,255,255,0.1);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;" onclick="goBack()"><svg viewBox="0 0 24 24" style="width:16px;height:16px;fill:#fff;"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg></div>
        <div style="color:#fff;font-size:15px;font-weight:700;">Scan & Pay</div>
      </div>
      <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;">
        <div class="scanner-area">
          <div class="scanner-corner tl"></div><div class="scanner-corner tr"></div><div class="scanner-corner bl"></div><div class="scanner-corner br"></div>
          <div class="scanner-line" id="scanLine"></div>
          <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;">
            <svg viewBox="0 0 100 100" width="75" height="75" opacity="0.15"><rect x="10" y="10" width="30" height="30" fill="none" stroke="#fff" stroke-width="3"/><rect x="15" y="15" width="20" height="20" fill="#fff"/><rect x="60" y="10" width="30" height="30" fill="none" stroke="#fff" stroke-width="3"/><rect x="65" y="15" width="20" height="20" fill="#fff"/><rect x="10" y="60" width="30" height="30" fill="none" stroke="#fff" stroke-width="3"/><rect x="15" y="65" width="20" height="20" fill="#fff"/><rect x="60" y="60" width="8" height="8" fill="#fff"/><rect x="72" y="60" width="8" height="8" fill="#fff"/><rect x="84" y="60" width="6" height="8" fill="#fff"/><rect x="60" y="72" width="8" height="8" fill="#fff"/><rect x="72" y="72" width="8" height="18" fill="#fff"/><rect x="84" y="72" width="6" height="6" fill="#fff"/></svg>
          </div>
        </div>
        <div style="color:rgba(255,255,255,0.65);font-size:13px;text-align:center;">Point at any UniPay vendor QR code</div>
        <div class="scanner-options">
          <div class="scan-option"><div class="scan-option-icon"><svg viewBox="0 0 24 24"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg></div><span>Torch</span></div>
          <div class="scan-option"><div class="scan-option-icon"><svg viewBox="0 0 24 24"><path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/></svg></div><span>Gallery</span></div>
          <div class="scan-option" onclick="show('p2p')"><div class="scan-option-icon"><svg viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg></div><span>Pay Friend</span></div>
        </div>
      </div>
    </div>
  </div>

  <!-- TRANSACTIONS -->
  <div class="screen-page" id="sc-txns">
    <div class="txn-header"><div style="font-size:15px;font-weight:700;">Transactions</div><div style="font-size:12px;opacity:0.75;margin-top:2px;">March 2025 · ₹2,060 spent</div></div>
    <div class="filter-row" style="background:#0052CC;border:none;">
      <div class="filter-chip" style="background:rgba(255,255,255,0.25);color:#fff;border-color:transparent;">All</div>
      <div class="filter-chip" style="background:transparent;color:rgba(255,255,255,0.7);border-color:rgba(255,255,255,0.3);">Food</div>
      <div class="filter-chip" style="background:transparent;color:rgba(255,255,255,0.7);border-color:rgba(255,255,255,0.3);">Events</div>
      <div class="filter-chip" style="background:transparent;color:rgba(255,255,255,0.7);border-color:rgba(255,255,255,0.3);">P2P</div>
      <div class="filter-chip" style="background:transparent;color:rgba(255,255,255,0.7);border-color:rgba(255,255,255,0.3);">Credits</div>
    </div>
    <div class="scroll-content">
      <div style="padding:12px 18px;">
        <div class="txn-date">Today</div>
        <div class="txn-row"><div class="txn-icon" style="background:#FFF8E1;">🍛</div><div style="flex:1;"><div class="txn-name">Canteen Block A</div><div class="txn-sub">Masala Thali · 12:45 PM</div></div><div class="txn-amount debit">-₹80</div></div>
        <div class="txn-row"><div class="txn-icon" style="background:#E3F2FD;">☕</div><div style="flex:1;"><div class="txn-name">Brew & Co.</div><div class="txn-sub">Cold Coffee · 10:20 AM</div></div><div class="txn-amount debit">-₹60</div></div>
        <div class="txn-date">Yesterday</div>
        <div class="txn-row"><div class="txn-icon" style="background:#E6F0FF;">🎟</div><div style="flex:1;"><div class="txn-name">Techfest Registration</div><div class="txn-sub">Entry pass · 3:00 PM</div></div><div class="txn-amount debit">-₹500</div></div>
        <div class="txn-row"><div class="txn-icon" style="background:#E8F5E9;">👤</div><div style="flex:1;"><div class="txn-name">Received from Rahul</div><div class="txn-sub">Pizza split · 8:30 PM</div></div><div class="txn-amount credit">+₹200</div></div>
        <div class="txn-date">March 13</div>
        <div class="txn-row"><div class="txn-icon" style="background:#E8F5E9;">🖨</div><div style="flex:1;"><div class="txn-name">PrintZone</div><div class="txn-sub">A4 prints · 20 pages</div></div><div class="txn-amount debit">-₹30</div></div>
        <div class="txn-row"><div class="txn-icon" style="background:#F3E5F5;">👕</div><div style="flex:1;"><div class="txn-name">Campus Store</div><div class="txn-sub">Techfest Hoodie</div></div><div class="txn-amount debit">-₹699</div></div>
        <div class="txn-row"><div class="txn-icon" style="background:#E0F7FA;">➕</div><div style="flex:1;"><div class="txn-name">Wallet Top-Up</div><div class="txn-sub">UPI · HDFC Bank</div></div><div class="txn-amount credit">+₹2,000</div></div>
      </div>
      <div style="height:20px;"></div>
    </div>
  </div>

  </div><!-- /screen -->

  <div class="android-nav">
    <div class="nav-btn" onclick="goBack()" title="Back"><svg viewBox="0 0 24 24"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg></div>
    <div class="nav-btn" onclick="show('home')" title="Home"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="#bbb" stroke-width="2"/></svg></div>
    <div class="nav-btn" title="Recents"><svg viewBox="0 0 24 24"><rect x="5" y="5" width="14" height="14" rx="2" fill="none" stroke="#bbb" stroke-width="2"/></svg></div>
  </div>
</div>

<script>
const screens=['home','login','dashboard','vendors','deals','events','credit','p2p','vdash','profile','scanner','txns'];
let hist=['home'];
function show(id){
  screens.forEach(s=>{
    const el=document.getElementById('sc-'+s);
    const tb=document.getElementById('t-'+s);
    if(el) el.classList.toggle('active',s===id);
    if(tb) tb.classList.toggle('active',s===id);
  });
  if(hist[hist.length-1]!==id) hist.push(id);
}
function goBack(){
  if(hist.length>1){hist.pop();show(hist[hist.length-1]);}
}
let amt='';
function addD(d){
  if(amt.length>6)return;
  if(d==='.'&&amt.includes('.'))return;
  if(d==='.'&&amt==='')amt='0';
  amt+=d;
  document.getElementById('amtDisplay').textContent='₹'+amt;
}
function delD(){
  amt=amt.slice(0,-1);
  document.getElementById('amtDisplay').textContent=amt?'₹'+amt:'₹0';
}
let lp=0,ld=1;
setInterval(()=>{
  const line=document.getElementById('scanLine');
  if(!line)return;
  lp+=ld*2;
  if(lp>=90)ld=-1;
  if(lp<=0)ld=1;
  line.style.top=lp+'%';
},20);
</script>
"""

    components.html(phone_html, height=980, scrolling=False)

# ── Footer ──────────────────────────────────────────────────────────────────────
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; padding: 0.5rem 0 1rem;'>
    <div style='font-family:Syne,sans-serif; font-size:1rem; font-weight:700; color:#e0e6f5;'>UniPay — One Campus. One Wallet. Zero Friction.</div>
    <div style='font-size:0.78rem; color:#3a4d7a; margin-top:0.4rem;'>Design Thinking & Innovation · Course Project · 2025</div>
</div>
""", unsafe_allow_html=True)
