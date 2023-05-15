CREATE TABLE IF NOT EXISTS "parameters_clr" (
  "id" SERIAL PRIMARY KEY,
  "stage" VARCHAR(55) NOT NULL,
  "adults_and_children" VARCHAR(220) NOT NULL,
  "children" VARCHAR(250) NOT NULL,
  "newborns" VARCHAR(160) NOT NULL
);

COMMENT ON TABLE public."parameters_clr" IS 'Параметры проведения базовой СЛР';
COMMENT ON COLUMN public."parameters_clr".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."parameters_clr".stage IS 'Этап';
COMMENT ON COLUMN public."parameters_clr".adults_and_children IS 'Взрослые и дети старше 14 лет';
COMMENT ON COLUMN public."parameters_clr".children IS 'Дети';
COMMENT ON COLUMN public."parameters_clr".newborns IS 'Новорожденные при рождении';

INSERT INTO "parameters_clr" ("stage", "adults_and_children", "children", "newborns") VALUES
  ('ДО применения ларингеальной трубки или интубации трахеи', 'Непрямой массаж сердца 100 компрессий в минуту. ИВЛ дыхательным мешком 30 компрессий : 2 вдоха', 'Начать ИВЛ 5 вдохов мешком, затем ИВЛ мешком 15:2 вне зависимости от количества реанимирующих. Непрямой массаж сердца 100-110 компрессий в минуту независимо от возраста', 'ИВЛ дыхательным мешком в соотношении 3:1. Непрямой массаж сердца 120 компрессий в минуту'),
  ('ПОСЛЕ применения ларингеальной трубки интубации трахеи', 'Непрямой массаж сердца 100 компрессий в минуту с перерывами только на DEFIBRILL. ИВЛ мешком или аппаратная ИВЛ независимо от массажа сердца ДО 6 мл/кг, ЧД = 10 в минуту, 100% кислород, с перерывами только на DEFIBRILL', 'Непрямой массаж сердца 100-110 компрессий в минуту независимо от возраста, с перерывами только на DEFIBRILL. ИВЛ мешком или аппаратная ИВЛ независимо от массажа сердца ДО 6 мл/кг, ЧД = 12-30 в минуту, 100% кислород, с перерывами только на DEFIBRILL', 'Непрямой массаж сердца 120 компрессий в минуту непрерывно. ИВЛ мешком с подключением 30-50% кислорода, ЧД = 30 в минуту. Независимо от непрямого массажа сердца');