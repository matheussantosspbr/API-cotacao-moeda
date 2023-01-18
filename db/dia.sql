SELECT 
    id,
    USD_BRL,
    BRL_USD,
    EUR_BRL,
    BRL_EUR,
    EUR_USD,
    USD_EUR,
    FROM_UNIXTIME(timestamp) as timestamp
 FROM
     precos  
WHERE
    DATE(FROM_UNIXTIME(timestamp)) = DATE_SUB(DATE(NOW()), INTERVAL 1 DAY);


-- MÉDIA

SELECT 
    AVG(USD_BRL) as USD_BRL,
    AVG(BRL_USD) as BRL_USD,
    AVG(EUR_BRL) as EUR_BRL,
    AVG(BRL_EUR) as BRL_EUR,
    AVG(EUR_USD) as EUR_USD,
    AVG(USD_EUR) as USD_EUR
 FROM
     precos  
WHERE
    DATE(FROM_UNIXTIME(timestamp)) = DATE_SUB(DATE(NOW()), INTERVAL 1 DAY);

DELETE FROM precos WHERE DATE(FROM_UNIXTIME(timestamp)) = DATE(DATE_SUB(NOW(), INTERVAL 1 DAY));