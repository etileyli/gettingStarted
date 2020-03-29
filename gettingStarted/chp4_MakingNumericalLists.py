# squares = [value**2 for value in range(1, 11)]
# for val in squares:
#     print(val)

for val in range (1, 61):
    txt = 'START /WAIT \"\" \"C:\\Program Files\\encevis\\encevis.exe\" \"/PID:PAT' + str(val) + '\" \"/TID:REC' + str(val) + '\" \"/FNAME:C:\\Users\\aslaptop1\\Desktop\\EDFNic\\EEG' + str(val) + '.edf\" \"/PLUGINS:EpiSpike\" \"/SILENT:TRUE\"'
    txt1 = '\nIF %ERRORLEVEL% NEQ 0 ECHO Error\n' + 'IF %ERRORLEVEL% EQU 0 ECHO Success'

    # "" "C:\Program Files\encevis\encevis.exe" "/PID:PAT1" "/TID:REC1" "/FNAME:C:\Study\EEG.edf" "/PLUGINS:EpiSpike" "/SILENT:TRUE"

    # 'START /WAIT "" "C:\Program Files\encevis\encevis.exe" "/PID:PAT1" "/TID:REC1" "/FNAME:C:\Study\EEG.edf" "/PLUGINS:EpiSpike" "/SILENT:TRUE")
    # 'START /WAIT "" "C:\Program Files\encevis\encevis.exe" "/PID:PAT1" "/TID:REC1" "/FNAME:C:\Study\EEG1.edf" "/PLUGINS:EpiSpike" "/SILENT:TRUE"
    print(txt + txt1)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[1:])


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods.append('some stuff')
#
# print(my_foods)
# print(friend_foods)

