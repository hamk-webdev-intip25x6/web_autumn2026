# suomalaiset päiväykset
# päivä.kuukausi.vuosi
# esim. 31.12.2020, 15.06.2021, 01.01.2022 1.1.2022
# seuraavat ovat virheellisiä: 31.13.2020, 32.12.2020, 15.06.20, 15.6.2020, 15-06-2020, 15/06/2020
# 
# amerikkalaiset päiväykset
# kuukausi/päivä/vuosi
# 11/02/2026
# kiinalaiset päiväykset
# vuosi-kuukausi-päivä
# 2026-11-02
# $123.45
# £123.45
# 123,45 €
# 123,45 SEK
# 1.234.567,89 €
# 1 234 567.89 
# 

import re 
re_date = re.compile(r'(3[01]|[1-2]\d|0?[1-9])\.(1[0-2]|0?[1-9])\.([1-9]\d{3,})')

text = "Here are some dates, which should be redacted 01.01.2020, 31.12.2020, 15.06.2021, 01.01.2022, 1.1.2022, 31.13.2020, 32.12.2020, 15.06.20, 15.6.2020, " \
"wrong ones: 15.2. and 15-06-2020, 15/06/2020"

print(re_date.sub("REDACTED", text))

while True:
    date = input("Anna päiväys (päivä.kuukausi.vuosi): ")
    if not date:
        break
    if re_date.fullmatch(date):
        print(f"{date} on kelvollinen suomalainen päiväys.")
    else:
        print(f"{date} ei ole kelvollinen suomalainen päiväys.")

                    
