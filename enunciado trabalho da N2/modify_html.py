import os
import re

def process_file(filename, is_detect_active):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic replaces for light mode
    content = content.replace("background-color: #081217;", "background-color: #f0f4f8;")
    content = content.replace("background-color: #0e222b;", "background-color: #ffffff;")
    content = content.replace("border: 10px solid #1a333f;", "border: 10px solid #d1d8dd;")
    content = content.replace("color: #e6f1f5;", "color: #1f2937;")
    content = content.replace("color: #a0b8c4;", "color: #6b7280;")
    content = content.replace("color: #ffffff;", "color: #111827;") # For headers and general
    content = content.replace("background-color: #00a8cc;", "background-color: #0ea5e9;")
    content = content.replace("color: #ffffff;\n      font-size: 11px;", "color: #ffffff;\n      font-size: 11px;") # badge-local fix, wait color was already replaced to 111827? Let's be careful.
    
    # CSS overrides: we will just append CSS to the end of the <style> block to override dark mode colors.
    
    override_css = """
    /* --- LIGHT MODE OVERRIDES --- */
    body { background-color: #e2e8f0; }
    .phone-container {
      background-color: #f8fafc;
      border: 10px solid #cbd5e1;
      box-shadow: 0 20px 50px rgba(0,0,0,0.1);
      color: #1e293b;
    }
    .status-bar { color: #64748b; }
    .header-title { color: #0f172a; }
    .badge-local { background-color: #0ea5e9; color: #ffffff; }
    .info-icon { background: #e0f2fe; color: #0284c7; }
    .header-subtitle { color: #64748b; }
    
    .card, .main-card, .history-card, .meta-card, .bbox-item, .metric-card-sec {
      background-color: #ffffff;
      border: 1px solid #e2e8f0;
    }
    .card-header, .card-title, .card-id, .meta-val, .geom-val { color: #0f172a; }
    .input-box, .detail-pill, .centroid-badge, .search-box {
      background-color: #f1f5f9;
      border: 1px solid #cbd5e1;
      color: #334155;
    }
    .btn-primary, .btn-action-big, .bbox-conf {
      background-color: #0ea5e9;
      color: #ffffff;
    }
    .btn-secondary, .btn-back {
      background-color: transparent;
      color: #0ea5e9;
      border: 1px solid #0ea5e9;
    }
    .slider-labels, .exec-info, .section-label, .geom-lbl, .meta-lbl, .card-details { color: #64748b; }
    .slider-labels span:last-child { color: #0ea5e9; }
    .slider-track { background-color: #e2e8f0; }
    .slider-fill, .slider-thumb { background-color: #0ea5e9; }
    .slider-thumb { box-shadow: 0 0 6px rgba(14,165,233,0.5); }
    .preview-box, .annotated-box {
      background-color: #f8fafc;
      border: 1px solid #e2e8f0;
    }
    .icon-blue, .btn-arrow, .table-title, .bbox-id { color: #0284c7; }
    
    /* Tela 2 specific overrides */
    .metric-card-big { background-color: #0ea5e9; }
    .metric-value { color: #ffffff; }
    .metric-card-sec .metric-value { color: #0f172a; }
    .class-pill { background-color: #f1f5f9; border: 1px solid #cbd5e1; color: #334155; }
    .bbox { border: 2px solid #0ea5e9; box-shadow: 0 0 4px rgba(14,165,233,0.6); background-color: rgba(14,165,233,0.1); }
    .bbox-label { background-color: #0ea5e9; color: #ffffff; }
    .fish-shape { background-color: #94a3b8; }
    
    /* Tela 3 specific */
    .app-header { border-bottom: 1px solid #e2e8f0; }
    .stat-banner { background: linear-gradient(135deg, #0ea5e9, #0284c7); border: none; }
    .stat-val { color: #ffffff; }
    .stat-lbl { color: #e0f2fe; }
    .card-date { color: #0ea5e9; }
    .card-footer { border-top: 1px solid #e2e8f0; }
    
    /* Tela 4 specific */
    .bbox-header { border-bottom: 1px solid #f1f5f9; }
    
    /* Bottom Navigation Bar CSS */
    .bottom-nav {
      display: flex;
      justify-content: space-around;
      align-items: center;
      background-color: #ffffff;
      border-top: 1px solid #e2e8f0;
      height: 60px;
      padding-bottom: 5px;
    }
    .nav-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #94a3b8;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      gap: 4px;
      flex: 1;
    }
    .nav-item.active {
      color: #0ea5e9;
    }
    .nav-icon {
      font-size: 20px;
    }
    """
    
    content = content.replace("</style>", override_css + "\n</style>")
    
    nav_html_detect = "active" if is_detect_active else ""
    nav_html_hist = "" if is_detect_active else "active"
    
    bottom_nav_html = f"""
  <!-- Bottom Navigation -->
  <div class="bottom-nav">
    <div class="nav-item {nav_html_detect}">
      <span class="nav-icon">🎯</span>
      <span>Detectar</span>
    </div>
    <div class="nav-item {nav_html_hist}">
      <span class="nav-icon">🕒</span>
      <span>Histórico</span>
    </div>
  </div>
</div>
"""
    
    content = content.replace("</div>\n\n</body>", bottom_nav_html + "\n</body>")
    content = content.replace("</div>\n</body>", bottom_nav_html + "\n</body>")
    
    # Specific fix for Tela1 color in HTML
    content = content.replace('color:#ffffff;', '')  # Remove hardcoded inline styles affecting texts that should be dark
    content = content.replace('color:#00e676;', 'color:#10b981;') # Make green a bit more readable on light background
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

os.chdir("/home/sergio/Documentos/unirv/2026-2/DESENVOLVIMENTO DE SOFTWARE PARA DISPOSITIVOS MÓVEIS/enunciado trabalho da N2")
process_file("tela1.html", True)
process_file("tela2.html", True)
process_file("tela3.html", False)
process_file("tela4.html", False)
print("Updated all 4 files.")
