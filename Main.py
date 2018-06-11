import time
file = open(r"E:\!Nysa\Polen_2017-11-29_085425\Polen\model and maps\model and maps\digital\example model\HQ100_Ist\06_iz10v15b_hq100stat.2dm", "r")
outFile = open(r"C:\!!Modele ISOKII\zz_NysaOdcPil\Polen_2017-11-29_085425\Polen\model and maps\model and maps\digital\example model\HQ100_Ist\06_iz10v15b_hq100stat.mesh", "w")
lines = file.readlines()
index = 0
HydroAsPoints = {}

for line in lines:
    line = line.split()
    if line[0] == 'ND':
        line = list(map(lambda x: float(x), line[1:5]))
        line.append(0)
        HydroAsPoints[int(line[0])] = line[1:]

print(HydroAsPoints[1])
pairs = {}
NewLine = []

for line in lines:
    line = line.split()
    if line[0] == 'E3T':
        NewLine.append('{} 0\n'.format(' '.join(line[1:5])))
        pairs['{} {}'.format(*sorted([line[2], line[3]]))] = pairs.get('{} {}'.format(*sorted([line[2], line[3]])), 0) + 1
        pairs['{} {}'.format(*sorted([line[3], line[4]]))] = pairs.get('{} {}'.format(*sorted([line[3], line[4]])), 0) + 1
        pairs['{} {}'.format(*sorted([line[4], line[2]]))] = pairs.get('{} {}'.format(*sorted([line[4], line[2]])), 0) + 1
    elif line[0] == 'E4Q':
        NewLine.append('{}\n'.format(' '.join(line[1:6])))
        pairs['{} {}'.format(*sorted([line[2], line[3]]))] = pairs.get('{} {}'.format(*sorted([line[2], line[3]])), 0) + 1
        pairs['{} {}'.format(*sorted([line[3], line[4]]))] = pairs.get('{} {}'.format(*sorted([line[3], line[4]])), 0) + 1
        pairs['{} {}'.format(*sorted([line[4], line[5]]))] = pairs.get('{} {}'.format(*sorted([line[4], line[5]])), 0) + 1
        pairs['{} {}'.format(*sorted([line[5], line[2]]))] = pairs.get('{} {}'.format(*sorted([line[5], line[2]])), 0) + 1

for field, possible_values in pairs.items():
    field = field.split()

    if possible_values == 1:
        wart = HydroAsPoints[int(field[0])][:-1]
        wart.append(1)

        HydroAsPoints[int(field[0])] = wart
        #print(field)
        wart = HydroAsPoints[int(field[1])][:-1]
        wart.append(1)

        HydroAsPoints[int(field[1])] = wart
pointsAmount = len(HydroAsPoints)
outFile.write('{} PROJCS["DHDN / Gauss-Kruger zone 4",GEOGCS["DHDN",DATUM["D_Deutsches_Hauptdreiecksnetz",SPHEROID["Bessel_1841",6377397.155,299.1528128]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",12],PARAMETER["scale_factor",1],PARAMETER["false_easting",4500000],PARAMETER["false_northing",0],UNIT["Meter",1]]\n'.format(pointsAmount))
for i in range(pointsAmount):

    outFile.write('{} '.format(str(i+1))+' '.join(str(x) for x in HydroAsPoints[i+1])+'\n')
outFile.write('{} 4 25\n'.format(len(NewLine)))
outFile.writelines(NewLine)
file.close()
outFile.close()
