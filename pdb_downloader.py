import wget
with open("tags1.txt", "r") as tag:
    datas = (tag.read().split(",")[:-1])
n_data = []
for x in datas[:5]:
    n_data.append(x.lower())
print(n_data)
lst = []

# https://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/ +middle 2 chars +/pdb + 4 chars in small letters + .ent.gz

for i in n_data:
    try:
        print("https://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/" +
              i[1:3]+"/pdb"+i+".ent.gz")
        wget.download("https://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/" +
                      i[1:3]+"/pdb"+i+".ent.gz", out="./PDB")
    except:
        print("Not found - " + i)
        lst.append(i)
print(lst)

# https://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/h7/pdb5h7a.ent.gz


# “HELIX”		character
# Helix serial number	right	integer
# Helix identifier	right	character
# Initial residue name	right	character
# Chain identifier		character
# Residue sequence number	right	integer
# Code for insertions of residues		character
# Terminal residue name	right	character
# Chain identifier		character
# Residue sequence number	right	integer
# Code for insertions of residues		character
# Type of helix†	right	integer
# Comment	left	character
# Length of helix
