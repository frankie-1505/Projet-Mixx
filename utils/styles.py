from .constants import COLORS


def get_modern_stylesheet() -> str:
    return f"""
        /* Global */
        * {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
        }}

        QMainWindow {{
            background-color: {COLORS['background']};
        }}

        QWidget {{
            color: {COLORS['text_primary']};
        }}

        /* Labels */
        QLabel {{
            color: {COLORS['text_secondary']};
            font-size: 14px;
            font-weight: 500;
        }}

        /* Input Fields */
        QLineEdit {{
            padding: 12px 16px;
            border: 2px solid {COLORS['border']};
            border-radius: 8px;
            background-color: {COLORS['white']};
            font-size: 14px;
            color: {COLORS['text_primary']};
            selection-background-color: {COLORS['primary']};
        }}

        QLineEdit:focus {{
            border-color: {COLORS['primary']};
            background-color: {COLORS['white']};
        }}

        QLineEdit:read-only {{
            background-color: #f9fafb;
            color: #6b7280;
        }}

        QLineEdit::placeholder {{
            color: #9ca3af;
        }}

        /* ComboBox */
        QComboBox {{
            padding: 12px 16px;
            border: 2px solid {COLORS['border']};
            border-radius: 8px;
            background-color: {COLORS['white']};
            font-size: 14px;
            color: {COLORS['text_primary']};
        }}

        QComboBox:focus {{
            border-color: {COLORS['primary']};
        }}

        QComboBox::drop-down {{
            border: none;
            width: 30px;
        }}

        QComboBox::down-arrow {{
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 6px solid {COLORS['text_secondary']};
            margin-right: 10px;
        }}

        QComboBox QAbstractItemView {{
            border: 1px solid {COLORS['border']};
            background-color: {COLORS['white']};
            selection-background-color: {COLORS['primary']};
            selection-color: {COLORS['white']};
            padding: 5px;
        }}

        /* DateEdit */
        QDateEdit {{
            padding: 12px 16px;
            border: 2px solid {COLORS['border']};
            border-radius: 8px;
            background-color: {COLORS['white']};
            font-size: 14px;
            color: {COLORS['text_primary']};
        }}

        QDateEdit:focus {{
            border-color: {COLORS['primary']};
        }}

        QDateEdit::drop-down {{
            border: none;
            width: 30px;
        }}

        QDateEdit::down-arrow {{
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 6px solid {COLORS['text_secondary']};
            margin-right: 10px;
        }}

        /* Buttons */
        QPushButton {{
            padding: 14px 28px;
            background-color: {COLORS['primary']};
            color: {COLORS['white']};
            border: none;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }}

        QPushButton:hover {{
            background-color: {COLORS['primary_hover']};
        }}

        QPushButton:pressed {{
            background-color: {COLORS['primary_active']};
        }}

        QPushButton:disabled {{
            background-color: #d1d5db;
            color: #9ca3af;
        }}

        /* Secondary Button */
        QPushButton[class="secondary"] {{
            background-color: {COLORS['white']};
            color: {COLORS['text_secondary']};
            border: 2px solid {COLORS['border']};
        }}

        QPushButton[class="secondary"]:hover {{
            background-color: {COLORS['card_bg']};
            border-color: {COLORS['primary']};
            color: {COLORS['primary']};
        }}

        /* Frame/Card */
        QFrame {{
            background-color: {COLORS['white']};
            border: 1px solid {COLORS['border']};
            border-radius: 12px;
        }}

        /* ScrollBar */
        QScrollBar:vertical {{
            width: 8px;
            background: transparent;
            margin: 0px;
        }}

        QScrollBar::handle:vertical {{
            background: {COLORS['input_border']};
            border-radius: 4px;
            min-height: 20px;
        }}

        QScrollBar::handle:vertical:hover {{
            background: #9ca3af;
        }}

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
            background: none;
        }}

        /* Table */
        QTableWidget {{
            border: 1px solid {COLORS['border']};
            background-color: {COLORS['white']};
            gridline-color: {COLORS['border_light']};
            font-size: 12px;
            border-radius: 8px;
        }}

        QTableWidget::item {{
            padding: 8px;
        }}

        QTableWidget::item:hover {{
            background-color: {COLORS['card_bg']};
        }}

        QHeaderView::section {{
            background-color: {COLORS['card_bg']};
            padding: 10px;
            border: none;
            border-bottom: 2px solid {COLORS['border']};
            font-weight: 600;
            color: {COLORS['text_secondary']};
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
    """
