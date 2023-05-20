CREATE TYPE enum_child_dosages AS ENUM ('age', 'weight', 'mg', 'blob');

CREATE TABLE IF NOT EXISTS "child_dosages" (
  "id" SERIAL PRIMARY KEY,
  "child_dosage" VARCHAR(255) NOT NULL,
  "unit_child_dosage" enum_child_dosages NOT NULL,
  "medicines_id" INTEGER REFERENCES medicines(id) NOT NULL,
  "diag_id" INTEGER REFERENCES diag(id) NOT NULL
);

COMMENT ON TABLE public."child_dosages" IS 'Таблица дозировок для детей';
COMMENT ON COLUMN public."child_dosages".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."child_dosages".child_dosage IS 'Детская дозировка';
COMMENT ON COLUMN public."child_dosages".unit_child_dosage IS 'Параметр возраста или веса';
COMMENT ON COLUMN public."child_dosages".medicines_id IS 'Внешний ключ к таблице Препаратов';
COMMENT ON COLUMN public."child_dosages".diag_id IS 'Внешний ключ к таблице Дагнозов(diag)';

INSERT INTO "child_dosages" ("child_dosage", "unit_child_dosage", "medicines_id", "diag_id") VALUES
  ('0.01-0.02 мг/кг', 'weight', '1', '1'),
  ('30 мг', 'mg', '2', '67'),
  ('0.1 мл/год', 'age', '3', '1'),
  ('4-5 мг/кг', 'weight', '4', '1'),
  ('5 мг/кг', 'weight', '5', '1'),
  ('1 мг', 'mg', '6', '8'),
  ('1 мг', 'mg', '6', '9'),
  ('0.5 мг', 'mg', '6', '10'),
  ('1 мг', 'mg', '6', '11'),
  ('0.5-1 мг', 'mg', '6', '12'),
  ('0.5-1 мг', 'mg', '6', '13'),
  ('0.1 мл/год', 'age', '7', '1'),
  ('0.6 мг/кг', 'weight', '8', '30'),
  ('0.6-1.2 мг/кг', 'weight', '8', '21'),
  ('0.6-1.2 мг/кг', 'weight', '8', '16'),
  ('0.2-0.6 мг/кг', 'weight', '8', '31'),
  ('0.6-1.2 мг/кг', 'weight', '8', '32'),
  ('0.2-0.6 мг/кг', 'weight', '8', '11'),
  ('0.6 мг/кг', 'weight', '8', '33'),
  ('0.6-1.2 мг/кг', 'weight', '8', '34'),
  ('0.2-0.6 мг/кг', 'weight', '8', '12'),
  ('0.6 мг/кг', 'weight', '8', '35'),
  ('0.6 мг/кг', 'weight', '8', '36'),
  ('0.6 мг/кг', 'weight', '8', '98'),
  ('0,1 мг/кг', 'weight', '10', '1'),
  ('1 капля', 'blob', '11', '1'),
  ('0.1 мг/кг', 'weight', '12', '45'),
  ('12.5 мг/кг', 'weight', '13', '1'),
  ('1 мг/кг', 'weight', '14', '1'),
  ('18-20 МЕ/кг/ч', 'weight', '15', '65'),
  ('25-30 МЕ/кг/ч', 'weight', '15', '66'),
  ('10 мг/кг', 'weight', '18', '1'),
  ('0,1-0,15 мг/кг', 'weight', '19', '1'),
  ('0.035 мг/кг', 'weight', '20', '68'),
  ('0.03 мг/кг', 'weight', '20', '69'),
  ('0.025 мг/кг', 'weight', '20', '70'),
  ('0.02 мг/кг', 'weight', '20', '71'),
  ('2 мг/кг', 'weight', '21', '91'),
  ('3-5 мг/кг', 'weight', '21', '30'),
  ('5-10 мг/кг', 'weight', '21', '21'),
  ('10 мг/кг', 'weight', '21', '92'),
  ('3-5 мг/кг', 'weight', '21', '93'),
  ('3-5 мг/кг', 'weight', '21', '8'),
  ('3-5 мг/кг', 'weight', '21', '94'),
  ('3-5 мг/кг', 'weight', '21', '95'),
  ('5-10 мг/кг', 'weight', '21', '96'),
  ('3-5 мг/кг', 'weight', '21', '77'),
  ('3-5 мг/кг', 'weight', '21', '11'),
  ('5 мг/кг', 'weight', '21', '33'),
  ('5-10 мг/кг', 'weight', '21', '34'),
  ('3-5 мг/кг', 'weight', '21', '12'),
  ('3-5 мг/кг', 'weight', '21', '35'),
  ('3-5 мг/кг', 'weight', '21', '36'),
  ('3-5 мг/кг', 'weight', '21', '97'),
  ('5 мг/кг', 'weight', '21', '98'),
  ('3-5 мг/кг', 'weight', '21', '99'),
  ('2 мг/кг', 'weight', '21', '73'),
  ('2.5 мг', 'mg', '22', '100'),
  ('0.4 мл/кг', 'weight', '24', '1'),
  ('10 мг/кг', 'weight', '25', '30'),
  ('10 мг/кг', 'weight', '25', '21'),
  ('10-20 мг/кг', 'weight', '25', '183'),
  ('10-20 мг/кг', 'weight', '25', '184'),
  ('20 мг/кг', 'weight', '25', '185'),
  ('30 мг/кг', 'weight', '25', '186'),
  ('30 мг/кг', 'weight', '25', '187'),
  ('20 мг/кг', 'weight', '25', '188'),
  ('20 мг/кг', 'weight', '25', '92'),
  ('20 мг/кг', 'weight', '25', '108'),
  ('20 мг/кг', 'weight', '25', '189'),
  ('20 мг/кг', 'weight', '25', '94'),
  ('10-20 мг/кг', 'weight', '25', '96'),
  ('5-10 мг/кг', 'weight', '25', '77'),
  ('10 мг/кг', 'weight', '25', '190'),
  ('10-20 мг/кг', 'weight', '25', '34'),
  ('10-20 мг/кг', 'weight', '25', '191'),
  ('10-20 мг/кг', 'weight', '25', '37'),
  ('10 мг/кг', 'weight', '25', '192'),
  ('20 мг/кг', 'weight', '25', '193');