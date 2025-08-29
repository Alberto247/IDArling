# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Qt compatibility module for IDA 9.1
This module provides compatibility between PyQt5 and PyQt6/PySide6
"""

try:
    # Try PyQt6 first (IDA 9.1 preference)
    from PyQt6.QtCore import QPoint, QRect, QSize, Qt, QTimer, QAbstractItemModel, QModelIndex, QObject, pyqtProperty, QPropertyAnimation, QDir, QEvent, QCoreApplication, QFileInfo
    from PyQt6.QtGui import QIcon, QImage, QPainter, QPixmap, QRegion, QAction, QColor, QBrush, QContextMenuEvent, QShowEvent, QRegularExpressionValidator
    from PyQt6.QtWidgets import QActionGroup, QLabel, QMenu, QWidget, QStyledItemDelegate, QApplication, QMainWindow, QHBoxLayout, QMessageBox, QProgressDialog, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QGroupBox, QCheckBox, QComboBox, QLineEdit, QPlainTextEdit, QPushButton, QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QFileDialog, QSplitter, QTableView, QSizePolicy, QColorDialog
    
    # Some imports moved between PyQt5 and PyQt6
    try:
        from PyQt6.QtCore import pyqtSignal as Signal
    except ImportError:
        from PyQt6.QtCore import Signal
        
    # Handle QRegExp which was moved/changed in Qt6
    try:
        from PyQt6.QtCore import QRegularExpression as QRegExp
    except ImportError:
        from PyQt6.QtGui import QRegularExpression as QRegExp
        
    # qApp equivalent
    qApp = QApplication.instance
    
    QT_VERSION = 6
    
except ImportError:
    try:
        # Fallback to PySide6
        from PySide6.QtCore import QPoint, QRect, QSize, Qt, QTimer, Signal, QAbstractItemModel, QModelIndex, QObject, QPropertyAnimation, QDir, QEvent, QCoreApplication, QFileInfo
        from PySide6.QtCore import Property as pyqtProperty
        from PySide6.QtGui import QIcon, QImage, QPainter, QPixmap, QRegion, QAction, QColor, QBrush, QContextMenuEvent, QShowEvent, QRegularExpressionValidator
        from PySide6.QtWidgets import QActionGroup, QLabel, QMenu, QWidget, QStyledItemDelegate, QApplication, QMainWindow, QHBoxLayout, QMessageBox, QProgressDialog, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QGroupBox, QCheckBox, QComboBox, QLineEdit, QPlainTextEdit, QPushButton, QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QFileDialog, QSplitter, QTableView, QSizePolicy, QColorDialog
        
        from PySide6.QtCore import QRegularExpression as QRegExp
        qApp = QApplication.instance
        
        QT_VERSION = 6
        
    except ImportError:
        try:
            # Fallback to PyQt5 for older IDA versions
            from PyQt5.QtCore import QPoint, QRect, QSize, Qt, QTimer, pyqtSignal as Signal, QAbstractItemModel, QModelIndex, QObject, pyqtProperty, QPropertyAnimation, QRegExp, QDir, QEvent, QCoreApplication, QFileInfo
            from PyQt5.QtGui import QIcon, QImage, QPainter, QPixmap, QRegion, QColor, QBrush, QContextMenuEvent, QShowEvent, QRegExpValidator as QRegularExpressionValidator
            from PyQt5.QtWidgets import QAction, QActionGroup, QLabel, QMenu, QWidget, QStyledItemDelegate, qApp, QMainWindow, QHBoxLayout, QMessageBox, QProgressDialog, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QGroupBox, QCheckBox, QComboBox, QLineEdit, QPlainTextEdit, QPushButton, QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QFileDialog, QSplitter, QTableView, QSizePolicy, QColorDialog
            
            QT_VERSION = 5
            
        except ImportError:
            # Final fallback to PySide2
            from PySide2.QtCore import QPoint, QRect, QSize, Qt, QTimer, Signal, QAbstractItemModel, QModelIndex, QObject, QPropertyAnimation, QRegExp, QDir, QEvent, QCoreApplication, QFileInfo
            from PySide2.QtCore import Property as pyqtProperty
            from PySide2.QtGui import QIcon, QImage, QPainter, QPixmap, QRegion, QColor, QBrush, QContextMenuEvent, QShowEvent, QRegExpValidator as QRegularExpressionValidator
            from PySide2.QtWidgets import QAction, QActionGroup, QLabel, QMenu, QWidget, QStyledItemDelegate, QMainWindow, QHBoxLayout, QMessageBox, QProgressDialog, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QGroupBox, QCheckBox, QComboBox, QLineEdit, QPlainTextEdit, QPushButton, QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QFileDialog, QSplitter, QTableView, QSizePolicy, QColorDialog
            
            from PySide2.QtWidgets import QApplication
            qApp = QApplication.instance
            
            QT_VERSION = 5

# Handle sip import
try:
    import sip
except ImportError:
    sip = None

# Export all commonly used Qt classes and constants
__all__ = [
    'QPoint', 'QRect', 'QSize', 'Qt', 'QTimer', 'Signal', 'QAbstractItemModel', 'QModelIndex', 'QObject', 'pyqtProperty', 'QPropertyAnimation', 'QDir', 'QRegExp', 'QEvent', 'QCoreApplication', 'QFileInfo', 'QRegularExpressionValidator',
    'QIcon', 'QImage', 'QPainter', 'QPixmap', 'QRegion', 'QAction', 'QColor', 'QBrush', 'QContextMenuEvent', 'QShowEvent',
    'QActionGroup', 'QLabel', 'QMenu', 'QWidget', 'QStyledItemDelegate', 'QApplication', 'QMainWindow', 'QHBoxLayout', 'QMessageBox', 'QProgressDialog', 
    'QDialog', 'QVBoxLayout', 'QGridLayout', 'QFormLayout', 'QGroupBox', 'QCheckBox', 'QComboBox', 'QLineEdit', 'QPlainTextEdit', 'QPushButton', 
    'QSpinBox', 'QTabWidget', 'QTableWidget', 'QTableWidgetItem', 'QHeaderView', 'QAbstractItemView', 'QFileDialog', 'QSplitter', 'QTableView', 'QSizePolicy', 'QColorDialog',
    'qApp', 'sip', 'QT_VERSION'
]
