import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


class ConnectGoogleSheet:
    def __init__(self, credentials_path, google_sheet_key):
        json_key = json.load(open(credentials_path))
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                                    json_key['private_key'].encode(), scope)
        gc = gspread.authorize(credentials)
        try:
            self.sheet = gc.open_by_key(google_sheet_key)
        except:
            raise PermissionError("""
Either sheet with key does not exist, or your account does\'t have right permission!
Try giving "can edit" rights to an email listed in your credentials: """ + json_key['client_email'])

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

    def write(self, df, worksheet=None, start_row=1, start_col='A'):
        rows, cols = [shape + 1 for shape in df.shape]
        if worksheet:
            if worksheet in self.sheet.worksheets():
                ws = self.sheet.worksheet(worksheet)
            else:
                ws = self.sheet.add_worksheet(title=worksheet, rows=max(rows, 26), cols=max(cols, 26))
        else:
            ws = self.sheet.Shee1

        index_range = 'A2:A' + str(rows)
        columns_range = 'B1:' + self._num2letters(cols) + '1'
        values_range = 'B2:' + self._num2letters(cols) + str(rows)

        self._update_cells(ws, index_range, df.index)
        self._update_cells(ws, columns_range, df.columns)
        self._update_cells(ws, values_range, df.values.ravel())
