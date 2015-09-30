select v.business_id, name, decoration_score, latitude, longitude
	from venues v 
	join venue_categories vc 
	on (v.business_id = vc.business_id)
	join categories c
	on (vc.category = c.category)
where 
	latitude > 31.3086 and 
	latitude < 31.315341 and 
	longitude > 121.3719 and 
	longitude < 121.3894 and
	decoration_score > 0 and 
	(c.parent = (select category from categories where en='food') or
	c.parent = (select category from categories where en='life'))
order by decoration_score desc;