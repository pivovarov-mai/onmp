CREATE TABLE IF NOT EXISTS "richmond_arousal_sedation_scale" (
  "id" SERIAL PRIMARY KEY,
  "points" VARCHAR(5) NOT NULL,
  "term" VARCHAR(25),
  "description" VARCHAR(100) NOT NULL
);

COMMENT ON TABLE public."richmond_arousal_sedation_scale" IS 'Шкала возбуждения-седации Ричмонда (Шкала RASS)';
COMMENT ON COLUMN public."richmond_arousal_sedation_scale".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."richmond_arousal_sedation_scale".points IS 'Баллы';
COMMENT ON COLUMN public."richmond_arousal_sedation_scale".term IS 'Термин';
COMMENT ON COLUMN public."richmond_arousal_sedation_scale".description IS 'Описание';

INSERT INTO "richmond_arousal_sedation_scale" ("points", "term", "description") VALUES
  ('+4', 'Агрессивен', 'Больной агрессивен, воинственен, представляет непосредственную опасность для медицинского персонала'),
  ('+3', 'Крайне возбужден', 'Тяне или удаляет катетеры или имеет агрессивное поведение по отношению к медицинскому персоналу'),
  ('+2', 'Возбужден', 'Частные нецеленаправленные движения и/или десинхронизация с аппаратом ИВЛ'),
  ('+1', 'Беспокоен', 'Взволнован, но движения не энергичные и не агрессивные'),
  ('0', NULL, 'Бодрствует, спокоен, внимателен'),
  ('-1', 'Сонлив', 'Потеря внимательности, но при вербальном контакте не закрывает глаза дольше 10 секунд'),
  ('-2', 'Легкая седация', 'При вербальном контакте закрывает глаза меньше, чем через 10 секунд'),
  ('-3', 'Умеренная седация', 'Любое движение (но не зрительный контакт), в ответ на голос'),
  ('-4', 'Глубокая седация', 'Никакой реакции на голос, но есть какие-либо движения на физическую стимуляцию'),
  ('-5', 'Отсутствие пробуждения', 'Никакой реакции на голос и физическую стимуляцию');