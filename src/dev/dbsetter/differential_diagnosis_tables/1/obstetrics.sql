CREATE TABLE IF NOT EXISTS "obstetrics" (
  "id" INTEGER PRIMARY KEY NOT NULL,
  "term" VARCHAR(10) NOT NULL,
  "wdm" VARCHAR(10) NOT NULL,
  "oj" VARCHAR(10)
);

COMMENT ON TABLE public."obstetrics" IS 'Акушерство';
COMMENT ON COLUMN public."obstetrics".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."obstetrics".term IS 'Срок';
COMMENT ON COLUMN public."obstetrics".wdm IS 'ВДМ';
COMMENT ON COLUMN public."obstetrics".oj IS 'ОЖ';

INSERT INTO "obstetrics" ("id", "term", "wdm", "oj") VALUES
  ('1', '12 недель', '2-6', NULL),
  ('2', '16 недель', '10-18', NULL),
  ('3', '20 недель', '18-24', '70-75'),
  ('4', '22 недели', '20-26', '72-78'),
  ('5', '24 недели', '22-27', '75-80'),
  ('6', '26 недель', '24-28', '77-82'),
  ('7', '28 недель', '26-32', '80-85'),
  ('8', '30 недель', '28-33', '82-87'),
  ('9', '32 недели', '30-33', '85-90'),
  ('10', '34 недели', '32-35', '87-92'),
  ('11', '36 недель', '33-38', '90-95'),
  ('12', '38 недель', '36-40', '92-98'),
  ('13', '40 недель', '34-38', '95-100');