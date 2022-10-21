# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd

cols = ["collectioncode", "title", "origination", "bioghist", "scopecontent"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('xquery-output_tw_s3.xml')
root = xmlparse.getroot()
for i in root:
    collectioncode = i.find("collectioncode").text
    title = i.find("title").text
    origination = i.find("origination").text
    #bioghist = i.find("bioghist").text
    #bioghist = bioghist.replace('\n', ' ').replace('\r', ' ').replace('Historical/Biographical Note', ' ')
    #bioghist = bioghist.strip()
    scopecontent = i.find("scopecontent").text
    scopecontent = scopecontent.replace('\n', ' ').replace('\r', ' ').replace('Scope and Contents Note', ' ')


    rows.append({"collectioncode": collectioncode,
                 "title": title,
                 "origination": origination,
                 #"bioghist": bioghist,
                 "scopecontent": scopecontent
                 })

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output_tw_scope_3.csv')