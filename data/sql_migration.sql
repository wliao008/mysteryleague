-- some sql statements that convert data into csv format, 
-- so they can be imported into google appengine

select i.ItemType as item_type, 
i.Title as title, REPLACE(REPLACE(i.Summary, CHAR(13), ''), CHAR(10), '') as summary,
ltrim(rtrim(REPLACE(REPLACE(Content_HTML, CHAR(13), ''), CHAR(10), ''))) as content_html, 
convert(varchar, i.Audit_CreatedDate, 121) as created_date,
i.Hits as hits, i.IsReviewable as is_reviewable, 
i.IsRatable as is_ratable,
i.Rating as rating, u.Nickname as [user],
'Item, Article' as class,
'Active' as status,
i.Icon as icon_url,
i.Id as item_id
from Items i
join Users u on u.Id=i.UserId
where i.ItemType=1
order by i.Id;


select Email as email, convert(varchar, Audit_CreatedDate, 121) as created_date, Nickname as nickname, GravatarIconUrl as gravatar_icon_url from Users;

select 
r.Title as [subject],
ltrim(rtrim(REPLACE(REPLACE(REPLACE(r.Content_HTML, '|', ''), CHAR(13), ''), CHAR(10), ''))) as content_html, 
r.ReviewerIP as ip_address,
convert(varchar, r.Audit_CreatedDate, 121) as created_date,
u.Nickname as [user],
i.Id as item_id
from Reviews r
join Users u on u.Id = r.UserId
join Items i on i.Id = r.ItemId
where LEN(r.Content_HTML) > 1
and r.ReviewerIP is not null;

--book
select i.ItemType as item_type, 
i.Title as title, REPLACE(REPLACE(i.Summary, CHAR(13), ''), CHAR(10), '') as summary,
ltrim(rtrim(REPLACE(REPLACE(Content_HTML, CHAR(13), ''), CHAR(10), ''))) as content_html, 
convert(varchar, i.Audit_CreatedDate, 121) as created_date,
i.Hits as hits, i.IsReviewable as is_reviewable, 
i.IsRatable as is_ratable,
i.Rating as rating, u.Nickname as [user],
'Item, Book' as class,
'Active' as status,
i.Icon as icon_url,
i.Id as item_id,
ib.ISBN as isbn,
ib.SubTitle as sub_title,
ib.OriginalTitle as original_title,
ib.Price as price,
ib.PublishedDate_Year as published_year,
ib.PublishedDate_Month as published_month,
ib.PublishedDate_Day as published_day,
ib.PageCount as page_count,
(
  select CAST(p.name + ', ' as nvarchar(max))
  from Items_Person p
  join BookPerson bp on bp.Books_Id = i.Id
  where (p.Id = bp.Authors_Id)
  for xml path('')
) as authors
from Items i
join Items_Book ib on ib.Id = i.Id
join Users u on u.Id=i.UserId

where i.ItemType=2
order by i.Id;

---------- dev below -------------

select * from Items where ItemType=2;

select i.Id, i.Title, p.Name from Items i
join BookPerson bp on bp.Books_Id = i.Id
join Items_Person p on p.Id = bp.Authors_Id
order by i.Id
