-- O arquivo log.sql documenta todas as consultas SQL executadas para resolver o mistério de Fiftyville.

-- PASSO 1: Obter o relatório do crime para entender os detalhes básicos.
-- O roubo ocorreu em 28 de julho de 2023 na Humphrey Street.
SELECT description
  FROM crime_scene_reports
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND street = 'Humphrey Street';
-- O relatório menciona que o roubo do pato CS50 ocorreu às 10:15.
-- Três testemunhas foram entrevistadas e todas mencionam o "courthouse" (tribunal).


-- PASSO 2: Encontrar as transcrições das entrevistas das testemunhas.
-- Vamos filtrar as entrevistas do dia que mencionam o tribunal.
SELECT name, transcript
  FROM interviews
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND transcript LIKE '%courthouse%';
-- Pistas obtidas das entrevistas:
-- PISTA 1 (de Ruth): O ladrão saiu do estacionamento do tribunal em um carro, em algum momento entre 10:15 e 10:25.
-- PISTA 2 (de Eugene): O ladrão foi visto mais cedo naquela manhã em um caixa eletrônico na Leggett Street, sacando dinheiro.
-- PISTA 3 (de Raymond): O ladrão ligou para alguém por menos de um minuto enquanto saía do tribunal. Ele planejava pegar o primeiro voo para fora de Fiftyville no dia seguinte (29 de julho). O cúmplice na ligação comprou a passagem.


-- PASSO 3: Investigar as pistas para encontrar uma lista de suspeitos.

-- Investigando a PISTA 1 (carro no estacionamento):
-- Encontrar as placas dos carros que saíram do tribunal entre 10:15 e 10:25.
SELECT license_plate
  FROM courthouse_security_logs
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND hour = 10
   AND minute BETWEEN 15 AND 25
   AND activity = 'exit';

-- Investigando a PISTA 2 (saque no caixa eletrônico):
-- Encontrar os números das contas das pessoas que sacaram dinheiro na Leggett Street naquela manhã.
SELECT account_number
  FROM atm_transactions
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND atm_location = 'Leggett Street'
   AND transaction_type = 'withdraw';

-- Investigando a PISTA 3 (voo e ligação):
-- A) Encontrar o ID do primeiro voo de Fiftyville em 29 de julho de 2023.
SELECT id
  FROM flights
 WHERE origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
   AND year = 2023
   AND month = 7
   AND day = 29
 ORDER BY hour, minute
 LIMIT 1;
-- O ID do primeiro voo é 36.

-- B) Encontrar os números de passaporte de todos os passageiros no voo 36.
SELECT passport_number
  FROM passengers
 WHERE flight_id = 36;

-- C) Encontrar os números de telefone de quem fez uma ligação com menos de 60 segundos de duração em 28 de julho.
SELECT caller
  FROM phone_calls
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND duration < 60;


-- PASSO 4: Cruzar todas as pistas para encontrar o ladrão.
-- Agora, vamos encontrar a pessoa que aparece em todas as listas de evidências.
SELECT p.name
  FROM people p
  JOIN courthouse_security_logs csl ON p.license_plate = csl.license_plate
  JOIN bank_accounts ba ON p.id = ba.person_id
  JOIN atm_transactions at ON ba.account_number = at.account_number
  JOIN passengers ps ON p.passport_number = ps.passport_number
  JOIN phone_calls pc ON p.phone_number = pc.caller
 WHERE csl.year = 2023
   AND csl.month = 7
   AND csl.day = 28
   AND csl.hour = 10
   AND csl.minute BETWEEN 15 AND 25
   AND csl.activity = 'exit'
   AND at.year = 2023
   AND at.month = 7
   AND at.day = 28
   AND at.atm_location = 'Leggett Street'
   AND at.transaction_type = 'withdraw'
   AND ps.flight_id = 36
   AND pc.year = 2023
   AND pc.month = 7
   AND pc.day = 28
   AND pc.duration < 60;
-- A consulta retorna um único nome: Bruce.
-- O LADRÃO É: Bruce


-- PASSO 5: Identificar a cidade para a qual o ladrão escapou.
-- Usamos o ID do voo (36) para encontrar o aeroporto de destino.
SELECT city
  FROM airports
 WHERE id = (SELECT destination_airport_id FROM flights WHERE id = 36);
-- A CIDADE DE DESTINO É: New York City


-- PASSO 6: Identificar o cúmplice.
-- O cúmplice foi a pessoa que recebeu a ligação de Bruce.
SELECT p.name
  FROM people p
  JOIN phone_calls pc ON p.phone_number = pc.receiver
 WHERE pc.year = 2023
   AND pc.month = 7
   AND pc.day = 28
   AND pc.duration < 60
   AND pc.caller = (SELECT phone_number FROM people WHERE name = 'Bruce');
-- A consulta retorna um único nome: Robin.
-- O CÚMPLICE É: Robin
