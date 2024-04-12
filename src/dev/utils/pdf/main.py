from fpdf import FPDF

def pline(pdf, page_limit):
    x1 = pdf.get_x() + 1
    y = pdf.get_y() + 2
    pdf.line(x1, y, page_limit, y)

def title(str):
    pdf.set_font('DejaVu-Bold', '', 9)
    pdf.write(2, str)
    pdf.set_font('DejaVu', '', 7)

def gap(pdf):
    pdf.line(pdf.get_x() + 1, pdf.get_y() + 2, pdf.get_x() + 40, pdf.get_y() + 2)
    pdf.set_x(pdf.get_x() + 40)

def lgap(pdf):
    pdf.line(pdf.get_x() + 1, pdf.get_y() + 2, pdf.get_x() + 4, pdf.get_y() + 2)
    pdf.set_x(pdf.get_x() + 4)

left = 17
top = 20
right = 12
bottom = 15
page_limit = 207 - left

pdf = FPDF()
pdf.set_margins(left, top, right)
pdf.set_auto_page_break(True, bottom)
pdf.add_page()
pdf.add_font('DejaVu-Bold', '', 'DejaVuSansCondensed-Bold.ttf', uni=True)
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)

title('ЖАЛОБЫ ')
pline(pdf, page_limit)
pdf.ln(4)
pline(pdf, page_limit)
pdf.ln(5)

title('АНАМНЕЗ ')
pdf.write(2, '(в т.ч.- эпид.,аллерг.,гинекол. по показаниям)')
for i in range(6):
    pline(pdf, page_limit)
    pdf.ln(4)

title('ОБЪЕКТИВНО: ')
pdf.write(2, 'общее состояние (удовл.,ср.тяжести,тяжелое,терминальное). Сознание: ясное, оглушение, сопор, кома.')
pdf.ln(4)
pdf.write(2, 'Положение активное, пассивное, вынужденное ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Кожные покровы: сухие, влажные, обычной окраски, бледные, гиперемия, цианоз, желтушность')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Сыпь ')
gap(pdf)
pdf.write(2, 'Зев ')
gap(pdf)
pdf.write(2, 'Миндалины ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Лимфоузлы ')
gap(pdf)
pdf.write(2, 'Пролежни ')
gap(pdf)
pdf.write(2, 'Отеки ')
gap(pdf)
pdf.write(2, 't°C ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Органы дыхания: ЧДД ')
lgap(pdf)
pdf.write(2, 'в мин., одышка эксператорная, инспираторная, смешанная. Патологическое дыхание ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Аускультативно: везикулярное, жесткое, бронхиалоное, пузрильное, ослаблено, отсутствует в ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Хрипы сухие (свистящие, жужжащие) в ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Влажные (мелко-, средне-, крупнопузырчатые) в ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Крепитация, шум трения плевры над ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Перкуторный звук легочный, тимпанический, коробочный, притупленный, тупой над ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Кашель сухой, влажный, лающий, отсутствует. Мокрота ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.set_font('DejaVu-Bold', '', 7)
pdf.write(2, 'Органы кровообращения: ')
pdf.set_font('DejaVu', '', 7)
pdf.write(2, 'пульс ')
lgap(pdf)
pdf.write(2, 'в мин., ритмичный, аритмичный, наполнение ')
lgap(pdf)
pdf.write(2, 'ЧСС ')
lgap(pdf)
pdf.write(2, 'в мин.')
pdf.ln(4)
pdf.write(2, 'дефицит пульса ')
lgap(pdf)
pdf.write(2, 'АД ')
lgap(pdf)
pdf.write(2, 'привычное ')
lgap(pdf)
pdf.write(2, 'максимальное ')
lgap(pdf)
pdf.write(2, 'мм.рт.ст.')
pdf.ln(4)
pdf.write(2, 'Тоны сердца звучные, приглушены, глухие. Шум систолический, диастолический на')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'проводится ')
gap(pdf)
pdf.write(2, 'Шум трения перикарда. Акцент тона ')
gap(pdf)
pdf.write(2, 'на ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.set_font('DejaVu-Bold', '', 7)
pdf.write(2, 'Органы пищеварения: ')
pdf.set_font('DejaVu', '', 7)
pdf.write(2, 'Язык сухой, влажный, обложен ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Живот форма ')
lgap(pdf)
pdf.write(2, 'мягий, напряжен в ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Безболезненный, болезненный в ')
pdf.line(pdf.get_x() + 1, pdf.get_y() + 2, page_limit - 64 + left, pdf.get_y() + 2)
pdf.set_x(page_limit - 64 + left)
pdf.write(2, 'Положительные симптомы (Образцова,')
pdf.ln(4)
pdf.write(2, 'Ровзинга, Ситковского, Ортнера, Мерфи, Мейро-Робонса, Щеткина-Блюмберга, Вааля) ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Перистальтика ')
gap(pdf)
pdf.write(2, 'Печень ')
gap(pdf)
pdf.write(2, 'Селезенка')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Рвота (частота) ')
pdf.line(pdf.get_x() + 1, pdf.get_y() + 2, pdf.get_x() + (page_limit - pdf.get_x() - 53)/2, pdf.get_y() + 2)
pdf.set_x(pdf.get_x() + (page_limit - pdf.get_x() - 53)/2)
pdf.write(2, 'Стул (консистенция, частота) ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.set_font('DejaVu-Bold', '', 7)
pdf.write(2, 'Нервная система: ')
pdf.set_font('DejaVu', '', 7)
pdf.write(2, 'Поведение спокойное, беспокойное, возбужден. Контакт  ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Чувствительность ')
pdf.line(pdf.get_x() + 1, pdf.get_y() + 2, pdf.get_x() + (page_limit - pdf.get_x() - 53)/2, pdf.get_y() + 2)
pdf.set_x(pdf.get_x() + (page_limit - pdf.get_x() - 53)/2)
pdf.write(2, 'Речь (внятная, дизартрия, афазия) ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Зрачки , обычные, широкие, узкие. Фотореакция ')
gap(pdf)
pdf.write(2, 'Нистагм ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Ассиметрия лица ')
pdf.line(pdf.get_x() + 1, pdf.get_y() + 2, page_limit - 87 + left, pdf.get_y() + 2)
pdf.set_x(page_limit - 87 + left)
pdf.write(2, 'Менингеальные симптомы (ригидность затылочных мышц,')
pdf.ln(4)
pdf.write(2, 'Кенинга, Брудзинского) ')
pdf.line(pdf.get_x() + 1, pdf.get_y() + 2, pdf.get_x() + (page_limit - pdf.get_x() - 42)/2, pdf.get_y() + 2)
pdf.set_x(pdf.get_x() + (page_limit - pdf.get_x() - 42)/2)
pdf.write(2, 'Очаговые симптомы ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Координатные пробы ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Мочеполовая система ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Симптом поколачивания  ')
pline(pdf, page_limit)
pdf.ln(4)
pdf.write(2, 'Status locales ')
for i in range(4):
    pline(pdf, page_limit)
    pdf.ln(4)
title('Данные инструментальных исследований (ЭКГ, глюкометрия, пульсоксиметрия и пр.) ')
for i in range(8):
    pline(pdf, page_limit)
    pdf.ln(4)
title('Оказанная помощь и ее эффект (в т.ч. результаты инстр. иссл. в динамике) ')
for i in range(6):
    pline(pdf, page_limit)
    pdf.ln(4)
title('Рекомендации: ')
pline(pdf, page_limit)
pdf.ln(4)
title('Сигнальная карта: ')
pline(pdf, page_limit)
pdf.ln(4)
title('Расходные материалы: Салфетки спиртовые № ')
lgap(pdf)
title(',Перчатки ')
lgap(pdf)
title(',Маска ')
lgap(pdf)
title(',Шпатель ')
lgap(pdf)
title(',Чехол д.терм ')
lgap(pdf)
pdf.set_x(page_limit - 1)
title(',')
#pline(pdf, page_limit)
pdf.ln(4)
title('Шприц 2,0 № ')
lgap(pdf)
title('5,0 № ')
lgap(pdf)
title('10,0 № ')
lgap(pdf)
title('20,0 № ')
lgap(pdf)
title(',Катерер. куб. ')
lgap(pdf)
title('G Фикс. пластырь ')
lgap(pdf)
title('Скариф ')
lgap(pdf)
title('Тест ')
pdf.ln(4)
title('полоски ')
lgap(pdf)
title(',Пакет мед.отхлд. ')
lgap(pdf)
title('Маска для небулайзера ')
lgap(pdf)
pdf.ln(4)
pline(pdf, page_limit)
pdf.ln(4)
title('Дата и номер наряда ')
gap(pdf)
title('Подпись ')
pdf.line(pdf.get_x() + 1, pdf.get_y() + 2, pdf.get_x() + 21, pdf.get_y() + 2)
pdf.set_x(pdf.get_x() + 21)
title('Карту проверил ')
pline(pdf, page_limit)
#print(pdf.get_x())
pdf.output('Result.pdf', 'F')