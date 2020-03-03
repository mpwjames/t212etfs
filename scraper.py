etf = []
etf_list = open("list.txt","w")
with open("t212.txt") as data:
    for line in data:
        if 'ETF' in line:
            line = line.replace('&amp;', '&')
            line = line.replace('                            data-label="Company">', '')
            line = line.replace('</div><div class="d-cell hidden js-cell js-target"', '')
            line = line.replace('                            data-label="ISIN">DE000ETFL011</div><div class="d-cell hidden js-target"', '')
            line = line.replace('                            data-label="ISIN">DE000ETFL235</div><div class="d-cell hidden js-target"', '')
            line = line.replace('                            data-label="Instrument">ETFC</div><div class="d-cell hidden js-cell js-target d-cell--break"', '')
            if line == '\n':
                pass
            else:
                etf.append(line)

del etf[0]
etf_list.writelines(etf)
etf_list.close()
print(etf)
