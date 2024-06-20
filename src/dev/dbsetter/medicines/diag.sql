CREATE TABLE IF NOT EXISTS "diag" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name" TEXT NOT NULL
);

COMMENT ON TABLE public."diag" IS 'Таблица Диагнозов(diag)';
COMMENT ON COLUMN public."diag".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."diag".name IS 'Название диагноза(diag)';

INSERT INTO "diag" ("id", "name") VALUES
  ('1', 'Общая дозировка'),
  ('2', 'Сохраненяющаяся крупноволновая фибрилляция желудочков или желудочковая тахикардия без пульса'),
  ('3', 'Устойчивые пароксизмы эктопической тахикардии QRS < 0.12 сек при ХСН'),
  ('4', 'Устойчивые пароксизмы эктопической тахикардии QRS > 0.12 сек'),
  ('5', 'Фибрилляция - трепетание предсердий'),
  ('6', 'Продолжающийся пароксизм фибрилляции предссердий'),
  ('7', 'Тахисистолия с признаками сердечной недостаточности'),
  ('8', 'Анафилактический шок при явлениях бронхоспазма'),
  ('9', 'Отек гортани (аллергический)'),
  ('10', 'Острый обструктивный ларингит (круп) I ст'),
  ('11', 'Острый обструктивный ларингит (круп) II ст'),
  ('12', 'Острый бронхит, бронхолит с явлениями бронхообструкции'),
  ('13', 'При лорингоспазме'),
  ('14', 'При аллергическом отеке верхних дыхательных путей'),
  ('15', 'При анафилактическом шоке'),
  ('16', 'Инфекционно-токсический шок'),
  ('17', 'Утопление'),
  ('18', 'Странгуляционная асфиксия (повешение, удушение)'),
  ('19', 'Отек головного мозга при малярии'),
  ('20', 'Серозный менингит и менингоэнцефалит: при отеке головного мозга'),
  ('21', 'Менингококкемия'),
  ('22', 'Ушиб горла, шейного отдела пищевода, глотки, гортани, трахеи'),
  ('23', 'Открытая рана, затрагивающая гортань и шейный отдел трахеи'),
  ('24', 'Перелом хрящей гортани, трахеи'),
  ('25', 'Спазм, стеноз гортани. Ларингизм'),
  ('26', 'Термические и химические ожоги уха и перегородка носа при ожогах II-III ст'),
  ('27', 'Термические и химические ожоги рта и глотки при ожогах II-III ст'),
  ('28', 'Тиреотоксический криз'),
  ('29', 'Токсический эффект, обусловенный контактом с ядовитыми животными, кроме укусов клещей'),
  ('30', 'Менингит, вызванный другими уточненными возбудителями'),
  ('31', 'Отек гортани (аллергический) II-III ст'),
  ('32', 'Отек гортани (аллергический) IV ст'),
  ('33', 'Острый обструктивный ларингит (круп) III ст'),
  ('34', 'Острый обструктивный ларингит (круп) IV ст'),
  ('35', 'Отравление препаратами нафазолина или ксилометазолина'),
  ('36', 'Отравлением калием перманганатом'),
  ('37', 'Термические и химические ожоги'),
  ('38', 'Эпилептический статус при гипогликемии'),
  ('39', 'Инсульт, неуточненный как кровоизлияние или инфаркт мозга при гипоглемии < 2.8 ммоль/л'),
  ('40', 'Сахарный диабет: гипогликемическое состояние'),
  ('41', 'Гипогликемическая кома'),
  ('42', 'Надпочечниковый криз (Аддисонов) при гипогликемии < 3.9 ммоль/л'),
  ('43', 'Отравление противодиабетическими препаратами'),
  ('44', 'Токсическое действие других и неуточненных веществ. отравление цианидами. отравление метгемоглобинобразователями'),
  ('45', 'Остановка сердца'),
  ('46', 'Кровотечение после аборта'),
  ('47', 'Апоплексия яичника. Разрыв кисты яичника'),
  ('48', 'Послеродовое кровотечение'),
  ('49', 'Субарахноидальные кровоизлияние нетравматического происхождения'),
  ('50', 'Острая гипертензивная энцефалопатия'),
  ('51', 'Носовое кровотечение'),
  ('52', 'Кровотечение из других отделов верхних дыхательных путей'),
  ('53', 'Кровотечение из наружного слухового прохода'),
  ('54', 'Кровотечение из трахеостомы'),
  ('55', 'Перелом костей носа при кровотечении'),
  ('56', 'Токсическое действие разъедающих веществ. Токсическое действие мыл и детергентов при наличии крови в промывных водах'),
  ('57', 'Травма наружных половых органов с кровотечением'),
  ('58', 'При развитии отека легких при утоплении'),
  ('59', 'Острая левожелудочковая недостаточность при систолическом АД >= 100 мм рт ст'),
  ('60', 'Острый приступ глоукомы'),
  ('61', 'Гломерулярные болезни почек при отеке легких'),
  ('62', 'Почечная недостаточность (острая) при достижении АД 105-110/60 мм рт ст'),
  ('63', 'Наличие трансплантированной почки: при отеке легких'),
  ('64', 'Цирроз печени: при напряженном асците'),
  ('65', 'Общая дозировка (старше 1 года)'),
  ('66', 'Общая дозировка (до 1 года)'),
  ('67', 'Общая дозировка (старше 16 лет)'),
  ('68', 'Общая дозировка (новорожденные и грудные)'),
  ('69', 'Общая дозировка (1-5 лет)'),
  ('70', 'Общая дозировка (6-10 лет)'),
  ('71', 'Общая дозировка (11-14 лет)'),
  ('72', 'Дифтерия при токсических формах'),
  ('73', 'Наследовательный дефицит фактора VIII (Гемофилия А). наследовательный дефицит фактора IX (Гемофилия В). Болезнь Виллебранда: при почечном кровотечении'),
  ('74', 'Надпочечниковый криз (Аддисонов)'),
  ('75', 'Болезни кожи и пожкожной клетчатки. Острая крапивница'),
  ('76', 'Ангионевротический отек'),
  ('77', 'Пневмония при некардиогенном отеке легких'),
  ('78', 'Хроническая обструктивная болезнь легких'),
  ('79', 'Бронхиальная астма'),
  ('80', 'Астматический статус (ДН III-IV ст)'),
  ('81', 'Отравление коаксилом'),
  ('82', 'Отравление трициклическими антидепрессантами'),
  ('83', 'Отравление антихолинергическими, антимускаринными и спазмолитическими средствами'),
  ('84', 'Отравление антагонистами кальция'),
  ('85', 'Отравление сердечными гликозидами'),
  ('86', 'Токсическое действие разъедающих веществ. Токсическое действие мыл и детергентов'),
  ('87', 'Отравление газами раздражающего, удушающего или прижигающего действия'),
  ('88', 'Отравление газами раздражающего, удушающего или прижигающего действия: при бронхообструктивном синдроме'),
  ('89', 'Отравление аконитом, цикутой, морозник'),
  ('90', 'Перелом позвоночника осложненный'),
  ('91', 'Грипп при осложнениях'),
  ('92', 'Инфекционно-токсичесский шок'),
  ('93', 'Анафилактический шок при сохранении артериальной гипотензии'),
  ('94', 'Острая сосудистая недостаточность при снижении САД > 20% от возрастной нормы'),
  ('95', 'Отек гортани (аллергичесский) II-III ст'),
  ('96', 'Отек гортани (аллергичесский) IV ст'),
  ('97', 'Термические и химические ожоги I ст >= 10% поверхности тела и ожоги II-III ст >= 5% поверхности тела'),
  ('98', 'Термические и химические ожоги верхних дыхательных путей'),
  ('99', 'Аллергическая генерализованная реакция на бактериальные, другие и неуточненные вакцины и биологические вещества'),
  ('100', 'Общая дозировка (старше 2 лет)'),
  ('101', 'Острая левожелудочковая недостаточность при систолическом АД >= 100 мм рт ст и при отсутствии эффекта и сохранении САД > 150 мм рт ст'),
  ('102', 'Гипертонический криз неосложненный при отсутствии эффекта'),
  ('103', 'Транзиторная ишемическая атака. синдром вертебробазилярной артериальной системы при САД > 200 мм рт ст'),
  ('104', 'Субарахноидальные кровоизлияние нетравматического происхождения при САД > 170 мм рт ст'),
  ('105', 'Инсульт, неуточненный как кровоизлияние или инфаркт мозга при САД > 200 мм рт ст'),
  ('106', 'Кома неустановленного генеза'),
  ('107', 'Аллергический отек верхних дыхательных путей'),
  ('108', 'Анафилактический шок'),
  ('109', 'Травматический шок, САД > 80 мм рт ст'),
  ('110', 'Травматический шок, САД 60-80 мм рт ст'),
  ('111', 'Травматический шок САД < 60 мм рт ст'),
  ('112', 'Общее охлаждение организма (гипотермия)'),
  ('113', 'Воздействие высоких температур, САД < 90 мм рт ст или снижении более чем на 30 мм рт ст от привычного уровня'),
  ('114', 'Поражение электрическим током'),
  ('115', 'Прерывание беременности в сроке до 22 недель, САД < 90 мм рт ст'),
  ('116', 'Осложнения, вызванные абортом, САД < 90 мм рт ст'),
  ('117', 'Нарушенная внематочная беременность'),
  ('118', 'Внематочная беременность, САД < 90 мм рт ст'),
  ('119', 'Апоплексия яичника или разрыв кисты яичника, САД < 90 мм рт ст'),
  ('120', 'Другие аномальные кровотечения из матки и влагалища, САД < 90 мм рт ст'),
  ('121', 'Рак женских половых органов'),
  ('122', 'Острый тазовый перитонит у женщин, острый параметрит и другое'),
  ('123', 'Предлежание плацента при кровянистых выделений'),
  ('124', 'Предлежание плацента при САД < 90 мм рт ст'),
  ('125', 'Преждевременная отслойка нормально расположенной плаценты'),
  ('126', 'Преждевременная отслойка нормально расположенной плаценты, САД < 90 мм рт ст'),
  ('127', 'Чрезмерная рвота беременных тяжелой степени (рвота более 10 раз в сутки)'),
  ('128', 'Вызванная беременностью гипертензия (гестационная артериальная гипертензия) умеренной и тяжелой АД'),
  ('129', 'Преэклампсия средней и тяжелой тяжести'),
  ('130', 'Эклампсия (при беременности и послеродовом периоде)'),
  ('131', 'Угрожающий разрыв матки'),
  ('132', 'Разрыв матки, САД < 90 мм рт ст'),
  ('133', 'Чума, оспа обезьян'),
  ('134', 'Вирусные лихорадки, передаваемые членистоногими, а также вирусные геморрагические лихорадки'),
  ('135', 'Грипп, при нарушении сознания, ЧДД >= 24 в мин, кровохаркании'),
  ('136', 'Столбняк'),
  ('137', 'Вирусный гипатит при острой печеночной энцефалопатии'),
  ('138', 'Брадиаритмин при ЧСС < 40 в минуту у гипотонии или рецидивирующихся приступах МЭС'),
  ('139', 'Кардиогенный шок'),
  ('140', 'Кардиогенный шок при распространении инфаркта миокарда нижней стенки и заднебазальной локации на правый желудочек'),
  ('141', 'Воспалительные болезни ЦНС'),
  ('142', 'Злокачественный нейролептический синдром'),
  ('143', 'Мигренозный статус'),
  ('144', 'Синдром Гийена-Барре'),
  ('145', 'Миастенический криз'),
  ('146', 'Другие болезни спинного мозга'),
  ('147', 'Инсульт, неуточненный как кровоизлияние или инфаркт мозга при САД < 100 мм рт ст'),
  ('148', 'Инсульт, неуточненный как кровоизлияние или инфаркт мозга при гипоглемии < 10 ммоль/л'),
  ('149', 'Перелом хрящей гортани, трахеи, при САД < 90 мм рт ст'),
  ('150', 'Отсрый синусит'),
  ('151', 'Тяжелые формы алкогольного делирия'),
  ('152', 'Диабетический кетоацидоз'),
  ('153', 'Пневмония при выраженной интоксикацией'),
  ('154', 'Отравление анальгезирующими, жаропонижающими и противоревматическими средствами'),
  ('155', 'Отравление наркотиками группы опия (опиатами и опиоидами) и лоперамидом гидрохлоридом: при ЧДД < 16 в 1 мин'),
  ('156', 'Отравление кокаином, амфетаминами (экстази), галлюциногенами'),
  ('157', 'Отравление психотропными средствами неклассифицированными в других рубриках'),
  ('158', 'Отравление антихолинергическими, антимускаринными и спазмолитическими средствами'),
  ('159', 'Отравление β-адреноблокаторами'),
  ('160', 'Отравление препаратами, действующими преимущественно на сердечно-сосудистую систему'),
  ('161', 'Токсическое действие алкоголя этанола'),
  ('162', 'Токсическое действие метанола, органических растворителей в т.ч. этиленгликоля'),
  ('163', 'Токсическое действие соединений тяжелых металлов'),
  ('164', 'Токсическое действие других неорганических веществ'),
  ('165', 'Токсическое действие окиси углерода, других газов, дымов и паров'),
  ('166', 'Токсическое действие пестицидов, инсектицидов'),
  ('167', 'Токсическое действие других ядовитых веществ, содержащиеся в съеденных пищевых продуктах'),
  ('168', 'Перелом свода и/или основания черепа, ушиб головного мозга, травматическое субарахноидальное кровоизлияние, внутричерепная гематома'),
  ('169', 'Перелом свода и/или основания черепа, ушиб головного мозга, травматическое субарахноидальное кровоизлияние, внутричерепная гематома при снижении САД < 100 мм рт ст'),
  ('170', 'Перелом костей таза'),
  ('171', 'Переломы костей верхних конечностей на уровне плечевого пояса и плеча'),
  ('172', 'Диафиз бедренной кости'),
  ('173', 'Перелом костей голени'),
  ('174', 'Гемоторакс'),
  ('175', 'Ушиб сердца'),
  ('176', 'Ранение сердца'),
  ('177', 'Размножения и отчленения конечностей'),
  ('178', 'Синдром длительного сдавливания'),
  ('179', 'Закрытая травма живота'),
  ('180', 'Открытая травма живота'),
  ('181', 'Трамватическая эвентрация'),
  ('182', 'Травма наружных половых органов при САД < 90 мм рт ст'),
  ('183', 'Клещевой энцефалит'),
  ('184', 'Успешная сердечно-легочная реанимация'),
  ('185', 'Геморрагический шок, САД на 20-30% от возрастной нормы'),
  ('186', 'Геморрагический шок, САД на 35-50% от возрастной нормые'),
  ('187', 'Геморрагический шок, САД > 35-50% от возрастной нормы'),
  ('188', 'Гиповолемичесский шок'),
  ('189', 'Сохранение артериальной гипотензии при анафилактическом шоке'),
  ('190', 'Пневмония при снижении САД > 20% от возрастной нормы'),
  ('191', 'Отравление препаратами нафазолина или ксилометазолина при снижении САД > 20% от возрастной нормы'),
  ('192', 'Геморрагическая болезнь новорожденного при снижении САД до 20% от возрасной нормы'),
  ('193', 'Перелом свода и/или основания черепа, ушиб головного мозга, травматическое субарахноидальное кровоизлияние, внутричерепная гематома: при снижении САД > 20% от возрастной нормы');