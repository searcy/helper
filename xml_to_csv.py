import xml.etree.ElementTree as ET
import csv

tree = ET.parse("xquery-output_tam.xml")
root = tree.getroot()

# open a file for writing

Result_data = open('BiogHistData.csv', 'w', newline='')

# create the csv writer object

csvwriter = csv.writer(Result_data)
results_head = []

count = 0
for item in root.findall('Results'):
	results = []
	#address_list = []
	if count == 0:
		call_number = item.find('collectioncode').tag
		results_head.append(call_number)
		coll_title = item.find('title').tag
		results_head.append(coll_title)
		note_content = item.find('bioghist').tag
		results_head.append(note_content)
		# Address = member[3].tag
		# resident_head.append(Address)
		csvwriter.writerow(results_head)
		count = count + 1

	call_number = item.find('collectioncode').text
	results.append(name)
	coll_title = item.find('title').text
	results.append(coll_title)
	note_content = item.find('bioghist').text
	results.append(note_content)
	# Address = member[3][0].text
	# address_list.append(Address)
	# City = member[3][1].text
	# address_list.append(City)
	# StateCode = member[3][2].text
	# address_list.append(StateCode)
	# PostalCode = member[3][3].text
	# address_list.append(PostalCode)
	# resident.append(address_list)
	csvwriter.writerow(results)
Result_data.close()