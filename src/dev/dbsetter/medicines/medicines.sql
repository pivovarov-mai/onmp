CREATE TYPE enum_medicines AS ENUM ('ml', 'mg', 'blob', 'ME');

CREATE TABLE IF NOT EXISTS "medicines" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "name" VARCHAR(50) NOT NULL,
  "name_genitive" VARCHAR(50) NOT NULL,
  "unit" enum_medicines NOT NULL
);

COMMENT ON TABLE public."medicines" IS 'Лекартсвенные препараты (медикаменты)';
COMMENT ON COLUMN public."medicines".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."medicines".name IS 'Название препарата';
COMMENT ON COLUMN public."medicines".name IS 'Название препарата в родительном падеже';
COMMENT ON COLUMN public."medicines".unit IS 'Единица измерения дозировки препарата';

INSERT INTO "medicines" ("id", "name", "name_genitive", "unit") VALUES
  ('1', 'S. Atropinum 1 mg/ml', 'S. Atropini 1 mg/ml', 'mg'),
  ('2', 'S. Ketorolacum 30 mg/ml', 'S. Ketorolaci 30 mg/ml', 'mg'),
  ('3', 'S. Drotaverinum 20 mg/ml', 'S. Drotaverini 20 mg/ml', 'mg'),
  ('4', 'S. Aminophyllinum 24 mg/ml', 'S. Aminophyllini 24 mg/ml', 'mg'),
  ('5', 'S. Amiodaronum 50 mg/ml', 'S. Amiodaroni 50 mg/ml', 'mg'),
  ('6', 'Susp. Budesonidum 0.5 mg/ml', 'Susp. Budesonidi 0.5 mg/ml', 'mg'),
  ('7', 'S. Chloropyraminum 20 mg/ml', 'S. Chloropyramini 20 mg/ml', 'mg'),
  ('8', 'S. Dexametasonum 4 mg/ml', 'S. Dexametasoni 4 mg/ml', 'mg'),
  ('9', 'S. Dextrosum 40%', 'S. Dextrosae 40%', 'ml'),
  ('10', 'S. Diphenhydraminum 10 mg/ml', 'S. Diphenhydramini 10 mg/ml', 'mg'),
  ('11', 'S. Dorzolamidum 20 mg/ml', 'S. Dorzolamidi 20 mg/ml', 'blob'),
  ('12', 'S. Epinephrinum 1 mg/ml', 'S. Epinephrini 1 mg/ml', 'mg'),
  ('13', 'Sol. Etamsylatum 125 mg/ml', 'Sol. Etamsylati 125 mg/ml', 'mg'),
  ('14', 'S. Furosemidum 10 mg/ml', 'S. Furosemidi 10 mg/ml', 'mg'),
  ('15', 'S. Heparinum natrium 5000 ME/ml', 'S. Heparini natrii 5000 ME/ml', 'ME'),
  ('16', 'S. Isosorbidi dinitras 1.25 mg/ml', 'S.Isosorbidi dinitratis 1.25 mg/ml', 'mg'),
  ('17', 'S. Ketoprofenum 0.05/ml', 'S. Ketoprofeni 0.05/ml', 'mg'),
  ('18', 'S. Metamizolum natrium 500 mg/ml', 'S. Metamizoli natrii 500 mg/ml', 'mg'),
  ('19', 'S. Metoclopramidum 5 mg/ml', 'S. Metoclopramidi 5 mg/ml', 'mg'),
  ('20', 'S. Platyphyllinum 2 mg/ml', 'S. Platyphyllini 2 mg/ml', 'mg'),
  ('21', 'S. Prednisolonum 30 mg/ml', 'S. Prednisoloni 30 mg/ml', 'mg'),
  ('22', 'S. Salbutamolum 1 mg/ml', 'S. Salbutamoli 1 mg/ml', 'mg'),
  ('23', 'S. Urapidilum 5 mg/ml', 'S. Urapidili 5 mg/ml', 'mg'),
  ('24', 'S. Verapamilum 2.5 mg/ml', 'S. Verapamili 2.5 mg/ml', 'mg'),
  ('25', 'S. Natrii chloridum 0.9%', 'S. Natrii chloridi 0.9%', 'mg');