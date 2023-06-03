-- Заболевание --
CREATE TABLE IF NOT EXISTS "diseases" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name" TEXT NOT NULL,
  "description" TEXT,
  "period" TEXT,
  "tag_id" INTEGER REFERENCES disease_tags(id) NOT NULL
);

COMMENT ON TABLE public."diseases" IS 'Заболевания';
COMMENT ON COLUMN public."diseases".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."diseases".name IS 'Название заболевания';
COMMENT ON COLUMN public."diseases".description IS 'Описание';
COMMENT ON COLUMN public."diseases".period IS 'Период заболевания';
COMMENT ON COLUMN public."diseases".tag_id IS 'Внешний ключ к таблице Теги заболеваний';

INSERT INTO "diseases" ("id", "name", "description", "period", "tag_id") VALUES
  ('1', 'Ангина', 'Ангина (angina pharyngis; синоним: острый тонзиллит, острый амигдалит) — это общее острое инфекционное заболевание, при котором воспалительные явления выражены главным образом в лимфаденоидной ткани глотки (чаще — миндалин).Острое воспаление лимфатического глоточного кольца, чаще небных миндалин, вызвано стрептококками, стафилококками или другими микроорганизмами.', NULL, '2'),
  ('2', 'Бешенство', 'Бешенство — это абсолютно смертельное заболевание, вызывает рабдовирус; передается через укусы или ослюнение больными животными, поражает ЦНС; проявляется возбуждением, судорогами дыхательной и глотательной мускулатуры и развитием параличей. Вирус может содержаться в слюне, слезах, моче. Длительность болезни - 4-7 дней - 2 нед.', 'Инкубационный период: от 10-90 дней и более года.', '2'),
  ('3', 'Ботулизм', 'Ботулизм — наиболее тяжелое заболевание из группы пищевых токсикоинфекций, характеризующееся развитием тяжелых поражении нервной системы - парезом аккомодации, парезом и параличами глазодвигательных, глотательных и дыхательных мышц.', 'Инкубационный период: от 3-12-24 ч до 2-5-14 дней.', '2'),
  ('4', 'Кишечные инфекции неясной этиологии', 'Кишечные инфекции неясной этиологии (КИНЭ) (сальмонеллез, шигеллез, дизентерия, пищевая токсикоинфекция — ПТИ). Термин КИНЭ объединяет большую группу острых инфекционных заболеваний бактериальновирусной этиологии, основными проявлениями которых являются боли в животе, рвота, частый жидкий стул, характеризующихся обезвоживанием, интоксикацией и развитием ИТШ.', NULL, '2'),
  ('5', 'Гепатит вирусный', 'Гепатит вирусный — общее название острых и хронических диффузных воспалительных заболеваний печени различной этиологии.', 'Инкубационный период: 2-26 нед.', '2'),
  ('6', 'Грипп, ОРВИ', 'Грипп, ОРВИ — острое респираторное вирусное заболевание, характеризующееся острым началом, выраженной лихорадкой, интоксикацией и респираторными симптомами.', NULL, '2'),
  ('7', 'Дифтерия', 'Дифтерия — острое инфекционное заболевание, передающееся воздушно-капельным путем, характеризующееся выраженной интоксикацией, поражением сердечно-сосудистой, нервной выделительной систем и воспалением слизистых оболочек рото-и носоглотки.', NULL, '2'),
  ('8', 'Малярия', 'Малярия — острое инфекционное заболевание, передаваемое человеку при укусах комаров («малярийных комаров»), сопровождающееся приступами лихорадки, ознобами, спленомегалиеи, гепатомегалиеи, анемией и характеризующееся хроническим рецидивирующим течением.', NULL, '2'),
  ('9', 'Коклюш', 'Коклюш — острое инфекционное заболевание, вызываемое коклюшной палочкой, передающееся воздушно-капельным путем, поражающее дыхательные пути и ЦНС, характеризующееся респираторными признаками, приступами спазматического кашля и интоксикацией (на 14-й день).', 'Инкубационный период: 5-9 дней (от 3 до 20).', '2'),
  ('10', 'Корь', 'Корь — высококонтагиозное острое инфекционное заболевание, вызываемое РНК-вирусом, проявляющееся интоксикацией, воспалением верхних дыхательных путей, конъюнктивитом, пятнисто-папулезной сыпью на теле. Источник — заболевший человек. Заразный период: за 2 дня до начала клинических проявлений и 4 дня после появления сыпи.', '1. Инкубационный: 7-17 дн. 2. Катаральный: 2-7 дн. 3. Период высыпаний: 3 дня. 4. Пигментация, реконвалесценция: 14—21 дн.', '2'),
  ('11', 'Коронавирусная инфекция', 'COVID-19 — острое инфекционное заболевание, вызываемое периодически изменяющимся РНК-вирусом; поражает сосудистую систему легких («кровавое» полнокровие, шоковое легкое, альвеолярно-геморрагический синдром); может проявляться как в форме ОРВИ, так и в форме тяжелого острого респираторного синдрома и пневмонии, гипоксемии, тромбоза, тромбоэмболии и/или других нарушений.', 'Инкубационный период: 2-14 (5-7) дней.', '2'),
  ('12', 'Скарлатина', 'Скарлатина — острое инфекционное заболевание, возникающее при проникновении стрептококка в организм через слизистые оболочки дыхательных путей, с токсическим действием на сердце, ЦНС и характеризующееся ангиной и мелкоточечной сыпью на коже.', 'Инкубационный период: 3-7 дней.', '2'),
  ('13', 'Менингококковая инфекция, менингит, менингококцемия', 'Менингококковая инфекция, менингит, менингококцемия — гнойное или серозное воспаление оболочек головного и спинного мозга, вызываемое бактериями, вирусами и другими причинами.', 'Инкубационный период: 2-12 дней.', '2'),
  ('14', 'Холера', 'Холера — острое инфекционное заболевание с фекально-оральным путем заражения, характеризующееся поражением тонкого кишечника, водянистым жидким стулом, рвотой, быстрым обезвоживанием организма, развитием гиповолемического шока и смертельным исходом.', NULL, '2'),
  ('15', 'Чума', 'Чума — это особо опасная инфекция, возбудитель передается через укусы крысиных блох, крыс, животных, воздушно-капельным путем от больного; в лимфоток, лимфоузлы - бактериемия - вторичные очаги; интоксикация, лихорадка, поражение лимфоузлов, легких, сепсис.', 'Инкубационный период: 1-2-6 дней.', '2'),
  ('16', 'Сибирская язва', 'Сибирская язва — это особо опасная инфекция, возбудитель передается через укусы насекомых, при обработке шкур больных животных, через мясные пищевые продукты, обсемененные спорами почву, воду, воздух. В.а. - через кожу (карбункул, язва), слизистые ЖКТ, дыхательных путей в лимфоток; лимфоузлы - серозно-геморрагическое воспаление - некроз тканей; интоксикация, лихорадка, поражение лимфоузлов, сепсис.', 'Инкубационный период: 1-2-8 дней.', '2'),
  ('17', 'Мерцательная аритмия', NULL, NULL, '3'),
  ('18', 'Брадиаритмия', 'Брадиаритмия (ЧСС <50 уд./мин) — нарушение ритма сердца, обусловленное нарушением способности синусно-предсердного узла генерировать электрические импульсы с ЧСС >60 уд./мин.', NULL, '3'),
  ('19', 'Блокада атриовентрикулярная полная', 'Блокада атриовентрикулярная (А-V) полная (синдром Морганьи-Адамса-Стокса) — это некоординированные сокращения предсердий и желудочков в результате прерывания прохождения импульсов через участок сердца, вызывающие резкое замедление сердечного ритма и гипоксию головного мозга.', NULL, '3'),
  ('20', 'Инфаркт миокарда', NULL, NULL, '3'),
  ('21', 'Инфаркт миокарда острый', 'Инфаркт миокарда острый — это одна из клинических форм ишемической болезни сердца, протекающая с развитием ишемического некроза участка миокарда, обусловленного абсолютной или относительной недостаточностью его кровоснабжения.', NULL, '3'),
  ('22', 'Криз гипертонический', NULL, NULL, '3'),
  ('23', 'Стенокардия', NULL, NULL, '3'),
  ('24', 'Острый коронарный синдром', 'Острый коронарный синдром (ОКС) — это любая группа клинических признаков или симптомов, которые позволяют заподозрить инфаркт миокарда или нестабильную стенокардию. Термин введен в связи с необходимостью подтвердить или исключить крупноочаговый инфаркт миокарда (после чего решается вопрос о применении тромболитической терапии).', NULL, '3'),
  ('25', 'Тахикардия', NULL, NULL, '3'),
  ('26', 'Левожелудочковая недостаточность', 'Левожелудочковая недостаточность острая: отек легких, сердечная астма — две последовательные фазы острой левожелудочковой недостаточности, возникающие вследствие резкого ослабления деятельности миокарда; состояние, проявляющееся приступами удушья за счет избыточной транссудации жидкости из сосудистого русла в интерстициальную ткань (сердечная астма), а затем и в альвеолы (отек легких).', NULL, '3'),
  ('27', 'Гипертензия церебральная', 'Гипертензия церебральная — синдром повышения внутричерепного давления, характеризующийся гиперпродукцией ликвора или отеком-набуханием головного мозга, одно из наиболее частых критических состояний, обусловленных поражением головного мозга или его оболочек, возникающий чаще при нейроинфекциях и травмах.', NULL, '4'),
  ('28', 'Острое нарушение мозгового кровообращения', NULL, NULL, '4'),
  ('29', 'Транзиторная ишемическая атака', 'Это остро возникающая недостаточность мозгового кровообращения с очаговыми или диффузными (общемозговыми) нарушениями, характеризующаяся полным восстановлением функций в течение 24 ч.', NULL, '4'),
  ('30', 'Инсульт неуточненный', 'Инсульт недифференцированный — это ОНМК, вызванное патологическим процессом (тромбозом, ишемией, эмболией, кровоизлиянием и др.), сохраняющимся не менее 24 ч, и сопровождающееся развитием стойких симптомов поражения ЦНС или приводящее к смерти.', NULL, '4'),
  ('31', 'Инсульт геморрагический', 'Инсульт геморрагический (ОНМК, мозговой удар, апоплексия, кровоизлияние в мозг) — это ОНМК с кровоизлиянием в вещество мозга (паренхиматозное) и под оболочки мозга (субарахноидальное, субдуральное, эпидуральное). Обычно разрыв сосуда происходит при высоком АД.', NULL, '4'),
  ('32', 'Инсульт ишемический', 'Инсульт ишемический (ОНМК, инфаркт мозга, нетравматическое субарахноидальное кровоизлияние, закупорка и стеноз мозговых артерий) — состояние гипоксии, ишемии и гибели клеток головного мозга в результате сужения (стеноза) или закупорки артерий, питающих клетки головного мозга.', NULL, '4'),
  ('33', 'Невралгия тройничного нерва', 'Невралгия тройничного нерва, синдром острой лицевой боли (болезнь Фозергиля) — это хроническое инфекционно-воспалительное заболевание нервной системы, проявляющееся приступами интенсивных стреляющих, жгучих болей в зонах иннервации тройничного нерва, обычно одностороннее (лицевая нейропатическая боль).', NULL, '4'),
  ('34', 'Эпилепсия', NULL, NULL, '4'),
  ('35', 'Бронхообструктивный синдром, ХОБЛ', 'Бронхообструктивный синдром, ХОБЛ — это нарушение вентиляционной способности легких, в основе которой лежит нарушение бронхиальной проходимости; является осложнением хронической обструктивной болезни легких и ряда других состояний.', NULL, '6'),
  ('36', 'Бронхиальная астма', NULL, NULL, '6'),
  ('37', 'Астматический статус', 'Это тяжелое угрожающее жизни осложнение бронхиальной астмы; возникает в результате длительного некупирующегося приступа и характеризуется отеком бронхиол, накоплением в них вязкой мокроты, приводит к нарастанию удушья и гипоксии.', NULL, '6'),
  ('38', 'Пневмония острая', 'Это острое инфекционное заболевание преимущественно бактериальной этиологии, поражающее респираторные отделы легких с внутриальвеолярной экссудацией и инфильтрацией тканей легких и характеризующееся лихорадкой и интоксикацией.', NULL, '6'),
  ('39', 'Тромбоэмболия легочной артерии', 'Это закупорка сосудистого русла легкого тромбом, образовавшимся в венозной системе большого круга кровообращения, правом предсердии или правом желудочке сердца.', NULL, '6'),
  ('40', 'Гипертензия легочная', 'Это патологическое состояние, характеризующееся повышением давления в легочной артерии, приводящее к развитию правожелудочковой недостаточности.', NULL, '6'),
  ('41', 'Обморок', 'Это внезапная кратковременная потеря сознания, вызванная острой гипоксией головного мозга.', NULL, '6'),
  ('42', 'Коллапс', 'Коллапс — это остро развивающаяся сосудистая недостаточность, характеризующаяся падением сосудистого тонуса и уменьшением ОЦК; проявляется резким снижение артериального и венозного давления, признаками гипоксии головного мозга и угнетением жизненно важных функций организма.', NULL, '6'),
  ('43', 'Крапивница острая', 'Крапивница острая — это состояние, характеризующееся внезапным распространенным высыпанием зудящих волдырей с зоной гиперемии и отеком кожных покровов, аллергического происхождения.', NULL, '6'),
  ('44', 'Отек ангионевротический, отек Квинке', 'Отек ангионевротический, отек Квинке — это остро развивающийся, быстро проходящий отек кожи и подкожной клетчатки или слизистых оболочек. Вызван как иммунными, так и неиммунными факторами, отличается от обычной крапивницы лишь глубиной поражения кожи (бесследно исчезает через несколько часов - 2-3 сут.).', NULL, '6'),
  ('45', 'Гипогликемическое состояние', 'Гипогликемическое состояние — это состояние, характеризующееся острым энергетическим дефицитом в нейронах головного мозга в результате снижения содержания сахара в крови при передозировке инсулина, сахароснижающих препаратов, салицилатов, алкоголя или недостаточном потреблении углеводов с пищей.', NULL, '6'),
  ('46', 'Криз тиреотоксический, криз тиреоидный', 'Криз тиреотоксический (криз тиреоидный) — редкое осложнение гипертиреоидизма, при котором проявления тиреотоксикоза возрастают до жизнеугрожающей степени у больных с нераспознанным или нелеченным гипертиреозом или при болезни Грейвса (диффузный токсический зоб), как наиболее частой причине гипертиреоидизма.', NULL, '6'),
  ('47', 'Артралгический синдром, суставной синдром', 'Артралгический (суставной) синдром — синдром, проявляющийся болями в суставах, их деформацией, ограничением движений, изменениями сухожильно-связочного аппарата окружающих мышц, в основе которого лежат воспалительные или дегенеративно-дистрофические изменения в суставах и околосвязочном аппарате.', NULL, '6'),
  ('48', 'Клиническая смерть, асистолия', 'Клиническая смерть, асистолия — экстремальное состояние, наступающее как фатальный исход ряда заболеваний, состояний или травм.', NULL, '7'),
  ('49', 'Кома гипогликемическая', 'Кома гипогликемическая — тяжелое состояние, развивающееся у больных сахарным диабетом при передозировке инсулина или непринятии пищи после введения обычной дозы инсулина; характеризуется резким снижением уровня глюкозы в крови.', NULL, '7'),
  ('50', 'Кома гипергликемическая', 'Кома гипергликемическая (диабетическая) — тяжелое осложнение сахарного диабета, развивающееся при недостатке инсулина и повышении уровня глюкозы в крови.', NULL, '7'),
  ('51', 'Кома неясного генеза', 'Кома неясного генеза — это остро развивающееся тяжелое состояние, характеризующееся угнетением ЦНС, отсутствием сознания, реакции на внешние раздражители, расстройствами дыхания, кровообращения и других жизненно важных функций организма.', NULL, '7'),
  ('52', 'Отек гортани и верхних дыхательных путей', 'Отек гортани и верхних дыхательных путей — опасное для жизни осложнение ангионевротического отека, крапивницы, ангины или других состояний воспалительного или невоспалительного происхождения, характеризующееся резким утолщением всех тканей гортани и области шеи с серозным выпотом или инфильтрацией и непредсказуемым течением с развитием асфиксии и удушья. Наибольшую опасность для жизни представляет вызванная отеком асфиксия.', NULL, '7'),
  ('53', 'Тепловой, солнечный удар', 'Тепловой, солнечный удар (воздействие высоких температур) — тяжелое поражение ЦНС и нервных центров в продолговатом мозге, вызванное интенсивным или длительным воздействием прямых солнечных лучей на голову, и общее перегревание организма вследствие проникновения тепловых лучей в глубину тканей.', NULL, '7'),
  ('54', 'Утопление', 'Утопление — это терминальное состояние, возникающее в результате обтурации просвета дыхательных путей жидкой средой (водой, грязью, нечистотами и др.), приводящей к механической асфиксии.', 'Спасти тонущего человека можно в первые 3—6 минут с начала утопления, в отдельных случаях этот срок достигает 20-30 мин.', '7'),
  ('55', 'Фибрилляция желудочков', 'Фибрилляция (мерцание) желудочков— это нарушение ритма сердца, характеризующееся полной дезорганизованностью (асинхронностью) сокращения миофибрилл желудочков, что ведет к прекращению насосной функции сердца - клинической смерти.', NULL, '7'),
  ('56', 'Шок анафилактический', 'Шок анафилактический — это остро развивающееся, угрожающее жизни состояние, характеризующееся тяжелыми нарушениями деятельности ЦНС, кровообращения, дыхания и обмена веществ в ответ на введение в организм аллергена.', NULL, '7'),
  ('57', 'Шок инфекционно-токсический', 'Шок инфекционно-токсический (эндотоксический, септический шок) — это экстремальное состояние, возникающее в результате массивной бактериемии и токсемии (воздействия микробных эндотоксинов на клеточные мембраны, компоненты свертывания крови и др.) при генерализации инфекционного процесса и характеризующееся острой недостаточностью кровообращения, тяжелыми метаболическими расстройствами и развитием полиорганной недостаточности.', NULL, '7'),
  ('58', 'Шок кардиогенный', 'Шок кардиогенный — крайняя степень левожелудочковой недостаточности, характеризующаяся резким снижением сократительной способности миокарда (ударного объема и мощности выброса), которое не компенсируется повышением сосудистого сопротивления и приводит к неадекватному кровоснабжению всех органов и тканей, прежде всего жизненно важных органов.', NULL, '7'),
  ('59', 'Шок травматический', 'Шок травматический — тяжелое состояние организма, возникающее как реакция на болевое раздражение или кровотечение.', NULL, '7'),
  ('60', 'Электротравма', 'Электротравма, вызванная электрическим током НИЗКОГО напряжения (<1000 В) — травма, вызванная воздействием на организм и ткани электрического тока большой силы или напряжения, в том числе молнии, характеризуется поражением нервной системы (судороги, потеря сознания), нарушениями кровообращения и дыхания, глубокими ожогами.', NULL, '7'),
  ('61', 'Инородное тело дыхательных путей', 'Инородное тело в дыхательных путях (в ротоглотке) — опасное для жизни экстремальное состояние, вызывающее остановку/прекращение дыхания в результате попадания в дыхательные пути различных предметов.', NULL, '7'),
  ('62', 'Сотрясение головного мозга', 'Сотрясение головного мозга — это черепно-мозговая травма (ЧМТ) с повреждением головного мозга легкой степени тяжести, без стойких органических изменений. При легкой степени травмы клинические признаки могут отсутствовать.', NULL, '9'),
  ('63', 'Ушиб, сдавление головного мозга', 'Ушиб, сдавление головного мозга — это ЧМТ с закрытым повреждением головного мозга, характеризующаяся возникновением очага деструкции его ткани и проявляющаяся неврологической и/или психопатологической симптоматикой соответственно локализации очагов.', NULL, '9'),
  ('64', 'Перелом позвоночника', 'Перелом позвоночника — тяжелая травма, при которой нарушаются частичная или полная целостность позвоночника, а также функции спинного мозга с развитием необратимого паралича и нарушениями функций тазовых органов.', NULL, '9'),
  ('65', 'Перелом костей таза', 'Перелом костей таза — одно из наиболее тяжелых повреждений опорно-двигательного аппарата, характеризующееся разрушением костных тканей таза, повреждением мягких тканей и развитием травматического шока.', NULL, '9'),
  ('66', 'Раны открытые', 'Раны открытые — это нарушения кожных покровов и слизистых оболочек, которые сопровождаются повреждением глубжележащих тканей (жировой клетчатки, фасций, сухожилий, мышц и др.).', NULL, '9'),
  ('67', 'Кровотечения', 'Кровотечение наружное — выход крови из поврежденных кровеносных сосудов через поврежденные кожные покровы непосредственно на поверхность тела. Кровотечение внутреннее — выход крови из поврежденных кровеносных сосудов или паренхиматозных органов в ткани, органы или полости тела.', NULL, '9'),
  ('68', 'Ушибы', 'Ушибы — это закрытые повреждения тканей и органов без нарушения их анатомической целостности, возникающее в результате внешнего воздействия.', NULL, '9'),
  ('69', 'Растяжение связок', 'Растяжения связок (дисторсии) — это надрыв или разрыв связочного аппарата какого-либо сустава в результате травмирующего воздействия, а также при нефункциональных движениях: неловко ступив или споткнувшись.', NULL, '9'),
  ('70', 'Синдром длительного сдавления', 'Синдром длительного сдавления (травматический токсикоз, краш-синдром) — тяжелая травма, обусловленная длительной компрессией (сдавлением) мягких тканей, преимущественно мышечной массы, одним из грозных проявлений которой является эндогенная интоксикация.', NULL, '9'),
  ('71', 'Травма почки', 'Травма почки — это состояние, возникающее в результате травматического воздействия различных физических или механических агентов/факторов на поясничную область (проекцию почек), вызывающих нарушение функции мочевыводящей системы.', NULL, '9'),
  ('72', 'Травма живота', NULL, NULL, '9'),
  ('73', 'Ушиб сердца', 'Ушиб сердца — это закрытое повреждение сердца, без видимого нарушения его анатомической целостности, вызванное тупой травмой грудной клетки.', NULL, '9'),
  ('74', 'Ранение сердца', 'Ранение сердца — открытая травма сердца, относится к числу крайне опасных повреждений. Обширные ранения приводят к немедленной смерти, которая наступает от развивающейся тампонады сердца. Независимо от повреждения камер сердца тампонада приводит к острой правожелудочковой недостаточности и ишемии миокарда левого желудочка.', NULL, '9'),
  ('75', 'Ампутация и размозжение', 'Ампутации и размозжения травматические — экстремальное состояние, обусловленное полным или частичным удалением или размозжением какой-либо части тела в результате внешнего травматического воздействия.', NULL, '9'),
  ('76', 'Ожог термический, химический', 'Ожог термические, химические — это повреждения кожных покровов и глубоких слоев кожи от воздействия термических (пламя, горячие жидкости, пар - контактные ожоги ; химических (кислоты, щелочи) или физических факторов (солнечные, радиационные ожоги).', NULL, '9'),
  ('77', 'Гипотермия', 'Гипотермия (общее охлаждение организма, замерзание) — холодовая травма, вызванная охлаждением всего тела, когда температура тела 35°С, характеризуется угнетением жизненных функций до их исчезновения.', NULL, '9'),
  ('78', 'Отморожения', 'Отморожение — холодовая травма, обусловленная локальным повреждением тканей, возникшим под действием низких температур.', NULL, '9'),
  ('79', 'Укусы животными', 'Укусы животными — повреждение целостности кожных покровов человека домашними или дикими животными, в том числе царапины или ослюнение. Многие животные (собаки, кошки, волки, лисы, белки, ежи, летучие мыши и др.) могут быть переносчиками опасных или абсолютно смертельных для человека болезней.', NULL, '9'),
  ('80', 'Почечная недостаточность острая', 'Почечная недостаточность острая (ОПН) — это синдром, характеризующийся гипоксией (аноксией) почечных канальцев, некрозом их эпителия, отеком и клеточной инфильтрацией интерстициальной ткани, повреждением капилляров почек, т.е. развитием некротического нефроза, нарушением почечной гемодинамики и экзогенной интоксикацией.', NULL, '10'),
  ('81', 'Мочекаменная болезнь, почечная колика', 'Мочекаменная болезнь (МКБ), приступ (почечная колика) — это осложнение МКБ, проявляющееся приступом резких схваткообразных болей в поясничной области и по ходу мочевыводящих путей, обусловленных растяжением почечной лоханки мочой вследствие нарушения ее оттока, а также внезапной закупоркой или спазмом мочеточника или прохождением по нему камня.', NULL, '10'),
  ('82', 'Кровотечение желудочно-кишечное', 'Кровотечение желудочно-кишечное — выхождение крови из кровеносного русла органов пищеварения; является причиной развития угрожающего жизни геморрагического шока.', NULL, '11'),
  ('83', 'Аппендицит острый', 'Аппендицит острый — это воспаление червеобразного отростка слепой кишки, проявляющееся приступом острых болей в животе с признаками раздражения брюшины и нарушением общего состояния организма.', NULL, '11'),
  ('84', 'Грыжа ущемленная', 'Грыжа ущемленная — внезапно возникшее сдавление грыжевого содержимого в грыжевых воротах. Эластическое ущемление — выхождение органа или его части через узкие грыжевые ворота в момент резкого повышения внутрибрюшного давления при физическом напряжении, сопровождающееся ишемией ущемленных органов, выраженным болевым синдромом и стойким мышечным спазмом вокруг грыжевых ворот.', NULL, '11'),
  ('85', 'Кишечная непроходимость острая', 'Кишечная непроходимость острая — синдром, вызванный частичным или полным нарушением продвижения содержимого по пищеварительному тракту, обусловленный механическим препятствием в нем или нарушением двигательной функции кишечника и характеризующийся гиповолемией, дегидратацией тканей, тканевой гипоксией, эндотоксикозом и развитием сепсиса.', NULL, '11'),
  ('86', 'Холецистит острый', 'Холецистит острый — приступ сильных схваткообразных или постоянных болей в правом подреберье и/или в животе, сопровождающийся повышением температуры до 39°С и интоксикацией, в результате обструкции протока желчного пузыря камнем или развития в нем острого воспаления, возникающий как осложнение желчнокаменной болезни или хронического холецистита.', NULL, '11'),
  ('87', 'Панкреатит острый', 'Панкреатит острый (панкреонекроз, токсическая энзимопатия) — болевой синдром в эпигастральной области и/или животе - угрожающее жизни, остро протекающее воспаление поджелудочной железы, в основе которого лежат отек, некробиоз клеток железы, ферментная аутоагрессия (самопереваривание) с развитием некроза и дистрофии железы и присоединением вторичной гнойной инфекции.', NULL, '11'),
  ('88', 'Перитонит', 'Перитонит — это воспаление париетального и висцерального листков брюшины, которое сопровождается тяжелым общим состоянием организма, осложнение течения острого или хронического заболевания и травм органов брюшной полости инфекционного или неинфекционного происхождения, состояние, угрожающее жизни; при неадекватной или несвоевременной помощи прогноз неблагоприятен.', NULL, '11'),
  ('89', 'Окклюзия, тромбоз сосудов конечностей', 'Окклюзия, тромбоз магистральных сосудов конечностей острый — экстремальное состояние, обусловленное эмболией или тромбозом сосуда, что приводит к одновременному выключению как минимум двух больших зон кровотока и сопровождается блокадой коллатерального кровообращения. Отсутствие пульса на периферических артериях подтверждает диагноз; бледность кожных покровов в начальной стадии сменяется цианозом с мраморным рисунком и резким снижением кожной температуры, что позволяет определить место окклюзии.', NULL, '11');