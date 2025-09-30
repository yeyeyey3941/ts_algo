-- 코드를 입력하세요
SELECT 
        order_id,product_id,date_format(out_date,"%Y-%m-%d"),
        if(date(out_date) <= '2022-05-01',"출고완료",
          if(date(out_date) is null, "출고미정","출고대기")) as 출고여부
FROM 
        FOOD_ORDER
ORDER BY
        order_id
