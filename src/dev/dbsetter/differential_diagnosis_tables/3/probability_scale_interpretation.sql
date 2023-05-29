CREATE TABLE IF NOT EXISTS "probability_scale_interpretation" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "sum" INTEGER NOT NULL,
  "probability" VARCHAR(7) NOT NULL
);

COMMENT ON TABLE public."probability_scale_interpretation" IS 'Шкала оценки вероятности ТЭЛА (Revised Geneva Score) - Интерпретация';
COMMENT ON COLUMN public."probability_scale_interpretation".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."probability_scale_interpretation".sum IS 'Сумма баллов';
COMMENT ON COLUMN public."probability_scale_interpretation".probability IS 'Клиническая вероятность';

INSERT INTO "probability_scale_interpretation" ("id", "sum", "probability") VALUES
  ('1', '25', 'Высокая'),
  ('2', '24', 'Высокая'),
  ('3', '23', 'Высокая'),
  ('4', '22', 'Высокая'),
  ('5', '21', 'Высокая'),
  ('6', '20', 'Высокая'),
  ('7', '19', 'Высокая'),
  ('8', '18', 'Высокая'),
  ('9', '17', 'Высокая'),
  ('10', '16', 'Высокая'),
  ('11', '15', 'Высокая'),
  ('12', '14', 'Высокая'),
  ('13', '13', 'Высокая'),
  ('14', '12', 'Высокая'),
  ('15', '11', 'Высокая'),
  ('16', '10', 'Средняя'),
  ('17', '9', 'Средняя'),
  ('18', '8', 'Средняя'),
  ('19', '7', 'Средняя'),
  ('20', '6', 'Средняя'),
  ('21', '5', 'Средняя'),
  ('22', '4', 'Средняя'),
  ('23', '3', 'Низкая'),
  ('24', '2', 'Низкая'),
  ('25', '1', 'Низкая'),
  ('26', '0', 'Низкая');