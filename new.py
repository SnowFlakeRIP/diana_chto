from fpdf import FPDF
import json
j='{ "pyoag":"a","member":[{"role":"g","fio":"sdjfsdhfsd"}],"pso":"d","pooy":"h","nopa":"g"}'
def main(data):
    pdf = FPDF()
    info=json.loads(data)
    print(info['pyoag'])
    pdf.add_page()
    pdf.add_font('times-new-roman', uni=True)
    pdf.set_font('times-new-roman', '', 11)
    pdf.cell(200, 6, txt='Приложение №5      ', ln=1, align="R")
    pdf.cell(200, 6, txt='к Правилам благоустройства      ', ln=1, align="R")
    pdf.cell(200, 6, txt='территории города Нижний Тагил      ', ln=10, align="R")

    pdf.cell(200, 6, txt='', ln=1, align="C")

    pdf.cell(200, 6, txt='АКТ', ln=1, align="C")
    pdf.cell(200, 6, txt='выполненных работ(приемки)', ln=1, align="C")
    pdf.cell(200, 6, txt='по восстановлению элементов благоустройства', ln=1, align="C")

    pdf.cell(200, 6, txt='', ln=1, align="C")

    pdf.cell(200, 6, txt='г. Нижний Тагил                                                                      «____»___________20__г.', ln=1)

    pdf.cell(200, 6, txt='', ln=1, align="C")

    pdf.cell(200, 6, txt='Представители:', ln=1, align="L")
    pdf.cell(200, 6, txt='Представитель уполномоченного', ln=1, align="l")
    pdf.cell(200, 6, txt=f'органа Администрации города                                      {info["pyoag"]}', ln=1, align="L")
    pdf.cell(200, 6, txt='', ln=1, align="C")
    pdf.cell(200, 6, txt='Уполномоченное', ln=1, align="l")
    pdf.cell(200, 6, txt=f'должностhное лицо администрации района                                  {info["member[0]"]}', ln=1, align="l")
    pdf.cell(200, 6, txt='', ln=1, align="l")
    pdf.cell(200, 6, txt='Представитель специализированной', ln=1, align="l")
    pdf.cell(200, 6, txt='организации, с которой заключен муницпальный', ln=1, align="l")
    pdf.cell(200, 6, txt='контракт по эксплуатационному содержанию', ln=1, align="l")
    pdf.cell(200, 6, txt=f'улично-дорожной сети                                                     {info["pso"]}', ln=1, align="l")
    pdf.cell(200, 6, txt='', ln=1, align="l")
    pdf.cell(200, 6, txt='Представитель организации, осуществляющей', ln=1, align="l")
    pdf.cell(200, 6, txt=f'управление многоквартирным жилым домом                                  {info["pooy"]}', ln=1, align="l")
    pdf.cell(200, 6, txt='', ln=1, align="l")
    pdf.cell(200, 6, txt='', ln=1, align="l")
    pdf.cell(200, 6, txt='', ln=1, align="l")
    pdf.cell(200, 6, txt='', ln=1, align="l")
    pdf.cell(200, 6, txt='УСТАНОВЛЕНО', ln=1, align="l")
    pdf.cell(200, 6, txt='В соответствии с Разрешением на производство земляных работ от «____»________20__г.', ln=1)
    pdf.cell(200, 6, txt='№____на производство работ__________________________________________________________________________________', ln=1, align="l")
    pdf.cell(200, 6, txt='_______________________________________________________________________________________________________________', ln=1, align="l")
    pdf.cell(200, 6, txt='                       (наименование объекта и объем работ в соответствии с записью в Разрешении)', ln=1, align="l")
    pdf.cell(200, 6, txt=f'на объекте по адресу:                               {info["nopa"]}', ln=1, align="l")

    pdf.cell(200, 6, txt='', ln=1, align="l")

    pdf.cell(200, 6, txt='объявлено для приемки:', ln=1, align="l")
    pdf.cell(200, 6, txt='-асфальтобетонное покрытие                                      800 кв.м.', ln=1, align="l")
    pdf.cell(200, 6, txt='-восстаноление благоустройства                                восстановлено', ln=1, align="l")
    pdf.cell(200, 6, txt='-восстановление озеленения                                       восстановлено', ln=1, align="l")
    pdf.cell(200, 6, txt='-восстановление малых архитектурных форм          восстановлено', ln=1, align="l")
    pdf.cell(200, 6, txt='-восстновление технических сооружений                 восстановлено', ln=1, align="l")
    pdf.cell(200, 6, txt='-прочие нарушения                                                             нет', ln=1, align="l")

    pdf.cell(200, 6, txt='РЕШЕНО', ln=1, align="l")
    pdf.cell(200, 6, txt='Принять предъявлнные работы по восстановлению элеменов благоустройства после', ln=1, align="l")
    
    
    pdf.output("akkt.pdf")
# with open("j.json", "r") as my_file:
# j = my_file.read()
# string = json.loads(j)
# # dictionary={'pyoag':'ggggg','ydlr':'gggg','pso':'gg','pooy': 'hhh','nopa':'ggtg'}
# # j = json.dumps(dictionary, indent=4)
# # print(j)
# # main('ggggg','gggg','gg','hhh','hhh')


# def main(data):
#     info=json.loads(data)
#     print(info['pyoag'])
main(j)

# pyoag,ydlr,pso,pooy,nopa