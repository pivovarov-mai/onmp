CREATE TABLE IF NOT EXISTS "adult_dosages" (
  "id" SERIAL PRIMARY KEY NOT NULL,
  "adult_dosage" VARCHAR(255) NOT NULL,
  "medicines_id" INTEGER REFERENCES medicines(id) NOT NULL,
  "diag_id" INTEGER REFERENCES diag(id) NOT NULL
);

COMMENT ON TABLE public."adult_dosages" IS 'Таблица дозировок для взрослых';
COMMENT ON COLUMN public."adult_dosages".id IS 'Уникальный идентификатор';
COMMENT ON COLUMN public."adult_dosages".adult_dosage IS 'Взрослая дозировка';
COMMENT ON COLUMN public."adult_dosages".medicines_id IS 'Внешний ключ к таблице препаратов';
COMMENT ON COLUMN public."adult_dosages".diag_id IS 'Внешний ключ к таблице диагнозов(diag)';

INSERT INTO "adult_dosages" ("adult_dosage", "medicines_id", "diag_id") VALUES
  ('0.5-1 мг', '1', '1'),
  ('30 мг', '2', '1'),
  ('40 мг', '3', '1'),
  ('240 мг', '4', '1'),
  ('300 мг', '5', '2'),
  ('300-450 мг', '5', '3'),
  ('150-300 мг', '5', '4'),
  ('150-300 мг', '5', '5'),
  ('300-600 мг', '5', '6'),
  ('150-300 мг', '5', '7'),
  ('1-2 мг', '6', '1'),
  ('20 мг', '7', '1'),
  ('16 мг', '8', '14'),
  ('16 мг', '8', '15'),
  ('12-16 мг', '8', '16'),
  ('8 мг', '8', '17'),
  ('16-20 мг', '8', '18'),
  ('8-16 мг', '8', '19'),
  ('8-16 мг', '8', '20'),
  ('8-12 мг', '8', '21'),
  ('8 мг', '8', '22'),
  ('8 мг', '8', '23'),
  ('8 мг', '8', '24'),
  ('8 мг', '8', '25'),
  ('8 мг', '8', '26'),
  ('8 мг', '8', '27'),
  ('8 мг', '8', '28'),
  ('12 мг', '8', '29'),
  ('20-50 мл', '9', '38'),
  ('20-40 мл', '9', '39'),
  ('20-60 мл', '9', '40'),
  ('40-60 мл', '9', '41'),
  ('40-60 мл', '9', '42'),
  ('50-100 мл', '9', '43'),
  ('20 мл', '9', '44'),
  ('10 мг', '10', '1'),
  ('1 капля', '11', '1'),
  ('1 мг', '12', '45'),
  ('0.5 мг', '12', '1'),
  ('500 мг', '13', '46'),
  ('500 мг', '13', '47'),
  ('500 мг', '13', '48'),
  ('250 мг', '13', '49'),
  ('250 мг', '13', '50'),
  ('250-500 мг', '13', '51'),
  ('250-500 мг', '13', '52'),
  ('250-500 мг', '13', '53'),
  ('250-500 мг', '13', '54'),
  ('250-500 мг', '13', '22'),
  ('250-500 мг', '13', '23'),
  ('250-500 мг', '13', '55'),
  ('250-500 мг', '13', '56'),
  ('250-500 мг', '13', '57'),
  ('40 мг', '14', '58'),
  ('40-80 мг', '14', '59'),
  ('20 мг', '14', '60'),
  ('120-160 мг', '14', '60'),
  ('60-100 мг', '14', '61'),
  ('40-120 мг', '14', '62'),
  ('40 мг', '14', '63'),
  ('5000 МЕ', '15', '1'),
  ('10 мг', '16', '1'),
  ('100 мг', '17', '1'),
  ('1000 мг', '18', '1'),
  ('10 мг', '19', '1'),
  ('2 мг', '20', '1'),
  ('120 мг', '21', '15'),
  ('90-120 мг', '21', '16'),
  ('60 мг', '21', '17'),
  ('120-150 мг', '21', '18'),
  ('90-120 мг', '21', '72'),
  ('120-150 мг', '21', '21'),
  ('60-90 мг', '21', '73'),
  ('60 мг', '21', '28'),
  ('90-120 мг', '21', '74'),
  ('60-90 мг', '21', '75'),
  ('60-90 мг', '21', '76'),
  ('90-150 мг', '21', '77'),
  ('90 мг', '21', '78'),
  ('90 мг', '21', '79'),
  ('90 мг', '21', '80'),
  ('60-90 мг', '21', '81'),
  ('90 мг', '21', '82'),
  ('90 мг', '21', '83'),
  ('60-90 мг', '21', '84'),
  ('60-90 мг', '21', '85'),
  ('90-120 мг', '21', '86'),
  ('120 мг', '21', '87'),
  ('90-120 мг', '21', '88'),
  ('90 мг', '21', '89'),
  ('90 мг', '21', '29'),
  ('150 мг', '21', '90'),
  ('2.5 мг', '22', '1'),
  ('12.5-25 мг', '23', '101'),
  ('25 мг', '23', '102'),
  ('12.5-25 мг', '23', '103'),
  ('12.5-25 мг', '23', '104'),
  ('12.5-25 мг', '23', '105'),
  ('12.5-25 мг', '23', '50'),
  ('10-50 мг', '23', '28'),
  ('5-10 мг', '24', '1'),
  ('500 мг', '25', '106'),
  ('250 мг', '25', '107'),
  ('500 мг', '25', '108'),
  ('500 мг', '25', '109'),
  ('500-1000 мг', '25', '110'),
  ('1000 мг', '25', '111'),
  ('500-1000 мг', '25', '16'),
  ('250-500 мг', '25', '112'),
  ('500 мг', '25', '113'),
  ('250-500 мг', '25', '17'),
  ('250-500 мг', '25', '114'),
  ('250-500 мг', '25', '18'),
  ('500-1000 мг', '25', '115'),
  ('500-1000 мг', '25', '116'),
  ('250-500 мг', '25', '117'),
  ('500-1000 мг', '25', '118'),
  ('250-500 мг', '25', '47'),
  ('500-1000 мг', '25', '119'),
  ('500-1000 мг', '25', '120'),
  ('500-1000 мг', '25', '121'),
  ('250-500 мг', '25', '122'),
  ('250-500 мг', '25', '123'),
  ('500-1000 мг', '25', '124'),
  ('250-500 мг', '25', '125'),
  ('500-1000 мг', '25', '126'),
  ('250-500 мл', '25', '127'),
  ('250 мг', '25', '128'),
  ('250 мг', '25', '129'),
  ('250 мг', '25', '130'),
  ('250 мг', '25', '131'),
  ('500-1000 мг', '25', '132'),
  ('500-1000 мг', '25', '48'),
  ('500 мг', '25', '133'),
  ('500-1000 мг', '25', '134'),
  ('500 мг', '25', '72'),
  ('400 мг', '25', '19'),
  ('500 мг', '25', '135'),
  ('500 мг', '25', '136'),
  ('500 мг', '25', '137'),
  ('250 мг', '25', '138'),
  ('500 мг', '25', '139'),
  ('500 мг', '25', '140'),
  ('250 мг', '25', '141'),
  ('500 мг', '25', '142'),
  ('250 мг', '25', '143'),
  ('250 мг', '25', '144'),
  ('250 мг', '25', '145'),
  ('250 мг', '25', '146'),
  ('500 мг', '25', '147'),
  ('250 мг', '25', '148'),
  ('250 мг', '25', '52'),
  ('500 мг', '25', '149'),
  ('500 мг', '25', '150'),
  ('250 мг', '25', '151'),
  ('500 мг', '25', '152'),
  ('500 мг', '25', '153'),
  ('500 мг', '25', '80'),
  ('500 мг', '25', '154'),
  ('500 мг', '25', '155'),
  ('500 мг', '25', '156'),
  ('500 мг', '25', '157'),
  ('500 мг', '25', '158'),
  ('500 мг', '25', '159'),
  ('500 мг', '25', '160'),
  ('500 мг', '25', '161'),
  ('500-1000 мг', '25', '162'),
  ('250 мг', '25', '86'),
  ('500-1000 мг', '25', '163'),
  ('500-1000 мг', '25', '164'),
  ('500-1000 мг', '25', '165'),
  ('500-1000 мг', '25', '166'),
  ('500 мг', '25', '167'),
  ('500-1000 мг', '25', '29'),
  ('500 мг', '25', '44'),
  ('250 мг', '25', '168'),
  ('250-500 мг', '25', '169'),
  ('250 мг', '25', '90'),
  ('500 мг', '25', '170'),
  ('500 мг', '25', '171'),
  ('500 мг', '25', '172'),
  ('500 мг', '25', '173'),
  ('500 мг', '25', '174'),
  ('500 мг', '25', '175'),
  ('250 мг', '25', '176'),
  ('500 мг', '25', '177'),
  ('500 мг', '25', '178'),
  ('250-500 мг', '25', '179'),
  ('500 мг', '25', '180'),
  ('500 мг', '25', '181'),
  ('500 мг', '25', '182');