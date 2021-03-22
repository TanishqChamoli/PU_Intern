import os
with open("tags1.txt", "r") as tag:
    datas = (tag.read().split(",")[:-1])
lst = []
location = "C:/Users/LENOVO/Desktop/Python Scripts/PU_Internship/PDB/"
type_of_file = ".pdb"


# predefined info_dic
type_of_helix = ["Right-handed alpha", "Right-handed omega", "Right-handed pi", "Right-handed gamma",
                 "Right-handed 3/10", "Left-handed alpha", "Left-handed omega", "Left-handed gamma", "2/7 ribbon/helix", "Polyproline"]
ls = ["A"]

for i in datas[:50]:
    # Define the variables for the data of helix
    n_helix = 0
    lst_helix = []

    if(os.path.exists(location+i+type_of_file)):
        print("Exists " + i)
        with open(location+i+type_of_file, 'r') as f:
            lines = f.read().split("\n")
            for s_line in lines:
                # parsing line by line to get the data of the helix and store it in a seperate list
                s_line = s_line.strip()

                if s_line[:5] == "HELIX":
                    n_helix += 1
                    lst_helix.append(s_line)

            if(len(lst_helix) > 1):
                data_lst = []
                for line in lst_helix:
                    data_dic = {}
                    data_dic['Helix_serial_number'] = line[7:10].strip()
                    data_dic['Helix_identifier'] = line[11:14].strip()
                    data_dic['Initial_residue_name'] = line[15:18].strip()
                    data_dic['Chain_identifier_1'] = line[19:20].strip()
                    data_dic['Residue_sequence_number_1'] = line[21:25].strip()
                    # //first one
                    data_dic['Code_for_insertions_of_residues_1'] = line[25:26].strip()
                    data_dic['Terminal_residue_name'] = line[27:30].strip()
                    data_dic['Chain_identifier_2'] = line[31:32].strip()
                    data_dic['Residue_sequence_number_2'] = line[33:37].strip()
                    # the last one
                    data_dic['Code_for_insertions_of_residue_2'] = line[37:38].strip()
                    data_dic['Type_of_helix'] = type_of_helix[int(
                        line[38:40].strip())-1]
                    data_dic['Comment'] = line[40:70].strip()
                    data_dic['Length_of_helix'] = line[71:76].strip()
                    if data_dic['Type_of_helix'] == "Right-handed alpha" and data_dic["Chain_identifier_1"] in ls:
                        data_lst.append(data_dic)
                print(data_lst)

    else:
        print("Error- File not found!")
        lst.append(i)
print(lst)
