import openpyxl
import re

xf = openpyxl.load_workbook(r'C:\Users\Chen.Liang\Projects\notebook\Gwendolyn #2612LB Daily Drilling Report.xlsx',
                            data_only=True)

path = []
act_log = []

path_headers = []
act_log_headers = []

for sn in xf.sheetnames:
    if re.search(u'Report\(\d+\)', sn) is not None:
        rpt = xf[sn]
        # name
        nm = rpt['B1'].value
        # date
        dt = rpt['F1'].value
        print '%s on [%s] @ %s' % (sn, nm, dt)

        # <drilling path>
        # headers
        if len(path_headers) == 0:
            for row in rpt['J3':'R3']:
                for cell in row:
                    path_headers.append(cell.value)
            path.append(path_headers)
        # values
        # TODO: ADD THE DRILLING DATE
        stage = []
        for row in rpt['J4':'R15']:
            rcd = []
            first_cell = row[0]
            if first_cell.value is not None:
                for cell in row:
                    rcd.append(cell.value)
                stage.append(rcd)

        if len(stage) > 0:
            path.append(stage)

        # <activity log>
        # headers
        if len(act_log_headers) == 0:
            for row in rpt['A17':'E17']:
                for cell in row:
                    act_log_headers.append(cell.value)
            act_log.append(act_log_headers)
        # values
        # TODO: ADD THE DRILLING DATE
        stage = []
        for row in rpt['A18':'E44']:
            rcd = []
            first_cell = row[0]
            if first_cell.value is not None:
                for cell in row:
                    rcd.append(cell.value)
                stage.append(rcd)

        if len(stage) > 0:
            act_log.append(stage)

print '~~~~~ path ~~~~~~'
print path

print '~~~~~ activity ~~~~~~'
print act_log