SELECT b.author_id, a.author_name, b.category, sum(b.price * bs.sales) TOTAL_SALES
FROM book b
JOIN AUTHOR a ON a.author_id = b.author_id
join book_sales bs on bs.book_id= b.book_id
WHERE year(bs.sales_date)=2022 and month(bs.sales_date)=1
group by author_id, category
order by author_id, category desc
