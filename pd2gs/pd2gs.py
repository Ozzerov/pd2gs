import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials
import re


class ConnectGoogleSheet:
    def __init__(self, path_to_credentials_json, google_sheet_key):
        json_key = json.load(open(path_to_credentials_json))
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                                    json_key['private_key'].encode(), scope)
        gc = gspread.authorize(credentials)
        try:
            self.sheet = gc.open_by_key(google_sheet_key)
        except:
            raise PermissionError("""
Either sheet with this key does not exist, or your account does\'t have right permission!
Double check sheet key. If this not the case,
try giving "can edit" rights to an email listed in your credentials: """ + json_key['client_email'])

    @staticmethod
    def _num2letters(n):
        n -= 1
        result = ''
        while n >= 0:
            remain = n % 26
            result = chr(remain + 65) + result
            n = n // 26 - 1
        return result

    @staticmethod
    def _update_cells(_ws, _range, _values):
        cell_list = _ws.range(_range)
        for cell, value in zip(cell_list, _values):
            cell.value = value
        _ws.update_cells(cell_list)

    def write(self, df, worksheet='Sheet1', start_from='A1'):
        """
        :param df: pandas DataFrame
        :param worksheet: worksheet name
        :param start_from: cell to use for top left corner of a DataFrame
        """
        n_rows, n_cols = df.shape
        start_col, start_row = re.findall('\\d+|\\D+', start_from)
        start_col = sum([(ord(l) - 64) * 26 ** n for (l, n) in zip(start_col.upper(),
                                                                   range(len(start_col) - 1, -1, -1))])
        start_row = int(start_row)
        try:
            ws = self.sheet.worksheet(worksheet)
        except:
            ws = self.sheet.add_worksheet(title=worksheet,
                                          rows=max(start_row + n_rows + 1, 26),
                                          cols=max(start_col + n_cols + 1, 26))

        index_range = '{0}{1}:{2}{3}'.format(self._num2letters(start_col), start_row + 1,
                                             self._num2letters(start_col), start_row + n_rows)
        columns_range = '{0}{1}:{2}{3}'.format(self._num2letters(start_col + 1), start_row,
                                               self._num2letters(start_col + n_cols), start_row)
        values_range = '{0}{1}:{2}{3}'.format(self._num2letters(start_col + 1), start_row + 1,
                                              self._num2letters(start_col + n_cols), start_row + n_rows)
        print(index_range, columns_range, values_range)

        self._update_cells(ws, index_range, df.index)
        self._update_cells(ws, columns_range, df.columns)
        self._update_cells(ws, values_range, df.values.ravel())
