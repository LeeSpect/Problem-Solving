select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from item_info i
join item_tree t on i.item_id = t.item_id
where i.item_id not in(select parent_item_id
                      from item_tree
                      where parent_item_id is not null
                      group by parent_item_id)
order by i.item_id desc