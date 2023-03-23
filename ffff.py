from fpdf import FPDF
import json
# j='{"member":[{"member1":{"role":"g","fio":"sdjfsdhfsd"},"member2":{"role":"j","fio":"uuuu"},"member3":{"role":"g","fio":"sdjfsdhfsd"},"member4":{"role":"g","fio":"sdjfsdhfsd"},"member5":{"role":"g","fio":"sdjfsdhfsd"}]}'

j = '{"member":[{"role":"g","fio":"sdjfsdhfsd"},{"role":"j","fio":"uuuu"},{"role":"g","fio":"sdjfsdhfsd"},{"role":"g","fio":"sdjfsdhfsd"},{"role":"g","fio":"sdjfsdhfsd"}]}'
def main(data):
    sos=''
    info=json.loads(data)
    members = info['member']
    for i in members:
        sos+=i['role']+' '+i['fio']+'\n'
    print(sos)
main(j)