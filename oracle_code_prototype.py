import xml.etree.cElementTree as ET 
import xlsxwriter

def get_title(ID):
    tree = ET.ElementTree(file='results.xccdf2.xml')
    root = tree.getroot()
    #fix = []
    for chld in root:
        if chld.tag == "{http://checklists.nist.gov/xccdf/1.1}Group":
            if chld.get('id') == "Section_1" or chld.get('id') == "Section_2" or chld.get('id') == "Section_3" or chld.get('id') == "Section_4" or chld.get('id') == "Section_5" or chld.get('id') == "Section_6" or chld.get('id') == "Section_7" or chld.get('id') == "Section_8":
                for x in chld:
                    if x.tag == "{http://checklists.nist.gov/xccdf/1.1}Rule":
                        if x.get('id') == ID:
                            for y in x:
                                 if y.tag == "{http://checklists.nist.gov/xccdf/1.1}title":
                                     fix = str(y.text)
                                     #fix.append(str(y.text))

    return(fix)


def get_description(ID):
    tree = ET.ElementTree(file='results.xccdf2.xml')
    root = tree.getroot()
    #fix = []
    for chld in root:
        if chld.tag == "{http://checklists.nist.gov/xccdf/1.1}Group":
            if chld.get('id') == "Section_1" or chld.get('id') == "Section_2" or chld.get('id') == "Section_3" or chld.get('id') == "Section_4" or chld.get('id') == "Section_5" or chld.get('id') == "Section_6" or chld.get('id') == "Section_7" or chld.get('id') == "Section_8":
                for x in chld:
                    if x.tag == "{http://checklists.nist.gov/xccdf/1.1}Rule":
                        if x.get('id') == ID:
                            for y in x:
                                 if y.tag == "{http://checklists.nist.gov/xccdf/1.1}description":
                                     fix = str(y.text)
                                     #fix.append(str(y.text))

    return(fix)


def get_fixtext(ID):
    tree = ET.ElementTree(file='results.xccdf2.xml')
    root = tree.getroot()
    #fix = []
    for chld in root:
        if chld.tag == "{http://checklists.nist.gov/xccdf/1.1}Group":
            if chld.get('id') == "Section_1" or chld.get('id') == "Section_2" or chld.get('id') == "Section_3" or chld.get('id') == "Section_4" or chld.get('id') == "Section_5" or chld.get('id') == "Section_6" or chld.get('id') == "Section_7" or chld.get('id') == "Section_8":
                for x in chld:
                    if x.tag == "{http://checklists.nist.gov/xccdf/1.1}Rule":
                        if x.get('id') == ID:
                            for y in x:
                                 if y.tag == "{http://checklists.nist.gov/xccdf/1.1}fixtext":
                                     fix = str(y.text)
                                     #fix.append(str(y.text))

    return(fix)


def get_fix(ID):
    tree = ET.ElementTree(file='results.xccdf2.xml')
    root = tree.getroot()
    #fix = []
    for chld in root:
        if chld.tag == "{http://checklists.nist.gov/xccdf/1.1}Group":
            if chld.get('id') == "Section_1" or chld.get('id') == "Section_2" or chld.get('id') == "Section_3" or chld.get('id') == "Section_4" or chld.get('id') == "Section_5" or chld.get('id') == "Section_6" or chld.get('id') == "Section_7" or chld.get('id') == "Section_8":
                for x in chld:
                    if x.tag == "{http://checklists.nist.gov/xccdf/1.1}Rule":
                        if x.get('id') == ID:
                            for y in x:
                                 if y.tag == "{http://checklists.nist.gov/xccdf/1.1}fix":
                                     fix = str(y.text)
                                     #fix.append(str(y.text))

    return(fix)



tree = ET.ElementTree(file='results.xccdf2.xml')
root = tree.getroot()

failed_IDs = []
sev = []

for chld in root:
    if chld.tag == "{http://checklists.nist.gov/xccdf/1.1}TestResult":
         for x in chld:
             if x.tag == "{http://checklists.nist.gov/xccdf/1.1}rule-result":                                  
                  for y in x:
                      if y.text == "fail":
                          print (x.get('idref') + "   " + x.get('severity') + "   " + y.text)
                          osc = str(x.get('idref'))
                          sev.append(str(x.get('severity')))
                          failed_IDs.append(osc)
                          #print(type(osc))
                      break    

print(len(failed_IDs))
print(len(sev))                    

output = []
output2 = []
output3 = []
output4 = []
i = 0

while i < len(failed_IDs):
    zzz = get_title(failed_IDs[i])
    xxx = get_description(failed_IDs[i])
    yyy = get_fixtext(failed_IDs[i])
    aaa = get_fix(failed_IDs[i])
    output.append(zzz)
    output2.append(xxx)
    output3.append(yyy)
    output4.append(aaa)
    i += 1


#output = get_title(failed_IDs[0])

print(output)

workbook = xlsxwriter.Workbook('Example6.xlsx') 
worksheet = workbook.add_worksheet() 
  
# Start from the first cell. 
# Rows and columns are zero indexed. 
row = 0
column = 0

for item in sev : 
  
    # write operation perform 
    worksheet.write(row, column, str(item)) 
  
    # incrementing the value of row by one 
    # with each iteratons. 
    row += 1

column = 1
row = 0

for item in output:
    worksheet.write(row, column, str(item))
    row += 1 

column = 2
row = 0

for item in output2:
    worksheet.write(row, column, str(item))
    row += 1     

column = 3
row = 0

for item in output3:
    worksheet.write(row, column, str(item))
    row += 1     
      
column = 4
row = 0

for item in output4:
    worksheet.write(row, column, str(item))
    row += 1    


workbook.close() 
