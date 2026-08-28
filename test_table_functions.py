"""Minimal tests for utils.fungsi.table_functions based on code review findings."""

import os
import sys
import unittest

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

from utils.fungsi.table_functions import (
    generate_table,
    get_row_data,
    update_from_table,
    format_cell_data,
)


_app = None


def setUpModule():
    global _app
    _app = QApplication.instance() or QApplication([])


class TestGenerateTableEmpty(unittest.TestCase):
    def test_empty_data_restores_table_state(self):
        """generate_table([], table) must not leave signals blocked / updates disabled."""
        table = QTableWidget()
        generate_table([], table)
        self.assertFalse(
            table.signalsBlocked(),
            "signalsBlocked should be False after empty generate_table",
        )
        self.assertTrue(
            table.updatesEnabled(),
            "updatesEnabled should be True after empty generate_table",
        )
        self.assertEqual(table.rowCount(), 0)
        self.assertEqual(table.columnCount(), 0)

    def test_empty_mode_input_with_columns(self):
        table = QTableWidget()
        generate_table([], table, column_names=["id", "nama"], mode_input=True)
        self.assertFalse(table.signalsBlocked())
        self.assertTrue(table.updatesEnabled())
        self.assertEqual(table.rowCount(), 1)
        self.assertEqual(table.columnCount(), 2)


class TestGetRowData(unittest.TestCase):
    def test_converts_numeric_and_date_by_header_name(self):
        """get_row_data should convert by column name, not column index."""
        table = QTableWidget(1, 2)
        table.setHorizontalHeaderLabels(["ID", "TGL LAHIR"])
        table.setItem(0, 0, QTableWidgetItem("12"))
        table.setItem(0, 1, QTableWidgetItem("29-08-2026"))

        row = get_row_data(table, row=0)

        # Current bug: both stay as strings because col index is compared to name lists.
        # After fix, id should be numeric and tgl_lahir a date-like value.
        self.assertIn("id", row)
        self.assertIn("tgl_lahir", row)

        # Document expected correct behavior:
        id_ok = isinstance(row["id"], (int, float)) and row["id"] == 12
        date_ok = row["tgl_lahir"] is not None and not isinstance(row["tgl_lahir"], str)

        if not (id_ok and date_ok):
            self.fail(
                f"get_row_data did not convert types by header name: {row!r}. "
                "Expected id=12 (number) and tgl_lahir as date object."
            )


class TestUpdateFromTable(unittest.TestCase):
    def test_no_column_lists_still_attempts_update(self):
        """update_from_table must attempt UPDATE when both column lists are None."""
        from unittest.mock import patch, MagicMock

        table = QTableWidget(1, 2)
        table.setHorizontalHeaderLabels(["ID", "NAMA"])
        table.setItem(0, 0, QTableWidgetItem("1"))
        table.setItem(0, 1, QTableWidgetItem("A"))
        table.setCurrentCell(0, 1)

        mock_con = MagicMock()
        mock_con.update_data.return_value = True
        with patch("utils.fungsi.table_functions.ConnectDB", return_value=mock_con):
            result = update_from_table(
                tabel_ui=table,
                tabel_sql="dummy_table",
                updatable_column=None,
                not_updatable_column=None,
                key="id",
                key_value="1",
            )

        self.assertTrue(result)
        mock_con.update_data.assert_called_once()
        sql, params = mock_con.update_data.call_args[0]
        self.assertIn("UPDATE dummy_table SET nama = %s WHERE id = %s", sql)
        self.assertEqual(params, ("A", "1"))


class TestFormatCellData(unittest.TestCase):
    def test_currency_separators(self):
        self.assertEqual(
            format_cell_data(1234567.5, separator_ribuan=".", separator_desimal=","),
            "1.234.567,50",
        )
        self.assertEqual(
            format_cell_data(1.25, separator_ribuan=".", separator_desimal=","),
            "1,25",
        )
        self.assertEqual(
            format_cell_data(-1.25, separator_ribuan=".", separator_desimal=","),
            "-1,25",
        )

    def test_none_and_zero(self):
        self.assertEqual(format_cell_data(None), "")
        self.assertEqual(format_cell_data(0, zero="-"), "-")
        self.assertEqual(format_cell_data(0), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
