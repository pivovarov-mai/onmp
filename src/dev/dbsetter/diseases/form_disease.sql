-- Формы --
CREATE TABLE IF NOT EXISTS "form_disease" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name_form_disease" TEXT NOT NULL,
  "description_form_disease" TEXT
);

COMMENT ON TABLE public."form_disease" IS 'Формы заболевания';
COMMENT ON COLUMN public."form_disease".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."form_disease".name_form_disease IS 'Название формы заболевания';
COMMENT ON COLUMN public."form_disease".description_form_disease IS 'Описание формы заболевания';

INSERT INTO "form_disease" ("id", "name_form_disease", "description_form_disease") VALUES
  ('1', 'Типичная форма', NULL),
  ('2', 'Паралитическая форма («тихое бешенство»)', 'Медленное прогрессирование параличей. Без мозжечковых нарушений, возбуждения, водобоязни.'),
  ('3', 'Среднетяжелая форма', NULL),
  ('4', 'Тяжелая форма', NULL),
  ('5', 'Гипертоксическая форма', NULL),
  ('6', 'Бубонная', NULL),
  ('7', 'Легочная', NULL),
  ('8', 'Кишечная', NULL),
  ('9', 'Септическая', NULL),
  ('10', 'Кожная', NULL),
  ('11', 'Карбункулезная', NULL),
  ('12', 'Септическая', NULL),
  ('13', 'Желудочно-кишечная', NULL),
  ('14', 'По продолжительности нарушения ритма: Пароксизмальная форма', 'Длительность до 7 дней, проходит самостоятельно. Пароксизмальная форма мерцательной аритмии, мерцание-трепетание предсердий, давность пароксизма до 2 сут. — это нарушение ритма сердца, полностью дезорганизованная электрическая и механическая работа предсердий с частотой крупных или мелких волн мерцания >350/мин.'),
  ('15', 'По продолжительности нарушения ритма: Персистирующая форма', 'длительность >7 дней, самостоятельно не проходит.'),
  ('16', 'По продолжительности нарушения ритма: Постоянная форма.', 'Постоянная форма мерцательной аритмии, мерцание-трепетание предсердий,  давность пароксизма более 2 сут. — это нарушение ритма сердца, полностью дезорганизованная электрическая и механическая работа предсердий с частотой крупных или мелких волн мерцания >350/мин.'),
  ('17', 'По ЧСС: Пароксизмальная форма', 'ЧСС >150 уд./мин.'),
  ('18', 'По ЧСС: Тахисистолическая форма', 'ЧСС >80 уд./мин.'),
  ('19', 'По ЧСС: Нормосистолическая форма', 'ЧСС 60-80 уд./мин.'),
  ('20', 'По ЧСС: Брадисистолическая форма', 'ЧСС <60 уд./мин.'),
  ('21', 'По ЭКГ-признакам: Крупноволновая форма ФП', 'Амплитуда ff-волн >0,5 мВ, частота волн — 350-450/мин.'),
  ('22', 'По ЭКГ-признакам: Средневолновая форма ФП', 'Амплитуда ff-волн <0,5 мВ, частота волн - 500-700/мин.'),
  ('23', 'По ЭКГ-признакам: Мелковолновая форма ФП', 'Трудноразличимые ff-волны.'),
  ('24', 'Абдоминальная форма', 'Симптомы инфаркта представлены болями в верхней части живота, икотой, вздутием живота, тошнотой, рвотой. В данном случае симптомы инфаркта могут напоминать симптомы острого панкреатита.'),
  ('25', 'Астматическая форма', 'Симптомы инфаркта представлены нарастающей одышкой и напоминают симптомы приступа бронхиальной астмы.'),
  ('26', 'Атипичный болевой синдром', 'Атипичный болевой синдром при инфаркте может быть представлен болями, локализованными не в груди, а в руке, плече, нижней челюсти, подвздошной ямке.'),
  ('27', 'Безболевая ишемия миокарда', 'Наблюдается редко. Такое развитие инфаркта наиболее характерно для больных сахарным диабетом, у которых нарушение чувствительности является одним из проявлений болезни (диабета).'),
  ('28', 'Церебральная форма', 'Симптомы инфаркта представлены головокружениями, нарушениями сознания, неврологическими симптомами.'),
  ('29', 'Ранние осложнения (первые часы - первые 3-4 дня)', NULL),
  ('30', 'Поздние осложнения (2-3-я недели)', NULL),
  ('31', 'Остро развившийся ангинозный приступ загрудинной или атипичной локализации', NULL),
  ('32', 'Криз гипертонический, гиперкинетический', 'Это внезапно возникающее у больного гипертонической болезнью или симптоматической гипертензией резкое повышение АД, преимущественно систолического (САД).'),
  ('33', 'Криз гипертонический, гипокинетический', 'Это медленно развивающееся у больного гипертонической болезнью или симптоматической гипертензией повышение АД, преимущественно диастолического (ДАД).'),
  ('34', 'Стенокардия стабильная', 'Это кратковременный клинический синдром, характеризующийся загрудинными болями, возникающими в результате преходящей недостаточности коронарного кровообращения; характерные признаки стабильной стенокардии - привычные для больного условия возникновения болей, их локализация, характер и условия купирования, длительность от секунд до нескольких минут.'),
  ('35', 'Стенокардия нестабильная', 'Это промежуточный период между стабильным течением ИБС и угрозой развития ИМ. Впервые возникшей стенокардия считается в течение 4—6 нед. с момента первого болевого приступа.'),
  ('36', 'Инфаркт миокарда с подъемом сегмента SТ.', NULL),
  ('37', 'Инфаркт миокарда без подъема SТ.', NULL),
  ('38', 'Инфаркт миокарда, установленный по изменению активности кардиоферментов (кардиомаркеров) и поздним ЭКГ-признакам.', NULL),
  ('39', 'Нестабильная стенокардия.', NULL),
  ('40', 'Тахикардия пароксизмальная, наджелудочковая', 'Тахикардия пароксизмальная наджелудочковая — внезапное резкое учащение ЧСС до 140-250 уд./мин в результате появления эктопического очага автоматизма или кругового возвратного возбуждения re-entry в атриовентрикулярном соединении, миокарде предсердий, синусно-предсердном узле.'),
  ('41', 'Тахикардия пароксизмальная, желудочковая', 'Тахикардия пароксизмальная желудочковая (однонаправленная. полиморфная, веретенообразная, типа пируэт - TORSADES DE POINTES) — это угрожающая жизни аритмия в виде внезапно начинающихся и так же внезапно прекращающихся приступов сердцебиения с сохранением правильной последовательности сердечных сокращений, обусловленная активностью необычных (гетеротопных) очагов возбуждения, которые подавляют нормальный (синусовый) водитель ритма.'),
  ('42', 'Переходящее (динамическое) нарушение мозгового кровообращения', 'Неврологическая симптоматика (неврологический дефицит) и/или общемозговые нарушения, с полным восстановлением нарушенных функций в течение 24 ч.'),
  ('43', 'Обратимый неврологический дефицит', 'Неврологическая симптоматика (неврологический дефицит) в результате острого нарушения церебральной циркуляции, при котором нарушенные функции восстанавливаются от 24 ч до 3 недель.'),
  ('44', 'Инсульт', 'Неврологическая симптоматика (неврологический дефицит) в результате острого нарушения церебральной циркуляции, при котором нарушенные функции сохраняются более 3 недель.'),
  ('45', 'Эпилептический (судорожный) припадок', 'Это внезапно возникающее, обычно многократно повторяющееся болезненное состояние, характеризующееся потерей сознания, сопровождающееся судорогами.'),
  ('46', 'Генерализованный припадок с тонико-клоническими судорогами', 'Это состояние, при котором эпилептический припадок сопровождается генерализованными тонико-клоническими судорогами.'),
  ('47', 'Эпилептический статус', 'Это состояние, при котором эпилептические припадки следуют один за другим (обычно более 30 мин) и в промежутках между припадками больной не приходит в сознание.'),
  ('48', 'Бронхиальная астма, легкая степень тяжести', 'Это эпизодические приступы нарушения дыхания, с затрудненным выдохом, возникающие днем >1 раза в неделю, ночные – >2 раз в месяц, у больных, страдающих бронхиальной астмой (ДН 0–II ст.).'),
  ('49', 'Бронхиальная астма, средняя степень тяжести', 'Это приступы резко выраженного нарушения дыхания, с затрудненным выдохом, возникающие днем – ежедневно, ночные – 1 раз в неделю, у больных, страдающих бронхиальной астмой (ДН 0–II ст.).'),
  ('50', 'Бронхиальная астма, тяжелая степень тяжести', 'Это тяжелые ежедневные приступы нарушения дыхания, с затрудненным выдохом, вызывающие ограничение физической активности, возникающие днем — ежедневно, ночные - более 1 раза в неделю, у больных, страдающих бронхиальной астмой (ДН III-IV ст.).'),
  ('51', '1 стадия', NULL),
  ('52', '2 стадия', NULL),
  ('53', '3 стадия - «атоническая»', NULL),
  ('54', '4 стадия - запредельная', NULL),
  ('55', 'Легкая степень', NULL),
  ('56', 'Средняя степень', NULL),
  ('57', 'Тяжелая степень', 'Развивается внезапно.'),
  ('58', '1 тип', NULL),
  ('59', '2 тип', NULL),
  ('60', '1-я степень - ранняя фаза (шоковый индекс - 0,7-1,0)', NULL),
  ('61', '2-я степень - фаза выраженного шока (шоковый индекс - 1,0-1,4)', NULL),
  ('62', '3-я степень - фаза декомпенсированного шока (шоковый индекс - 1,5)', NULL),
  ('63', '4-я степень - поздняя стадия шока (шоковый индекс >1,5)', NULL),
  ('64', 'Электротравма, вызванная электрическим током НИЗКОГО напряжения (<1000 В)', 'Это травма, вызванная воздействием на организм и ткани электрического тока большой силы или напряжения, в том числе молнии, характеризуется поражением нервной системы (судороги, потеря сознания), нарушениями кровообращения и дыхания, глубокими ожогами.'),
  ('65', 'Электротравма, вызванная электрическим током ВЫСОКОГО напряжения (>1000 В)', 'Это электротравмы, полученные на линиях высоковольтных передач, трансформаторных подстанциях, в промышленных зонах.'),
  ('66', 'Период компрессии', NULL),
  ('67', 'Посткомпрессионный период', 'В течение 72 ч после освобождения от сдавления (помощь в стационаре) - период локальных изменений и эндогенной интоксикации, признаки травматического шока.'),
  ('68', 'Закрытые повреждения почки', NULL),
  ('69', 'Открытые повреждения почки', NULL),
  ('70', 'Травма живота закрытая (тупая)', 'Травма живота закрытая (тупая) — это травма живота без нарушения целостности наружных покровов тела и сопровождающаяся тяжелыми повреждениями органов брюшной полости (разрывы органов, кровотечения, инфицирование, перитонит) и развитием травматического шока.'),
  ('71', 'Травма живота открытая (ранения брюшной полости проникающие, эвентрация травматическая)', 'Травма живота открытая (ранения брюшной полости проникающие, эвентрация травматическая) — это раны, проникающие через брюшную стенку и повреждающие органы брюшной полости, преимущественно кишечник, проявляющиеся выпадением через раневое отверстие на поверхность тела внутренних органов, чаще петель кишечника (эвентрация) и осложняющиеся развитием шока.'),
  ('72', 'Сотрясение сердца', 'Клинические проявления наблюдаются сразу после травмы.'),
  ('73', 'Ожоги 1 степени', 'Это повреждения клеток рогового слоя кожи (покраснение обожженных участков кожи, их отек и жгучая боль).'),
  ('74', 'Ожоги 2 степени', 'Полное повреждение рогового слоя кожи (резкая боль, сильное покраснение обожженной кожи, пузыри с прозрачным желтоватым содержимым).'),
  ('75', 'Ожоги 3 степени', 'Корочки-струпы: повреждаются глубокие слои кожи.'),
  ('76', 'Ожог 3А степени', 'Кожа омертвевает не на всю толщину, ее нижние слои сохраняются.'),
  ('77', 'Ожог 3Б степени', 'кожа омертвевает на всю толщину и все слои гибнут.'),
  ('78', 'Ожоги 4 степени', 'Обугливание кожи, подкожной клетчатки и подлежащих тканей.'),
  ('79', '1 степень', 'Адинамическая: озноб, усталость, сонливость, апатия, жажда; движения пассивны; кожные покровы бледные или синюшные, «гусиная кожа»; скандированная речь; снижение ректальной температуры до 33-35°С.'),
  ('80', '2 степень', 'Средняя (ступорозная): угнетение сознания, отсутствие мимики; ограниченность движений; пульс 32-50 уд./мин, слабого наполнения; ректальная температура 30-33°С.'),
  ('81', '3 степень (тяжелая, судорожная)', 'Отсутствие сознания; судороги, может быть прикусывание языка; верхние конечности согнуты в локтевых суставах; нижние конечности полусогнуты; напряжение мышц живота; ЧСС <36 уд./мин. Т - 29°С. ЧДД до 3—4/мин, дыхание поверхностное, прерывистое. Сужение зрачков, реакция их на свет слабая.'),
  ('82', '1 степень', 'Кожные покровы отечные и бледным.'),
  ('83', '2 степень', 'Пузыри, наполненные прозрачным экссудатом.'),
  ('84', '3 степень', 'Пузыри, содержащие геморрагический экссудат.'),
  ('85', '4 степень', 'Темные, дряблые пузыри.'),
  ('86', 'Разрыв варикозных вен пищевода; массивное кровотечение из язвы желудка; синдром Мэллори-Вейса', NULL),
  ('87', 'Кровотечение из язвы желудка или двенадцатиперстной кишки и другие причины кровотечения в желудке', NULL),
  ('88', 'Кровотечение в пищеводе, желудке или двенадцатиперстной кишке; в тонкой кишке', NULL),
  ('89', 'Кровотечение в слепой или восходящей толстой кишке', NULL),
  ('90', 'Кровотечение в нисходящей или сигмовидной кишке', NULL),
  ('91', 'Геморроидальное кровотечение или кровотечение из анальной трещины', NULL),
  ('92', '1 степень', NULL),
  ('93', '2 степень', NULL),
  ('94', '3 степень', NULL),
  ('95', '4 степень', NULL);