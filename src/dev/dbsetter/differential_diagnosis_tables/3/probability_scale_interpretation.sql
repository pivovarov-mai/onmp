CREATE TABLE IF NOT EXISTS "probability_scale_interpretation" (
  "id" SERIAL PRIMARY KEY,
  "sum" INTEGER,
  "probability" VARCHAR(7) NOT NULL
);

COMMENT ON TABLE public."probability_scale_interpretation" IS 'Шкала оценки вероятности ТЭЛА (Revised Geneva Score) - Интерпретация';
COMMENT ON COLUMN public."probability_scale_interpretation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."probability_scale_interpretation".sum IS 'Сумма баллов';
COMMENT ON COLUMN public."probability_scale_interpretation".probability IS 'Клиническая вероятность';

INSERT INTO "probability_scale_interpretation" ("sum", "probability") VALUES
  ('25', 'Высокая'),
  ('24', 'Высокая'),
  ('23', 'Высокая'),
  ('22', 'Высокая'),
  ('21', 'Высокая'),
  ('20', 'Высокая'),
  ('19', 'Высокая'),
  ('18', 'Высокая'),
  ('17', 'Высокая'),
  ('16', 'Высокая'),
  ('15', 'Высокая'),
  ('14', 'Высокая'),
  ('13', 'Высокая'),
  ('12', 'Высокая'),
  ('11', 'Высокая'),
  ('10', 'Средняя'),
  ('9', 'Средняя'),
  ('8', 'Средняя'),
  ('7', 'Средняя'),
  ('6', 'Средняя'),
  ('5', 'Средняя'),
  ('4', 'Средняя'),
  ('3', 'Низкая'),
  ('2', 'Низкая'),
  ('1', 'Низкая'),
  ('0', 'Низкая');